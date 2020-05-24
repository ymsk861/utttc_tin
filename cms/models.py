from django.db import models

# Create your models here.
from django.contrib.auth.base_user import (
    AbstractBaseUser, BaseUserManager,
)
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# User-related
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class AbstractUser(AbstractBaseUser, PermissionsMixin):

    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)

    email = models.EmailField(_('email address'), unique=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    twitter = models.CharField(_('Twitter'), max_length=50, blank=True)
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def __str__(self):
        return self.email

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"


class Article(models.Model):
    name = models.CharField("名前", max_length=100)


class Comment(models.Model):
    name = models.CharField("名前", max_length=100)


class BookmarkBase(models.Model):
    class Meta:
        abstract = True
    user = models.ForeignKey(User, verbose_name="User", on_delete = models.CASCADE)
    def __str__(self):
        return self.user.username

class Like(models.Model):
    user = models.IntegerField()#ハコを作る
    circle = models.IntegerField()#ハコを作る



class BookmarkArticle(BookmarkBase):
    class Meta:
        db_table = "bookmark_article"
    obj = models.ForeignKey(Article, verbose_name="Article", on_delete = models.CASCADE)

class BookmarkComment(BookmarkBase):
    class Meta:
        db_table = "bookmark_comment"
    obj = models.ForeignKey(Comment, verbose_name="Comment", on_delete = models.CASCADE)


from django.db import models
from django.forms import ModelForm

# Create your models here.

class Todo(models.Model):
    todo_id = models.CharField(primary_key=True, max_length=5)
    # title = models.CharField(max_length=50)
    # main_text = models.CharField(max_length=300)
    # update_date = models.DateTimeField('date published')

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['todo_id', 'title', 'main_text', 'update_date']
        exclude = ['todo_id', 'update_date']


##自作のフォーム
class Jisaku(models.Model):
    url = models.URLField(max_length = 200)