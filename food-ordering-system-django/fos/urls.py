from django.urls import path
from django.conf.urls import url

from . import views


urlpatterns = [
    path("", views.index),
    url(r'^employees/add-food-category/$', views.AddFoodCategory.as_view(), name="food_category"),  # ok
    url(r'^employees/add-food-details/$', views.AddFoodDetails.as_view(), name="food_details"),  # ok
    url(r'^employees/add-delivery-person/$', views.AddDeliveryPerson.as_view(), name="delivery_person"),  # ok
    url(r'^employees/assign-deliver-person-to-deliver-order/$', views.AssignDeliverPersonToDeliverOrder.as_view(), name="assign_order"),  # ok
    url(r'^employees/update-order/$', views.UpdateOrder.as_view(), name="update_order"),  # ok
    url(r'^employees/delete-order/$', views.DeleteOrder.as_view(), name="delete_order"),  # ok
    url(r'^customers/view-menu', views.ViewMenu.as_view(), name="menu"),  # ok
    url(r'^add_user/$', views.UserList.as_view(), name='addUser'),  # ok
    url(r'^login_user/$', views.UserLogin.as_view(), name='userLogin'),  # ok
    url(r'^validate_OTP/$', views.Otp.as_view(), name='validate_OTP'),  # ok
    url(r'^customers/create-order', views.CreateOrderId.as_view(), name="order_id"),  # ok
    url(r'^customers/add-food-to-order', views.AddFoodToOrder.as_view(), name="add_food"),  # ok
    url(r'^customers/remove-food-to-order', views.RemoveFoodToOrder.as_view(), name="remove_food"),  # ok
    url(r'^customers/update-food-to-order', views.UpdateFoodToOrder.as_view(), name="update_food"),  # ok
    url(r'^customers/checkout/$', views.Checkout.as_view(), name="checkout"),  # ok
    url(r'^customers/cancel-order/$', views.CancelOrderById.as_view(), name="cancel_order"),  # ok
    url(r'^view-order/$', views.ViewOrderById.as_view(), name="view_order"),  # Down ok
    url(r'^view-order-status/$', views.ViewOrderStatusById.as_view(), name="view_order_status"),  # Down ok
    url(r'^view-order-total/$', views.ViewOrderTotalById.as_view(), name="view_order_total")  # Down ok
]