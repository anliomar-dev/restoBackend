# 🍽️ Restaurant API - Le Banquet

This is the backend API for the restaurant website. It provides endpoints to view dishes, filter them by categories, and paginate the results.

## 🚀 Features

- **View Dishes**: Fetch a list of all dishes available in the restaurant.
- **Category Filtering**: Filter dishes by categories such as Starter, Breakfast, Lunch, Dinner, and Dessert.
- **Pagination**: Fetch results with pagination to display a limited number of dishes per page.

## 🛠️ Technologies Used

- **[Django](https://www.djangoproject.com/)**: Web framework for building the backend API.
- **[Django REST Framework (DRF)](https://www.django-rest-framework.org/)**: Toolkit for building APIs.
- **[MySQL](https://www.mysql.com/)**: Database used to store restaurant and dish data.

## 🌐 API Endpoints

### 1. **List Dishes**
- **Endpoint**: `/dishes/`
- **Method**: `GET`
- **Description**: Fetch a list of all dishes with pagination.
- **Query Parameters**:
  - `page`: Specify the page number for pagination (default is 1).
  
  Example:
production: https://omaranli.alwaysdata.net/dishes/?page=1
local: http://localhost:3000/dishes/?page=1

### 2. **Filter Dishes by Category**
- **Endpoint**: `/dishes/`
- **Method**: `GET`
- **Description**: Fetch dishes filtered by a specific category (e.g., starter, lunch).
- **Query Parameters**:
- `category`: Filter dishes by category. Categories available: `starter`, `breakfast`, `lunch`, `dinner`, `dessert`.
- `page`: Specify the page number for pagination (default is 1).

Example:
prod: https://omaranli.alwaysdata.net/dishes/?category=starter&page=1
local: http://localhost:3000/dishes/?category=starter&page=1

### 3 other endpoints
- **Reviews**: `GET https://omaranli.alwaysdata.net/reviews/`
    - Currently, you can only fetch reviews.
    - Authentication is required to submit reviews, but there is no authentication or registration system implemented yet. Therefore, reviews cannot be posted as of now.

- **Reservations**: `POST https://omaranli.alwaysdata.net/reservations/`
    - You can create reservations without needing authentication.


## 🔧 Local Setup

If you want to run the API locally, follow these steps:
 # 1. Clone the repository:
 ```bash
 git clone https://github.com/username/restoBackend.git
```
 cd restoBackend
 create a virtual environnement
 acitivate the virtual environnement
 then run:
```bash
  pip install -r requirements.txt
````

# 2 create .env file in the root folder if you use mysql or postgresql
DEBUG=True( in local) if you want to deploy your own version of the api you have to set DEBUG to False
SECRET_KEY=you_secret_jey
ALLOWED_HOSTS=localhost,127.0.0.1, and prod ulr if you want to deploy your own version
DATABASE_NAME=your_database_name
DATABASE_USER=you_database_user
DATABASE_PASSWORD=your_database_password
HOST=host(localhost for local)

The API will be accessible at http://localhost:8000/.
if you donn't want to use mysql database and want to quickly test the api localy, you can change configurations for database in settings and use sqlite database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

 # 3. Clone the repository:
 ```bash
 cd restoBackend
```bash
  python manage.py migrate
  python manage.py runserver
````

## Backend API Deployment
The backend API is hosted and available at:
Production URL: https://omaranli.alwaysdata.net/

For testing purposes, you can also interact with the API locally by running it on your development server.

## Authors
- [anliomar](https://github.com/anliomar-dev)


## Consuming the API
You can create your own frontend to consume the API and display dishes. The API is available at [https://omaranli.alwaysdata.net/](https://omaranli.alwaysdata.net/) and allows you to:
- Fetch dishes and restaurant data.
- Display the available dishes in a user-friendly interface.

## Contributing to the API
If you want to contribute to the backend, you can help improve the API by adding features like:
- Allowing users to create an account and log in.
- Enabling users to create a restaurant and add dishes specifically related to that restaurant.
- Allowing users to display their own dishes in their personalized interface.## Contributing

If you want to extend the functionality of this API, here are some ideas for improvements:

- **User Authentication**: Implement a user registration and authentication system to allow users to leave reviews and manage their own accounts.
  
- **Ordering System**: Add an ordering system so that users can place orders for dishes via the API.

- **Additional Models and Endpoints**: Feel free to add more features or models, such as a `User` model for customer management, or additional endpoints to handle things like dish ordering or payment processing.

You can fork or clone the project and adapt it to suit your needs by adding the necessary features. Once modified, submit a pull request, and the API can be improved to handle new functionality.
