from django.urls import path
from .views import UsersViewSet, PayerCreateView, SpendPointsView, UserPayersBalanceListView, WelcomeMessageView

urlpatterns = [
    path("",view=WelcomeMessageView.as_view()),
    path("users/",view=UsersViewSet.as_view()),
    path("add/",view=PayerCreateView.as_view()),
    path("spend/",view=SpendPointsView.as_view()),
    path("balance/<int:user_id>/", view=UserPayersBalanceListView.as_view())
]