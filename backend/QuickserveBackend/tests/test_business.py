from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
# from django.contrib.auth.models import User
from core.models import Category, Subcategory
from business.models import Business, Service
from django.contrib.auth import get_user_model

User = get_user_model()

class AddServiceViewTest(APITestCase):
    def setUp(self):
        # Create user and business
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.business = Business.objects.create(user=self.user, business_name='Test Business')
        
        # Create category and subcategory
        self.category = Category.objects.create(category_name='Test Cat')
        self.subcategory = Subcategory.objects.create(
            subcategory_name='Test Sub', category_id=self.category
        )
        
        # Setup API client and URL
        self.client = APIClient()
        self.url = reverse('addservice') # Update with your URL name

        # Valid payload
        self.valid_payload = {
            "category": self.category.category_id,
            "subcategory": self.subcategory.subcategory_id,
            "service_name": "New Service",
            "description": "Service Description",
            "price": "100.00"
        }

    def test_add_service_authenticated(self):
        """Test authorized user can add a service."""
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.url, self.valid_payload, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Service.objects.count(), 1)
        self.assertEqual(Service.objects.get().service_name, "New Service")

    def test_add_service_unauthenticated(self):
        """Test unauthorized user cannot add a service."""
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_add_service_missing_fields(self):
        """Test validation error for missing fields."""
        self.client.force_authenticate(user=self.user)
        invalid_payload = self.valid_payload.copy()
        del invalid_payload['service_name']
        
        response = self.client.post(self.url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_service_no_business(self):
        """Test forbidden access if user has no business."""
        user_no_biz = User.objects.create_user(username='nobiz', password='password')
        self.client.force_authenticate(user=user_no_biz)
        
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
