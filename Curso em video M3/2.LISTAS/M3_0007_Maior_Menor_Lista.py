valores = []
for c in range(0, 5):
    valores.append(int(input("Digite um valor: ")))
maior = max(valores)
menor = min(valores)
print(f'Seus valores em ordem {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print()

print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
