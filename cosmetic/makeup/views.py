from django.shortcuts import render , redirect
from  django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
# Create your views here.
from django.contrib import messages

from  .models import Brand , Product , Customer
from .forms import BrandForm , ProductForm , CreateUserForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, admin_only
from django.contrib.auth.models import Group

all_products = Product.objects.all()
all_brands = Brand.objects.all()



def index(request):

    return render(request,'makeup/index.html',
                  {
                      'products_count': len(all_products),
                      'brands_count': len(all_brands),

                  })

def register_user(request):
    try:
        if request.user.is_authenticated:
            return redirect('home')
        else:
                form = CreateUserForm()
                if request.method == 'POST':
                    form = CreateUserForm(request.POST)
                    if form.is_valid():
                        user = form.save()
                        username = form.cleaned_data.get('username')
                        group = Group.objects.get(name='customer')
                        user.groups.add(group)
                        Customer.objects.create(
                            user=user,
                            name=user.username,
                            email=user.email
                        )
                        messages.success(request, 'Account was created for ' + username)
                        return redirect('login')

                context = {'form': form, 'show': True}
                return render(request, 'makeup/forms/register.html',
                          context)
    except Exception as exc:
        return render(request, 'makeup/forms/register.html',
                  {'show': False, })




def login_user(request):
    try:
        if request.user.is_authenticated:
            return redirect('home')
        else:
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.info(request, 'Username OR password is incorrect')

            context = {'show': True}
            return render(request, 'makeup/forms/login.html',context)

    except Exception as exc:
        return render(request, 'makeup/forms/register.html',
              {'show': False, })

def logout_user(request):
    try:
        if not request.user.is_authenticated:
            return redirect('home')
        else:
            logout(request)
            return redirect('login')

    except Exception as exc:
        return render(request, 'makeup/forms/register.html',{'show': False, })









def products(request):

    if len(all_products) != 0:
        return render(request, 'makeup/products.html',
                      {'show': True,
                       'all_products': all_products
                       }
                      )
    else:
        return render(request, 'makeup/products.html',
                      {'show': False,
                       })
def product_details(request, product_id):


    try:
        selected_product = Product.objects.get(id=product_id)
        return render(request, 'makeup/product-details.html',
                      {'show': True,
                       'id': product_id,
                       'product_name': selected_product.name,
                       'product_kind': selected_product.kind,
                       'product_description': selected_product.description,
                       'product_price': selected_product.price,
                       'product_expir_date': selected_product.expir_date,
                       'product_brand': selected_product.brand,
                       'product_image': selected_product.image,



                       })
    except Exception as exc:
        return render(request, 'makeup/product-details.html',
                      {'show': False,})




def brands(request):

    if len(all_brands) != 0:
        return render(request, 'makeup/brands.html',
                      {'show': True,
                       'all_brands': all_brands
                       }
                      )
    else:
        return render(request, 'makeup/brands.html',
                      {'show': False,
                       })




def brand_details(request, brand_id):

    try:
        selected_brand = Brand.objects.get(id=brand_id)
        return render(request, 'makeup/brand-details.html',
                      {'show': True,
                       'id':brand_id,
                       'brand_name': selected_brand.name,
                       'brand_origin': selected_brand.origin,
                       'brand_image':selected_brand.image
                       })
    except Exception as exc:
        return render(request, 'makeup/brand-details.html',
                      {'show': False,})

@login_required(login_url='login')
@admin_only
def add_brands(request):
    try:
        form = BrandForm()
        if request.method == 'POST':
            form = BrandForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/brands/')

        context = {'form':form,'show' : True}
        return render(request, 'makeup/forms/brand-form.html', context)

    except Exception as exc:
        return render(request, 'makeup/forms/brand-form.html',
                      {'show': False, })

@login_required(login_url='login')
@admin_only
def update_brands(request,  brand_id):
    try:
        brand = Brand.objects.get(id=brand_id)
        form = BrandForm(instance=brand)

        if request.method == 'POST':
            form = BrandForm(request.POST, instance=brand)
            if form.is_valid():
                form.save()
                return redirect('/brands/')

        context = {'form': form,'show' : True}
        return render(request, 'makeup/forms/brand-form.html', context)
    except Exception as exc:
        return render(request, 'makeup/forms/brand-form.html',
                      {'show': False, })


@login_required(login_url='login')
@admin_only
def delete_brands(request,  brand_id):
    try:
        brand = Brand.objects.get(id=brand_id)
        if request.method == 'POST':
            brand.delete()
            return redirect('/brands/')
        context = {'item': brand ,'show' : True}
        return render(request, 'makeup/forms/delete.html', context)
    except Exception as exc:
        return render(request, 'makeup/forms/delete.html',
                      {'show': False, })


#................

@login_required(login_url='login')
@admin_only
def add_products(request):
    try:
        form = ProductForm()
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/products/')

        context = {'form':form,'show' : True}
        return render(request, 'makeup/forms/brand-form.html', context)

    except Exception as exc:
        return render(request, 'makeup/forms/brand-form.html',
                      {'show': False, })

@login_required(login_url='login')
@admin_only
def update_products(request,  product_id):
    try:
        product = Product.objects.get(id=product_id)
        form = ProductForm(instance=product)

        if request.method == 'POST':
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect('/products/')

        context = {'form': form,'show' : True}
        return render(request, 'makeup/forms/brand-form.html', context)
    except Exception as exc:
        return render(request, 'makeup/forms/brand-form.html',
                      {'show': False, })


@login_required(login_url='login')
@admin_only
def delete_products(request,  product_id):
    try:
        product = Product.objects.get(id=product_id)
        if request.method == 'POST':
            product.delete()
            return redirect('/brands/')
        context = {'item': product,'show' : True}
        return render(request, 'makeup/forms/delete.html', context)
    except Exception as exc:
        return render(request, 'makeup/forms/delete.html',
                      {'show': False, })


