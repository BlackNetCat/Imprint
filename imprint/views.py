from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

def index(request):
    form = ApplicationForm(request.POST)
    if form.is_valid():
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        email = form.cleaned_data["email"]
        date = form.cleaned_data["date"]

        Form.objects.create(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            date=date)

        message_body = (f"You have successfully registered for the start of the course. \n"
                        f"Thank you {first_name}")
        email_message = EmailMessage("Form submission confirmation", message_body, to=[email])

        # Sending emails is currently disabled.
        # email_message.send()

        messages.success(request, "Form submitted successfully!")
    return render(request,"index.html")

def about(request):
    return render(request, "about.html")
