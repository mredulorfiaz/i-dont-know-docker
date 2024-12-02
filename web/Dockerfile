FROM node:15.14.0 AS dev

WORKDIR /app/web

ENV BASE_URL="http://localhost:5051/api"

COPY package.json package-lock.json ./

RUN npm install -g @vue/cli && npm install

COPY . .

EXPOSE 8080

CMD ["npm", "run", "serve"]

FROM node:15.14.0 AS prod

WORKDIR /app/web

COPY --from=dev /app/web .

RUN npm run build

FROM nginx:stable-alpine AS prod-static

COPY --from=prod /app/web/dist /usr/share/nginx/html

COPY nginx.conf /etc/nginx/nginx.conf
