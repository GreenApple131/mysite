from django import template
from ..models import Post
from django.db.models import Count


register = template.Library() # there are two types of user templates


@register.simple_tag   # get data and return string
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')  # get data and return the fragment of template //// Инклюзивные теги должны возвращать только словари контекста, который затем будет использован для формирования HTML-шаблона
def show_latest_posts(count=5):  #  Чтобы задать любое другое количество статей, используйте такую запись в HTML шаблоне: {% show_latest_posts *число статей* %}
	latest_posts = Post.published.order_by('-publish')[:count]
	return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
	return Post.published.annotate(total_comments=Count('comments')
						).order_by('-total_comments')[:count]
