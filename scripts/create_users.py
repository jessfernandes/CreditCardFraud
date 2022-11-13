from django.contrib.auth.models import User
from decouple import config

username=config('SUPERUSER')
password=config('SUPERUSER_PASS')

if not User.objects.filter(username=username).exists():
    print('>>----- Creating superuser')
    User.objects.create_superuser(
        username=username,
        email=f'{username}@test.com',
        password=password
    )
