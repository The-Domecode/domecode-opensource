from django import template
from quizzes.models import Answer

register = template.Library()


@register.simple_tag
def notsolved(user, question):
    if Answer.objects.filter(user=user, question=question).count() < 1:
        return True
    else:
        return False


@register.simple_tag
def notcorrect(user, question):
    if Answer.objects.filter(user=user, question=question,
                             iscorrect=True).count() < 1:
        return True
    else:
        return False
