from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import  CapitalRisque,Article,Achat
from .serializers import  CapitalRisqueSerializer,ArticleSerializer,AchatSerializer

class HelloAPIView(APIView):
    def get(self, request):
        return Response({"message": "Bonjour, monde !"})

class CapitalRisqueListView(APIView):
    def get(self, request):
        capital_risque = CapitalRisque.objects.all()
        serializer = CapitalRisqueSerializer(capital_risque, many=True)
        return Response(serializer.data)
    def post(self, request):
        print("Données reçues :", request.data)  # Debug
        serializer = CapitalRisqueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Erreurs de validation :", serializer.errors)  # Debugreturn Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleListView(APIView):
    def get(self, request):
        articles = Article.objects.all()  # Récupère tous les articles
        serializer = ArticleSerializer(articles, many=True)  # Sérialise les données
        return Response(serializer.data) 
    def get_article_details(request, article_id):
        try:
            article = get_object_or_404(Article, id=article_id)
            data = {
            "nom_article": article.nom,  # Adaptez selon vos champs
            "description_article": article.description,
            }
            return JsonResponse(data, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

class AchatListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        achats = Achat.objects.all()  # Récupère toutes les transactions d'achats
        serializer = AchatSerializer(achats, many=True)  # Sérialise les données
        return Response(serializer.data)
    def get(self, request, client=None):
        try:
            # Récupérer tous les achats associés à ce client
            achats = Achat.objects.filter(client=client)

            # Sérialiser les achats
            achat_serializer = AchatSerializer(achats, many=True)

            # Récupérer les détails des articles et les ajouter à la réponse
            achats_data = achat_serializer.data

            for achat in achats_data:
                article = Article.objects.get(id_article=achat['article'])  # Utilise 'id_article' à la place de 'id'
     # Récupérer l'article lié à l'achat
                achat['article_nom'] = article.nom  # Ajouter le nom de l'article
                achat['article_description'] = article.description  # Ajouter la description de l'article

            return Response(achats_data, status=status.HTTP_200_OK)

        except Achat.DoesNotExist:
            return Response({"detail": "Aucun achat trouvé pour ce client."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        print("Données reçues :", request.data)  # Log des données envoyées
        serializer = AchatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            print("Erreur dans les données :", serializer.errors)  # Log des erreurs du serializer
            return Response(serializer.errors, status=400)
   