import codecs

def rot13(inp: str):
    ans = codecs.encode(inp, "rot13")
    return ans

def rot13_kw(inp: str):
    ans = []
    
    for i in range(len(inp)):
        if not inp[i].isalpha():
            ans.append(inp[i])
            continue

        is_upper = inp[i].isupper()
        char_offset = ord('A') if is_upper else ord('a')
        print(char_offset)
        
        ans.append(
            str(chr(
                ((ord(inp[i]) + 13) - char_offset) % 26 + char_offset
            ))
        ) 

    return "".join(ans)

if __name__ == "__main__":
    ans = rot13_kw("cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}")
    print(ans)



