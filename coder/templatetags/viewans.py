from django import template
from coder.models import Question, Answer

register = template.Library()


@register.simple_tag
def notsolved(user, question):
    if Answer.objects.filter(user=user, question=question, iscorrect=True).count() < 1:
        return True
    else:
        return False
