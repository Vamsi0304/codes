#password genearator
import random
from string import *
alphabets=ascii_letters
numbers="0123456789"
symbols="!@#$%^&*?/"
passinput=alphabets+numbers+symbols
length_of_password=8
password="".join(random.sample(passinput,length_of_password))
print(password)