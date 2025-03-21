import smtplib
import random

def read_data_send_mail():
    emails ="santoshrati91@gmail.com"
    
    sender_email="santoshrati30@gmail.com" 

    
    otp_number=random.randint(00000,99999)
    print(otp_number)
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(sender_email,"vefu gncr mxnn qbdc")
    message=f"your OTP is {otp_number}"

    
    s.sendmail(sender_email,emails,message)
    print("mail sent successfully")
    s.quit()
    
read_data_send_mail()