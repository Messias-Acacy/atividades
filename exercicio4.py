variav = input('digite alguma coisa e vamos checar seus dados: ')
print(f'o tipo da variavel é {type(variav)}')
print(f'é número? {variav.isnumeric()}')
print(f'é alfabético? {variav.isalpha()}')
print(f'é só espaço? {variav.isspace()}')
print(f'é alfanumérico? {variav.isalnum()}')
print(f'é maiúsculo? {variav.isupper()}')
print(f'é minúscula? {variav.islower()}')
print(f'é capitalizada? {variav.istitle()}')