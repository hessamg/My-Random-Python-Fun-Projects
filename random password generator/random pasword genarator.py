import random
import string

# This program generates a random password 
# with random size length of 8-15 
# containing letters, digits and punctiuations 

my_string = string.ascii_letters + string.digits + string.punctuation
random_length = random.randint(8,16)
password = ""
for i in range(random_length):
    password += random.choice(my_string)
print("The random password is: {}".format(password))
print("The length of the random password is: {}".format(len(password)))

