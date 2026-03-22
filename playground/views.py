from django.core.mail import EmailMessage, BadHeaderError  # noqa
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage


def say_hello(request):
    try:
        message = BaseEmailMessage(
            template_name="emails/hello.html", context={"name": "Ankit"}
        )
        message.send(["recipient1@testing.com"])
    except BadHeaderError:
        pass
    return render(request, "hello.html", {"name": "Ankit"})
