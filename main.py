from Produto import Produto

def main():
    produto1 = Produto("Teclado mecânico", 350, estoque=10)
    produto2 = Produto("Mouse Game", 150, estoque=20)

    print("Lista de produtos")
    print(produto1)
    print(produto2)

    print("\nVendendo 5 teclados...")
    if produto1.vender(2):
        print("Venda realizada com sucesso!")
    else:
        print("Estoque insuficiente.")

if __name__ == "__main__":
    main()
