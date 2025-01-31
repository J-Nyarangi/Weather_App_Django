# Weather App (Django)

A Django-based web application that fetches real-time weather data for a given city using the OpenWeather API.  It also displays a relevant image of the city, if available, using the Unsplash API.

## Features

*   **Real-time Weather Data:** Fetches current weather conditions (temperature, description, and icon) for any city using the OpenWeather API.
*   **City Image:** Displays a relevant image of the searched city using the Unsplash API.
*   **User-Friendly Interface:** Simple and intuitive interface for users to input a city name and view weather details.
*   **Default City:** If no city is provided, the app defaults to Nairobi.

## Technologies Used

*   **Django:** A Python-based web framework for building the application.
*   **OpenWeather API:** Provides real-time weather data.
*   **Unsplash API:** Fetches high-quality images of cities.
*   **Bootstrap, CSS:** For styling the frontend.

## Prerequisites

Before running the project, ensure you have the following installed:

*   Python 3.x
*   Django
*   `requests` library (for making API calls)

## Installation

1.  **Clone the Repository:**

    ```bash
    git clone [https://github.com/your-username/weather-app.git](https://github.com/your-username/weather-app.git)
    cd weather-app
    ```

2.  **Set Up a Virtual Environment:**

    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On Windows: myenv\Scripts\activate
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1.  **Migrate Database:**

    ```bash
    python manage.py migrate
    ```

2.  **Start the Development Server:**

    ```bash
    python manage.py runserver
    ```

3.  **Open your web browser and navigate to `http://127.0.0.1:8000/` to view the application.**

## API Keys

You will need to obtain API keys for both OpenWeather and Unsplash and add them to your project settings.  Create a `.env` file in your project's root directory and add the following:
