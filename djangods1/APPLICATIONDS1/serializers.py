from rest_framework import serializers
from .models import CapitalRisque,Article,Achat # Assurez-vous d'importer correctement votre modèle

class CapitalRisqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapitalRisque
        fields = '__all__'  
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class AchatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achat
        fields = ['client', 'article', 'quantite'] 

   
        






