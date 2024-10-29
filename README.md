# **I Don't Know Docker**

This project is one of the assignments of my internship at [Welcome Software](https://github.com/newscred). The main objective of this project is to learn working with docker by doing practice. So far, my progress is:

- Created a REST API with flask.
- Worked with MySQL database using an ORM **FlaskSQL-Alchemy**.
- Applied _Separation of concerns_ design principle while structuring API.
- Created a Single Page Application using Vue.js [Working on React version].
- Used docker and docker-compose to run these services using containers:
  - SPA as a service.
  - API as a service.
  - Database as a service.

## **Prerequisite**

Make sure you have docker installed. Use this commands below to check:

```bash
$ docker --version

> Docker version 20.10.6
```

## **How to start**

To run this project open your terminal on the project's root directory and run the command below:

```bash
$ docker compose up -d

> Build starts [....]
```

After building successfully, you can test the website by opening:

```bash
http://localhost:5050/
```

on your browser which will route you to the homepage of the Single Page Application like the screenshots below 👇.

## Dependency

In the docker-compose.yml three services have been introduced with the dependency cycle **(Web -> API -> DB)**:

- **Web**: Single page application built using Vuetify.js and Vuex.
- **API**: REST API developed using Flask and Flask-SQLAlchemy.
- **DB**: MySQL Database version 8.0.25.
