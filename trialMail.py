import smtplib, ssl

port = 465  # For SSL
sender_email = "ineedacatasap@gmail.com"
password = input("Type the password: \n")

smtp_server = "smtp.gmail.com"

receiver_email = "arianna.fici@gmail.com"  # Enter receiver address

message = """\
Subject: Hi there

Check out the cats website: https://kattens-vaern.dk/adoption?field_internat_tid=All&field_race_tid=All&field_environment_tid=16&field_gender_value=All&field_cat_age_name_tid=All."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
