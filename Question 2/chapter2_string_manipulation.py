def process_string(s):
    # Separate numbers and letters
    number_string = ''.join([char for char in s if char.isdigit()])
    letter_string = ''.join([char for char in s if char.isalpha()])

    # Convert even numbers to their ASCII decimal values
    even_numbers = [int(char) for char in number_string if int(char) % 2 == 0]
    even_numbers_ascii = [ord(str(num)) for num in even_numbers]

    # Convert uppercase letters to ASCII decimal values
    uppercase_letters = [char for char in letter_string if char.isupper()]
    uppercase_ascii = [ord(char) for char in uppercase_letters]

    # Return the ASCII decimal values
    return even_numbers_ascii, uppercase_ascii

# Example usage
s = "56aAww1984sktr235270aYmn145ss785fsq31D0"  # Replace this with your input string
even_numbers_ascii, uppercase_ascii = process_string(s)

# Output results
print(f"Even Numbers in ASCII: {even_numbers_ascii}")
print(f"Uppercase Letters in ASCII: {uppercase_ascii}")