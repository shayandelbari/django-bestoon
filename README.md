# Bestoon

Bestoon is a Django-based web application for managing expenses and incomes. It provides APIs to submit expenses and incomes, and stores the data in a database.

## Features

- Submit expenses and incomes through POST requests
- User authentication using tokens
- Admin interface to manage expenses, incomes, and tokens

## Requirements

- Python 3.8+
- Django 5.0.3

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/django-bestoon.git
    cd django-bestoon
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:

    ```sh
    python manage.py migrate
    ```

5. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```sh
    python manage.py runserver
    ```

7. Access the application at `http://127.0.0.1:8000/`.

## API Endpoints

### Submit Expense

- **URL:** `/submit/expense/`
- **Method:** POST
- **Input:**
  - `date` (optional)
  - `text`
  - `amount`
  - `user` (token)
- **Output:**
  - `status: OK`

### Submit Income

- **URL:** `/submit/income/`
- **Method:** POST
- **Input:**
  - `date` (optional)
  - `text`
  - `amount`
  - `user` (token)
- **Output:**
  - `status: OK`

## Project Structure

- `bestoon/`: Main project directory
  - `asgi.py`: ASGI configuration
  - `settings.py`: Project settings
  - `urls.py`: URL configuration
  - `wsgi.py`: WSGI configuration
- `web/`: Application directory
  - `admin.py`: Admin interface configuration
  - `apps.py`: Application configuration
  - `models.py`: Database models
  - `tests.py`: Unit tests
  - `urls.py`: URL configuration for the app
  - `views.py`: View functions
  - `migrations/`: Database migrations

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
