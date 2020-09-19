
function myFunction() {
    var x = document.getElementById("password");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }

function check()
  {
    var name=document.getElementById('email');
    var pwd=document.getElementById('password');
    var op=document.getElementsByName('radio');
  
   
    if(name.value.trim()=="")
    {
      //alert("Username is blank...");
      document.getElementById("7").style.visibility="visible";
      return false;
    }
    else if(pwd.value.length<8)
    {

      //alert("Password is blank...");
      document.getElementById("8").style.visibility="visible";
      return false;
    }

    else
    {
      true;
     
      confirm("Login Successfully!!");
    }
  }