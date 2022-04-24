import string
import random

LENGTH = 15
string_pool = string.ascii_letters
result = ""
for i in range(LENGTH) :
    result += random.choice(string_pool)
print(result)

# string.digits (0123456789)
# string.ascii_lowercase (영어, 소문자)
# string.ascii_uppercase (영어, 대문자)
# string.ascii_letters (영어 대소문자)
# string.punctuation (기호)
