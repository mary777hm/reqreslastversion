Description

Reqreslastversion is a Python-based testing project designed to validate API endpoints using the ReqRes API. The project includes tests for various HTTP methods including GET, POST, PUT, PATCH, and DELETE requests. It leverages pytest for test execution and Allure for generating detailed test reports.
Table of Contents

    Features
    Installation
    Usage
    Configuration
    Testing
    Contributing
    License
    Acknowledgements

Features

    GET Requests: Test endpoints for listing users, single user retrieval, and handling delays.
    POST Requests: Validate user registration and login functionalities.
    PUT/PATCH Requests: Test updating user information.
    DELETE Requests: Verify user deletion.
    Allure Reporting: Integration for detailed test reports.

Installation

To set up the project locally, follow these steps:

    Clone the Repository:

    git clone <repository-url>
    cd reqresnew

    Set Up a Virtual Environment (recommended):

    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    Install Dependencies:

    pip install -r requirements.txt

    Install Allure: Follow the Allure installation guide to install Allure CLI.

Usage
Running Tests

To execute the tests, use the following command:

pytest --alluredir=allure-results

