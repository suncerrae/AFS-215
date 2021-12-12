class ShoppingCart {
  constructor() {
    this.total = 0;
    this.items = {};
  }

  addItem(itemName, quantity, price) {
    
      this.total += quantity * price;
      this.items[itemName] = quantity;
  
  }

  removeItem(itemName, quantity, price) {
    this.total -= quantity * price;
    this.items[itemName] = this.items[itemName] - quantity;
    
  }

  getTotal() {
    return this.total
  }

  getDiscount(code){
    
    if(code == '20'){
      let reduction = this.total * .20
      let sale = this.total - reduction
      return sale
    }
    else if(code == 30){
      let reduction = this.total * .30
      let sale = this.total - reduction
      return sale
    }
  }
}

module.exports = ShoppingCart

let shop = new ShoppingCart()

console.log(shop.addItem('item1', 2,))
// shop.removeItem('item1', 1, 9)

// console.log('Your current total is: $' + shop.getTotal())
// console.log('Your new total is: ' + shop.getDiscount(20))