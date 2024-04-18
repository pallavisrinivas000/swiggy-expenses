# Swiggy Order History Retrieval

This Python script allows you to retrieve and display your order history from Swiggy, an online food ordering and delivery platform. It utilizes Swiggy's API to fetch the order data.

## Features

- Retrieves order history from Swiggy.
- Calculates total money spent, total number of orders placed, and average money spent per order.
- Reads Swiggy cookies from a JSON file for authentication.

## Requirements

- Python 3.x
- `requests` library
- `rich` library (for colorful console output)

## Usage

1. Clone or download the repository to your local machine.
2. Ensure you have Python 3.x installed.
3. Install the required libraries using `pip install -r requirements.txt`.
4. Obtain your Swiggy cookies and save them in a file named `cookies.json` in the same directory as the script. The `cookies.json` file should contain an array of JSON objects, each representing a cookie with `name` and `value` fields.
5. Run the script using `python swiggy_order_history.py`.

## Example `cookies.json` Format

```json
[
    {
        "name": "cookie_name_1",
        "value": "cookie_value_1"
    },
    {
        "name": "cookie_name_2",
        "value": "cookie_value_2"
    },
    ...
]
