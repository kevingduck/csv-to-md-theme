---
title: Share a Meme
---

<form name="submitMeme" action="success.html" netlify>
  <p>
    <label>Name: <input type="text" name="name" size="40"></label>
  </p>
  <p>
    <label>Email: <input type="text" name="email" size="40"></label>
  </p>
  <p>
    <label>Meme URL: <input type="text" name="memeurl" size="40"></label>
  </p>
  <p>
    <button type="submit">Send</button>
  </p>
</form>


<form name="submitMeme" netlify-honeypot="bot-field" action="/succes.html" netlify>
  <p style="display:none;">
    <label>Don’t fill this out: <input name="bot-field"></label>
  </p>
</form>
