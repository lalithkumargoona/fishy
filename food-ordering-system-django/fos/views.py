import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.conf import settings
from .serializers import *
import requests
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from .models import Employee, Customer, DeliveryPerson, get_grand_total


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return ''


def index(request):
    """ Home page """

    return HttpResponse("Hello, Welcome to the Food Ordering System App!")


def request_method(request):
    """ Func that handles methods and decoding data """

    methods = ['POST', 'PUT', 'DELETE', 'GET']
    if request.method in methods:
        json_data = json.loads(request.body)
        return json_data


# Employee's func and routes


class AddFoodCategory(APIView):  # {"category_name":"test"}
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        email_data_length = str(request.headers) + str(request) + str(request.data)
        print(str(email_data_length))
        print(str(request.data))
        serializer = AddFoodCategorySerializer(data=request.data)
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            category_name = serializer.data['category_name']
            category_name = FoodCategory(category_name=category_name)
            category_name.save()
            return JsonResponse({"INFO": "ADDED"}, status=status.HTTP_200_OK)


class AddFoodDetails(APIView):  # {"category_name":"test"}
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = AddFoodDetailsSerializer(data=request.data)
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            category_id = serializer.data['category_id']
            name = serializer.data['name']
            image = serializer.data['image']
            description = serializer.data['description']
            customer_price = serializer.data['customer_price']
            dealer_price = serializer.data['dealer_price']
            offer_price = serializer.data['offer_price']
            gross_weight = serializer.data['gross_weight']
            net_weight = serializer.data['net_weight']
            food_details = FoodDetails(category_id_id=category_id, food_name=name, customer_price=customer_price, dealer_price=dealer_price, offer_price=offer_price, image=image, description=description, gross_weight=gross_weight, net_weight=net_weight)
            food_details.save()
            return JsonResponse({"INFO": "ADDED"}, status=status.HTTP_200_OK)


class AddDeliveryPerson(APIView):  # {"category_name":"test"}
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = AddDeliveryPersonSerializer(data=request.data)
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            delivery_person_phone = serializer.data['delivery_person_phone']
            delivery_person_name = serializer.data['delivery_person_name']
            details = DeliveryPerson(delivery_person_name=delivery_person_name, delivery_person_phone=delivery_person_phone)
            details.save()
            return JsonResponse({"INFO": "ADDED"}, status=status.HTTP_200_OK)


class AssignDeliverPersonToDeliverOrder(APIView):  # {"category_name":"test"}
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = AssignDeliverPersonToDeliverOrderSerializer(data=request.data)
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            order_id = serializer.data["order_id"]
            delivery_person_id = serializer.data["delivery_person_id"]
            assign_order = CustOrderStatus.objects.select_related('delivery_person_id').filter(id=order_id).update(delivery_person_id_id=delivery_person_id)
            return JsonResponse({"INFO": "Assigned"}, status=status.HTTP_200_OK)


class DeliverPersonLocation(APIView):  # {"category_name":"test"}
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def put(self, request):
        serializer = AssignDeliverPersonToDeliverOrderSerializer(data=request.data)
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            order_id = serializer.data["order_id"]
            delivery_person_id = serializer.data["delivery_person_id"]
            assign_order = CustOrderStatus.objects.select_related('delivery_person_id').filter(id=order_id).update(delivery_person_id_id=delivery_person_id)
            return JsonResponse({"INFO": "Assigned"}, status=status.HTTP_200_OK)


class UpdateOrder(APIView):  # {"category_name":"test"}
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def put(self, request):
        serializer = UpdateOrderSerializer(data=request.data)
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            order_id = serializer.data["order_id"]
            order_status = serializer.data["order_status"]
            update = CustOrderStatus.objects.filter(id=order_id).update(order_status=order_status)
            return JsonResponse({"INFO": "Updated"}, status=status.HTTP_200_OK)


class DeleteOrder(APIView):  # {"category_name":"test"}
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = DeleteOrderSerializer(data=request.data)
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            order_id = serializer.data["order_id"]
            Employee.delete_order(request, order_id)
            dict_obj = {
                "order_id": order_id
                }
            return JsonResponse(dict_obj)


#  Customer's func and routes


class ViewMenu(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def get(self, request):
        result = []
        menu = FoodDetails.objects.select_related('category_id').all()
        for m in menu:
            dict_obj = {
                "category_id": m.category_id.id,
                "category_name": m.category_id.category_name,
                "food_id": m.id,
                "food_name": m.food_name,
                "price": m.offer_price
                }
            result.append(dict_obj)
        return JsonResponse(result, status=status.HTTP_200_OK, safe=False)


class ViewMenuById(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def get(self, request, id):
        result = []
        menu = FoodDetails.objects.filter(category_id=id)
        print(menu)
        for m in menu:
            dict_obj = {
                "category_id": m.category_id.id,
                "category_name": m.category_id.category_name,
                "food_id": m.id,
                "food_name": m.food_name,
                "price": m.offer_price
                }
            result.append(dict_obj)
        return JsonResponse(result, status=status.HTTP_200_OK, safe=False)


class CustomerSignup(APIView):  # {"cust_name":"test", "cust_phone":111, "cust_email":"test"}
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = CustomerSignupSerializer(data=request.data)
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            device_records = CustomerDetails.objects.filter(cust_phone=serializer.data['cust_phone'])
            print(device_records)
            if len(device_records) > 0:
                return JsonResponse({"INFO": "Already Registered "}, status=status.HTTP_200_OK)
            cust_name = serializer.data['cust_name']
            cust_phone = serializer.data['cust_phone']
            cust_email = serializer.data['cust_email']
            cust_details = Customer.customer_signup(request, cust_name, cust_phone, cust_email)
            dict_obj = {
                "cust_id": cust_details.id,
                "cust_name": cust_details.cust_name,
                "cust_phone": cust_details.cust_phone,
                "cust_email": cust_details.cust_email
            }
            return JsonResponse({"INFO": dict_obj}, status=status.HTTP_200_OK)


class UserList(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = CustomerDetailsSerializer(data=request.data)
        if serializer.is_valid():
            user = CustomerDetails.objects.filter(cust_phone=serializer.data['phone'])
            if user.exists():
                return JsonResponse({"INFO": "number already exists"})
            parent_rec = CustomerDetails(cust_phone=serializer.data['phone'])
            if 'name' in serializer.data:
                parent_rec.cust_name = serializer.data['name']
            if 'email' in serializer.data:
                parent_rec.cust_email = serializer.data['email']
            parent_rec.save()
            parent_rec_serialised = CustomerDataSerializer(parent_rec, context={'request': request})
            otp_sent = False
            print("1")
            try:
                api = "http://control.msg91.com/api/sendotp.php"
                data = {'authkey': '241566AzbypoaVSBZB5bb9ec50', 'message': 'Your One Time Password for GThink Inventors Registration is ##OTP##.', 'sender': 'GTHINK', 'mobile': serializer.data['phone']}
                # , 'email':serializer.data['email']}
                if 'email' in serializer.data:
                    data['email'] = serializer.data['email']
                r = requests.post(url=api, data=data)
                resp = json.loads(r.text)
                print("2")
                if r.status_code == 200 and resp["type"] == 'success':
                    otp_sent = True
            except ImportError:
                otp_sent = False
            print(serializer.data['phone'])
            return JsonResponse({"INFO": "User created successfully", "user_info": {"id": parent_rec_serialised.data['phone'], "phone": parent_rec_serialised.data['phone']}, "OTP_Sent": otp_sent}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = SendOTPSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            otp_sent = False
            try:
                try:
                    parent_rec = CustomerDetails.objects.get(Usernumber=serializer.data['cust_phone'])
                    parent_exists = True
                except CustomerDetails.DoesNotExist:
                    parent_exists = False
                if parent_exists is True:
                    api = "http://control.msg91.com/api/sendotp.php"
                    data = {'authkey': '241566AzbypoaVSBZB5bb9ec50', 'sender': 'Fishy', 'mobile': serializer.data['phone'], 'message': 'Your One Time Password for FISHY APP Login is ##OTP##.'}
                    if 'email' in serializer.data:
                        data['email'] = serializer.data['email']
                    if serializer.data['cust_phone'] == '918008182410':
                        data['otp'] = '1234'
                        data['message'] = 'Your One Time Password for FISHY APP Login is 1234.'
                    if serializer.data['cust_phone'] == '919908799084':
                        data['otp'] = '1234'
                        data['message'] = 'Your One Time Password for FISHY APP Login is 1234.'
                    r = requests.post(url=api, data=data)
                    resp = json.loads(r.text)
                    if r.status_code == 200 and resp["type"] == 'success':
                        otp_sent = True
                    else:
                        return JsonResponse({"OTP_Sent": otp_sent, "INFO": resp}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({"OTP_Sent": otp_sent, "INFO": "No User exists with this Phone Number."}, status=status.HTTP_400_BAD_REQUEST)
            except ImportError:
                otp_sent = False
            return JsonResponse({"OTP_Sent": otp_sent, "INFO": "OTP sent successfully"}, status=status.HTTP_200_OK)


class Otp(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        resp = ''
        serializer = OtpSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                api = "http://control.msg91.com/api/verifyRequestOTP.php"
                data = {'authkey': '241566AzbypoaVSBZB5bb9ec50', 'mobile': serializer.data['cust_phone'], 'otp': serializer.data['otp']}
                r = requests.post(url=api, data=data)
                resp = json.loads(r.text)
                if r.status_code == 200:
                    if resp["type"] == 'success' and resp["message"] == 'otp_verified':
                        parent_rec = CustomerDetails.objects.get(Usernumber=serializer.data['cust_phone'])
                        parent_rec.cust_device_id = serializer.data['cust_device_id']
                        parent_rec.save()
                        parent_rec_serialised = CustomerDataSerializer(parent_rec, context={'request': request})
                        return JsonResponse({"INFO": "User Authorised successfully", "rooms_info_available": False, "auth_key": settings.AUTH_KEY, "user_info": {"id": parent_rec_serialised.data['id'], "name": parent_rec_serialised.data['name'], "phone": parent_rec_serialised.data['phone']}}, status=status.HTTP_202_ACCEPTED)
                    else:
                        return JsonResponse({"INFO": "Got bad response from msg91", "error": resp}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return JsonResponse({"INFO": "Unable to authorise with the given OTP", "error": resp}, status=status.HTTP_406_NOT_ACCEPTABLE)
            except ImportError:
                return JsonResponse({"INFO": "Unable to request msg91", "error": resp}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def customer_login(request, cust_id):
    """
    >> curl http://127.0.0.1:8000/customers/1/login
    """

    cust = Customer.customer_login(request, cust_id)
    dict_obj = {
        "cust_id": cust.id,
        "cust_name": cust.cust_name
    }
    return JsonResponse(dict_obj, safe=False)


class CreateOrderId(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def put(self, request):
        serializer = CreateOrderIdSerializer(data=request.data)
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            cust_id = serializer.data["cust_id"]
            order_id = CustOrderStatus(cust_id_id=cust_id)
            order_id.save()
            return JsonResponse({"INFO": "Order Created"}, status=status.HTTP_200_OK)


class AddFoodToOrder(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def put(self, request):
        serializer = UpdateFoodToOrderSerializer(data=request.data)
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            order_id = serializer.data["order_id"]
            food_id = serializer.data["food_id"]
            food_qty = serializer.data["food_qty"]
            add_food = CustOrderSelection(order_id_id=order_id, food_id_id=food_id, food_qty=food_qty)
            add_food.save()
            dict_obj = {
                "order_id": order_id,
                "food_id": food_id,
                "food_qty": add_food.food_qty
            }
            return JsonResponse(dict_obj, status=status.HTTP_200_OK)


class RemoveFoodToOrder(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def put(self, request):
        serializer = RemoveFoodToOrderSerializer(data=request.data)
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            order_id = serializer.data["order_id"]
            food_id = serializer.data["food_id"]
            remove_food = CustOrderSelection.objects.filter(order_id_id=order_id).filter(food_id_id=food_id).delete()
            dict_obj = {
                "order_id": order_id,
                "food_id": food_id
            }
            return JsonResponse(dict_obj, status=status.HTTP_200_OK)


class UpdateFoodToOrder(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def put(self, request):
        serializer = UpdateFoodToOrderSerializer(data=request.data)
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            order_id = serializer.data["order_id"]
            food_id = serializer.data["food_id"]
            food_qty = serializer.data["food_qty"]
            update_food = CustOrderSelection.objects.filter(order_id_id=order_id).filter(food_id_id=food_id).update(food_qty=food_qty)
            dict_obj = {
                "order_id": order_id,
                "food_id": food_id,
                "food_qty": food_qty
            }
            return JsonResponse(dict_obj, status=status.HTTP_200_OK)


class Checkout(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def put(self, request):
        serializer = CheckoutSerializer(data=request.data)
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            order_id = serializer.data["order_id"]
            order_status = "Checked out"
            order_address = serializer.data["order_address"]
            checkout_time = timezone.now()
            estimated_time = serializer.data["estimated_time"]
            bill_amount = get_grand_total(order_id)
            checkout_update = CustOrderStatus.objects.filter(id=order_id).update(order_status=order_status, order_address=order_address, checkout_time=checkout_time, estimated_time=estimated_time, bill_amount=bill_amount)
            dict_obj = {
                "order_id": order_id,
                "order_status": order_status,
                "order_address": order_address,
                "estimated_time": estimated_time,
                "bill_amount": bill_amount
            }
            return JsonResponse(dict_obj, status=status.HTTP_200_OK)


class CancelOrderById(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def put(self, request):
        serializer = OrderIdSerializer(data=request.data)
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            order_id = serializer.data["order_id"]
            order_status = "Cancelled"
            update_order = CustOrderStatus.objects.filter(id=order_id).update(order_status=order_status)
            dict_obj = {
                "order_id": order_id,
                "order_status": order_status
            }
            return JsonResponse(dict_obj, status=status.HTTP_200_OK)


# Common func and routes


class ViewOrderById(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = OrderIdSerializer(data=request.data)
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            order_id = serializer.data["order_id"]
            result = []
            view_order = CustOrderSelection.objects.select_related('food_id__category_id').filter(order_id_id=order_id)
            for i in view_order:
                dict_obj = {
                    "customer_name": i.cust_id.cust_name,
                    "order_id": i.id,
                    "order_status": i.order_status,
                    "total_bill": i.bill_amount,
                    "delivery_person_name": i.delivery_person_id.delivery_person_name
                    }
                result.append(dict_obj)
            return JsonResponse(result, status=status.HTTP_200_OK)


class ViewOrderStatusById(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = OrderIdSerializer(data=request.data)
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            order_id = serializer.data["order_id"]
            result = []
            view_order = CustOrderStatus.objects.select_related('cust_id').select_related('delivery_person_id').filter(id=order_id)
            for i in view_order:
                dict_obj = {
                    "customer_name": i.cust_id.cust_name,
                    "order_id": i.id,
                    "order_status": i.order_status,
                    "total_bill": i.bill_amount,
                    "delivery_person_name": i.delivery_person_id.delivery_person_name
                    }
                result.append(dict_obj)
            return JsonResponse(result, status=status.HTTP_200_OK)


class ViewOrderTotalById(APIView):
    permission_classes = [AllowAny]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        serializer = OrderIdSerializer(data=request.data)
        if not serializer.is_valid():
            data = {"INFO": serializer.errors}
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            order_id = serializer.data["order_id"]
            result = []
            view_order = CustOrderStatus.objects.select_related('cust_id').filter(id=order_id)
            for i in view_order:
                dict_obj = {
                    "customer_name": i.cust_id.cust_name,
                    "order_id": i.id,
                    "grand_total": i.bill_amount
                    }
                result.append(dict_obj)
            return JsonResponse(result, status=status.HTTP_200_OK)

