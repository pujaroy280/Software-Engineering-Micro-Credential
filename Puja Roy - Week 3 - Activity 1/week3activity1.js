// Anoymous Function
  var x = function(){
    var a, b;
    a = 5;
    b = 8;
    if(a>b){
      console.log('a is greater than b');
    }
    else{
      console.log('b is greater than a');
    }
  }
  x();  // Call the variable at the end of the Anoymous function

  // --- SCOOPING IN JS ---
  var fullMoon = true;
  // Initialize a global variable
  let species = "human";

  if (fullMoon){
    // Initialize a local variable
    let species = "werewolf";
    console.log(`It is a full moon. Lupin is currently a ${species}`);
  }
   console.log(`It is not a full moon. Lupin is currently a ${species}`);

    // Let variable
    for (let i=0; i<10; i++){
      console.log(i);
    }
  //  console.log(`The last number is ${i}`);

  // "use strict"
  "use strict";

  name = "Peter Pan";



// Get element by tag name
// single access
var pArray = document.getElementsByTagName('p');   // put index [1] to select which Paragraph to color
// pArray.style.color = 'green';

// multiple access to array pArray by using a for Loop
for(var i=0 ; i<pArray.length; i++){
  pArray[i].style.color = 'green';  //previously yellow
}

// document.getElementById('one').style.color = 'blue'
// Get element by id
var pOne = document.getElementById('one');    // Call an element from a tree
pOne.style.color = 'blue';

// document.querySelector() ==> select the first element that matched the condition in between the parenthesis
var animal = document.querySelector('#species p');

// query select all
var animal2 = document.querySelectorAll('#species p');

// EXMAPLE 1
var hour = 22;  //2AM
var greeting;
if(hour>18){
  greeting = 'Good evening';
}
else if(hour>12){
  greeting = 'Good afternoon';
}
else if(hour>0){
  greeting = 'Good morning';
}
else{
  greeting = 'Wrong hour';
}

// mehthod.write() always displays the text content at the end of the html
// document.write(`<h2> ${greeting} </h2>`);  // document.write -> Writes after what html u have


// EXAMPLE 2
var price, quantity, subtotal, total, tax;
price = 5; //Was 5
quantity = 6;  //type in 35 for the activity to output OUT OF STOCK      // was 10
shipping = 8.99;
subtotal = price*quantity;
tax = 0.08;
total = (subtotal*tax) + subtotal;
var costElem = document.getElementById('cost');
costElem.textContent = `TOTAL $${total} \n for ${quantity} tiles \n for ${shipping}`;

// WEEK 3 ACTIVITY 1
if (quantity < 1){
  costElem.textContent = `${quantity} is not a valid quantity`;
}
else if (quantity > 20){
  costElem.textContent = `OUT OF STOCK. We don't have ${quantity} tiles on stock`;
}
else {
  costElem.innerHTML =
  `<br>Quantity = ${quantity}</br>
  <br>Subtotal  $${subtotal}</br>
  <br>Shipping  $${shipping}</br>
  <br>------------------------</br>
  <b><br>TOTAL  $${total}</br></b>`;
}
