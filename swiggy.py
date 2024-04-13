import requests
import json
import sys
from rich import print

HEADERS = {
    'Host':'www.swiggy.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
    'Accept':'*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.swiggy.com/my-account/orders',
    'Content-Type': 'application/json'
    }

SWIGGY_URL = 'https://www.swiggy.com/dapi/order/all'

def getOrders(cookies):
    print("Retrieving...")
    spent = 0
    num_of_orders = 0
    req = requests.get(SWIGGY_URL, headers=HEADERS, cookies=cookies)
    final_data = json.loads(req.text)
    for order in final_data['data']['orders']:
        order_id = order['order_id']
        print(order_id)
        order_total = order['order_total']
        print(order_total)
        num_of_orders+=1
        spent+=order_total
        
    average_spent = spent//num_of_orders
    print()
    print(f"[green]Total money spent on swiggy.com : [bold]INR {spent:,}[/bold][/green]")
    print(f"[green]Total number of orders placed : [bold]{num_of_orders:,}[/bold][/green]")
    print(f"[green]Average money spent on each order : [bold]INR {average_spent:,}[/bold][/green]")





def cookiesToDict():
    print("[green][+][/green] Getting cookies from [u]cookies.json[/u]")
    data = None
    cookies = {}
    try:
        with open("cookies.json","r") as f:
            data = json.load(f)
    except Exception as e:
        print("[red][-] [u]cookies.json[/u] not found in the path[/red]")
        print(str(e))
        return None
    
    try:
        for i in data:
            cookies[i['name']] = i['value']
    except Exception as e:
        print("[red][-] Cookies are not in proper format[/red]")
        print(str(e))
        return None

    return cookies 



if __name__ == "__main__":
    print("Started Script..:vampire:")
    cookies = cookiesToDict()
    getOrders(cookies)
    