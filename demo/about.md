---
title: About
---
<div v-for="item of myJson">
  <h1>{{ item['business-name'] }}</h1>
  <h2>{{ item['tagline'] }}</h2>

  ::: tip Specialists in {{ item['specialty'] }}
  <span> </span>
  :::

  <span>{{ item['competitive-advantage'] }}</span>

  ::: warning Check out what our customers have to say
  <span> {{ item['review'] }}</span>
  :::

  <p>{{ item['business-description'] }}</p>

  > {{ item['call-to-action'] }}

  <p>{{ item['contact-number'] }}</p>

  <p>{{ item['contact-email'] }}</p>

  <p>{{ item['business-address'] }}</p>
</div>

<button v-on:click=downloadForm()>Click to get form data</button>

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
