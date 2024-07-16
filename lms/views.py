from django.shortcuts import render , redirect, get_object_or_404
from . models import Books , Cateogry
from . forms import Add_book ,Add_cateogry

def lms (requset):
    if requset.method == "POST":
        add_book=Add_book(requset.POST , requset.FILES)
        if add_book.is_valid():
           add_book.save()
    
        add_cateogry=Add_cateogry(requset.POST)
        if add_cateogry.is_valid():
            add_cateogry.save()
        

    context= {
            'lms': Books.objects.all(),
            'cateogryies': Cateogry.objects.all(),
            'form': Add_book(),
            'form_add_cateogry':Add_cateogry(),
            'statusavailable': Books.objects.filter(status='متاح').count(),  
            'statussolid': Books.objects.filter(status='تأجير').count(),  
            'statusrental': Books.objects.filter(status='غير متاح').count(),  
    }
    return render (requset , 'pages/index.html', context )


def books (requset):
    context={
        'lms': Books.objects.all(),
        'cateogryies': Cateogry.objects.all()
    }
    return render (requset , 'pages/books.html',context )


def update (requset , id):
    update_book = Books.objects.get(id = id)
    if requset.method =='POST':
        update_books=Add_book(requset.POST , requset.FILES , instance=update_book)
        if update_books.is_valid():
            update_books.save()
            return redirect("/")
        
    else:
        update_books =Add_book(instance=update_book)        
    
    context={
    'update_book': update_books
    }
    return render (requset , 'pages/update.html' ,context )


def delete (requset , id):
    delete_book = get_object_or_404(Books , id=id)
    if requset.method == 'POST':
        delete_book.delete()
        return redirect('/')
    return render (requset , 'pages/delete.html' )
