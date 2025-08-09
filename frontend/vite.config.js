import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      // Your existing proxy configuration
      '/api': 'http://localhost:5000'
    }
  }
})
