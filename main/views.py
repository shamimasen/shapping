from django.shortcuts import render, redirect
from main.forms import MoodEntryForm
from main.models import MoodEntry
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import datetime, timedelta

@login_required(login_url='/login')
def show_main(request):
    # Ambil last_login dari cookies
    last_login_cookie = request.COOKIES.get('last_login')

    if last_login_cookie:
        # Parsing last_login dari cookies ke datetime (UTC time)
        last_login_utc = datetime.fromisoformat(last_login_cookie)

        # Kurangi waktu UTC dengan 7 jam (untuk Asia/Jakarta)
        last_login_local = last_login_utc + timedelta(hours=7)

        # Format menjadi date/month/year hour:minute
        last_login = last_login_local.strftime('%d/%m/%Y %H:%M')
    else:
        last_login = None

    context = {
        'name': request.user.username,
        'kelas': 'PBP B',
        'npm': '2306245535',
        'last_login': last_login,
    }

    return render(request, "main.html", context)

def create_mood_entry(request):
    form = MoodEntryForm(request.POST or None)

    if request.method == "POST":
        product_name = request.POST.get('product_name', '').strip()

        # Validasi apakah input product_name kosong atau hanya mengandung tag HTML
        if not product_name or not strip_tags(product_name):
            form.add_error('product_name', 'This field cannot be blank')

        if form.is_valid():
            mood_entry = form.save(commit=False)
            mood_entry.user = request.user
            mood_entry.save()
            return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_mood_entry.html", context)

def show_xml(request):
    data = MoodEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MoodEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      last_login_utc = timezone.now()

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', last_login_utc.isoformat())
            return response
      
      else:
        messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Get mood entry berdasarkan id
    mood = MoodEntry.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = MoodEntryForm(request.POST or None, instance=mood)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get mood berdasarkan id
    product = MoodEntry.objects.get(pk = id)
    # Hapus mood
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    product_name = strip_tags(request.POST.get("product_name"))
    price = request.POST.get("price")
    rating = request.POST.get("rating")
    description = strip_tags(request.POST.get("description"))
    user = request.user

    new_product = MoodEntry(
        product_name=product_name, price=price, description=description,  rating=rating,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)