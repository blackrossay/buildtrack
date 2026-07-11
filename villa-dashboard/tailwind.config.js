/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#f3f9ea',
          100: '#e3f1cf',
          200: '#c9e5a5',
          300: '#a8d472',
          400: '#8ECA3C', // palette light
          500: '#499A13', // palette primary
          600: '#3d820f',
          700: '#276F27', // palette dark
          800: '#245a15',
          900: '#1f4a15',
          lime: '#BBDC12', // palette accent
        },
      },
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif', 'system-ui', '-apple-system', 'Segoe UI', 'Roboto', 'Helvetica', 'Arial', 'sans-serif'],
      },
      boxShadow: {
        card: '0 1px 2px rgba(16,24,40,.05), 0 1px 3px rgba(16,24,40,.06)',
        soft: '0 4px 20px rgba(16,24,40,.06)',
        pop: '0 12px 40px rgba(16,24,40,.14)',
      },
      borderRadius: {
        xl2: '1rem',
      },
      keyframes: {
        fadeUp: { '0%': { opacity: 0, transform: 'translateY(8px)' }, '100%': { opacity: 1, transform: 'none' } },
        scaleIn: { '0%': { opacity: 0, transform: 'scale(.96)' }, '100%': { opacity: 1, transform: 'none' } },
        slideIn: { '0%': { transform: 'translateX(100%)' }, '100%': { transform: 'none' } },
      },
      animation: {
        fadeUp: 'fadeUp .4s cubic-bezier(.32,.72,0,1) both',
        scaleIn: 'scaleIn .25s ease both',
        slideIn: 'slideIn .3s cubic-bezier(.32,.72,0,1) both',
      },
    },
  },
  plugins: [],
}
