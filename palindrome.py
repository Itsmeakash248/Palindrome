originalstring = "madam"
reverse_text = originalstring[::-1]

print("The original string is:", originalstring)
print("The reversed string is:", reverse_text)

if originalstring == reverse_text:
    print(f"'{originalstring}' is a palindrome.")
else:
    print(f"'{originalstring}' is not a palindrome.")
