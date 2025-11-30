import requests
import time
from datetime import datetime

def get_price(coin):
    url = (
        "https://api.coingecko.com/api/v3/simple/price"
        f"?ids={coin}&vs_currencies=usd"
    )
    response = requests.get(url)
    data = response.json()

    if coin not in data:
        return None
    
    return data[coin]["usd"]

def main():
    coin = input("Enter coin to monitor (e.g., bitcoin, ethereum, solana): ").lower()
    threshold = float(input("Enter alert threshold (USD): "))
    interval = int(input("Check every how many seconds? "))
    print(f"Monitoring {coin} price... (Ctrl+C to stop)")

    while True:
        try:
            price = get_price(coin)

            if price is None:
                print(f"'{coin}' not found on CoinGecko. Check spelling.")
                break


            print(f"Current {coin.upper()} Price: ${price}")

            if price >= threshold:
                with open("crypto_alerts.log", "a") as f:
                    f.write(f'{datetime.now().isoformat()} - {coin.upper()} hit ${price}\n')
                print(f"🔥 ALERT! {coin} is above your threshold!")
                # optional: play sound, send email, etc.

            time.sleep(interval) 

        except KeyboardInterrupt:
            print("\nStopped monitoring.")
            break

        except Exception as e:
            print("Error occurred:", e)
            time.sleep(5)

if __name__ == "__main__":
    main()
