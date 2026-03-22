from django.core.mail import EmailMessage, BadHeaderError  # noqa
from django.shortcuts import render


def say_hello(request):
    try:
        message = EmailMessage(
            "subject", "message", "from@testing.com", ["recipient1@testing.com"]
        )
        message.attach_file("playground/static/images/image.jpg")
        message.send()
    except BadHeaderError:
        pass
    return render(request, "hello.html", {"name": "Ankit"})
