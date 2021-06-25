import random
import string

print(' ******Welcome to Password generator!******')
length = int(input('\nEnter the length of password: '))
all = string.ascii_letters + string.digits + string.punctuation  # combines the upper,lower, digit,symbols
password = "".join(random.sample(all, length))  # randomly generates te character based on the given lenght
print(password)
