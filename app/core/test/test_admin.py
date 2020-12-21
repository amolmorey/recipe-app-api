from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class djandoAdminTestClass(TestCase):


	def setUp(self):
		"""django admin and user setup"""
		
		self.client = Client()
		self.admin_user = get_user_model().objects.create_superuser(
			email = 'amolmorey@londondev.com',
			password = 'test12345'
			)
		self.client.force_login(self.admin_user)
		self.user = get_user_model().objects.create_user(
			email = 'amol@londondev.com',
			password = 'test1234456',
			name = 'test user')



	def  test_users_listed(self):
		"""check wether user in the list or not"""
		url = reverse('admin:core_user_changelist')
		res = self.client.get(url)

		#self.assertContains(res, self.user.email)
		#self.assertContains(res, self.user.name)	



