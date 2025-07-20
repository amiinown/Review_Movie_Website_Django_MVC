from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, phone_number, email, password):
        if not phone_number:
            raise ValueError("user must have an phone number.")
        if len(phone_number) != 11:
            raise ValueError("user must have an phone number.")
        
        if not email:
            raise ValueError("user must have an email.")

        user = self.model(phone_number=phone_number, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone_number, email, password):
        user = self.create_user(phone_number, self.normalize_email(email), password)
        user.is_staff = True
        user.save(using=self._db)
        return user