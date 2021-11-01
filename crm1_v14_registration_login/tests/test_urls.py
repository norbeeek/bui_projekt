from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import registerPage, loginPage, logoutUser, home

class TestUrls(SimpleTestCase):

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, loginPage)

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, registerPage)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logoutUser)

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)
