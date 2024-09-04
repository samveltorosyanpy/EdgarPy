from admin import add_product

data = {
    "products": [
        {}
    ]
}

def main():
    choose_status = input("""
1) Admin
2) User

Enter: """)

    if choose_status == "1":
        choose_function = input("""
1) Add product
2) Delete product

Enter: """)

        if choose_function == "1":
            p_name = input("Enter product name")
            p_description = input("Enter product description")
            p_price = input("Enter product price")

            add_product(name=p_name, description=p_description, price=p_price)

        elif choose_function == "2":
            pass

    elif choose_status == "2":
        pass



if __name__ == "__main__":
    main()
