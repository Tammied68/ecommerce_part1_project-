# Security & Access Control Plan – eCommerce Application

## 1. Authentication
- Use Django’s built‑in authentication system
- Passwords stored using secure hashing
- Login required for:
  - Uploading custom images
  - Checkout
  - Leaving reviews
  - Viewing order history

## 2. Authorization
- **Regular Users**
  - Can upload images
  - Can checkout
  - Can leave reviews
  - Can manage their own cart and profile

- **Admin Users**
  - Can manage products
  - Can manage orders
  - Can approve/remove reviews
  - Can manage user permissions

## 3. Data Security
- Validate uploaded images (file type, size)
- Sanitize file names
- Store uploads in MEDIA directory
- Use HTTPS in production
- Never store raw payment information
- Use environment variables for secrets (API keys, DB credentials)

## 4. API Security
- Use DRF permissions (IsAuthenticated, IsAdminUser)
- Use throttling to prevent abuse
- Validate all incoming data
- Return proper HTTP status codes

## 5. Database Security
- Use parameterized queries (Django ORM)
- Restrict admin access
- Regular backups
- Enforce strong password policies

## 6. Session & Token Security
- Use secure cookies
- Use CSRF protection
- Password reset tokens expire after a short time
