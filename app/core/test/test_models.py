from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):
	
	def test_create_user_with_email_done(self):
		"""test to check user is created or not"""
		email = 'amolmorey@londondev.com'
		password = 'abcd1234'
		user = get_user_model().objects.create_user(email=email, password=password)
		self.assertEqual(user.email, email)
		self.assertTrue(user.check_password(password))

	def test_user_email_normalized_check(self):
		"""test normalized email"""
		email = 'amolmorey@LONDONDEV.com'
		user = get_user_model().objects.create_user(email, 'test123')
		self.assertEqual(user.email, email.lower())


	def test_user_email_validation(self):
		""" email validations checking"""
		with self.assertRaises(ValueError):
			get_user_model().objects.create_user(None, 'test123')	


	def test_create_superuser(self):
		""" test to check super user"""
		user = get_user_model().objects.create_superuser('amolmorey@gmail.com', 'test1234')
		self.assertTrue(user.is_staff)
		self.assertTrue(user.is_active)