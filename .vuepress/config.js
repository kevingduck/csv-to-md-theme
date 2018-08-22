// .vuepress/config.js
module.exports = {
  themeConfig: {
    search: false,
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Demo', items: [
        { text: 'About', link: '/demo/about'},
        { text: 'Products', link: '/demo/products'},
        { text: 'Contact', link: '/demo/contact'},
        { text: 'Blog', link: '/demo/blog'},
        { text: 'Testimonials', link: '/demo/testimonials'},
      ]
    }
    ]
  }
}
