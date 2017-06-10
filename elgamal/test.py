import elgamal
import time

k = elgamal.generate_keys()
#returns a dictionary {'privateKey': privateKeyObject, 'publicKey': publicKeyObject}
print (k['publicKey'])
#elgamal.generate_keys(n, t)
fp = open("150kb")
text = []
for line in fp:
    text.append(line)
text = "".join(text)
start_time = time.time()
cipher = elgamal.encrypt(k['publicKey'],text)
print("---150kb Encryption  %s seconds ---" % (time.time() - start_time))
#returns a string

f = open ('encryption150.txt', 'w')
f.write(str(cipher)) #write ciphertext to file
f.close()
start_time = time.time()
plaintext = elgamal.decrypt(k['privateKey'], cipher)
print("---150kb Decryption  %s seconds ---" % (time.time() - start_time))
#returns the message passed to elgamal.encrypt()

f = open ('decryption150.txt', 'w')
f.write(str(plaintext)) #write ciphertext to file
f.close()

