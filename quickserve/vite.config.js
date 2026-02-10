import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'


// https://vite.dev/config/
export default defineConfig({
  server: {
    proxy: {
      "/api": {
        target: "https://quickserve.pythonanywhere.com",
        changeOrigin: true,
        secure: false,
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
    },
    host: true, // required to be accessible in the container network
    port: 5173,
    watch: {
      usePolling: true, // enables file watching in certain environments like WSL
    },
  },
  plugins: [react(),
  tailwindcss(), ],
})
