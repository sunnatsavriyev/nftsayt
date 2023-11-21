from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView, name='index'),
    path('addnft/<int:addid>',AddNFTView, name='addnft'),
    path('register/', RegisterView, name='register'),
    path('edituser/<int:imgid>', EditUserView, name='edituser'),
    path('eddnft/<int:eddid>',EditNftProjectView, name='eddnft'),
    path('delnft/<int:delete_id>',DeleteNfTView, name='delnft'),
    path('login/', LoginView, name='login'),
    path('logout/',LogoutView, name='logout'),
    path('rankings/',RankingView, name='rankings'),
    path('connect/',ConnectView, name='connect'),
    path('marketpace/',MarketpaceView, name='marketpace'),
    path('nft.html/',MarketpaceView, name='nft'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)