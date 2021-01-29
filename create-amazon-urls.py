import random
import string


source = "https://www.amazon.com"

letters = string.ascii_lowercase


for i in range(250):
    slash = random.randint(1,5)
    ext = "/"
    for i in range(slash): 
        word = ''.join(random.choice(letters) for i in range(random.randint(1,10)))
        ext += word+"/"
    print(source+ext)
