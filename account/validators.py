from django.core.validators import RegexValidator

username_validators = (
    RegexValidator(r"[A-Za-z0-9]{5,}"),
)
