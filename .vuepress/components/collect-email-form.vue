<template>
<form name="collect-email" action="https://formspree.io/tensorwebservices@gmail.com" method="POST">
  <ul style="list-style:none">
    <input type="hidden" name="_next" value="/status.html" />
    <input type="hidden" name="_subject" value="Check the status of this website!" />
    <input type="text" name="_gotcha" style="display:none" />
    <p>Still can't find the email? Enter the contact email address you used and check the status:</p>
    <input type="text" name="_replyto" placeholder="Email Address" />
  </ul>
  <p>
    <button id="form-button" value="Generate site" type="submit">Check status</button>
  </p>
</form>
</template>

<style>
  form {
    border: 1px solid grey;
    border-radius: 10px;
  }
  form input {
    font-size: 16px;
    width:90%;
    height:30px;
  }
  li {
    margin-top:15px;
  }
  #form-button {
    height:45px;
    margin:20px;
    width:80%;
    border-radius: 40px;
    background-color: lightgreen;
    font-size:18px;
    font-weight: 700;
    /* margin-left:40%; */
  }
</style>
