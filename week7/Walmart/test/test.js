const assert = require('chai').assert
const app = require('../Walmart.js')


const shop = new app()

describe('App', function(){
   
    it('add item and price to get total $18', function(){
        shop.addItem('item1', 2, 9)
        assert.equal(shop.getTotal(), 18)
    })
    it('add multiple items get total $37', function(){
        //remove item one total carried over from 1st test:
        shop.removeItem('item1',2,9)
        //adding multple items  get total
        shop.addItem('item1',1,9)
        shop.addItem('item2',2,8)
        shop.addItem('item3',1,12)
        assert.equal(shop.getTotal(), 37)
    })
    it('apply 20% discount to total $29.60', function(){
        assert.equal(shop.getDiscount(20), 29.6)
    })
    
})