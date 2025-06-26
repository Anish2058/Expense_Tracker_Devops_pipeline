FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# Inject env var for build-time API endpoint
ARG REACT_APP_API_URL
ENV REACT_APP_API_URL=$REACT_APP_API_URL

# Create optimized production build
RUN npm run build

# Install static server for production
RUN npm install -g serve

# Serve the build folder
EXPOSE 3000
CMD ["serve", "-s", "build", "-l", "3000"]
