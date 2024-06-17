alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('>').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letters e or d')

# Enter the key value
while True:
    key_value = input(f'Please enter the key value 0-{len(alphabets)-1}')
    if not key_value.isdecimal():
        continue
    if 0<= int(key_value)< len(alphabets):
        key = int(key_value)
        break
    
print('Enter the message')
message = input('>').upper()

translated = ''

for i in message:
    if i in alphabets:
        n = alphabets.find(i)
        if mode=='encrypt':
            n = n+key
        elif mode=='decrypt':
            n = n-key

        if n >= len(alphabets):
            n = n - len(alphabets)
        elif n < 0:
            n = n + len(alphabets)
            
        translated = translated+alphabets[n]
    else:
        translated = translated+i

print(translated)
            