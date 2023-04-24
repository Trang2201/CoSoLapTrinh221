def convert_to_decimal(num, base):
    """Converts a number from an arbitrary base to base 10."""
    if base < 2 or base > 16:
        print("Error: Base must be between 2 and 16.")
        exit()

    decimal = 0
    power = 0
    for digit in num[::-1]:
        if digit.isdigit():
            decimal += int(digit) * (base ** power)
        else:
            decimal += (ord(digit.upper()) - 55) * (base ** power)
        power += 1

    return decimal


def convert_from_decimal(decimal, base):
    """Converts a number from base 10 to an arbitrary base."""
    if base < 2 or base > 16:
        print("Error: Base must be between 2 and 16.")
        exit()

    result = ""
    while decimal > 0:
        remainder = decimal % base
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(remainder + 55) + result
        decimal //= base

    return result


def main():
    """Reads the input number and bases from the user and performs the conversion."""
    num = input("Enter the number to convert: ")
    from_base = int(input("Enter the base of the input number (2-16): "))
    to_base = int(input("Enter the base of the desired result (2-16): "))

    decimal = convert_to_decimal(num, from_base)
    result = convert_from_decimal(decimal, to_base)

    print(f"{num} (base {from_base}) = {result} (base {to_base})")


if __name__ == '__main__':
    main()
