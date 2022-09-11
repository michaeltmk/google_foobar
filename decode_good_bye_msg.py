import base64
from itertools import cycle

message = """YOUR SECRET MESSAGE"""

key = bytes("YOUR GOOGLE USERNAME", "utf8")

print(bytes(a ^ b for a, b in zip(base64.b64decode(message), cycle(key))))

#b"{'success' : 'great', 'colleague' : 'esteemed', 'efforts' : 'incredible', 'achievement' : 'unlocked', 'rabbits' : 'safe', 'foo' : 'win!'}"