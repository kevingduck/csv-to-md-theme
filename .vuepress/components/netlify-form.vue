<template>
<!-- <form name="new-website" action="https://formspree.io/tensorwebservices@gmail.com" method="POST" netlify> -->
  <form name="new-website" id="new-website" netlify>
  <ul style="list-style:none">
    <input type="hidden" name="_next" value="/go.html" />
    <input type="hidden" name="_subject" value="New request to build a website!" />
    <input type="text" name="_gotcha" style="display:none" />
    <div class="submitter-info">
      <h4>Your Contact Info:</h4>
      <li><input type="text"  class="form-control" name="_replyto" placeholder="Your email (the link to the new site will be sent to this email address)" /></li>
    </div>
    <div class="business-info">
      <h4>Your Business's Info:</h4>
      <li><input type="text" class="form-control" name="business-name" placeholder="Business Name"></li>
      <li><input type="text" class="form-control" name="tagline" placeholder="Tagline"></li>
      <li><input type="text" class="form-control" name="contact-number" placeholder="Business Contact Phone Number"></li>
      <li><input type="text" class="form-control" pname="contact-email" placeholder="Business Contact Email Address"></li>
      <li><input type="text" class="form-control" name="business-address" placeholder="Business Address"></li>
      <li><input type="text" class="form-control" name="specialty" placeholder="Business Specialty"></li>
      <li><textarea rows="3" class="form-control" type="text" name="business-description" placeholder="Business Description"></textarea></li>
    </div>
    <div class="services">
      <h4>List Your Business's Top Products/ Services:</h4>
      <li><input type="text" class="form-control" name="pr1" placeholder="Product 1"></li>
      <li><textarea rows="2" class="form-control" name="pr1-desc" placeholder="Product 1 Description"></textarea></li>
      <li><input type="text" class="form-control" name="pr2" placeholder="Product 2"></li>
      <li><textarea rows="2" class="form-control" name="pr2-desc" placeholder="Product 2 Description"></textarea></li>
      <li><input type="text" class="form-control" name="pr3" placeholder="Product 3"></li>
      <li><textarea rows="2" class="form-control" name="pr3-desc" placeholder="Product 3 Description"></textarea></li>
    </div>
  </ul>
  <p style="margin:10px;">
    <button class="btn btn-success btn-block" type="submit">Generate Site</button>
  </p>
</form>
</template>

<style>
.submitter-info {
  margin:10px;
  padding:10px;
  background-color: lightblue;
  }
  .business-info {
    margin:10px;
    padding:10px;
    background-color: lightgreen;
  }

  .services {
    margin:10px;
    padding:10px;
    background-color: lightblue;
  }


  form input {
    font-size: 16px;
    width:90%;
    height:30px;
  }
  li {
    margin:15px;
  }
  form h4 {
    margin:10px;
  }
</style>
