//const readlineSync = require("readline-sync");
//const num = readlineSync.keyIn("Please enter a number from 1-10.  ");

function fizzbuzz(num) {
    if (num === 1) {
        return "1"
        //console.log("1")
    } else if (num === 2) {
        return "2"
        //console.log("2")
    } else {
        return "fizzbuzz"
        //console.log("fizzbuzz")
    }
}

//fizzbuzz()
//module.exports = fizzbuzz;
export default fizzbuzz
