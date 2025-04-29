/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './src/**/*.html',
    './src/**/*.js',  
               // если шаблоны лежат в других местах
  ],
  darkMode: 'class',
  theme: {
    extend: {},
  },
  plugins: [],
  safelist: [
    'grid',
    'grid-cols-2',
    'bg-red-500',
    'bg-blue-500',
    'text-white',
    'p-10',
    'p-4',
    'gap-4',
    'dark'
  ],




}
