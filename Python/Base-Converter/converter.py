def convert_base(n, base1, base2):
    base10_num = int(str(n), base1)

    converted_num = ''
    while base10_num > 0:
        converted_num = str(base10_num % base2) + converted_num
        base10_num //= base2

    return converted_num

def main():
    n = input('Enter a number: ')
    base1 = int(input('Enter the base of the number: '))
    base2 = int(input('Enter the base to convert to: '))

    print(f'{n} in base {base1} is {convert_base(n, base1, base2)} in base {base2}')
    
if __name__ == '__main__':
    main()