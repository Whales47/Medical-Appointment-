# Medical Appointment API

The Medical Appointment API is a robust backend service designed to manage appointments between patients and doctors in a clinical setting. It breaksdown  the process of scheduling, updating, and cancelling appointments, ensuring efficient utilization of medical resources and enhancing patient care through digital means.

## Key Features

- **Patient Management**: Supports full CRUD (Create, Read, Update, Delete) operations for patient records, enabling the maintenance of up-to-date patient information.
- **Doctor Management**: Facilitates CRUD operations for doctor records, including the ability to update availability status dynamically.
- **Appointment Scheduling**: Allows patients to book appointments, which are automatically assigned to doctors available. It prevents the occurence of double-booking by ensuring a doctor can only have one scheduled appointment with a patient at a time.
- **Appointment Management**: Provides functionality to approve and cancel appointments, thereby updating doctor availability in real-time.

## Technologies Used

- **Python**: A  high-level programming language that lets you work more efficiently and effectively, chosen for its readability and robust ecosystem.
- **FastAPI**: A modern web framework for building RESTful APIs in Python based on standard Python-type hints.
- **Pydantic**: A fast and powerful library that uses type hints to validate and serialize data.

