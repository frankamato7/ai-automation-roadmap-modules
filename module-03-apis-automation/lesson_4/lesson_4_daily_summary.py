from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import smtplib
from email.mime.text import MIMEText
import os

scheduler = BlockingScheduler()

def get_btc_price():
    url = (
        "https://api.coingecko.com/api/v3/simple/price"
        "?ids=bitcoin&vs_currencies=usd"
    )
    response = requests.get(url)
    data = response.json()
    return data["bitcoin"]["usd"]

def get_nyc_temp_c():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=40.71&longitude=-74.01"
        "&current_weather=true"
    )
    response = requests.get(url)
    data = response.json()
    return data["current_weather"]["temperature"]

def send_email(subject: str, body: str, to_email: str):
    """
    Send a plain-text email using SMTP.
    Fill in your own email + app password via environment variables.
    """
    from_email = os.getenv("SUMMARY_FROM_EMAIL")
    app_password = os.getenv("SUMMARY_EMAIL_APP_PASSWORD")

    if not from_email or not app_password:
        print("Email not sent: SUMMARY_FROM_EMAIL or SUMMARY_EMAIL_APP_PASSWORD not set.")
        return

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    # For Hotmail: smtp.gmail.com, port 587 (TLS)
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(from_email, app_password)
        server.send_message(msg)

def job():
    now = datetime.now().isoformat(timespec='seconds')
    try:
        btc_price = get_btc_price()
        temp_c = get_nyc_temp_c()

        subject = f"Daily Summary {now[:10]}"
        body = (
            f"Daily summary for {now}\n\n"
            f"  - BTC price: ${btc_price}\n"
            f"  - NYC temperature: {temp_c}°C\n"
        )

        print(f"[{now}] Sending daily summary email...")
        print(body)

        to_email = "jbftheshow@gmail.com"

        send_email(subject, body, to_email)

    except Exception as e:
        print(f"[{now}] Error while building or sending summary:", e)


if __name__ == "__main__":
    scheduler.add_job(job, "interval", seconds=30)  # every 30 seconds for testing
    print("Scheduler started. Press Ctrl+C to stop.")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("\nScheduler stopped.")