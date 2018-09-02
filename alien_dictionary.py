from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.backends import default_backend


class AlienTranslator:

    def __init__(self, human2alien, key, nonce):
        self.e2m_dic = {}
        self.m2e_dic = human2alien

        for m in self.m2e_dic.keys():
            self.e2m_dic[self.m2e_dic[m]] = m

        algorithm = algorithms.ChaCha20(key, nonce)
        self.cipher = Cipher(algorithm, mode=None, backend=default_backend())

    def encrypt_to_code(self, msg):
        encryptor = self.cipher.encryptor()
        ct = encryptor.update(msg.encode())

        raw_code_num = int.from_bytes(ct, byteorder='big')
        code_text = ""

        while raw_code_num > 0:
            code_text += self.m2e_dic[raw_code_num & 15]
            raw_code_num = raw_code_num >> 4

        return code_text

    def decrypt_to_msg(self, code):
        decryptor = self.cipher.decryptor()
        raw_code_num = 0
        end = len(code)
        blen = 0

        for i in range(len(code) - 1, -1, -1):
            if code[i:end] in self.e2m_dic:
                raw_code_num = raw_code_num << 4
                raw_code_num = raw_code_num | self.e2m_dic[code[i:end]]
                end = i
                blen += 1

        msg = decryptor.update(raw_code_num.to_bytes(blen // 2, byteorder='big'))

        return msg.decode()
