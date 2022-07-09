from django.urls import path

from .views import AddCashBacksAPI, AddChequesCSVAPI, GetCashBacksCSVAPI, GetStatAdminAPI, UserPurchaseHistoryAPI


app_name = 'reccomendai'
urlpatterns = [
    path('addcashbacks/', AddCashBacksAPI.as_view()),
    path('addcheques/', AddChequesCSVAPI.as_view()),
    path('getcashbacks/', GetCashBacksCSVAPI.as_view()),
    path('getstat/', GetStatAdminAPI.as_view()),
    path('purchasehistory/<int:user_id>/', UserPurchaseHistoryAPI.as_view())
]
