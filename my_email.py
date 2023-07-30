class SendEmail:
    def __init__(self, to_addr, subject, body):
        import os
        import smtplib

        EMAIL = os.environ['SEXY_MAIL']
        PASSWORD = os.environ['SEXY_PASWRD']

        self.to_addr = to_addr
        self.subject = subject
        self.body = body

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs= self.to_addr,
                msg=f"Subject:{self.subject}\n\n{self.body}"
                )


