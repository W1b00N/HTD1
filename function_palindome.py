from IPython.utils.text import strip_ansi
def is_palindrome(char):
    # Convert the character tO a string
    string_char = str(char)

    # Chaek if the string is equal to its reverse
    if string_char == string_char[::-1]:
      print("The character is a palindrome")
    else:
      print("The character is not a palindrome")