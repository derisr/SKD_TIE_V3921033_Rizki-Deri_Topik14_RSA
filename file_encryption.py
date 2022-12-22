from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii


file_enc = open("text_asli.txt", "r")

# baca isi file
baca = file_enc.readlines()
print (baca)
#print (baca[1])

teks = str(baca[0])
teks_binary = teks.encode()
print(teks_binary)

keyPair = RSA.generate(3072)

pubKey = keyPair.publickey()
pubKeyPEM = pubKey.exportKey()
key2 = pubKeyPEM.decode('ascii')

privKeyPEM = keyPair.exportKey()

encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(teks_binary)
print("Hasil Enkripsi : ", binascii.hexlify(encrypted))
cipher_ascii = binascii.hexlify(encrypted)
cipherteks = cipher_ascii.decode()

decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
plainteks = decrypted.decode()
print('Hasil Dekripsi : ', plainteks)

file_dec = open("key_encrypt_text.txt", "a")
file_dec.write(key2)
