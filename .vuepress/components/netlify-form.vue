<template>
<form>
  <p>
    <label>
      Your Name: <input type="text" name="name" v-model="form.name" />
    </label>
  </p>
  <p>
    <label>
      Your Email: <input type="email" name="email" v-model="form.email" />
    </label>
  </p>
  <p>
    <label>
      Message: <textarea name="message" v-model="form.message" />
    </label>
  </p>
  <p>
    <button type="submit" @click.prevent="handleSubmit">Send</button>
  </p>
</form>
</template>


<!-- <template>
  <form name="new-website" method="POST" action="/success.html" netlify>
    <ul style="list-style:none">
      <li>Your Contact Info:</li>
      <li><input type="text" name="submitter-email" placeholder="Your contact email (link will be sent to this email address)"></li>
      <li>Your Business's Info:</li>
      <li><input type="text" name="business-name" placeholder="Business Name"></li>
      <li><input type="text" name="tagline" placeholder="Tagline"></li>
      <li><input type="text" name="contact-number" placeholder="Business Contact Phone Number"></li>
      <li><input type="text" pname="contact-email" placeholder="Business Contact Email Address"></li>
      <li><input type="text" name="business-address" placeholder="Business Address"></li>
      <li><input type="text" name="specialty" placeholder="Business Specialty"></li>
      <li><input type="text" name="business-description" placeholder="Business Description"></li>
      <li>List Your Products/ Services:</li>
      <li><input type="text" name="pr1" placeholder="Product 1"></li>
      <li><input type="text" name="pr1-desc" placeholder="Product 1 Description"></li>
      <li><input type="text" name="pr2" placeholder="Product 2"></li>
      <li><input type="text" name="pr2-desc" placeholder="Product 2 Description"></li>
      <li><input type="text" name="pr3" placeholder="Product 3"></li>
      <li><input type="text" name="pr3-desc" placeholder="Product 3 Description"></li>
    </ul>
    <button type="submit">Generate site</button>
  </form>

</template> -->

<script>
export default {
  data() {
    return {
      form: {
        name: '',
        email: '',
        message: '',
      },
    };
  },
  methods: {
    encode(data) {
      return Object.keys(data)
        .map(
          key => `${encodeURIComponent(key)}=${encodeURIComponent(data[key])}`
        )
        .join('&');
    },
    handleSubmit() {
      fetch('/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: this.encode({ 'form-name': 'contact', ...this.form }),
      })
        .then(() => alert('Success!'))
        .catch(error => alert(error));
    },
  },
};
</script>
