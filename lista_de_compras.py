lista_de_compras = ["maças", "bananas", "laranjas", "abacates", "kiwis"]
def adicionar_item(item):
    if item not in lista_de_compras:
        lista_de_compras.append(item)
        print(f"{item} adicionado à lista de compras.")
    else:
        print(f"{item} já está na lista de compras.")

print("Lista de compras atual:")
for item in lista_de_compras:
    print(f"- {item}")

adicionar_item("peras")
print("Lista de compras atualizada:")
for item in lista_de_compras:
    print(f"- {item}")

lista_de_compras.remove ("maças")
print("Lista de compras após remoção:")
for item in lista_de_compras:
    print(f"- {item}")

