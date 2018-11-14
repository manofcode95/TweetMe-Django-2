from django.core.exceptions import ValidationError
def validate_content(value):
    content=value
    rude_words=['fuck','shit','dick']
    for x in rude_words:
        if x in content:    
            raise ValidationError('Included forbidden words')
    return content