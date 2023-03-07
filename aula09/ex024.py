cidade = input('Insira o nome da cidade: ')
if cidade[0:5] == 'Santo':
    print('Esta cidade tem Santo no começo do nome!')
elif 'Santo' in cidade:
    print('Esta cidade tem Santo no meio do nome!')
else:
    print('Esta cidade não tem Santo no nome!')
