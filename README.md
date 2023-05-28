# Scanning Platform(Under Development)

This is a scanning platform that allows users to input information and communicate with Greenbone for scanning purposes. It provides a user-friendly interface and generates reports based on the scan results.

## Branch: feature/flask-development

This branch focuses on the Flask development of the scanning platform. It includes the implementation of routes, views, forms, and other Flask-related components to handle user interactions and integrate with the Greenbone API for scanning functionality.

## Installation

To install and run the scanning platform, follow the steps below:

1. Clone the repository
2. Create and activate a virtual environment
3. Install the depencies:

    pip install -r requirements.txt

4. Run the Flask development server:

    flask run

5. Access the application in web browser

## Usage(Planned)

1. Log in.
2. Fill in the scan details in the provided form.
3. Submit the form to initiate the scanning process
4. Check for status of the process
5. View the generated reported for the scan results.

## Technologies Used

- Python
- Flask - Web framework
- SQLAlechemy - MySQL
- Docker - Greenbone
