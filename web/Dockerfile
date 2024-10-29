FROM node:15.14.0 as dev

WORKDIR /app/web

RUN npm install -g @vue/cli

COPY package.json ./

COPY package-lock.json ./

RUN npm install

COPY . /app/web/

CMD npm run serve

FROM node:15.14.0 as build

WORKDIR /app/web

COPY package.json package-lock.json ./

RUN npm install -g @vue/cli && npm install

COPY . /app/web/

FROM node:15.14.0 as production

WORKDIR /app/web

COPY --from=build /app/web .

RUN npm run build

FROM nginx:stable-alpine as final

COPY --from=production /app/web/dist /usr/share/nginx/html

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
