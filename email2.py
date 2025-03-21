import smtplib
import random
import os

def read_data_send_mail():
    try:
        with open("emails.txt", "r") as f:
            emails = f.read().strip()  # Remove leading/trailing whitespace
        print(emails)
        emails = [email.strip() for email in emails.split(",") if email.strip()]  # Clean up the list
        print(emails)

    except FileNotFoundError:
        print("File not available.")
        return

    sender_email = "santoshrati30@gmail.com"
    sender_password = os.getenv("vefu gncr mxnn qbdc")  # It's safer to load this from an environment variable

    # Ensure the password is loaded, or exit the function
    if sender_password is None:
        print("Error: Email password not found in environment variables.")
        return

    try:
        # Start SMTP session once, outside the loop
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.starttls()
            s.login(sender_email, sender_password)

            # Loop through emails and send OTP
            for email in emails:
                otp_number = random.randint(10000, 99999)  # Ensure the OTP is always 5 digits
                otp_message = f"Your OTP is {otp_number}"

                try:
                    s.sendmail(sender_email, email, otp_message)
                    print(f"Mail sent successfully to {email}")
                except smtplib.SMTPException:
                    print(f"Failed to send mail to {email}")
    
    except smtplib.SMTPException as e:
        print(f"Error with SMTP: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_data_send_mail()