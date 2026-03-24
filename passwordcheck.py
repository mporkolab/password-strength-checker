import math
import time
import itertools
import string
import sys

"""Python Password Checker """



""""Entropy"""
def calculate_entropy(password):
    if not password:
        return 0.0

    #types
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    #Checking the String by characters
    for char in password:
        if has_lower and has_upper and has_digit and has_special:
            break
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True



    #Character pool calculation

    pool_size = 0
    if has_lower: pool_size += 26 #English lower chars
    if has_upper: pool_size += 26 #English upper chars
    if has_digit: pool_size += 10 #Digits from 0-9
    if has_special: pool_size += 32 #Usual special chars

    if pool_size == 0:
        return 0.0
    #Entropy: Password length * log2(pool_size)
    pw_length = len(password)
    entropy = pw_length * math.log2(pool_size)
    return round(entropy, 2)


def load_dict(file_path):
    print(f"Loading {file_path}....")
    password_set = set()

    try:
        with open(file_path, 'r',encoding='utf-8',errors='ignore') as file:
            for line in file:
                password_set.add(line.strip())
        print(f"Successfully loaded! Summarized {len(password_set)} unique passwords in the memory.")
        return password_set

    except FileNotFoundError:
        print("Error: The password file was not found.")
        return set()




def dict_attack(target_password, password_set):
    print(f"Dictionary based attack initiating against the {target_password} password.")

    #Timer
    start_time = time.time()


    is_found = target_password in password_set

    end_time = time.time()
    elapsed_time = end_time - start_time

    if is_found:
        print(f"Password found successfully! The password was decrypted in {elapsed_time:.6f} seconds.")
        return True
    else:
        print(f"Password was not found in the dictionary. (Time taken: {elapsed_time:.6f} seconds)")
        return False

def brute_force_attack(target_password, max_length=6):
    print(f"\n Brute-Force attack initiating against the {target_password} password (max {max_length} characters).")
    #The charset: For testing, only use the string.ascii_lowercase, but if you want full scan through
    # the characters with Uppercase and symbols, then add string.ascii_uppercase and string.punctuation
    chars = string.ascii_lowercase + string.digits
    start_time = time.time()
    attempts = 0

    for length in range(1,max_length+ 1):
        print(f"Attempting with {length} characters long...")

        for guess_tuple in itertools.product(chars,repeat=length):
            attempts += 1
            guess = ''.join(guess_tuple)

            if guess == target_password:
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Brute-Force Successful! The password was decrypted! -> {guess}")
                print(f"  -Attempts number: {attempts}")
                print(f"  -Time taken: {elapsed_time:.2f} seconds")
                return True
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"[-] Brute-Force failed. Couldn't crack until {max_length} characters.")
    print(f"  -Attempts number: {attempts}")
    print(f"  -Time taken: {elapsed_time:.2f} seconds")
    return False




def menu():
    print(f"\n " + "="*45)
    print("="*45)
    print("Welcome to Password Strength Checker \n Please enter the number of the function you want to try")
    print("[1] Password Strength checker")
    print("[2] Dictionary based attack on password")
    print("[3] Brute-Force attack simulation")
    print("[4] Exit")
    print("="*45)

def main():
    dict_passwords = load_dict('rockyou.txt')
    while True:
        menu()
        target = input("Enter the password to check: ")
        choice = input("Enter your choice: ")
        if choice == "1":
            entropy = calculate_entropy(target)
            print(f"Your password's entropy is: {entropy} bit")

            if entropy < 28:
                print("Your password is too weak!")
            elif entropy < 50:
                print("Your password is weak!")
            elif entropy < 70:
                print("Your password is strong!")
            else:
                print("Your password is super strong!")
        elif choice == "2":
            if dict_passwords:
                dict_attack(target, dict_passwords)
            else:
                print("The dictionary is empty, please try again")
        elif choice == "3":
            brute_force_attack(target,max_length=6)
        elif choice == "4":
            print("Thank you for using Password Checker! \n Exiting now... \n " + "="*45)
            sys.exit(0)
        else:
            print("Invalid input, please try again")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] The program exited (CTRL+C).")
        sys.exit(0)













