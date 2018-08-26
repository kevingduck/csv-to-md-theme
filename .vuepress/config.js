// .vuepress/config.js
module.exports = {
  title: 'FormToSite',
  themeConfig: {
    search: false,
    nav: [
      { text: 'FormToSite', link: '/' },
      { text: 'Demo', items: [
        { text: 'About', link: '/demo/about'},
        { text: 'Products', link: '/demo/products'},
        { text: 'Contact', link: '/demo/contact'},
        { text: 'Blog', link: '/demo/blog'},
        { text: 'Testimonials', link: '/demo/testimonials'},
      ]
    },
      { text: 'Advertise', link: '/advertise' },
    ]
  }
}
