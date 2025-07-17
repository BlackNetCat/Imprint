from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form, Course, COURSE_TYPE
from django.contrib import messages
from django.core.mail import EmailMessage
from django.views import generic

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

# def courses(request):
#     return render(request, "courses.html")

def about(request):
    return render(request, "about.html")

class CourseList(generic.ListView):
    queryset = Course.objects.order_by("-date_created")
    template_name = "courses.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = COURSE_TYPE
        return context

class CourseItemDetail(generic.DetailView):
    model = Course
    template_name = "course_item_detail.html"
