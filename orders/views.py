from django.shortcuts import render
import requests
from django.conf import settings
from django.views.decorators.http import require_http_methods
import urllib.parse
from .models import Order
from rest_framework import viewsets, permissions
from .serializers import OrderSerializer


# Create your views here.
def index(request):
    return render(request, 'orders/index.html')


def menu(request):
    if request.method == "GET":
        restaurant_menu = generate_menu()

        return render(request, 'orders/menu.html', {'menu': restaurant_menu})


@require_http_methods(["POST"])
def order_pending(request):
    # this should be handled with a Django form, wanted to submit sooner
    if request.method == "POST":
        username = None
        user = None
        if request.user.is_authenticated:
            user = request.user
            username = user.username

        choice = int(request.POST['choice'])

        dish = request.POST.getlist('dish')[choice]
        description = request.POST.getlist('description')[choice]
        photo_url = request.POST.getlist('photo_url')[choice]

        token = settings.DRF_TOKEN

        order = Order.objects.create(dish_name=dish, description=description, customer=user)

        context = {
            'username': username,
            'order': order,
            'photo_url': photo_url,
            'drf_token': token
        }

        return render(request, 'orders/order_pending.html', context=context)


def generate_menu():
    url = settings.RANDOM_RESTAURANT_URI + "food/random_food?size=5"
    menu_data = requests.get(url).json()

    # move to frontend JS if there's time
    auth_header = {'Authorization': 'Client-ID ' + settings.UNSPLASH_TOKEN}
    random_food_url = settings.UNSPLASH_URI + "photos/random?count=1&query=food"
    restaurant_menu = []
    for menu_item in menu_data:
        url = settings.UNSPLASH_URI + "search/photos?query=" + \
              urllib.parse.quote_plus(menu_item['dish']) + "&count=1"
        response = requests.get(url, headers=auth_header)
        if response.status_code == 200:  # check if the response is ok
            data = response.json()
            if data['total'] == 0:
                data = requests.get(random_food_url, headers=auth_header)
            photo_url = data['results'][0]['urls']['thumb']
            menu_item['photo_url'] = photo_url
        else:
            menu_item['photo_url'] = ""
        restaurant_menu.append(menu_item)

    return restaurant_menu


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-datetime_ordered')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]