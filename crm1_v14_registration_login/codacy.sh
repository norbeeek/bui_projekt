coverage run crm1_v14_registration_login/manage.py test
coverage xml -o output.xml
bash <(curl -Ls https://coverage.codacy.com/get.sh) report -r output.xml
