import requests
import json
import sys
from rich import print

# Set the headers for the Swiggy API requests
HEADERS = {
    'Host': 'www.swiggy.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.swiggy.com/my-account/orders',
    'Content-Type': 'application/json'
}

# The Swiggy API endpoint for retrieving order history
SWIGGY_API_URL = 'https://www.swiggy.com/dapi/order/all?order_id='

def get_orders(cookies: dict) -> None:
    """
    Retrieves and displays the user's order history from Swiggy.

    Args:
        cookies (dict): A dictionary containing the user's Swiggy cookies.

    Returns:
        None
    """
    print("Retrieving...")
    total_spent = 0
    total_orders = 0
    last_order_id = ''

    while True:
        # Construct the API URL with the last order ID
        print(SWIGGY_API_URL + str(last_order_id))
        response = requests.get(SWIGGY_API_URL + str(last_order_id), headers=HEADERS, cookies=cookies)
        response_data = json.loads(response.text)
        orders = response_data['data']['orders']

        # Check if the orders list is empty, which means we've retrieved all orders
        if not orders:
            break

        # Iterate through the orders and collect the necessary information
        for order in orders:
            order_id = order['order_id']
            order_total = order['order_total']
            print(order_id)
            print(order_total)
            total_orders += 1
            total_spent += order_total
            last_order_id = order_id

    # Calculate the average money spent per order
    average_spent = total_spent // total_orders if total_orders else 0

    # Print the summary of the order history
    print()
    print(f"[green][bold]Total money spent on swiggy.com: INR {total_spent:,}[/bold][/green]")
    print(f"[green][bold]Total number of orders placed: {total_orders:,}[/bold][/green]")
    print(f"[green][bold]Average money spent on each order: INR {average_spent:,}[/bold][/green]")

def get_cookies_from_file() -> dict:
    """
    Reads the user's Swiggy cookies from a JSON file and returns them as a dictionary.

    Returns:
        dict: A dictionary containing the user's Swiggy cookies.
    """
    print("[green][+][/green] Getting cookies from [u]cookies.json[/u]")
    try:
        # Load the cookies from the JSON file
        with open("cookies.json", "r") as f:
            cookies_data = json.load(f)
    except FileNotFoundError:
        # Handle the case where the cookies.json file is not found
        print("[red][-] [u]cookies.json[/u] not found in the path[/red]")
        return {}

    cookies = {}
    try:
        # Convert the cookies data to a dictionary
        for cookie in cookies_data:
            cookies[cookie['name']] = cookie['value']
    except (KeyError, TypeError):
        # Handle the case where the cookies data is not in the expected format
        print("[red][-] Cookies are not in proper format[/red]")
        return {}

    return cookies

if __name__ == "__main__":
    print("Started Script..:vampire:")
    cookies = get_cookies_from_file()
    get_orders(cookies)