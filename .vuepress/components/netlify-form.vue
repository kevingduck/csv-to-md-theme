<template>
<form name="new-website" action="https://formspree.io/tensorwebservices@gmail.com" method="POST" netlify>
  <ul style="list-style:none">
    <input type="hidden" name="_next" value="/go.html" />
    <input type="hidden" name="_subject" value="New request to build a website!" />
    <input type="text" name="_gotcha" style="display:none" />
    <p>Your Contact Info:</p>
    <input type="text" name="_replyto" placeholder="Your email (the link to the new site will be sent to this email address)" />
    <p>Your Business's Info:</p>
    <li><input type="text" name="business-name" placeholder="Business Name"></li>
    <li><input type="text" name="tagline" placeholder="Tagline"></li>
    <li><input type="text" name="contact-number" placeholder="Business Contact Phone Number"></li>
    <li><input type="text" pname="contact-email" placeholder="Business Contact Email Address"></li>
    <li><input type="text" name="business-address" placeholder="Business Address"></li>
    <li><input type="text" name="specialty" placeholder="Business Specialty"></li>
    <li><input type="text" name="business-description" placeholder="Business Description"></li>
    <p>List Your Products/ Services:</p>
    <li><input type="text" name="pr1" placeholder="Product 1"></li>
    <li><input type="text" name="pr1-desc" placeholder="Product 1 Description"></li>
    <li><input type="text" name="pr2" placeholder="Product 2"></li>
    <li><input type="text" name="pr2-desc" placeholder="Product 2 Description"></li>
    <li><input type="text" name="pr3" placeholder="Product 3"></li>
    <li><input type="text" name="pr3-desc" placeholder="Product 3 Description"></li>
  </ul>
  <p>
    <button id="form-button" value="Generate site" type="submit">Generate site</button>
  </p>
</form>
</template>
