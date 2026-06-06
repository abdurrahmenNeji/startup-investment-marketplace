# Startup Investment Marketplace

A full-stack web application built with **Django REST Framework** and **Svelte**.  
The platform allows users to register, browse a product catalogue, create purchases, and view purchase history through a simple client interface.

## GitHub Repository Name

Recommended repository name:

```text
startup-investment-marketplace
```

Alternative names:

```text
django-svelte-ecommerce-platform
venture-capital-product-marketplace
ds1-django-svelte-shop
```

Suggested GitHub description:

```text
Full-stack Django REST and Svelte platform for user registration, product catalogue management, purchases, and purchase history.
```

## Features

- User/client registration form
- Product catalogue interface
- Purchase creation from the catalogue
- Purchase history page for a client
- Django REST API with serializers and API views
- Token-based API authentication for purchase endpoints
- PostgreSQL database configuration
- Svelte frontend with client-side routing
- Static media assets for product and interface visuals

## Tech Stack

### Backend

- Python
- Django
- Django REST Framework
- Django Token Authentication
- django-cors-headers
- PostgreSQL

### Frontend

- Svelte
- JavaScript
- Axios
- Svelte Routing
- Rollup
- CSS

## Project Structure

```text
DS1DJANGO/
│
├── djangods1/
│   ├── manage.py
│   ├── djangods1/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   └── APPLICATIONDS1/
│       ├── models.py
│       ├── serializers.py
│       ├── views.py
│       ├── admin.py
│       └── migrations/
│
└── svelte-app/
    ├── src/
    │   ├── App.svelte
    │   ├── inscription.svelte
    │   ├── profileCapitaux.svelte
    │   ├── achat_client.svelte
    │   └── style.css
    │
    ├── public/
    │   ├── images/
    │   ├── index.html
    │   └── global.css
    │
    ├── package.json
    └── rollup.config.js
```

## Main Database Models

### CapitalRisque

Stores client/investor information such as name, CIN, email, username, and password.

### Article

Stores product information such as name, description, price, and stock.

### Achat

Stores purchase transactions between a client and an article with a selected quantity.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Returns article list |
| `GET` | `/hello/` | Test endpoint |
| `GET` | `/capital-risque/` | List registered clients |
| `POST` | `/capital-risque/` | Register a new client |
| `POST` | `/capitalRisque/` | Register a new client |
| `GET` | `/articles/` | List all articles |
| `GET` | `/article/<article_id>/` | Get article details |
| `GET` | `/achats/` | List purchases |
| `POST` | `/achats/` | Create a purchase |
| `GET` | `/achats/client/<client>/` | Get purchases for a specific client |
| `POST` | `/api-token-auth/` | Generate authentication token |
| `GET` | `/admin/` | Django admin panel |

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/startup-investment-marketplace.git
cd startup-investment-marketplace
```

### 2. Backend Setup

Go to the Django backend folder:

```bash
cd djangods1
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

Install the required Python packages:

```bash
pip install django djangorestframework django-cors-headers psycopg2-binary
```

Update the database settings in `djangods1/settings.py` according to your local PostgreSQL configuration.

Then run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create an admin user:

```bash
python manage.py createsuperuser
```

Start the Django server:

```bash
python manage.py runserver
```

The backend will run by default at:

```text
http://127.0.0.1:8000/
```

### 3. Frontend Setup

Open another terminal and go to the Svelte frontend folder:

```bash
cd svelte-app
```

Install dependencies:

```bash
npm install
```

Run the frontend in development mode:

```bash
npm run dev
```

To build the frontend:

```bash
npm run build
```

To serve the production build:

```bash
npm run start
```

## Future Improvements

- Add a real login system for clients
- Replace hardcoded client IDs with authenticated users
- Improve product management from the admin dashboard
- Add stock validation before purchase
- Add order confirmation and total price calculation
- Improve frontend responsiveness
- Add form validation and error handling
- Add unit tests for API endpoints

## Author

Abdurrahmen Neji.
Developed as a full-stack academic project using Django REST Framework and Svelte.
