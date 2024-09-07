# Function to decrypt Caesar Cipher text
def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_text = ''

    # Loop through each character in the ciphertext
    for char in ciphertext:
        if char.isalpha():  # Process only alphabetic characters
            shift_amount = shift % 26  # Ensure the shift is within the alphabet range
            if char.isupper():
                # Decrypt uppercase letters
                decrypted_text += chr((ord(char) - shift_amount - 65) % 26 + 65)
            elif char.islower():
                # Decrypt lowercase letters
                decrypted_text += chr((ord(char) - shift_amount - 97) % 26 + 97)
        else:
            # Non-alphabetic characters remain the same (e.g., spaces, punctuation)
            decrypted_text += char

    return decrypted_text


# Function to try all shift values and print the result
def try_all_shifts(ciphertext):
    for shift in range(1, 26):  # Shift from 1 to 25
        decrypted_text = decrypt_caesar_cipher(ciphertext, shift)
        print(f"\nShift {shift}:")
        print(decrypted_text)


# Example usage
if __name__ == "__main__":
    # Example cipher text from the image provided
    ciphertext = (
        "VZ FRYSVF UZNCGVRAQ NAQ N VHGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY "
        "NAQNG GZVRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF "
        "URYYQBAQ QRFRER ZR NG ZL ORFG ZNEVYL ZBAEBR"
    )

    #### Uncomment the approach you want to use: ####

    # 1. Try all shift values (Brute Force Approach)
    # try_all_shifts(ciphertext)

    # 2. Use a known fixed shift value
    shift = 13  # Replace with the correct shift value
    decrypted_text = decrypt_caesar_cipher(ciphertext, shift)
    print(f"\nDecrypted Text with Shift {shift}:")
    print(decrypted_text)