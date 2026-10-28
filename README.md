

# Vehicle Rental Management System

A simple, menu-driven Vehicle Rental Management System built using Python to manage vehicle records, rent vehicles, process returns, and calculate rental fees.

## About

This project is a console-based application that manages a fleet of up to **10 vehicles**. Users can add vehicles, view available vehicles, rent vehicles for a specified number of hours, return rented vehicles, and view currently rented vehicles.

The system calculates rental fees based on the vehicle's hourly rental rate and the rental duration.

## Features

- Display available vehicles
- Add new vehicles
- Assign unique IDs to vehicles
- Store vehicle models and hourly rental rates
- Prevent duplicate vehicle IDs
- Validate rental rates
- Rent available vehicles
- Set rental duration in hours
- Calculate total rental fees
- Return rented vehicles
- Display rented vehicles
- Track available vehicle capacity
- Handle invalid menu choices

## Technologies Used

- Python

## Python Concepts Practiced

- Variables and data types
- Lists
- Dictionaries
- Functions
- `while` loops
- `for` loops
- Conditional statements
- User input using `input()`
- Type conversion using `int()` and `float()`
- List methods such as `append()` and `remove()`
- Dictionary operations
- F-strings
- Arithmetic operations
- Data validation

## How It Works

### 1. Show Available Vehicles

Displays the number of available vehicles and their IDs, models, and hourly rental rates.

### 2. Add a Vehicle

Allows the user to enter a vehicle ID, model, and rental rate. The system prevents duplicate IDs and rejects rates that are zero or negative.

### 3. Rent a Vehicle

Allows the user to select an available vehicle and enter the rental duration in hours.

The vehicle is moved to the rented vehicles list, and the rental fee is calculated.

### 4. Calculate Rental Fee

The rental fee is calculated using the following formula:

```text
Total Rental Fee = Rental Hours × Hourly Rate
```

**Example:**

- Vehicle hourly rate: Rs. 500
- Rental duration: 4 hours
- Total rental fee: Rs. 2,000

### 5. Return a Vehicle

Allows the user to return a rented vehicle. The system displays the rental fee and moves the vehicle back to the available vehicles list.

### 6. Show Rented Vehicles

Displays the IDs, models, rental durations, and fees of all currently rented vehicles.

## Menu Options

| Option | Function |
|---|---|
| 0 | Exit |
| 1 | Show Available Vehicles |
| 2 | Add Vehicle |
| 3 | Rent Vehicle |
| 4 | Return Vehicle |
| 5 | Show Rented Vehicles |

## How to Run

1. Clone or download the repository.
2. Open the project folder in your code editor.
3. Make sure Python is installed.
4. Run the following command in the terminal:

```bash
python Vehicle_Rental_Management_System.py
```

## Data Storage

The application uses Python lists and dictionaries to store vehicle information.

- `vehicles` stores available vehicles.
- `rented_vehicles` stores currently rented vehicles.
- `total_vehicles` sets the maximum fleet capacity to 10 vehicles.

The data is stored in memory and is lost when the program closes.

## Purpose

This project was created to practice Python programming fundamentals by building a practical vehicle rental application.

## Future Improvements

- Add customer information
- Add vehicle search functionality
- Track rental dates and times
- Support different vehicle categories
- Save records permanently using file handling
- Connect the system to a database
- Improve input validation
- Add a graphical user interface

## Author

**Fatima Aziz**

GitHub: [fatimaaziz27](https://github.com/fatimaaziz27)

