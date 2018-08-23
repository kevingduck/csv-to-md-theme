<div v-for="item of myJson">
  <h1>{{ item['business-name'] }}</h1>
  <h2>{{ item['tagline'] }}</h2>
  <h4>{{ item['specialty'] }}</h4>

  [Call {{ item['contact-number'] }}](tel:{{item['contact-number']}}) <!-- fix-->

  [Email {{ item['contact-email'] }}](mailto:{{item['contact-email']}}) <!-- fix-->

  Our address is

  > {{ item['business-address'] }}

  <h3>{{ item['call-to-action'] }}</h3>

</div>

<script>
  import json from './data.json'

  export default {
    data () {
      return {
        myJson: json,
      };
    },
    methods: {
      downloadForm () {
        console.log('downloading Form ...');
      }
    }
  }
</script>
