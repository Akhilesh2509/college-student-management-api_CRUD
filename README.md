# College Student Management API (Django)

This is a simple backend project built using Django to manage colleges and students.
It provides basic CRUD APIs for both entities and demonstrates how relational data works using ForeignKey.

---

## Project Overview

The system allows:

* Managing colleges
* Managing students linked to colleges
* Performing Create, Read, Update, Delete operations
* Searching and pagination for students
* Basic validation for inputs

---

## Tech Stack

* Python
* Django
* SQLite (default database)

---

## Setup Instructions

1. Clone the repository

```
git clone https://github.com/Akhilesh2509/college-student-management-api_CRUD.git
cd college_management
```

2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies

```
pip install django
```

4. Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser (for admin)

```
python manage.py createsuperuser
```

6. Run server

```
python manage.py runserver
```

---

## API Endpoints

### College APIs

| Method | Endpoint                   | Description        |
| ------ | -------------------------- | ------------------ |
| POST   | /api/colleges/create/      | Create college     |
| GET    | /api/colleges/             | Get all colleges   |
| GET    | /api/colleges/<id>/        | Get single college |
| PUT    | /api/colleges/update/<id>/ | Update college     |
| DELETE | /api/colleges/delete/<id>/ | Delete college     |

---

### Student APIs

| Method | Endpoint                   | Description        |
| ------ | -------------------------- | ------------------ |
| POST   | /api/students/create/      | Create student     |
| GET    | /api/students/             | Get all students   |
| GET    | /api/students/<id>/        | Get single student |
| PUT    | /api/students/update/<id>/ | Update student     |
| DELETE | /api/students/delete/<id>/ | Delete student     |

---

## Extra Features

* Pagination using query params (`page`, `limit`)
* Search students by name (`search`)
* Email and phone validation
* Proper error handling (404, 400, etc.)

---

## Testing

APIs can be tested using Postman.

Make sure to:

* Set `Content-Type: application/json`
* Use correct HTTP methods (GET, POST, PUT, DELETE)

---

## Project Structure

```
college_management/
│
├── student_management/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── college_management/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
```

---

## Author

Akhilesh Bajaj
BTech – Cloud Technology and Information Security

