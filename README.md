# Weather_App_Django

A Django-based web application that fetches real-time weather data for a given city using the OpenWeather API and displays a relevant city image from Unsplash.

## Features

- **Real-time Weather Data**: Fetches current weather conditions (temperature, description, and icon) for any city using the OpenWeather API.
- **City Images**: Displays a beautiful image of the city using the Unsplash API.
- **User-Friendly Interface**: Simple and intuitive interface for users to input a city name and view weather details.
- **Default City**: If no city is provided, the app defaults to Nairobi.

## Technologies Used

- **Django**: A Python-based web framework for building the application.
- **OpenWeather API**: Provides real-time weather data.
- **Unsplash API**: Fetches high-quality images of cities.
- **Bootstrap**: For styling the frontend (optional, if used in your templates).

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Django
- `requests` library (for making API calls)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone [https://github.com/your-username/weather-app.git](https://github.com/your-username/weather-app.git)
   cd weather-app
````

2.  **Set Up a Virtual Environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up API Keys**:

      * Obtain an API key from OpenWeather and Unsplash.
      * Replace the placeholders in the `views.py` file with your actual API keys:
        ```python
        UNSPLASHAPIKEY = "yourunsplashapikey"
        OPENWEATHERAPIKEY = "youropenweatherapikey"
        ```

5.  **Run Migrations**:

    ```bash
    python manage.py migrate
    ```

6.  **Start the Development Server**:

    ```bash
    python manage.py runserver
    ```

7.  **Access the Application**: Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

1.  On the homepage, enter the name of a city in the input field and click "Search."
2.  The app will display:
      - Current weather conditions (temperature, description, and weather icon).
      - A beautiful image of the city.
3.  If no city is entered, the app defaults to Nairobi.

## Project Structure

```
weather-app/
├── manage.py
├── weather_app/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── (CSS, JS, and images)
└── README.md
```

## Live Site

You can access the live version of this project at:  
[Live Weather App](https://www.google.com/url?sa=E&source=gmail&q=your-pythonanywhere-username.pythonanywhere.com)  *(Replace `your-pythonanywhere-username`)*

## Screenshots

*Example: Weather details for Nairobi with a city image.*  *(Add screenshot here)*

## Contributing

Contributions are welcome\! If you'd like to contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeatureName`).
3.  Commit your changes (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature/YourFeatureName`).
5.  Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

  - OpenWeather for providing the weather data API.
  - Unsplash for providing high-quality images.
  - Django and the Python community for their amazing tools and libraries.

## Contact

For questions or feedback, feel free to reach out:

  - **Your Name**
  - **Email**: your.email@example.com
  - **GitHub**: your-username

<!-- end list -->

```
```
