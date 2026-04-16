def caesar_cipher(text, shift, mode):
    result = ""
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  

    return result


def main():
    print("=" * 40)
    print("       CAESAR CIPHER PROGRAM")
    print("=" * 40)

    message = input("\nEnter your message: ")

    while True:
        try:
            shift = int(input("Enter shift value (1-25): "))
            if 1 <= shift <= 25:
                break
            else:
                print("Please enter a value between 1 and 25.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nChoose mode:")
    print("1. Encrypt")
    print("2. Decrypt")

    while True:
        choice = input("Enter choice (1 or 2): ")
        if choice in ("1", "2"):
            break
        print("Invalid choice. Enter 1 or 2.")

    mode = "encrypt" if choice == "1" else "decrypt"
    output = caesar_cipher(message, shift, mode)

    print("\n" + "-" * 40)
    print(f"Original Message : {message}")
    print(f"Shift Value      : {shift}")
    print(f"Mode             : {mode.capitalize()}")
    print(f"Result           : {output}")
    print("-" * 40)


if __name__ == "__main__":
    main()
