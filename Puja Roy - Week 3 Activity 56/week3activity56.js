// Example 1
let btn1 = document.querySelector('.button1');
// Calling an event handler using an anonoymous function
/*
btn1.onclick = function(){
  alert ("You just clicked!");
};
*/
//Calling an event handler using a named function
function named(){
  alert('You just clicked!');
}
btn1.onclick = named;
//Example 2
let btn2 = document.querySelector('.button2');
// Use named function
/*
btn2.addEventListener('click', clickAgain, false);
function clickAgain(){
  alert('Click using addEventListener!');
}
*/
// Use anonoymous function
btn2.addEventListener('click', function(){
  alert('Click using addEventListener, anonoymous function!');
});

// Example 3
let btn3 = document.querySelector('.button3');

btn3.addEventListener('click', function(){
  alert('1st click! 1st window');
});
btn3.addEventListener('click', function(){
  alert('1st click! 2nd window');
});

// Example 4
let btn4 = document.querySelector('.button4');

let displayMsg = document.querySelector('.display1');

btn4.addEventListener('click', function(){
  alert('Button clicked!');
});

btn4.addEventListener('mouseover', function(){
  displayMsg.innerHTML += '<br>Mouse over';
});



// ACTIIVTY 5
let count = 0;
let btn5 = document.querySelector('.button5');
let displayMsg2 = document.querySelector('.display2');
btn5.addEventListener('mouseover', function(){
displayMsg2.innerHTML = displayMsg2.innerHTML + '<br> Moused over ' +  ++count + " "
});

btn5.addEventListener('click', function(){
  alert(`The button was hovered ${count} times`);
  count = 0;
  displayMsg2.innerHTML = "";
  displayMsg2.innerHTML = displayMsg2.innerHTML + 'The mouseover is reset to 0';
});


// Example 6
let btn6 = document.querySelector('.button6');
btn6.addEventListener('click', function(event){
  event.target.style.backgroundColor = 'purple';
  alert('Button was clicked!');
});

// Example 7
let linkQCC = document.querySelector('.qccLink');
linkQCC.addEventListener('click', function(e){
  e.preventDefault();
  alert('QCC website is OFF!');
});

// Example 8
let myForm = document.querySelector('.form1');   // Find form and put in variable
let pDisplay = document.querySelector('.display3');  // find paragraph and put in variable


myForm.addEventListener('submit', function(e){
  e.preventDefault();
  let name = document.querySelector('.inputName').value;  //find label and put in variable
   pDisplay.innerHTML = `Welcome to the program ${name}`;
});

// ACTIVITY 6
let myForm2 = document.querySelector('.form2');   // Find form and put in variable
let input2 = document.querySelector('inputName1');  // find paragraph and put in variable
let pDisplay1 = document.querySelector('.display4');

myForm2.addEventListener('submit', function(e){
  e.preventDefault();

  let input2 = document.querySelector('.inputName1').value;  //find label and put in variable
  var otherinput = isNaN(input2);

  if (otherinput) {
    pDisplay1.innerHTML = `Welcome to the program ${input2}`;
  }
  else if(input = " "){  // THERE NEEDS TO BE A SPACE FOR INPUTTING VALUE
    alert(`You did not enter a name, please enter a name again`);
  }
  else{
    alert(`${input2} is not a name. Please enter a name again`);
  }
});


// Example 9
let pageTop;
window.addEventListener('scroll', function(){
  pageTop = window.pageYOffset;
  console.log(`The window if scrolled ${pageTop} px from top`);
});

// Example 10
// For the variable, go back to check the class name of the div and apply to it
let topIcon = document.querySelector('.toTop');
let pageTopLoc;
window.addEventListener('scroll', function(){  //ADD anonoymous function
//  document.body.scrollTop
  pageTopLoc = window.pageYOffset;
  if (pageTopLoc>10){
    topIcon.style.display = 'block';
  }
  else{
    topIcon.style.display = "none"; // THIS REMOVES THE TOP ICON scroll
  }
});
