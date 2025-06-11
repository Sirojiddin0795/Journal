from modeltranslation.translator import register, TranslationOptions
from .models import Requirement

@register(Requirement)
class RequirementTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
