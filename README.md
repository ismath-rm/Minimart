# MiniMart – Refactored & Deployed Backend System

## **Objective**

This project focuses on refactoring the **MiniMart Django backend system**, implementing full CRUD operations for Customer, Order, and Product models using **Django Rest Framework (DRF)**. The backend has been deployed on **AWS EC2**, integrated with **AWS RDS for database management**, and SSL has been configured for secure communication. The project also includes comprehensive **Postman API documentation** with a performance goal of ensuring that all APIs respond in under 1 second.

## **Features**
1. **Project Structure & Code Quality**:
    - Refactored and organized the project into a modular Django app structure.
    - Consolidated duplicate files and moved business logic to appropriate folders.
    - Removed unused code and files for a cleaner and more maintainable codebase.
    - Replaced hard-coded values with environment variables for flexibility and security.
    - Improved naming conventions, code formatting, and separation of concerns for better readability and maintainability.

2. **CRUD Operations**:
   - Customer: Implemented full CRUD functionality to manage customer data.
   - Product: Implemented full CRUD functionality to manage product listings.
   - Order: Implemented full CRUD functionality to manage orders and related transactions.

3. **RESTful API Design**:
   - Created API endpoints using Django Rest Framework for efficient data interaction.
   - Ensured proper status codes, error handling, and validations are implemented.
   - Optimized for performance with response times under 1 second for all API requests.

4. **Deployment**:
   - Deployed the backend on AWS EC2 (Ubuntu instance) with Gunicorn as the application server and Nginx as the reverse proxy.
   - Integrated AWS RDS for PostgreSQL database hosting to ensure scalability and high availability.
   - Configured SSL with Let’s Encrypt to ensure secure, encrypted communications via HTTPS.

5. **Postman Documentation**
   - Documented all API endpoints in a Postman collection with detailed request and response examples.
   - Included request headers, body payloads, and sample output for each endpoint.
   - https://documenter.getpostman.com/view/36423727/2sB2j3Ar2H


## **Project Setup**
### **1. Clone the Repository**
Clone this repository to your local machine:

git clone https://github.com/ismath-rm/Minimart.git
cd MiniMart