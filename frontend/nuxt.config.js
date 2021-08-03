export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'moonshot',
    htmlAttrs: {
      lang: 'en',
     


    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: 'https://www.leanix.net/hubfs/LeanIX_favi.png' },
      {
        rel: 'stylesheet',
        href: 'http://fonts.cdnfonts.com/css/axiforma'
      },
      {
        rel: 'stylesheet',
        href: 'https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css'
      }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/tailwindcss
    '@nuxtjs/tailwindcss',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    '@nuxtjs/axios'
  ],
  axios: {
    baseURL: 'http://localhost',
    // browserBaseURL: 'http://localhost/8000'
    // dev: http://localhost
    // prod: http://knowlix.duckdns.org

  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  }
}
