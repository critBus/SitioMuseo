from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.conf import settings
from django import forms
from django.utils.html import format_html
# Create your models here.

from solo.models import SingletonModel

from django.core.validators import RegexValidator
from django.forms import TextInput

