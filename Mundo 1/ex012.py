preco = float(input("Qual o preço do produto? "))
promo = preco - (5/100)*preco
print("O produto que custava {}, agora está de {:.2f}".format(preco, promo))