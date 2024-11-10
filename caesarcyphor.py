alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = '''           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
'''
print(logo)
direction = input("Which action do you want to perform: Type 'encrypt' for encryption or 'decrypt' for decryption: ")
message = input("Write the message: ").lower()
shift = int(input("Enter how much you want to shift: "))

should_continue = True
while should_continue == True:
    def caeser(start_message, shift_amount, cypher_direction):
        result = ""
        for char in start_message:
            if char in alphabet:    
                position = alphabet.index(char)
                if cypher_direction == "encrypt":
                    new_position = (position + shift_amount) % 26
                elif cypher_direction == "decrypt":
                    new_position = (position - shift_amount) % 26
        
                new_char = alphabet[new_position]
                result  += new_char
            else:
                result += char
        print(result)

    caeser(message, shift, direction)
    yes_or_no = input("Do you want to continue: Yes or No: ").lower()
    if yes_or_no == "no":
        should_continue = False


# if direction == 'encrypt':
#     encrypted_message = encrypt(message, shift)
    
# elif direction == 'decrypt':
#     decrypted_message = decrypt(message, shift)

# else:
#     print("Invalid Input. Write 'encrypt' or 'decrypt'.")