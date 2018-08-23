---
title: Testimonials
---
<div v-for="item in myJson">
  <h1>{{ item['business-name'] }}</h1>
  <h2>Testimonials from {{ item['business-name']}}'s customers</h2>

  {{ item['customer-name'] }} says:
  > "{{ item['review'] }}"

  {{ item['customer-name'] }} says:
  > "{{ item['review'] }}"

  {{ item['customer-name'] }} says:
  > "{{ item['review'] }}"

  <h2>{{ item['call-to-action'] }}</h2>

  [ {{ item['contact-number'] }} ](tel:{{item['contact-number']}}) <!--fix-->

  [ {{ item['contact-email'] }} ](mailto:{{item['contact-email']}}) <!--fix-->

  <p>{{ item['business-address'] }}</p>

</div>

<script>
  import json from './data.json'

  export default {
    data () {
      return {
        myJson: json,
      };
    },
  }
</script>
