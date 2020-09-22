from django import template

register = template.Library()


@register.filter(name="answers", is_safe=True)
def submissions(query):
    return query.answer_set.order_by("-last_modified")


@register.filter(name="comments", is_safe=True)
def comments(answer):
    return answer.comment_set.order_by("last_modified")
