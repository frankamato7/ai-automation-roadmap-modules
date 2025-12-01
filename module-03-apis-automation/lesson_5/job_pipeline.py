import requests
import pandas as pd
from datetime import datetime
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


REMOTEOK_API_URL = "https://remoteok.com/api"


def fetch_raw_jobs():
    """Fetch raw job posts JSON from RemoteOK API."""
    try:
        response = requests.get(REMOTEOK_API_URL,timeout=10)
        response.raise_for_status()
        data = response.json()
        return data[1:] # Skip metadata
    except Exception as err:
        print(f"Error occurred while fetching jobs: {err}")
        return[]


def clean_jobs(raw_jobs):
    """Transform raw job JSON into a clean list of dicts for pandas."""
    cleaned = []
    for job in raw_jobs:
        cleaned.append({
            "date": job.get("date"),
            "company": job.get("company"),
            "position": job.get("position"),
            "location": job.get("location"),
            "tags": ", ".join(job.get("tags", [])),
            "salary_min": job.get("salary_min"),
            "salary_max": job.get("salary_max"),
            "url": job.get("url")
        })
    return cleaned


def save_jobs_to_csv(jobs):
    df = pd.DataFrame(jobs)
    today = datetime.now().date().isoformat()
    filepath = f"jobs_{today}.csv"
    df.to_csv(filepath, index=False)
    return filepath


def send_email_with_attachment(subject: str, body: str, to_email: str, attachment_path: str):
    from_email = os.getenv("SUMMARY_FROM_EMAIL")
    app_password = os.getenv("SUMMARY_EMAIL_APP_PASSWORD")

    if not from_email or not app_password:
        print("Email not sent: SUMMARY_FROM_EMAIL or SUMMARY_EMAIL_APP_PASSWORD not set.")
        return

    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    body_part = MIMEText(body)
    msg.attach(body_part)

    with open(attachment_path, "rb") as f:
        file_data = f.read()
        filename = os.path.basename(attachment_path)
        file_part = MIMEApplication(file_data, Name = filename)
    msg.attach(file_part)

    # For Gmail: smtp.gmail.com, port 587 (TLS)
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(from_email, app_password)
        server.send_message(msg)

def main():
    raw_jobs = fetch_raw_jobs()
    cleaned = clean_jobs(raw_jobs)
    path = save_jobs_to_csv(cleaned)
    print(f"Saved CSV to: {path}")

    subject = f"Daily Job Digest {datetime.now().date().isoformat()}"
    body = "Attached: today's remote job listings."
    to_email = "jbftheshow@gmail.com"


    send_email_with_attachment(subject, body, to_email, path)

if __name__ == "__main__":
    main()
