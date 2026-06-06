import svelte from 'rollup-plugin-svelte';
import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import serve from 'rollup-plugin-serve';
import livereload from 'rollup-plugin-livereload';
import terser from '@rollup/plugin-terser';
import css from 'rollup-plugin-css-only'; 



const production = !process.env.ROLLUP_WATCH;

export default {
  input: 'src/main.js', // Point d'entrée de votre application
  output: {
    sourcemap: true,
    format: 'iife',
    name: 'app',
    file: 'public/build/bundle.js', // Fichier de sortie
  },
  plugins: [
	svelte({
		compilerOptions: {
		  dev: !production,
		},
		emitCss: true, // Cette option est pour générer le fichier CSS
	  }),
	  
		css({ output: 'bundle.css' }),  // Ajout du plugin pour traiter les fichiers CSS
	  
    resolve({
      browser: true,
      dedupe: ['svelte'],
    }),
    commonjs(),
    !production &&
      serve({
        open: true,
        contentBase: ['public'], // Dossier où se trouve votre build
        historyApiFallback: true, // Gérer les routes côté client
        port: 5005,
      }),
    !production && livereload('public'),
    production && terser(), // Minification en production
  ],
  watch: {
    clearScreen: false,
  },
};
