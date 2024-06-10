# Parts Unlimited API
This is a service built for Parts Unlimited that exposes a API that allows CRUD operations on parts.
The solution is built using python 3.12 with [django](https://www.djangoproject.com/) and [django-rest-framework](https://www.django-rest-framework.org/).
## How to run

Steps to run the service along with a database(MariaDB)

1. Install [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/)
1. Clone the repository
1. Build app and run all containers with `docker compose up -d`
1. After both the database and the app are ready you will be able to access it at 127.0.0.1:8000 

## Endpoints
All available endpoints are documented within the app at 127.0.0.1:8000/swagger/
