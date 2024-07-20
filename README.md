# ExpertHandymanServices

ExpertHandymanServices provides handyman services for customers at their homes. This README will guide you through the setup and usage of the application, including how to manage database migrations with Flask-Migrate.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
  - [Using Flask-Migrate](#using-flask-migrate)
    - [Initial Setup](#initial-setup)
    - [Making Model Changes](#making-model-changes)
    - [Generating and Applying Migrations](#generating-and-applying-migrations)
- [Running the Application](#running-the-application)
- [Usage](#usage)

## Installation

Instructions on how to install and set up the project.

1. Clone the repository:
    ```sh
    git clone https://github.com/kedabdure/expert-handyman.git
    cd expert-handyman
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

Create a `.env` file in the root directory and add your configuration variables, for example:

```env
FLASK_APP=app.py
FLASK_ENV=development
SQLALCHEMY_DATABASE_URI=sqlite:///site.db
SECRET_KEY=your_secret_key
