num = int(input("Enter the number: "))

if num< 0:
    print(num, "is a negative nummber")
else:
    original_number = num
    reversed_number = 0

    while num > 0:
        last_digit = num % 10
        reversed_number = (reversed_number * 10) + last_digit
        num //= 10


    if original_number == reversed_number:
        print(original_number, "is a palindrome number")
    else:
        print(original_number, "is  not a palindrome number")
