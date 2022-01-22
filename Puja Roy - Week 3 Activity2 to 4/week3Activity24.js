// Example 3
let par1 = document.querySelector('.p1');
par1.className = 'foodList';

// Example 4
var colors = ['red', 'green', 'blue', 'purple','yellow'];
let colorSel = colors[2];
let span1 = document.querySelector('.color1');
let span2 = document.querySelector('.displayColor');
span1.style.color = colorSel;
span2.innerHTML = `<b> ${colorSel} </b>`;

// Example 5
let g1 = 60;
let g2 = 80;
let avg = (g1+g2)/2;
let pDisplay = document.querySelector('.displayGrade');

if(avg>=60){
  pDisplay.innerHTML = 'YOU PASSED!';
}
else {
  pDisplay.innerHTML = 'YOU FAILED!';
}

// ACTIVITY 2
var d = document.querySelector('#result');

// If the average grade is between 60 and 100, it displays a message that says "YOU PASSED!" with a font color of green.
if(avg>=60 && avg<=100){
  d.style.color = 'green';
  d.innerHTML = 'YOU PASSED!';
}
// If the average grade is between 0 and 59, it displays a message that says "YOU FAILED!" with a font color of red.
else if (avg>=0 && avg<=59){
  d.style.color = 'red';
  d.innerHTML = 'YOU FAILED!';
}
// If the average is not a number between 0 and 100, it diplays a message that says 'INVALID ENTRY!' with a font color of orange.
else{
  d.style.color = 'orange';
  d.innerHTML = 'INVALID ENTRY!';
}


// Example 6
let listFood = document.querySelectorAll('.food');

if(listFood.length>=3){
    listFood[2].style.backgroundColor = 'purple';
    listFood[2].style.fontSize = '1.2em';
    listFood[2].style.color = 'pink';
}

// ACTIVITY 3  (FOR LOOP)
let foods = document.querySelectorAll('.foodList');

for(let i = 3; i < foods.length; i++){
    foods[i].style.backgroundColor = 'purple';
    foods[i].style.fontSize = '1.2em';
    foods[i].style.color = 'pink';
}

// Example 7
// Step 1: Create an element using createElement()
let myPara = document.createElement('p');
// Step 2: Create the text content to the element using creatTextNode()
let mySentence = document.createTextNode('New paragraph: Puja Roy');
// Step 3a: Append the nex text node with the new element
myPara.append(mySentence);

//Step 3b: append the new element into an existing element in the HTML
let divP = document.querySelector('.example7');
divP.append(myPara);


// ACTIVITY 4
// STEP 1: Create a new element using createElement()
let newItem = document.createElement('li');
// STEP 2: Create text content for the element using creatTextNode()
let itemContent = document.createTextNode('APPLE');
// STEP 3A: Append the new text node to the new element
newItem.append(itemContent);
newItem.className = 'foodL';
// STEP 3B: Append the new element into an existing element in the HTML
let newli = document.querySelector('.listFood');
newli.append(newItem);
