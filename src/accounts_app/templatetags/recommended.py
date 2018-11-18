from django import template
from django.contrib.auth import get_user_model
from accounts_app.models import UserProfile
User=get_user_model()

register = template.Library()

@register.inclusion_tag('profiles_app/snippets/recommended.html')
def show_recommended(user):
    if isinstance(user,User):
        recommended=UserProfile.objects.recommended(user)
        return {'recommended':recommended}