
MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():

    def get_password():
        print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
              "characters, and contain:")
        print("\t1 or more uppercase characters")
        print("\t1 or more lowercase characters")
        print("\t1 or more numbers")
        print("\t1 or more special characters")
        password = input("Please enter a valid password: ")
        return password

    password=get_password()
    """Determine if the provided password is valid."""
    if 2<=len(password)<=6:
        count_lower = 0
        count_upper = 0
        count_digit = 0
        count_special = 0
        for char in password:
            if char.isdigit():
                count_digit+=1
            if char.islower():
                count_lower+=1
            if char.isupper():
                count_upper+=1
            if char in SPECIAL_CHARACTERS:
                count_special+=1
    if (count_digit>=1 and count_lower>=1 and count_upper>=1 and count_special>=1):
        print("Valid password.")
        print("Your {}-character password: ".format(len(password)),end=" ")
    else:
        print("Invalid password.")
    for i in range(len(password)):
        print("*",end="")

main()