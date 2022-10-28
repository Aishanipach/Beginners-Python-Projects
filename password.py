# "password Generator"
# generator password of 12 characters
# 4 with small, 4 cap, 2 disital 2 special char
import string as s
from random import randint, sample
c_lower = s.ascii_lowercase
print("lowercase:",c_lower)
c_upper = s.ascii_uppercase
print("uppercase:",c_upper)
c_digits = s.digits
print("digits:",c_digits)
c_special = s.punctuation
print("special:",c_special)
cl = sample(c_lower,3); print(cl)
cu = sample(c_upper,1); print(cu)
cd = sample(c_digits,3); print(cd)
cs = sample(c_special,1); print(cs)

c = cl+cu+cd+cs
print(c)
password_new="".join(sample(c,8))
print("\password by @saurav = ", password_new)
