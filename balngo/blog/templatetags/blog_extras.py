from django.contrib.auth.models import User
from django import template
from django.template.defaultfilters import stringfilter
from blog.models import Post
from django.utils.html import escape
# import django.utils.safestring.mark_safe
# # from django.utils.html import format_html

register = template.Library()

@register.filter
def author_details(author, current_user):
    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""

    if author == current_user:
        return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html('{}{}{}', prefix, name, suffix)


'''
By default, the simple_tag function uses
the name of the function as the template tag’s name
'''

@register.simple_tag
def row(extra_classes=""):
    return format_html('<div class="col {}">', extra_classes)

@register.simple_tag
def endrow():
    return format_html('</div>')


@register.simple_tag
def row(extra_classes=""):
    return format_html('<div class="col {}" >', extra_classes)

@register.simple_tag
def endcol():
    return format_html('</div>')


@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
    posts = Post.objects.exclude(pk=post.pk)[:5]
    return {"title": "Recent Posts", "posts": posts}