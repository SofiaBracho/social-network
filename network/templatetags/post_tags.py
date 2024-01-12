from django import template
register = template.Library()

@register.simple_tag
def is_liked_by(post, user):
    return post.is_liked_by(user)