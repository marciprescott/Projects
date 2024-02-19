# inputs original text, and an int that represents shifts
# outputs
def caesar_crypto_encode(text, shift):
    # Check if input is empty, null or whitespace
    if not text.strip():
        return ""
    # Initialize an empty string to store text
    encoded_text = ""
    for char in text:
        # Check to see if a letter is alphabetic
        if char.isalpha():
            # Determine the case of the letter (upper or lower)
            if char.isupper():
                # Calculate the new ASCII code for the uppercase letter
                new_char_code = ord("A") + ((ord(char) - ord("A") + shift) % 26)
                encoded_text += chr(new_char_code)
            else:
                # Calculate the new ASCII code for the lowercase letter
                new_char_code = ord("a") + ((ord(char) - ord("a") + shift) % 26)
                # Convert the ASCII code back to a character and append
                encoded_text += chr(new_char_code)
        else:
            # If the character is not a letter, append it unchanged to the encoded text
            encoded_text += char
    return encoded_text


print(
    caesar_crypto_encode(
        "You have to implement the function “Encode” of CaesarCrypto class that codes or decodes text based on Caesar’s algorithm.",
        3,
    )
)
