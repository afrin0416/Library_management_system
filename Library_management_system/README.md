# Library Management System (Django + DRF)

A RESTful API for managing books, authors, and library users with role-based permissions.  
This project uses Django, Django REST Framework, Djoser, and JWT for authentication, and `drf-yasg` for API documentation.

---

## Features

- **Role-based permissions**
  - Librarian: full access (add/update/delete books and users)
  - Member: view books, borrow/return books
- JWT authentication for secure API access
- Borrow and return system for books
- Clean nested JSON responses with serializers
- Auto-generated API documentation with Swagger and ReDoc

---

## Tech Stack

- Python 3.10+
- Django 4.x
- Django REST Framework
- Djoser (User management)
- SimpleJWT (JWT authentication)
- drf-yasg (Swagger / ReDoc API documentation)
- SQLite3 (default DB, can change to PostgreSQL/MySQL)

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd Library_management_system

---
