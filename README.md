# Django Docker Setup with PostgreSQL

This project runs a Django app with PostgreSQL using Docker. It includes Employee, Department, Attendance, and Performance models, with throttling enabled for API endpoints.

---

## 1. Prerequisites

- Docker Desktop installed
- Docker Compose installed
- Python 3.x installed (optional, for local management commands)
- Git installed

---

## 2. File Sharing (for Docker Desktop)

Before starting Docker, ensure the host directories are shared in Docker Desktop:

- Open Docker Desktop → Settings → Resources → File Sharing
- Add the following directories:

/media/dico/Important/Python-Projects/Assignment
/media/dico/Important/Python-Projects/Assignment/postgres-data

# Django Docker Setup with PostgreSQL

This project runs a Django app with PostgreSQL using Docker. It includes Employee, Department, Attendance, and Performance models, with throttling enabled for API endpoints.


- Apply & Restart Docker Desktop if prompted.

---

## 3. Clone the Repository

```bash
git clone <your-repo-url>
cd Assignment


run 
docker compose up --build

docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate


docker compose exec web python manage.py populate_initial_data

