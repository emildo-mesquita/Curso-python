
decrescente = True	
anterior = int(input("Digite o primeiro número da sequência: ")) # 100

valor = 1

while valor != 0 and decrescente:
	valor = int(input("Digite o próximo número da sequência: "))
	if valor > anterior:
		decrescente = False	
	anterior = valor

if decrescente:
	print("A sequência está na ordem decrescente :-)")
else:
	print("A sequência não está na ordem decrescente :-)")
