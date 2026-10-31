products=[
   {"category": "bread" ,"price": 70, "stock": 10},
   {"category":"milk", "price": 250, "stock": 12 },
   {"category":"sugar", "price": 160, "stock":3},
   {"category": "rice", "price": 110, "stock": 14},
   {"category":"sweets", "price":10, "stock":50}
    
]

def show_menu():
    print("==MINISHOP SYSTEM==")
    print("1.View_products")
    print("2.Add_products")
    print("3.Changeprice_products")
    print("4.Exit")

def View_products():
    for product in products:
        print(product["category"], product["price"], product["stock"])

def Add_products():
    newproduct=input("Which product would you like to add?")
    try:
     newprice= int(input("Enter price:"))
     if newprice <=0:
        print("price must be greater than zero")
        return
    except ValueError:
     return
    try:
     newstock=int(input("Enter stock of the new product:"))
     if newstock <0:
        print("Stock cannot be negative")
        return
    except ValueError:
       return


    product={
        "category":newproduct,
        "price": newprice,
        "stock": newstock
    }

    products.append(product)
    print("New product added!")


def Change_price():
    name = input("Which product price do you want to change? ")
    found = False

    for item in products:
        if item["category"] == name:
            found = True

            newprice = int(input("Enter the new price: "))

            if newprice <= 0:
                print("Price must be greater than zero")
                return

            item["price"] = newprice
            print("Product price updated successfully!")
            return

    if not found:
        print("Product not found!")

def main():
   while True:
      show_menu()
      choice= input("Choose an option...")
      if choice =="1":
         View_products()
      elif choice=="2":
         Add_products()
      elif choice=="3":
         Change_price()
      elif choice=="4":
         print("Goodbye")
         break
      else:
         print("Invalid option!")

main()

      
   
         

  
   

