from django.test import TestCase
from .models import Bucketlist
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class ModelTestCase(TestCase):
    def setUp(self):
        self.bucketlist_name = "Travel"
        user = User.objects.create(username = "collins")
        self.bucketlist = Bucketlist(name=self.bucketlist_name, owner = user)

    def test_model_can_create_bucketlist(self):
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)
     

class ViewTestCase(TestCase):
    def setUp(self):
        # create the user
        user = User.objects.create(username = "collins")
        # initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.bucketlist_data = {'name':'Travelling', 'owner':user.id}
        self.response = self.client.post(reverse('create'),self.bucketlist_data,format="json")

    def test_api_can_create_bucketlist(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        new_client = APIClient()
        res = new_client.get('/bucketlists/', kwargs={'pk': 3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_api_can_get_bucketlist(self):
        bucketlist = Bucketlist.objects.all(id=1)
        response = self.client.get(
            reverse('details', kwargs={'pk':bucketlist.id}),
            format= "json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(bucketlist, response)

    def test_api_can_update_bucketlist(self):
        bucketlist = Bucketlist.objects.get()
        data = {'name':'roadtrip'}
        response = self.client.put(
            reverse('details', kwargs={'pk':bucketlist.id}),
            data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        bucketlist = Bucketlist.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk':bucketlist.id}),
            format="json",
            follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


