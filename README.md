# eCommerce Application – Practical Task 1

## Overview
This project is a Django-based eCommerce application that supports buyers, vendors, and administrators. The application demonstrates role-based access control, authentication, and relational data modeling in a realistic online shopping scenario.

## Planning Documentation

This project includes a Planning Documentation folder containing design and pre‑implementation materials for Part 1 of the assignment.

The planning documents outline:
- Functional and non‑functional requirements
- User interface layout and navigation flow
- Security considerations and access control
- Failure‑handling and recovery strategies

These documents demonstrate system planning and design decisions made prior to implementation and support the completed Django application.

## User Roles
- **Buyer**
  - Browse products
  - View product details
  - Add products to a cart
  - Leave reviews
- **Vendor**
  - Create and manage stores
  - Add, edit, and delete products
- **Admin**
  - Manage users, stores, products, and reviews through Django Admin

## Key Features
- User registration and login
- Role-based access using a Profile model
- Vendor store and product management
- Buyer product browsing and reviews
- Password recovery using Django authentication
- Django Admin for data management

## Technologies Used
- Python
- Django
- HTML (Django Templates)
- SQLite / MariaDB (development)
- Django Admin

## Authentication
Authentication and password recovery are implemented using Django’s built-in authentication framework. Password reset emails are delivered via the console backend in development.

## How to Run
1. Activate virtual environment
2. Run migrations: python manage.py migrate
3. Start the development server: python manage.py runserver
4. Open the application in a browser: http://127.0.0.1:8000/