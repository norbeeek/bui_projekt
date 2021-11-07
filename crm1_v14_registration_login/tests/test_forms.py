from django.test import SimpleTestCase
from accounts.forms import CreateUserForm

class TestForms(SimpleTestCase):

    def test_form_for_valid_data(self):
        form = CreateUserForm.Meta.fields={
            'username': 'TestowaNazwa',
            'email': 'Testemail@gmail.com',
            'password1': 'Str0ngPaSsWoRd123.',
            'password2': 'Str0ngPaSsWoRd123.'
        }

        self.assertEqual(form['username'],'TestowaNazwa')
        self.assertEqual(form['email'], 'Testemail@gmail.com')
        self.assertEqual(form['password1'], 'Str0ngPaSsWoRd123.')
        self.assertEqual(form['password2'], 'Str0ngPaSsWoRd123.')

    def test_form_for_invalid_data(self):
        form = CreateUserForm.Meta.fields={
            'username': 'TestowaNazwa',
            'email': 'Testemail@gmail.com',
            'password1': 'Str0ngPaSsWoRd123.',
            'password2': 'Str0ngPaSsWoRd123.'
        }

        self.assertNotEqual(form['username'],'Test')
        self.assertNotEqual(form['email'], 'Test')
        self.assertNotEqual(form['password1'], 'Str0ng')
        self.assertNotEqual(form['password2'], 'Str0ng')