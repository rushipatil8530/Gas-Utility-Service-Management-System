# Gas-Utility-Management-System

## Overview

The Gas Utility Service Request Management System is a web application built with Django, designed to facilitate the management of service requests for a gas utility company. It provides functionalities for customers to submit requests, track their status, and for staff members to manage the workflow efficiently.

## Features

- **User Authentication**: Secure login system for customers and staff members.
- **Service Request Submission**: Customers can easily submit service requests through a user-friendly interface.
- **Service Request Tracking**: Users can track the status of their service requests in real-time.
- **order Dashboard**: Staff members have access to a dashboard for viewing, assigning, and managing service requests.
- **Workflow Management**: Define and customize workflow stages for handling service requests.
- **Reporting**: Generate reports and analytics to analyze performance and identify areas for improvement.

## Installation

1. **Clone the Repository**: 
   ```
   https://github.com/rushipatil8530/Gas-Utility-Service-Management-System.git
   ```

2. **Install Dependencies**: 
   ```
   cd Gas_utility_project
   pip install -r requirements.txt
   ```

3. **Database Setup**:
   - Configure your database settings in `settings.py`.
   - Run migrations to create database schema:
     ```
     python manage.py migrate
     (you can also use mysql or other database)
     ```

4. **Environment Variables**:
   - Create a `.env` file based on `.env.example` and configure the necessary environment variables.

5. **Start the Server**:
   ```
   python manage.py runserver
   ```

6. **Access the Application**:
   - Open a web browser and navigate to `http://localhost:8000` to access the application.

## Usage

- **Customer Portal**: Customers can log in, submit service requests, and track their status.
- **Staff Dashboard**: Staff members can log in, view incoming service requests, assign them to appropriate personnel, and update their status as they are processed.
- **Workflow Configuration**: Admin users can customize the workflow stages and permissions through the admin panel.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Some Pictures Of Project


---

You can adjust this README to fit your project structure and specific implementation details. Let me know if you need further assistance!
![image](https://github.com/rushipatil8530/Gas-Utility-Service-Management-System/assets/145107024/4b6b2f07-370e-41b5-9a2a-233f6a6c9ac1)

![image](https://github.com/rushipatil8530/Gas-Utility-Service-Management-System/assets/145107024/d1fe4b57-5859-4e69-9099-408dc209ea84)

![image](https://github.com/rushipatil8530/Gas-Utility-Service-Management-System/assets/145107024/d35b2cb6-832b-4cf3-919f-b3040843e02f)

![image](https://github.com/rushipatil8530/Gas-Utility-Service-Management-System/assets/145107024/9c644bd4-1d41-4c74-9078-cb2450a02cbd)

![image](https://github.com/rushipatil8530/Gas-Utility-Service-Management-System/assets/145107024/9e47bce5-2e36-4b79-b585-ea3345250e3d)
