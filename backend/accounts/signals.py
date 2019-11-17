from django.dispatch import Signal

user_signup = Signal(providing_args=["user"])
