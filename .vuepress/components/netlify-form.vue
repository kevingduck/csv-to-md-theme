<template>
<form name='contact-form'>
  <p>
    <label>
      Your Contact Email (link will be sent to this email address): <input type="email" name="submitter_email" v-model="form.submitter_email" />
    </label>
  </p>
  <p>
    <label>
      Business Name <input type="text" name="business_name" v-model="form.business_name" />
    </label>
  </p>
  <p>
    <label>
      Tagline <input type="text" name="tagline" v-model="form.tagline" />
    </label>
  </p>
  <p>
    <button type="submit" @click.prevent="handleSubmit">Send</button>
  </p>
</form>
</template>




<script>
export default {
  data() {
    return {
      form: {
        business_name: '',
        submitter_email: '',
        tagline: '',
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
