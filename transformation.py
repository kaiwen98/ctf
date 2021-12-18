import os
import base64
import sys
import json
import os
"""
This is solved by filling and referring to a symmetric cipher.
"""


def encrypt_fun(a, b):
    """
    Function appears to be at least injective.
    """
    return (a << 8) + b

with open(os.path.join(os.getcwd(), "in", "enc"), "r", encoding="utf-8") as f:
    raw = f.read()
    flag_e = raw
    # print(base64.b64decode(bytes(raw, "utf-8").decode("ascii")))
    # flag = "picoCTF}"
    # for i in range(0, len(flag), 2):
    #     n = (ord(flag[i]) << 8) + ord(flag[i + 1])
    #     print(chr(n))
    for i in raw:
        # print(int.from_bytes(i.encode("utf-8"), "big"))
        print(ord(i))

    table = {}
        
    print(table)
    if not os.path.exists("./in/transformation_cipher.json"):
        with open("in/transformation_cipher.json", "w") as f:
            for i in range(256):
                for j in range(256):
                    key = encrypt_fun(i, j)
                    print(key)
                    if key not in list(table.keys()):
                        table[key] = [chr(i), chr(j)]
                    else:
                        print("nonoe ", i, " ", j)
                        exit(0)
            json.dump(table, f)

    with open("in/transformation_cipher.json", "r") as f:
        table = json.load(f)

    # flag_e = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
    out = []
    for i in flag_e:
        first_and_second = table[str(ord(i))]
        out += first_and_second
    flag_d= ''.join(out)
    print(flag_e)
    print(flag_d)
#     print()
#     flag = str(f.read())[3:][:-1].split('\\')
#     print(flag)
    
#     # a_flag = [ bytes.fromhex(i[1:]) for i in flag ]
#     # print(a_flag)
#     # v = ''.join([chr((ord(a_flag[i])<< 8) + ord(a_flag[i + 1])) for i in range(0, len(a_flag), 2)])
    

# print(flag)
