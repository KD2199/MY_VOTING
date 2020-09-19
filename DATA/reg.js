function check()
    {
      var name=document.getElementById('email');
      var pwd=document.getElementById('password');
      var rpass=document.getElementById('rpassword');
      var voting_id=document.getElementById('vid');
      var mob_no=document.getElementById('mobile');
      var uname=document.getElementById('uname');

      if(uname.value.trim()=="" )
      {
        //alert("Username is blank...");
        document.getElementById("12").style.visibility="visible";
        return false;
      }

      else if(voting_id.value.trim()=="" )
      {
        //alert("Username is blank...");
        document.getElementById("10").style.visibility="visible";
        return false;
      }
      else if(name.value.trim()=="" )
      {
        //alert("Username is blank...");
        document.getElementById("7").style.visibility="visible";
        return false;
      }
      else if(mob_no.value.length<10 )
      {
        //alert("Username is blank...");
        document.getElementById("11").style.visibility="visible";
        return false;
      }
      else if(pwd.value.length<8)
      {
        /*alert("Password is too short...");*/
        document.getElementById("8").style.visibility="visible";
        return false;
      }
      else if(pwd.value!=rpass.value)
      {
        //alert("Password is blank...");
        document.getElementById("9").style.visibility="visible";
        return false;
      }
      {
        true;
        alert("Registration Successfull!!!");
      }
    }