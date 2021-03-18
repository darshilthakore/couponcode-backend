import datetime

from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CouponSerializer
from .models import Coupon

# Create your views here.

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class CouponList(APIView):
    def get(self, request, format=None):
        coupons = Coupon.objects.all()
        serializer = CouponSerializer(coupons, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CouponSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApplyCode(APIView):
    def get(self, request, format=None):

        print(request.query_params['code'])
        code = request.query_params['code']
        amount = float(request.query_params['amount'])

        coupon = Coupon.objects.filter(code=code)
        if len(coupon) == 0:
            #coupon doesnot exist
            return Response({"msg": "Coupon Not found"}, status=status.HTTP_404_NOT_FOUND)
        coupon = coupon[0]
        end_date = coupon.end_date
        current_date = datetime.date.today()

        if current_date > end_date:
            #coupon validity over
            return Response({"msg": "Coupon Expired"}, status=status.HTTP_404_NOT_FOUND)            
            

        if coupon.coupon_type == "FLAT":
            discount = coupon.discount
            total_amount = amount - discount
        else:

            discount = (amount * coupon.discount) / 100
            if coupon.maximum_discount != None:
                if discount > coupon.maximum_discount:
                    discount = coupon.maximum_discount
            
            total_amount = amount - discount

        res = {
            "total": total_amount,
            "discount": discount
        }

        return Response(res)