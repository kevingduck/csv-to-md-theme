Submit new form
<form name="contact" method="POST" data-netlify="true">
  <p>
    <label>Your Name: <input type="text" name="name" /></label>
  </p>
  <p>
    <label>Your Email: <input type="email" name="email" /></label>
  </p>
  <p>
    <label>Message: <textarea name="message"></textarea></label>
  </p>
  <p>
    <button type="submit">Send</button>
  </p>
</form>

<div id='success'>
  # Success!

  <h1>Success! Your site is being generated.</h1>

  <h2>Check your email for a link.</h2>

  <span>Or check the status of your site by entering your email address:</span>
  <p><input type="text" placeholder="Email Address"></p>
</div>

<style>
  #success {
    opacity: 0.0;
  }
</style>
