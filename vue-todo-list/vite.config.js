import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import autoprefixer from 'autoprefixer'
import { resolve, basename } from 'path'
import Components from 'unplugin-vue-components/vite'
import { BootstrapVue3Resolver } from 'unplugin-vue-components/resolvers'


export default defineConfig({
  resolve:{
    alias:{
      '@' : resolve(__dirname, './src'),
      '@c' : resolve(__dirname, './src/components'),
      '@api' : resolve(__dirname, './src/api'),
      '@plugins' : resolve(__dirname, './src/plugins'),
    },
  },
  plugins: [
    vue(),
    Components({
      resolvers: [BootstrapVue3Resolver()]
    })
  ],
  css: {
    postcss: {
        plugins: [
            autoprefixer,
        ],
    }
  },
})
