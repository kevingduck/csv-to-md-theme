---
title: Products & Services
---
<div v-for="item of myJson">
  <h1>{{ item['business-name'] }}</h1>
  <h2>{{ item['tagline'] }}</h2>
  <h4>{{ item['specialty'] }}</h4>

  > {{item['pr1']}}

  {{item['pr1-desc']}}

  > {{item['pr2']}}

  {{item['pr2-desc']}}

  > {{item['pr3']}}

  {{item['pr3-desc']}}

  > {{item['pr4']}}

  {{item['pr4-desc']}}

  > {{ item['call-to-action'] }}

  [ {{ item['contact-number'] }} ](tel:{{item['contact-number']}}) <!--fix-->

  [ {{ item['contact-email'] }} ](mailto:{{item['contact-email']}}) <!--fix-->

  <p>{{ item['business-address'] }}</p>
</div>

<script>
  import json from './data.json'

  export default {
    data() {
      return {
        myJson: json,
      };
    },
  }
</script>
