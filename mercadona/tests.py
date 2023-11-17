from django.test import TestCase

# promo_app/tests.py

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Produit
from .forms import ProductForm

class AddProductViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='admin', password='adminpass', is_staff=True)
        self.client.login(username='admin', password='adminpass')

    def test_get_add_product_view(self):
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mercadona/add_product.html')

    def test_post_add_product_view(self):
        form_data = {
            'field1': 'value1',  # Remplacez field1 par les champs réels de votre formulaire
            'field2': 'value2',
            # Ajoutez d'autres champs en fonction de votre modèle
        }
        response = self.client.post(reverse('add_product'), data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)  # Vérifie que la redirection est effectuée avec succès

        # Vérifie que le produit a été correctement ajouté à la base de données
        self.assertEqual(Product.objects.count(), 1)
        new_product = Product.objects.first()
        self.assertEqual(new_product.field1, 'value1')  # Assurez-vous de remplacer field1 par le vrai nom de champ
        self.assertEqual(new_product.field2, 'value2')
        # Ajoutez d'autres assertions en fonction de votre modèle

    def test_add_product_view_requires_authentication(self):
        self.client.logout()
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 302)  # Redirection vers la page de connexion
        self.assertRedirects(response, reverse('login') + '?next=' + reverse('add_product'))

        # Vous pouvez également vérifier le message de connexion requis dans le contenu de la réponse
        self.assertContains(response, 'Connectez-vous pour continuer.')

    def test_add_product_view_requires_admin(self):
        # Créer un utilisateur non administrateur
        non_admin_user = User.objects.create_user(username='user', password='userpass')
        self.client.login(username='user', password='userpass')

        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 403)  # Accès interdit pour les utilisateurs non administrateurs

