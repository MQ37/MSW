import time
import math
import hashlib
import pyautogui

N = 1000
positions = []

def get_pos():
    pos = pyautogui.position()
    return (pos.x, pos.y)

def pos_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    return math.sqrt( (x1-x2)**2 + (y1-y2)**2 )

def get_seed(data):
    _hash = hashlib.sha256(data.encode("utf-8")).hexdigest()

    seed = 1
    for _hex in zip(_hash[::2], _hash[1::2]):
        shex = "%s%s" % _hex
        dec = int( shex, 16 )
        for char in shex:
          dec *= ord(char)

        seed *= math.log2(dec)
    return int(seed)

input("Pohybujte náhodně kurzorem pro získání náhodných dat.\n\
Stiskněte klávesu enter pro pokračování")

prev_pos = (0, 0)

while len(positions) < N:
    time.sleep(0.01)
    x, y = get_pos()
    if pos_distance(prev_pos, (x, y)) > 20:
        positions.append( (x, y) )
    print("%s/%s" % (len(positions), N),end = "\r")
    prev_pos = (x, y)
print()

seed = get_seed( str(positions) )
print("Váš seed je: %s" % seed)
