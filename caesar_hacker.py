# This program can hack messages encrypted with the Caesar cipher
# even if you don’t know the key. 
# There are only 26 possible keys for the Caesar cipher, 
# so a computer can easily try all possible decryptions and display the results to the user. 
# In cryptography, we call this technique a brute-force attack.


print('Enter Caesar Cipher Message to be Hacked?')
message = input('>')

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(alphabets)):
    translated = ''
    
    for s in message:
        if s in alphabets:
            num = alphabets.find(s)
            num = num - i
            
            if num<0:
                num = num + len(alphabets)
            
            translated = translated + alphabets[num]
        else:
            translated= translated + s
    print(f'Key - {i} , Translation - {translated}')