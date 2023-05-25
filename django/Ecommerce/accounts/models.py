from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError("El usuario debe tener un email")
        if not username:
            raise ValueError('El usuario debe tener un nombre de usuario')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        # para el password
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username= username,
            password = password,
            first_name = first_name,
            last_name = last_name
        )

        # estos valores hace que sea un administrador
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        # guardamos los valores
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=10)

    # campos atributo de django por defecto
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superdadmin = models.BooleanField(default=False)

    # lo que queremos que cuando inicie la sesion sea por el email no por el nombre...
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username','first_name','last_name']

    # ahora quiero que estos métodos se incluyan en el modelo Account, para ello hacemos...
    objects = MyAccountManager()

    # dentro de la plataforma para que se liste los registros de una tabla que por defecto sea un label que represente
    # cada registro....
    def __str__(self):
        return self.email

    #otra función para ver que permisos tiene
    def has_perm(self, obj=None):
        return self.is_admin

    # si es administrador debe indicar que tiene acceso a los modulos
    def has_module_perms(self, add_label):
        return True











