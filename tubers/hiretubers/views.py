from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Hiretuber

# Create your views here.

def hiretuber(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        interested_in = request.POST['interested_in']
        city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['phone']
        message = request.POST['message']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        user_id = request.POST['user_id']

        # TODO: to all the sanitization checks

        hiretuber = Hiretuber(first_name=first_name, last_name=last_name, email=email, interested_in=interested_in, city=city, state=state, phone=phone, message=message, tuber_id=tuber_id, tuber_name=tuber_name, user_id=user_id)
        hiretuber.save()
        messages.success(request, "Thanks for reaching out!")
        return redirect('youtubers')