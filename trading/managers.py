from .models import Order


class OrderManager:
    @staticmethod
    def place_order(user, stock, quantity, buy_order):
        if buy_order:
            # Logic for buying order
            Order.objects.create(user=user, stock=stock, quantity=quantity, buy_order=True)
            return {'success': True, 'detail': 'Successful buying transaction'}
        else:
            # Logic for selling order
            existing_orders = Order.objects.filter(user=user, stock=stock, buy_order=True)
            total_quantity_bought = sum(order.quantity for order in existing_orders)
            if total_quantity_bought >= quantity:
                Order.objects.create(user=user, stock=stock, quantity=quantity, buy_order=False)
                return {'success': True, 'detail': 'Successful selling transaction'}
            else:
                return {'success': False, 'detail': 'Insufficient stocks to sell'}

    @staticmethod
    def get_total_investment(user, stock):
        total_value = sum(order.order_value for order in Order.objects.filter(user=user, stock=stock))
        return total_value
