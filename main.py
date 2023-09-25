import random
import string
import uuid
digits = random.sample(string.digits, 2)
lowercase = random.sample(string.ascii_lowercase, 4)
uppercase = random.sample(string.ascii_uppercase, 1)
special = random.sample(['@', '$', '!', '_'], 1)
password_list = uppercase + lowercase + digits + special
random.shuffle(password_list)
password = "".join(password_list)
print("New unique id: ",str(uuid.uuid4())[0:15])
print("New password: ",password)


