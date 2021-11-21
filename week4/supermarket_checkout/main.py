from product import Product
from checkout import CheckoutRegister

def construct_product_items(productItemsArrayList):
    productItemsArrayList.append(Product(501,"Chocolate",4,1))
    productItemsArrayList.append(Product(502,"ice cream",1,3))
    productItemsArrayList.append(Product(503,"rice",2,2))
    productItemsArrayList.append(Product(504,"mouthwash",1,5))
    productItemsArrayList.append(Product(505,"Bread",2,4))
    productItemsArrayList.append(Product(506,"candy bars",2,6))
    productItemsArrayList.append(Product(508,"Grapes",1,3))
    productItemsArrayList.append(Product(507,"BodyWash",3,7))
    productItemsArrayList.append(Product(509,"soda",1,8))
    productItemsArrayList.append(Product(510,"Milk",2,2))


print("** Welcome to Cerrae's Store checkout! **")
input1 = "N"
input2 = "Y"
productItems = []

construct_product_items(productItems)

while (input1 != "Q"):
    regsisterObject = CheckoutRegister()
    input2 = "Y"
    totalCost = 0
    regsisterObject.save_product_list(productItems)
    while (input2 == "Y"):
        enteredCode = input("Enter the Code of your product : ")
        matchedItem = 0
        for itemInstance in productItems:
            if str(itemInstance.productItemCode) == str(enteredCode):
                matchedItem = 1
                break
        if matchedItem == 0:
            print("Entered Product does not exist in our store!!!")
        else:
            print("%s - $%s" % (str(itemInstance.productItemName),str(itemInstance.productItemCost)))
            totalCost = totalCost + itemInstance.productItemCost
            regsisterObject.scan_item(enteredCode)
            input2 = input("Do you want to scan more products ? (Y/N) ")

    regsisterObject.payBill(totalCost)
    regsisterObject.print_receipt()
    print("* We Thank you for shopping at Cerrae's Store! *")
    input1 = input("(N)ext customer, or (Q)uit ? ")