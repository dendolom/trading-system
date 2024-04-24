# Trading System API
Welcome to the Trading System API! This project provides a RESTful API for trading stocks, allowing authenticated users to place buy and sell orders and track their investments.

## Features
- **User Authentication:** Users can create accounts and log in to access trading functionalities.
- **Place Orders:** Authenticated users can place orders to buy or sell stocks.
- **Track Investments:** Users can track the overall value of their investments in each stock.
- **REST API:** Follows RESTful principles with well-defined endpoints for various operations.
- **Data Persistence:** Utilizes the Django ORM for data storage and retrieval.

## Architecture and Design
- **MVC Architecture:** The project follows the Model-View-Controller (MVC) architecture pattern:
  - **Model:** The models in `models.py` represent the data entities such as Users, Stocks, and Orders.
  - **View:** The views in `views.py` handle HTTP requests and responses, serving as the interface between the client and the application.
  - **Controller:** The business logic and request handling are implemented in the views and managers (`managers.py`), following the controller role in MVC.
- **SOLID Principles:** The project applies SOLID principles to improve code quality and maintainability:
  - **Single Responsibility Principle (SRP):** Each class and function has a single responsibility, making it easier to understand, test, and maintain.
  - **Open/Closed Principle (OCP):** The code is designed to be open for extension but closed for modification, allowing for new features to be added without modifying existing code.
  - **Liskov Substitution Principle (LSP):** Subclasses can be substituted for their base classes without affecting the functionality of the program.
  - **Interface Segregation Principle (ISP):** Interfaces are tailored to the needs of clients, preventing them from depending on methods they do not use.
  - **Dependency Inversion Principle (DIP):** High-level modules do not depend on low-level modules; both depend on abstractions. Abstractions do not depend on details; details depend on abstractions.
- **Object-Oriented Design (OOD):** The project leverages object-oriented design principles to create modular, reusable, and scalable code:
  - **Encapsulation:** Data and methods are encapsulated within classes, hiding internal implementation details and exposing a clean interface.
  - **Inheritance:** Subclasses inherit attributes and behaviors from their parent classes, promoting code reuse and specialization.
  - **Polymorphism:** Different classes can be treated interchangeably through inheritance and interfaces, allowing for flexibility and extensibility.
  - **Abstraction:** Complex systems are represented by simplified models, focusing on essential characteristics and hiding unnecessary details.

## Installation and Setup
1. Python version:
> Python 3.11
2. Install dependencies:
> pip install -r requirements.txt
3. Apply migrations to set up the database:
> python manage.py migrate
4. Start the development server:
> python manage.py runserver
5. Access the API endpoints using tools like cURL, Postman, or your web browser.


## API Endpoints
1. #### **Place Order:** `/api/place_order/` (POST)
- Allows authenticated users to place buy or sell orders for stocks.
2. #### **Retrieve Total Investment:** `/api/total_investment/<stock_id>/` (GET)
- Retrieves the total value invested in a single stock by a user.

## Testing
The project uses pytest for automated tests. To run the test:
> pytest -s


## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request for new features, bug fixes, or improvements.
