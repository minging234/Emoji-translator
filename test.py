import sys
from alien_dictionary import AlienTranslator

temp_nonce = b'\xca\xdd%\x9b\x15\xc9\x19\xbc/\xacQ\xc7\xc1\xf6\xaf\xca'
temp_key = b'\nk\xb5\xa4/\xe2\xabJw\xa3\x85$v\xc2\xa7\x16\x17\xcbI\xd2}\xc6\x87\xd4\xd1o\xbf\x08("2\xce'

m2e_dic = {0: "[微笑]", 1: "[色]", 2: "[坏笑]", 3: "[悠闲]", 4: "/::P", 5: "/:8-)", 6: "/:B-)", 7: "/:,@!", 8: "/:heart",
           9: "/:ladybug", 10: "/::*", 11: "/:coffee", 12: "/:basketb", 13: "/:@>", 14: "/:<@", 15: "/:beer"}

translator = AlienTranslator(m2e_dic, temp_key, temp_nonce)


if sys.argv[1] == "enc":
    ans = translator.encrypt_to_code(sys.argv[2])
    with open("out.txt", "w") as file:
        file.write(ans)
    print(ans)

elif sys.argv[1] == "dec":
    with open("out.txt", "r") as file:
        data = file.read()
        data = data.strip("\n")
        ans = translator.decrypt_to_msg(data)
    print(ans)


