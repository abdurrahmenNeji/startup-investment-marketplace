from django.contrib import admin
from django.urls import path
from APPLICATIONDS1.views import CapitalRisqueListView, HelloAPIView, ArticleListView, AchatListView
from rest_framework.authtoken import views



urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
   
    path('api-token-auth/', views.obtain_auth_token),  # URL pour obtenir le jeton
    # autres URLs

    path('admin/', admin.site.urls),  # URL pour l'administration Django
    path('hello/', HelloAPIView.as_view(), name='hello'),  # URL pour la vue HelloAPIView
    
    # URL pour l'API des investisseurs en capital-risque
    path('capital-risque/', CapitalRisqueListView.as_view(), name='capital-risque-list'),
    
    # URL pour l'API des articles
    path('articles/', ArticleListView.as_view(), name='article-list'),
    
    # URL pour l'API des achats
  path('achats/', AchatListView.as_view(), name='achat-list'),
  path('achats/client/<int:client>/', AchatListView.as_view(), name='achats_client'),
  path('article/<int:article_id>/', ArticleListView.as_view(), name='get_article_details'),
  path('capitalRisque/', CapitalRisqueListView.as_view(), name='inscription client'),
  
   ]
