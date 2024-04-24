# api/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from trading.models import Stock
from trading.managers import OrderManager
from rest_framework.response import Response
from rest_framework import status


class PlaceOrderViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        user = request.user
        stock_id = request.data.get('stock_id')
        quantity = request.data.get('quantity')
        buy_order = request.data.get('buy_order')

        try:
            stock = Stock.objects.get(id=stock_id)
        except Stock.DoesNotExist:
            return Response({'error': 'Stock not found'}, status=status.HTTP_404_NOT_FOUND)

        order_manager = OrderManager()
        result = order_manager.place_order(user, stock, quantity, buy_order)
        if result['success']:
            return Response({'message': 'Order placed successfully'})
        else:
            return Response({'error': result['error']}, status=status.HTTP_400_BAD_REQUEST)


class TotalInvestmentViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        user = request.user
        try:
            stock = Stock.objects.get(id=pk)
        except Stock.DoesNotExist:
            return Response({'error': 'Stock not found'}, status=status.HTTP_404_NOT_FOUND)

        order_manager = OrderManager()
        total_value = order_manager.get_total_investment(user, stock)
        return Response({'total_investment': total_value})
