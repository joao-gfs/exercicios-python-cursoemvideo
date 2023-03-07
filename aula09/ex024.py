cidade = input('Insira o nome da cidade: ').strip()
if cidade[0:6].lower() == 'santo ':
    print('Esta cidade tem Santo no começo do nome!')
elif 'santo ' in cidade.lower():
    print('Esta cidade tem Santo no meio do nome!')
else:
    print('Esta cidade não tem Santo no nome!')
