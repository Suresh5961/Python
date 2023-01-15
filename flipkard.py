# flipkart order

ordername=input("Tell us product name: ")
price=int(input("Tell the price: "))
delivery={
    "doorno":input("Tell us doorno: "),
    "street":input("Tell us street: "),
    "pin":int(input("Enter pin code: ")),
    "contact":int(input("Contact number: "))
}
print("Order has placed with details of the product",ordername,
      "for the cost of",price,"to the address",delivery,"successfully")  
      