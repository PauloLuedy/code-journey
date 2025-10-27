const bookPrices = [12, 8, 15, 22, 5];


let cheapestBook = 0;

for (let current = 0; current < bookPrices.length; current++) {
   console.log(bookPrices[current]);
   if(bookPrices[current] < bookPrices[cheapestBook]) {
       cheapestBook = current;
   }
}

console.log("Cheapest book price: " + bookPrices[cheapestBook]);