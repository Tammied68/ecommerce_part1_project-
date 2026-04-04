# System Requirements – eCommerce Application

## 1. Overview
This system is an online eCommerce platform where users can browse products, upload custom images for t‑shirt designs, manage a shopping cart, place orders, and leave reviews. Admin users can manage products, orders, and user permissions.

---

## 2. User Types and Their Requirements

### Guest Users
- Browse products
- View product details
- Add items to cart
- Register for an account
- View reviews

### Registered Users
- Log in securely
- Upload images for custom t‑shirt designs
- Select product size, color, and quantity
- Add/remove items from cart
- Checkout and pay
- View order history
- Leave verified or unverified reviews
- Reset forgotten password via email

### Admin Users
- Add, update, or delete products
- Approve or remove reviews
- Manage orders
- Manage user permissions
- View system activity logs

---

## 3. Functional Requirements

### Product Management
- Display product listings
- Display product details
- Support image uploads for custom designs
- Allow admin CRUD operations

### Cart & Checkout
- Add/remove items
- Update quantities
- Persist cart for logged‑in users
- Process checkout and payment
- Validate payment responses

### User Accounts
- Registration and login
- Password reset via email token
- Profile management

### Reviews
- Users can leave reviews
- Admin can approve or remove reviews

### API Requirements
- REST API endpoints for all major features
- Authentication required for protected endpoints

---

## 4. Non‑Functional Requirements
- Secure authentication and authorization
- Fast and responsive user interface
- Scalable backend architecture
- Proper validation for uploads and forms
- Error logging and monitoring
- Data integrity and consistency
