# Storefront

A Django-based e-commerce backend API providing endpoints for product catalog, user authentication, customer management, ordering, and cart functionality.

## Features

- Custom user model and JWT authentication via Djoser.
- Product catalog including collections, products, and reviews.
- Cart and order management system.
- Asynchronous task processing using Celery and Redis.
- Background caching with Redis.
- API performance profiling using Django Silk and Debug Toolbar.

## Tech Stack

- Django 5.x
- Django REST Framework (DRF)
- Celery & Redis
- Djoser (JWT Authentication)
- SQLite (Default database)

## Project Structure

- `store`: Core e-commerce logic (products, collections, carts, orders, reviews, customers).
- `core`: Custom user management and authentication serializers.
- `tags` & `likes`: Generic content classification and user interaction models.
- `playground`: Experimental and background task endpoints.

## Getting Started

### Prerequisites

- Python 3.x
- Redis server running on `localhost:6379` (for Celery and caching).

### Installation & Setup

1. Clone the repository and navigate to the project root.
2. Create and activate a Python virtual environment.
3. Install the required dependencies.
4. Set up environment variables by copying `.env.example` to `.env`.
5. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the Django development server:
   ```bash
   python manage.py runserver
   ```
7. Start the Celery worker for background tasks:
   ```bash
   celery -A storefront worker --loglevel=info
   ```
8. Start the Celery beat scheduler:
   ```bash
   celery -A storefront beat --loglevel=info
   ```
