from random import choice

from services.product_service import ProductService

def main():
    service = ProductService()

    while True:
        print("\n=== Магазин ===")
        print("1. Показать все товары")
        print("2. Добавить товар")
        print("0. Выход")

        choice = input("Выберите опцию: ")

        if choice == "1":
            service.list_products()
        elif choice == "2":
            name = input("Название: ")
            description = input("Описание: ")
            price = float(input("Цена: "))
            category = input("Категория (Должна быть заранее создана): ")
            service.create_product(name, description, price, category)
        elif choice == "0":
            break
        else:
            print("Неверный ввод")

    service.close()

if __name__ == "__main__":
    main()
