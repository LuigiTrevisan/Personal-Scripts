# Shipping Tracker

This script will track the shipping status of a package using the tracking number.

## Setup

```sh
$ pip install -r requirements.txt
```

This script uses Link & Track's (correiosApi)[https://github.com/chipytux/correiosApi?tab=readme-ov-file#como-usar] to track the package. You will need to follow the instructions on the correiosApi page to get a BASE_URL, USER, and TOKEN. Once you have those, create a .env file in the same directory as the script and add the following:

```sh
BASE_URL=<base url>
USER=<user>
TOKEN=<token>
```

Link & Track offers a test account in the repository above. You can use that to test the script.


## Running

```sh
$ python tracker.py <tracking number>
```

## Screenshots

![Screenshot 1](https://i.imgur.com/wOkh8dk.jpg)