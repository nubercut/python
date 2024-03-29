import getopt
import random
import string
import sys
import os.path
import jsonpickle
from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "test data file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)
n = 5
f = "data/contacts.json"
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a
def random_string(prefix, maxlen):
    symbols_to_use = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols_to_use) for i in range(random.randrange(maxlen))])
test_data = [Contact(firstname="", lastname="")] + [Contact(firstname=random_string("firstname", 15),
                                                           lastname=random_string("lastname", 30),
                                                           address=random_string("address", 10))
                for i in range(5)
            ]
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))