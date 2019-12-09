from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, 'project_app/index.html')


def log_reg(request):
    if request.POST['logreg'] == 'login':
        errors = User.objects.loginValidator(request.POST)
        if len(errors) > 0:
            for key,val in errors.items():
                messages.error(request, val)
            
        else:
            user = User.objects.get(username=request.POST['login_username'])
            request.session['logged_in'] = user.id
            print(user.username)
            return redirect('/dash')
        return redirect('/')
        
    if request.POST['logreg'] == 'register':
        print(User.objects.all().values())
        errors = User.objects.regValidator(request.POST)
        if len(errors) > 0:
            for key,val in errors.items():
                messages.error(request, val)
        else:
            password = request.POST['password']         
            hashpass = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = User.objects.create(username=request.POST['username'], password=hashpass)
            print(user.username)
        return redirect('/')

    
def dashboard(request):
    try:  
        if request.session['logged_in']:
            # Category.objects.create(title = "Activities")
            # Category.objects.create(title = "Dining")
            # Category.objects.create(title = "Sightseeing")
            context = {
                'user': User.objects.get(id=request.session['logged_in']),
                'places': Place.objects.all(),
                'cats': Category.objects.all(),
            }
        
        return render(request,'project_app/dashboard.html', context)
    except:    
        return redirect('/')


def add(request):
    context ={
        'cats': Category.objects.all(),
        'user': User.objects.get(id=request.session['logged_in']),
    }
    return render(request,'project_app/add.html',context)


def view_place(request,place_id):
    context = {
        'place': Place.objects.get(id=place_id),
        'user': User.objects.get(id=request.session['logged_in'])
    }
    return render(request, 'project_app/view.html',context)



def place_add(request):
    errors = Place.objects.placeValidator(request.POST)
    if len(errors) > 0:
        for key,val in errors.items():
            messages.error(request, val)

    else:
        user = User.objects.get(id=request.session['logged_in'])
        new_place = Place.objects.create(title=(request.POST['title'].title()),desc=(request.POST['desc'].capitalize()),
        city=(request.POST['city'].title()),state=(request.POST['state'].title()),uploaded_by=user)
        new_category = Category.objects.get(id=request.POST['category'])
        new_place.categories.add(new_category)
        return redirect('/dash')
    
    return redirect('/add')

def add_cat(request):
    cat = Category.objects.create(title=request.POST['cat_title'])
    return redirect('/add')


def edit(request,place_id):
    context = {
        'place': Place.objects.get(id=place_id),
        'user': User.objects.get(id=request.session['logged_in'])
    }
    return render(request,'project_app/edit.html',context)

    
def place_edit(request,place_id):
    errors = Place.objects.placeValidator(request.POST)
    if len(errors) > 0:
        for key,val in errors.items():
            messages.error(request, val)

    else:
        update = Place.objects.get(id=place_id)
        update.title = request.POST['title'].title()
        update.desc = request.POST['desc'].capitalize()
        update.city = request.POST['city'].title()
        update.state = request.POST['state'].title()
        update.uploaded_by = User.objects.get(id=request.session['logged_in'])
        update.recommend = request.POST['recommend']
        update.save()
        return redirect('/dash')
    return redirect('/edit/'+place_id)


def delete(request, place_id):
    delete = Place.objects.get(id=place_id)
    delete.delete()
    return redirect('/dash')


def logout(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return redirect('/')
    
def maplocation(request, place_id):
    context = {
        'place': Place.objects.get(id=place_id),
    }
   
    return render(request, 'project_app/map2.html', context)

def map(request):
    context = {
        'places': Place.objects.all(),
        'user': User.objects.get(id=request.session['logged_in'])
    }
    return render(request, 'project_app/map.html', context)