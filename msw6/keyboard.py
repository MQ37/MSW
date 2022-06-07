import math
import hashlib

def get_seed(data):
    hash = hashlib.sha256(data.encode("utf-8")).hexdigest()

    seed = 1
    for hex in zip(hash[::2], hash[1::2]):
        shex = "%s%s" % hex
        dec = int( shex, 16 )
        for char in shex:
          dec *= ord(char)

        seed *= math.log2(dec)
    return int(seed)

data = input("Mačkejte náhodná tlačítka na klávesnici (nebo mlaťte hlavou do klávesnice) pro získání náhodných dat a poté stiskněte enter:\n")

seed = get_seed(data)
print("Váš seed je: %s" % seed)
