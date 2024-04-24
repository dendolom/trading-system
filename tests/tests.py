import pytest

from trading.managers import OrderManager
from trading.models import Stock, Order
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_trading():
    # Create a test user
    user = User.objects.create_user(username='test_user', password='password')
    print("Test user created:", user.username)

    # Create a test stock
    stock = Stock.objects.create(name='Test Stock', price=100)
    print("Test stock created:", dict(name=stock.name, price=stock.price))

    # Create an instance of the OrderManager
    order_manager = OrderManager()

    # Place a buy order
    result_buy = order_manager.place_order(user, stock, quantity=5, buy_order=True)
    print("Result of placing buy order:", result_buy)
    assert result_buy['success'] is True

    # Check if the buy order is created
    assert Order.objects.filter(user=user, stock=stock, buy_order=True).exists()
    print("Buy order created successfully")

    # Place a sell order
    result_sell = order_manager.place_order(user, stock, quantity=3, buy_order=False)
    print("Result of placing sell order:", result_sell)
    assert result_sell['success'] is True

    # Check if the sell order is created
    assert Order.objects.filter(user=user, stock=stock, buy_order=False).exists()
    print("Sell order created successfully")

    # Retrieve the total value invested in a specific stock by a user
    total_investment = order_manager.get_total_investment(user, stock)
    assert total_investment
    print(f"Total value invested on {stock.name} by {user.username}: {total_investment}")
