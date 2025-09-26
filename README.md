# Poll Project

## Description
The Poll Project is a Django-based web application that allows users to create and participate in polls. It features a clean user interface built with Bootstrap, a robust backend for managing questions and choices, and an administrative interface for content management. This project serves as a practical example of building a full-stack web application using Django.

## Features
*   **User-Friendly Polling:** Create and vote on questions with multiple choices.
*   **Dynamic Content Display:** Displays the latest poll questions on the homepage.
*   **Detailed Poll Views:** View individual poll questions and their choices.
*   **Real-time Results:** See the current vote counts for each choice.
*   **Administrative Interface:** Django's built-in admin site for easy management of questions and choices.
*   **Responsive Design:** Utilizes Bootstrap for a mobile-first and responsive user experience.
*   **Modular Application Structure:** Divided into `landingPage` and `pollApp` for clear separation of concerns.

## Technologies Used
*   **Backend:**
    *   Python 3.x
    *   Django 4.x
    *   Django REST Framework (though not fully utilized in the provided code, it's included in dependencies)
    *   SQLite3 (default database)
*   **Frontend:**
    *   HTML5
    *   CSS3 (with Bootstrap 4.4.1)
    *   JavaScript (minimal, for Bootstrap functionality)
*   **Dependency Management:**
    *   Pipenv (Pipfile)
    *   pip (requirements.txt)

## Getting Started

### Prerequisites
*   Python 3.x installed on your system.
*   Pipenv (recommended for dependency management): `pip install pipenv`

### Installation Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/alx-project-nexus.git
    cd alx-project-nexus
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd pollProject
    ```

3.  **Install dependencies:**
    If using Pipenv (recommended):
    ```bash
    pipenv install
    pipenv shell
    ```
    Alternatively, using pip:
    ```bash
    pip install -r ../requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create your admin username and password.

### Running the Application

1.  **Start the Django development server:**
    ```bash
    python manage.py runserver
    ```

2.  **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:8000/`.

3.  **Access the Admin Panel:**
    Navigate to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials you created.

## Project Structure

```
alx-project-nexus/
├── .gitignore
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── render.yaml
├── requirements.txt
└── pollProject/
    ├── manage.py
    ├── landingPage/          # Handles the main landing page
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py         # No models defined
    │   ├── tests.py
    │   ├── urls.py           # Defines URL patterns for the landing page
    │   └── views.py          # Renders the landing page
    ├── pollApp/              # Core polling application
    │   ├── __init__.py
    │   ├── admin.py          # Registers models for the admin interface
    │   ├── apps.py
    │   ├── models.py         # Defines Question and Choice models
    │   ├── tests.py
    │   ├── urls.py           # Defines URL patterns for polls (detail, results, vote)
    │   └── views.py          # Handles poll logic (index, detail, results, vote)
    ├── pollProject/          # Main project configuration
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py       # Project settings (database, installed apps, templates)
    │   ├── urls.py           # Main URL dispatcher, includes app URLs
    │   └── wsgi.py
    └── templates/            # HTML templates
        ├── base.html         # Base template with Bootstrap integration
        ├── index.html        # Empty, likely superseded by pages/index.html
        ├── pages/
        │   └── index.html    # Landing page content
        ├── partials/
        │   └── _navbar.html  # Navigation bar partial
        └── polls/
            ├── detail.html   # Displays poll question and choices
            ├── index.html    # Lists latest poll questions
            └── results.html  # Displays poll results
```

## Usage

*   **Homepage:** Access the main landing page at `/`.
*   **Polls List:** View the latest poll questions at `/polls/`.
*   **Vote:** Click "Vote Now!" on a poll question to see details and cast your vote.
*   **Results:** Click "Results!" to see the current voting statistics for a poll.
*   **Admin:** Log in to the Django admin at `/admin/` to add, edit, or delete poll questions and choices.

## Contributing
Contributions are welcome! Please feel free to fork the repository, create a new branch, and submit a pull request with your improvements.

## License
This project is licensed under the [LICENSE](LICENSE) file.

## Acknowledgments
*   Django Documentation
*   Bootstrap
