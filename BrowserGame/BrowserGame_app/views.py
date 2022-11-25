from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Users
from django.db import connection, connections
from .my_captcha import FormWithCaptcha
from django.template import RequestContext
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import hashlib
import datetime
from django.utils import timezone


def login_page(request):
    try:
        del request.session['errorregistration']
    except:
        pass

    return render(request, 'login_page.html')


def registration_page(request):
    try: del request.session['errorlogin']
    except: pass
    try: del request.session['errorregistration']
    except: pass
    context = {
        'captcha': FormWithCaptcha,
    }

    return render(request, 'registration_page.html', context)


def Game(request):
    salt = "2Xc7Y!4rtv1vcgOa"
    try: del request.session['errorregistration']
    except: pass
    try: del request.session['errorlogin']
    except: pass

    password = (request.POST.get('password'))

    db_password = password+salt
    hashed = hashlib.sha512(db_password.encode())
    success = 0
    login = (request.POST.get('login'))
    data = Users.objects.all()

    datauser = (data.values('user'))
    for i in range(len(datauser)):
        if login == str(datauser[i]['user']):
            position = i
            datapassword = (data.values('password'))
            if hashed.hexdigest() == str(datapassword[position]['password']):
                success = 1
            break

    if success == 1:
        now = timezone.now() + datetime.timedelta(hours = 1)
        wood = (data.values('wood'))
        wood = int(wood[position]['wood'])
        email = (data.values('email'))
        email = str(email[position]['email'])
        stone = (data.values('stone'))
        stone = int(stone[position]['stone'])
        food = (data.values('food'))
        food = int(food[position]['food'])
        premium_time = (data.values('premium_time'))
        premium_time = (premium_time[position]['premium_time'])
        #now = premium_time + datetime.timedelta(240)

        if (now>premium_time):
            difference_time = now - premium_time
            premium_information = 'Premium inactive from'

        else:
            difference_time = premium_time - now
            premium_information = 'Premium remained for'
        difference_str = str(difference_time.days) + ' days ' + \
                         str(difference_time.seconds//3600) + ' hours ' + \
                         str((difference_time.seconds//60)%60) + ' minutes'

        context = {
            'login': login,
            'wood': wood,
            'email': email,
            'stone': stone,
            'food': food,
            'premium_time': difference_str,
            'current_datetime': now,
            'premium_information': premium_information,
        }

        return render(request, 'Game.html', context)
    else:
        errorlogin = 'Password or login is incorrect!'
        request.session['errorlogin'] = errorlogin


        return render(request, 'login_page.html')


def registrationtogame(request):
    salt = "2Xc7Y!4rtv1vcgOa"
    try: del request.session['errorregistration']
    except: pass
    try: del request.session['errorlogin']
    except: pass


    password1 = (request.POST.get('password1'))
    password2 = (request.POST.get('password2'))
    nick = (request.POST.get('nick'))
    email = (request.POST.get('email'))
    regulamin = (request.POST.get('regulamin'))
    captcha = request.POST['g-recaptcha-response']

    if email == '' or nick == '' or password1 == '' or password2 == '':
        errorregistration = 'Fill in all fields!'
        request.session['errorregistration'] = errorregistration
        return redirect('/registration')

    elif password1 != password2:
        errorregistration = 'Passwords are not the same!'
        request.session['errorregistration'] = errorregistration
        return redirect('/registration')
    elif len(password1) < 8 or len(password1) > 20:
        errorregistration = 'Password must be at least 8 to 20 characters long!'
        request.session['errorregistration'] = errorregistration
        return redirect('/registration')
    elif(captcha == ""):
        errorregistration = "We don't know if you are human."
        request.session['errorregistration'] = errorregistration
        return redirect('/registration')

    elif regulamin == None:
        errorregistration = 'Accept the website regulations!'
        request.session['errorregistration'] = errorregistration
        return redirect('/registration')
    else:

        try:
            validate_email(email)
        except ValidationError as e:
            request.session['errorregistration'] = e
            return redirect('/registration')


        data = Users.objects.all()

        datauser = (data.values('user'))
        for i in range(len(datauser)):
            if nick == str(datauser[i]['user']):
                errorregistration = 'Please choose a different nickname. This one is already in the database.'
                request.session['errorregistration'] = errorregistration
                return redirect('/registration')

        dataemail = (data.values('email'))

        for i in range(len(dataemail)):
            if email == str(dataemail[i]['email']):
                errorregistration = 'Please choose a different email. This one is already in the database.'
                request.session['errorregistration'] = errorregistration
                return redirect('/registration')

        db_password=password1+salt
        hashed = hashlib.sha512(db_password.encode())


        adddata = Users(user=nick, password=hashed.hexdigest(), email=email)
        adddata.save()

        return render(request, 'Hello.html')


def Hello(request):
    #return render(request, 'Hello.html')
    return redirect('/')
