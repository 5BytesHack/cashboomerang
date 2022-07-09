from django.urls import path

from .views import (
    AddCashBacksAPI, AddChequesCSVAPI, GetCashBacksCSVAPI, GetStatAdminAPI, UserPurchaseHistoryAPI,
    UserRecommendationAPI, UserPopularProductsAPI, UserPopularShopsAPI, GetAllShopsAPI
)

app_name = 'reccomendai'
urlpatterns = [
    path('addcashbacks/', AddCashBacksAPI.as_view()),
    path('addcheques/', AddChequesCSVAPI.as_view()),
    path('getcashbacks/', GetCashBacksCSVAPI.as_view()),
    path('getstatadmin/', GetStatAdminAPI.as_view()),
    path('purchasehistory/<int:user_id>/', UserPurchaseHistoryAPI.as_view()),
    path('recommendations/<int:user_id>/', UserRecommendationAPI.as_view()),
    path('popularproducts/', UserPopularProductsAPI.as_view()),
    path('popularshops/', UserPopularShopsAPI.as_view()),
    path('shops/', GetAllShopsAPI.as_view())
]
