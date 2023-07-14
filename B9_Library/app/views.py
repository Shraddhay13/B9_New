from django.shortcuts import render, HttpResponse, redirect
from .models import Book
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

# FBV -- Function Based Views

@login_required
def welcome_page(request):  # http request
    return render(request, "welcome.html")

import datetime


@login_required
def show_all_books(request):
    books = Book.objects.filter(is_active=True)  # get only active records from database
    print(books)
    return render(request, "showbooks.html", {"allbooks": books, "today": datetime.datetime.now()})


@login_required
def show_single_book(request, bid): # req  # 1
    try:
        book_obj = Book.objects.get(id=bid) # 1
    except Book.DoesNotExist:
        return HttpResponse("Book does not exist..!")
    return render(request=request, template_name="bookdetail.html", context={"book": book_obj})

def common_var(req):
    final_dict = req.POST
    book_name = final_dict.get("nm")
    book_price = final_dict.get("prc")
    book_qty = final_dict.get("qty")
    book_is_pub = final_dict.get("ispub")
    return book_name, book_price, book_qty, book_is_pub


@login_required
def add_single_book(request):
    if request.method == "POST":
        book_name, book_price, book_qty, book_is_pub = common_var(request)
        if book_is_pub == "YES":
            is_pub = True
        else:
            is_pub = False
        Book.objects.create(name=book_name, price=book_price, qty=book_qty, is_published=is_pub)
        messages.success(request, "Book has been added successfully..!" )
        return redirect("show_books")

    elif request.method == "GET":
        # request.GET  --- query params 
        return render(request, "addbook.html")

@login_required
def edit_single_book(request, bid):
    book_obj = Book.objects.get(id=bid)
    if request.method == "GET":
        return render(request, "bookedit.html", {"single_book": book_obj})
    elif request.method == "POST":
        book_name, book_price, book_qty, book_is_pub = common_var(request)
        if book_is_pub == "YES":
            is_pub = True
        else:
            is_pub = False
        # update data
        book_obj.name = book_name
        book_obj.price = book_price
        book_obj.qty = book_qty
        book_obj.is_published = is_pub
        book_obj.save()
        messages.success(request, f"Book: {book_obj.name} has been updated successfully..!" )
        return redirect("show_books")


@login_required
def delete_single_book(request, bid):
    book_obj = Book.objects.get(id=bid)
    book_obj.delete()  # hard delete
    return redirect("show_books")


@login_required
def soft_delete_single_book(request, bid):
    book_obj = Book.objects.get(id=bid)
    book_obj.is_active = False   # soft delete
    book_obj.save()
    return redirect("show_books")

# ----------------------- for forms

from .forms import GeeksForm, BookForm, AddressForm
  
# Create your views here.
@login_required
def form_view(request):
    if request.method == "POST":
        print("in post request")
        data = request.POST
        form = BookForm(data)
        if form.is_valid():
            form.save()
        return redirect("show_books")
    elif request.method == "GET":
        print("get request")
        return render(request, "book_form_test.html", {"bookform": BookForm()})
    



"""
<!-- <form method = "post">
    {% csrf_token %}
    <div class="form-row">
        <div class="form-group col-md-6 mb-0">
          {{ form.email|as_crispy_field }}
        </div>
        <div class="form-group col-md-6 mb-0">
          {{ form.password|as_crispy_field }}
        </div>
    </div>
      {{ form.address_1|as_crispy_field }}
      {{ form.address_2|as_crispy_field }}
      <div class="form-row">
            <div class="form-group col-md-6 mb-0">
            {{ form.city|as_crispy_field }}
            </div>
            <div class="form-group col-md-4 mb-0">
            {{ form.state|as_crispy_field }}
            </div>
            <div class="form-group col-md-2 mb-0">
            {{ form.zip_code|as_crispy_field }}
            </div>
      </div>
      {{ form.check_me_out|as_crispy_field }}
      <button type="submit" class="btn btn-primary">Sign in</button>
</form> -->
"""