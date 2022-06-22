import string
import random

with open("D:\project\phone.txt",'w') as f :

    length = 6
    Certification_Number = string.digits
    result = ""
    for i in range(length) :
        result +=random.choice(Certification_Number)

    f.write(result)