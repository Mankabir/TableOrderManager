# TableOrderManager

## Overview
TableOrderManager is a Python-based project designed to manage restaurant table orders. It streamlines the process of adding and removing orders, calculating bills, including service charges, and splitting the bill among diners.

## Code Explanation

### Class: Table
The `Table` class is the core of the project, managing orders for a restaurant table.

- **Initialization (`__init__(self, num_of_diners)`)**: Sets up a new table with the specified number of diners. Raises an error if the number of diners is zero.
- **Order Addition (`order(self, item, price, quantity=1)`)**: Adds an order to the table. If the same item (with the same price) is already ordered, it increments the quantity.
- **Order Removal (`remove(self, item, price, quantity=1)`)**: Removes a specified quantity of an item from the order. If the quantity to remove is more than what's in the order, it returns `False`.
- **Calculating Subtotal (`get_subtotal(self)`)**: Calculates the subtotal of all the items ordered at the table.
- **Calculating Total with Service Charge (`get_total(self, service_charge=0.10)`)**: Calculates the total bill including a service charge. The service charge percentage is customizable.
- **Splitting the Bill (`split_bill(self)`)**: Divides the subtotal evenly among the diners. Returns an error if the number of diners is zero.

### Unit Tests: test_module
Unit tests are implemented to ensure the reliability and correctness of the `Table` class functionalities.

- **Setup (`setUp(self)`)**: Initializes tables with different numbers of diners for testing.
- **Testing Order Addition**: Verifies that orders are added correctly, including cases with no specified quantity.
- **Testing Order Removal**: Ensures correct behavior when removing orders, including cases where the item or quantity doesn't match.
- **Testing Subtotal Calculation**: Checks the accuracy of the subtotal calculation.
- **Testing Total Calculation with Service Charge**: Validates the total bill calculation, including the service charge.
- **Testing Bill Splitting**: Confirms that the bill is split correctly among diners.

### Main Script: main
The main script demonstrates the usage of the `Table` class.

- **Creating Table Instances**: Demonstrates how to create a `Table` instance.
- **Adding and Removing Orders**: Shows how to add and remove orders from the table.
- **Displaying Bill Calculations**: Illustrates how to display the subtotal, total with service charge, and split bill.


## Installation
(Provide instructions on how to install your project, such as downloading the files or cloning the repository.)

## Usage
### Creating a Table Instance
```python
from restaurant import Table
table = Table(num_of_diners)
```

### Adding an Order
```python
table.order(item_name, price, quantity)
```

### Removing an Order
```python
table.remove(item_name, price, quantity)
```

### Calculating Subtotal
```python
subtotal = table.get_subtotal()
```

### Calculating Total with Service Charge
```python
total = table.get_total(service_charge)
```

### Splitting the Bill
```python
split_amount = table.split_bill()
```

## Running Tests
Ensure the functionality of the project by running the provided unit tests:

1. **Install Python**: Make sure Python is installed on your system.
2. **Clone the Repository**: Clone the repository to your machine.
   ```bash
   git clone https://github.com/Mankabir/TableOrderManager.git
   ```
3. **Navigate to the Project Directory**:
   ```bash
   cd TableOrderManager
   ```
4. **Run the Tests**:
   ```bash
   python -m unittest
   ```

Review the results in the command line interface. Successes and failures will be clearly indicated.

