/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./application/templates/**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        Helvetica: ["Helvetica", "Arial", "sans-serif"],
      },
    },
  },
  plugins: [],
};
