import random
import sys
import time

def _code():
    random.seed()
    foo = random.randrange(9)

    print("Woah...", foo)
    time.sleep(foo)
    print(sys.argv[0], foo)

_code()

thing = """
def _code():
    random.seed()
    foo = random.randrange(9)

    print("Woah...", foo)
    time.sleep(foo)
    print(sys.argv[0], foo)

_code()

new_code = compile(thing, "", 'exec')
eval(new_code)

_code()
"""

new_code = compile(thing, "", 'exec')
eval(new_code)

_code()