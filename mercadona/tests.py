from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Produit
from .forms import ProductForm

class AddProductViewTest(TestCase):
    def setUp(self):
        # Set up the client and create an admin user for testing
        self.client = Client()
        self.user = User.objects.create_user(username='admin', password='adminpass', is_staff=True)
        self.client.login(username='admin', password='adminpass')

    def test_get_add_product_view(self):
        # Test the GET request to the add product view
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mercadona/add_product.html')

    def test_post_add_product_view(self):
        # Test the POST request to the add product view
        form_data = {
            'field1': 'value1',  # Replace field1 with actual fields from your form
            'field2': 'value2',
            # Add more fields based on your model
        }
        response = self.client.post(reverse('add_product'), data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)  # Check that the redirection is successful

        # Check that the product has been successfully added to the database
        self.assertEqual(Produit.objects.count(), 1)
        new_product = Produit.objects.first()
        self.assertEqual(new_product.field1, 'value1')  # Make sure to replace field1 with the actual field name
        self.assertEqual(new_product.field2, 'value2')
        # Add more assertions based on your model

    def test_add_product_view_requires_authentication(self):
        # Test that adding a product requires authentication
        self.client.logout()
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 302)  # Redirect to the login page
        self.assertRedirects(response, reverse('login') + '?next=' + reverse('add_product'))

        # You can also check the required login message in the response content
        self.assertContains(response, 'Log in to continue.')

    def test_add_product_view_requires_admin(self):
        # Test that adding a product requires an admin user
        # Create a non-admin user
        non_admin_user = User.objects.create_user(username='user', password='userpass')
        self.client.login(username='user', password='userpass')

        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 403)  # Forbidden access for non-admin users
