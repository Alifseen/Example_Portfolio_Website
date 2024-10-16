import smtplib, ssl ## 1. Import smtplib and ssl standard modules

## Make sure your gmail account has 2-Factor Auth on and your App password is created.
## 2. We then save the username and password in variables
username = "alifseen@gmail.com"
password = "xshw awpj sfue pyuy"

## 3. We save email service providers smtp server address and port
emailHost = "smtp.gmail.com"
hostPort = 465

## 4. We create an ssl certificate
sslContext = ssl.create_default_context()

## 5. Specify receiver
receiver = "mayfairenergysolutions@gmail.com"

## 6. specify message
message = """Subject: Test
This is the body of the email 
"""

## 7. Using context manager, we send the email:
with smtplib.SMTP_SSL(emailHost, hostPort, context=sslContext) as server:
    ## 8. We add login information to login method
    server.login(username, password)

    ## 9. Create and send an email
    server.sendmail(username, receiver, message)



