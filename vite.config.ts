import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  base: '/codebase-figma-alignment-demo/',
  plugins: [react()],
  resolve: {
    dedupe: ['react', 'react-dom'],
  },
})
