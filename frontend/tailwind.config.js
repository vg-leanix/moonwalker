module.exports = {
  
  purge:
    {
      content:[
      './components/**/*.{vue,js}',
      './layouts/**/*.vue',
      './pages/**/*.vue',
      './plugins/**/*.{js,ts}',
      './nuxt.config.{js,ts}',
    ],
    options: {
      safelist: [
        /data-theme$/,
      ]
    },
  
  },
  
  daisyui: {
    themes: [
      {
        'vg': {                          /* your theme name */
           'primary' : '#166bff',
           'primary-focus' : '#2474ff',     /* Primary color - focused */
           'primary-content' : '#fcfdff',   /* Foreground content color to use on primary color */

           'secondary' : '#5662f6',         /* Secondary color */
           'secondary-focus' : '#5662f6',   /* Secondary color - focused */
           'secondary-content' : '#ffffff', /* Foreground content color to use on secondary color */

           'accent' : '#37cdbe',            /* Accent color */
           'accent-focus' : '#16a5ff',      /* Accent color - focused */
           'accent-content' : '#ffffff',    /* Foreground content color to use on accent color */

           'neutral' : '#c0c3c3',           /* Neutral color */
           'neutral-focus' : '#2a2e37',     /* Neutral color - focused */
           'neutral-content' : '#ffffff',   /* Foreground content color to use on neutral color */

           'base-100' : '#ffffff',          /* Base color of page, used for blank backgrounds */
           'base-200' : '#f9fafb',          /* Base color, a little darker */
           'base-300' : '#d1d5db',          /* Base color, even more darker */
           'base-content' : '#1f2937',      /* Foreground content color to use on base color */

           'info' : '#2094f3',              /* Info */
           'success' : '#009485',           /* Success */
           'warning' : '#ff9900',           /* Warning */
           'error' : '#ff5724',           /* Primary color */

        },
      },
    ],
  },

  darkMode: false, // or 'media' or 'class'
  theme: {
    borderColor: theme => ({
      ...theme('colors'),
      'lix-main': '#166BFF',
      'lix-second': '#222F4B',
      'lix-third': '#4D5C7D'
    }),

    backgroundColor: theme => ({
      ...theme('colors'),
      'lix-main': '#166BFF',
      'lix-second': '#222F4B',
      'lix-third': '#4D5C7D'

    }),

    textColor: theme => ({
      ...theme('colors'),
      'lix': '#166BFF',
      'lix-second': '#222F4B'

    }),

    extend: {
      fontFamily: {
        'lix': ['Axiforma']
      },
      margin: {
        '18': '4.5rem',
      }
    }
  },
  variants: {

  },
  plugins: [
    require('daisyui'),
  ],
}
