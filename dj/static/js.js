const name = document.getElementById("name");
const pass = document.getElementById("pass");
const email = document.getElementById("email");
function matchpassword(form){
    // var p1 =document.getElementById("pass");
     //var p2 =document.getElementById("pass1");
    var dec=/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{6,15}$/;
    if(form.pass.value.length==0){
        alert("password shouldn't be blanck");
        //return false;
    }
    else if(!form.pass.value.match(dec)){
        alert("enter a strong password");
       // return false;
    }
    else if(form.pass.value != form.pass1.value){
         alert("passwords doesn't match");
        // return false;
     }
     else if(form.pass.value == form.pass1.value && form.name.value.length != 0 && form.email.value.length !=0){
         alert("password confirmed");
         //return true;
     }
     else{
         alert("something wrong check once");
         //return false;
     }
 }