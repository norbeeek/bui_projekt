from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

class BaseTest(TestCase):
    def setUp(self):
        self.register_url=reverse('register')
        self.login_url=reverse('login')
        self.user = {
            'email' : 'TestAccount@gmail.com',
            'username': 'TestAccount',
            'password1': 'Sup3rS3cr3tP4$$w0rd123.',
            'password2': 'Sup3rS3cr3tP4$$w0rd123.'
        }
        self.wrong_user = {
            'email': 'TestAccount',
            'username': 'T',
            'password1': 'Sup11',
            'password2': 'Sup11'
        }

class RegisterTest(BaseTest):
    def test_can_view_page_correctly(self):
        response = self.client.get(self.register_url, secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'accounts/register.html')

    def test_can_register_user(self):
        response = self.client.post(self.register_url,self.user,format='text/html', secure=True)
        self.assertEqual(response.status_code,302)

    def test_cant_register_user_with_wrong_email(self):
        response = self.client.post(self.register_url,self.wrong_user,format='text/html', secure=True)
        self.assertAlmostEqual(response.status_code,200)

    def test_cant_register_user_with_not_matching_passwords(self):
        response = self.client.post(self.register_url,{
            'email': 'TestAccount111@gmail.com',
            'username': 'TestAcc',
            'password1': 'Sup11',
            'password2': 'Sup'
        },format='text/html', secure=True)
        self.assertAlmostEqual(response.status_code,200)

    def test_cant_register_user_with_blank_fields(self):
        response = self.client.post(self.register_url,{
            'email': '',
            'username': '',
            'password1': '',
            'password2': ''
        },format='text/html', secure=True)
        self.assertAlmostEqual(response.status_code,200)

    def test_cant_register_user_without_email(self):
        response = self.client.post(self.register_url,{
            'email': '',
            'username': 'TestAcc',
            'password1': 'Sup11',
            'password2': 'Sup11'
        },format='text/html', secure=True)
        self.assertAlmostEqual(response.status_code,200)

    def test_cant_register_user_without_username(self):
        response = self.client.post(self.register_url,{
            'email': 'TestAccount112@gmail.com',
            'username': '',
            'password1': 'Sup11',
            'password2': 'Sup11'
        },format='text/html', secure=True)
        self.assertAlmostEqual(response.status_code,200)

    def test_cant_register_user_without_password_confirm(self):
        response = self.client.post(self.register_url,{
            'email': 'TestAccount114@gmail.com',
            'username': 'TestAcc',
            'password1': 'Sup11',
            'password2': ''
        },format='text/html', secure=True)
        self.assertAlmostEqual(response.status_code,200)



class LoginTest(BaseTest):

    def test_can_access_page(self):
        response = self.client.get(self.login_url, secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'accounts/login.html')

    def test_login_success(self):
        self.client.post(self.register_url, self.user, format='text/html',secure=True)
        response = self.client.post(self.login_url, {'username':'TestAccount', 'password':'Sup3rS3cr3tP4$$w0rd123.'},format='text/html', secure=True)
        self.assertEqual(response.status_code,302)

    def test_login_failed_wrong_credentials(self):
        self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.post(self.login_url, {'username':'TestAccount', 'password':'test'},format='text/html', secure=True)
        self.assertEqual(response.status_code,200)

    def test_login_failed_without_username(self):
        self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.post(self.login_url, {'username':'', 'password':'test'},format='text/html', secure=True)
        self.assertEqual(response.status_code,200)

    def test_login_failed_without_password(self):
        self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.post(self.login_url, {'username':'TestAccount', 'password':''},format='text/html', secure=True)
        self.assertEqual(response.status_code,200)

    def test_login_failed_blank_fields(self):
        self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.post(self.login_url, {'username':'', 'password':''},format='text/html', secure=True)
        self.assertEqual(response.status_code,200)

class LogoutTest(BaseTest):

    def test_logout(self):
        self.client.post(self.register_url, self.user, format='text/html', secure=True)
        self.client.post(self.login_url, {'username': 'TestAccount', 'password': 'Sup3rS3cr3tP4$$w0rd123.'},
                                    format='text/html',secure=True)
        response = self.client.get(reverse('logout'), secure=True)
        self.assertEqual(response.status_code,302)

class HomeTest(BaseTest):

    def test_access_home_page_after_logging_in(self):
        self.client.post(self.register_url, self.user, format='text/html')
        self.client.post(self.login_url, {'username': 'TestAccount', 'password': 'Sup3rS3cr3tP4$$w0rd123.'},
                         format='text/html')
        response = self.client.get(reverse('home'), secure=True)
        self.assertEqual(response.status_code,200)

    def test_access_home_page_without_logging_in(self):
        response = self.client.get(reverse('home'), secure=True)
        self.assertEqual(response.status_code,302)
