

FROM node:20-slim AS builder
WORKDIR /app


COPY package*.json ./
RUN npm install

# Copy the rest of the application code and build
COPY . .
# RUN npm run build


# Expose the port your app runs on
EXPOSE 5173
 
# Define the command to run your app
CMD ["npm", "run","dev"]

# Stage 2: Serve the application using Nginx
# FROM nginx:stable-alpine
# # Copy the built files from the builder stage to Nginx's public folder
# COPY --from=builder /app/build /usr/share/nginx/html

# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]


# Stage 1: Build the React app
# FROM node:20-alpine AS builder
# WORKDIR /app
# COPY package*.json ./
# RUN npm install
# COPY . .
# RUN npm run build

# # Stage 2: Serve the static files with Nginx
# FROM nginx:alpine
# # Copy the built files from the 'builder' stage to Nginx's serving directory
# COPY --from=builder /app/dist /usr/share/nginx/html
# # Expose port 80
# EXPOSE 80
# # Command to start Nginx
# CMD ["nginx", "-g", "daemon off;"]
