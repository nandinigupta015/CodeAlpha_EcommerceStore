from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Product, CartItem, Order, OrderItem, Category

from .models import Product, CartItem, Order, OrderItem


def product_list(request):
    categories = Category.objects.all()

    selected_category = request.GET.get("category")
    search_query = request.GET.get("q", "")
    sort_option = request.GET.get("sort", "")

    products = Product.objects.all()

    # ✅ Filter by Category
    if selected_category:
        products = products.filter(category__id=selected_category)

    # ✅ Search by product name
    if search_query:
        products = products.filter(name__icontains=search_query)

    # ✅ Sorting
    if sort_option == "low":
        products = products.order_by("price")
    elif sort_option == "high":
        products = products.order_by("-price")
    elif sort_option == "new":
        products = products.order_by("-id")

    cart_count = 0
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(user=request.user).count()

    return render(request, "product_list.html", {
        "products": products,
        "categories": categories,
        "selected_category": selected_category,
        "cart_count": cart_count,
        "search_query": search_query,
        "sort_option": sort_option
    })



def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart_count = 0

    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(user=request.user).count()

    return render(request, "product_detail.html", {
        "product": product,
        "cart_count": cart_count
    })


@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1

    cart_item.save()
    return redirect("cart")


@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)

    cart_data = []
    total = 0

    for item in cart_items:
        subtotal = item.product.price * item.quantity
        total += subtotal

        cart_data.append({
            "id": item.id,
            "product": item.product,
            "quantity": item.quantity,
            "subtotal": subtotal
        })

    cart_count = CartItem.objects.filter(user=request.user).count()

    return render(request, "cart.html", {
        "cart_items": cart_data,
        "total": total,
        "cart_count": cart_count
    })


@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(CartItem, pk=pk, user=request.user)
    item.delete()
    return redirect("cart")


@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    cart_count = CartItem.objects.filter(user=request.user).count()

    if request.method == "POST":
        order = Order.objects.create(user=request.user, total_amount=total)

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        cart_items.delete()
        return render(request, "success.html", {"order": order, "cart_count": 0})

    return render(request, "checkout.html", {"total": total, "cart_count": cart_count})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("product_list")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})


@login_required
def increase_quantity(request, pk):
    item = get_object_or_404(CartItem, pk=pk, user=request.user)
    item.quantity += 1
    item.save()
    return redirect("cart")


@login_required
def decrease_quantity(request, pk):
    item = get_object_or_404(CartItem, pk=pk, user=request.user)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect("cart")
@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).prefetch_related("items").order_by("-created_at")
    cart_count = CartItem.objects.filter(user=request.user).count()

    return render(request, "my_orders.html", {
        "orders": orders,
        "cart_count": cart_count
    })
@login_required
def profile(request):
    cart_count = CartItem.objects.filter(user=request.user).count()
    return render(request, "profile.html", {"cart_count": cart_count})

