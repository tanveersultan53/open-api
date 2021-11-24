from django.urls import path

from .views import AliBahiView
urlpatterns = [

     path("searching/", AliBahiView.as_view()),
    # path("company_pin_to_top/<int:pk>/",CompanyPinToTopView.as_view()),

]