---
title: Blog
---
<div v-for="item of myJson">
  <h1>{{ item['business-name'] }}</h1>
  <h3>{{ item['blog-desc'] }}</h3>

  <h3>{{ item['blog-title']}}</h3>
  <h4>By {{ item['blog-post-author'] }}</h4>
  <p>{{ item['blog-post-content']}}</p>
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
