# Decryption function to reverse the Caesar cipher-like encryption
def decrypt(text, key):
    decrypted_text = ''
    for char in text:
        if char.isalpha():  # Process only alphabetic characters
            shifted = ord(char) - key  # Shift backward by the key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26  # Wrap around for lowercase letters
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26  # Wrap around for uppercase letters
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char  # Non-alphabetic characters remain the same
    return decrypted_text

# Example encrypted code (from the provided image)
encrypted_code = (
    "tybony_inevonyr = 100\n"
    "zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}\n"
    "qrs cebprff_ahzoref():\n"
    "    tybony_inevonyr = 5\n"
    "    ahzoref = [1, 2, 3, 4, 5]\n"
    "    juvyr tybony_inevonyr > 0:\n"
    "        vs tybony_inevonyr % 2 == 0:\n"
    "            ahzoref.erzbir(tybony_inevonyr)\n"
    "        tybony_inevonyr -= 1\n"
    "    erghea ahzoref\n"
    "zl_frg = [1, 2, 3, 4, 5, 4, 3, 2, 1]\n"
    "erfhyg = cebprff_ahzoref(ahzoref=zl_frg)\n"
    "qrs zbqysl_qvpg(5)\n"
    "qrs hcqngr_tybony():\n"
    "    tybony tybony_inevonyr\n"
    "    tybony_inevonyr += 10\n"
    "sbe v va enatr(5):\n"
    "    cevag(v + 1)\n"
    "vs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10:\n"
    "    cevag('pbagvba zrg!')\n"
    "vs 5 abg va zl_qvpg:\n"
    "    cevag('S abg sbhaq va gur qvpgvbanerl!')\n"
    "cevag(tybony_inevonyr)\n"
    "cevag(zl_qvpg)\n"
    "cevag(zl_frg)"
)

# Example key (let's assume key = 13 for ROT13 encryption)
key = 13  # Replace with the correct key if necessary

# Decrypt the code
decrypted_code = decrypt(encrypted_code, key)
print("Decrypted Code:")
print(decrypted_code)

# ----------------------------------------
# The following is the corrected decrypted code based on the decrypted output:
# ----------------------------------------

# Initialize a global variable and dictionary
global_varibale = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 10}  # Added 'key4'

# Function to process numbers
def process_numbers():
    global global_varibale  # Use the global variable
    global_varibale = 5
    numbers = [1, 2, 3, 4, 5]
    while global_varibale > 0:
        if global_varibale % 2 == 0:
            numbers.remove(global_varibale)
        global_varibale -= 1
    return numbers

# Initialize a set and call process_numbers function
my_set = [1, 2, 3, 4, 5, 4, 3, 2, 1]
result = process_numbers()  # Call the function without arguments

# Function to modify the dictionary
def modify_dict(value):
    my_dict['key5'] = value  # Example of adding a new key to the dictionary

# Function to update global variable
def update_global():
    global global_varibale  # Access the global variable
    global_varibale += 10

# Loop through a range and print values
for i in range(5):
    print(i + 1)

# Check conditions and print messages
if my_set is not None and my_dict.get('key4') == 10:  # Use .get() to avoid KeyError
    print('Condition met!')

if 5 not in my_dict:  # Check if 5 is not a key in the dictionary
    print('5 not found in the dictionary!')

# Print final values
print(global_varibale)
print(my_dict)
print(my_set)

# Another part of the logic that handles numbers
total = 0
for i in range(5):  # Outer loop for i from 0 to 4
    for j in range(3):  # Inner loop for j from 0 to 2
        if i + j == 5:  # Condition when the sum of i and j is 5
            total += i + j  # Add i and j to total
        else:
            total -= i - j  # Subtract the difference of i and j from total

print(total)  # Print the final total

# Counter logic
counter = 0
while counter < 5:  # Loop while counter is less than 5
    if total < 13:  # If total is less than 13
        total += 1  # Increment total by 1
    elif total > 13:  # If total is greater than 13
        total -= 1  # Decrement total by 1
    else:
        counter += 2  # Increment counter by 2

print("Counter =", counter)  # Print the final counter value