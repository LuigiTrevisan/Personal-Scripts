# this is a script that will make a get request from a website, parse the json data and show the tracking information of a package informed by the user as an argument

import os
import time
import requests
from dotenv import load_dotenv
import argparse

load_dotenv()

URL = os.environ.get("BASE_URL") + "?user=" + os.environ.get("USER") + "&token=" + os.environ.get("TOKEN") + "&codigo="


def get_tracking_info(tracking_number):
    url = URL + tracking_number
    response = requests.get(url)
    while response.status_code == 429:
        sleeptime = int(response.text.split("Try again in ")[1].split("ms")[0])
        print(f"Too many requests, waiting {(sleeptime/1000):.1f} seconds...")
        time.sleep(sleeptime/1000)
        response = requests.get(url)
    data = response.json()
    return data["eventos"]


def print_tracking_info(tracking_number, tracking_info):
    recent = tracking_info[0]
    print(f"\n{'-'*20}")
    print(f"Tracking number: {tracking_number}")
    print(f"Status: {recent['status']}")
    print(f"Location: {recent['local']}")
    print(f"Date: {recent['data']}")
    print(f"Time: {recent['hora']}")
    print(f"{'-'*20}\n")
    
def receive_args():
    parser = argparse.ArgumentParser(
        description='Get tracking information from a package')
    parser.add_argument('tracking_number', type=str,
                        help='tracking number of the package')
    args = parser.parse_args()
    return args.tracking_number


def main():
    tracking_number = receive_args()
    try:
        tracking_info = get_tracking_info(tracking_number)
    except Exception as e:
        print(e)
        return
    if len(tracking_info) == 0:
        print("No tracking information found")
        return
    print_tracking_info(tracking_number, tracking_info)
    option = input("Do you want to see the full tracking information? (y/n): ")
    if option == "y" or option == "Y":
        for event in tracking_info:
            print(f"{'-'*20}")
            print(f"Status: {event['status']}")
            print(f"Location: {event['local']}")
            print(f"Date: {event['data']}")
            print(f"Time: {event['hora']}")
            print(f"{'-'*20}\n")


if __name__ == "__main__":
    main()
