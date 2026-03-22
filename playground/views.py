from django.core.mail import send_mail, mail_admins, BadHeaderError  # noqa
from django.shortcuts import render


def say_hello(request):
    try:
        # send_mail("subject", "message", "from@testing.com", ["recipient1@testing.com"])
        mail_admins("subject", "message", html_message="message2")
    except BadHeaderError:
        pass
    return render(request, "hello.html", {"name": "Ankit"})
