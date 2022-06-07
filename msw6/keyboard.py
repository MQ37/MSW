import math
import hashlib

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

data = input("Mačkejte náhodná tlačítka na klávesnici (nebo mlaťte hlavou do klávesnice) pro získání náhodných dat a poté stiskněte enter:\n")

seed = get_seed(data)
print("Váš seed je: %s" % seed)
