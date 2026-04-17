# 🛒 eCommerce Application (Capstone Submission)

## 📌 Overview

This project is a Django-based eCommerce application developed as part of a capstone assignment. It demonstrates full-stack development skills including authentication, role-based access control, database design, and application structure using Django.

The system supports multiple user roles and allows structured interaction between buyers, vendors, and administrators.

---

## ✨ Key Features

* User authentication (login/logout)
* Role-based access control
* Product browsing and detail views
* Product review functionality
* Vendor store creation and management
* CRUD operations for products
* Django admin for full system control

---

## 👥 User Roles

### Buyer

* Browse available products
* View product details
* Leave reviews

### Vendor

* Create and manage stores
* Add, edit, and delete products

### Admin

* Full access via Django Admin
* Manage users, stores, products, and reviews

---

## 🛠️ Tech Stack

* Python
* Django
* HTML / Django Templates
* MySQL
* Django Admin

---

## ⚙️ Installation & Setup (Local Environment)

### 1. Clone the Repository

```bash
git clone https://github.com/Tammied68/ecommerce_part1_project-.git
cd ecommerce_part1_project-
```

### 2. Create & Activate Virtual Environment

#### macOS / Linux

```bash
python -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\\Scripts\\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Database

Update `settings.py` with your MySQL credentials:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "your_database_name",
        "USER": "your_mysql_username",
        "PASSWORD": "your_mysql_password",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/

```

---

## 🔐 Admin Panel

Access the admin panel at:

```
http://127.0.0.1:8000/admin/
```

---

## 📂 Project Structure

```
ecommerce_project/   # Main Django project
planning_app/        # Planning-related logic
products/            # Product models and views
stores/              # Store management
templates/           # HTML templates
docs/                # Documentation
manage.py
requirements.txt
README.md
```

---

## 📚 Documentation

Documentation for this project is included in the `docs/` folder.

---

## ⚠️ Notes for Reviewers

* Ensure MySQL is running before starting the project
* Database credentials must be configured locally
* No sensitive data is stored in this repository
* Virtual environments and system files are excluded via `.gitignore`

---

## 🚀 Capstone Requirements Covered

* ✔ Django application development
* ✔ Role-based access control
* ✔ Database integration (MySQL)
* ✔ Version control (Git/GitHub)
* ✔ Project documentation

---

## 👩‍💻 Author

**TammieD**
