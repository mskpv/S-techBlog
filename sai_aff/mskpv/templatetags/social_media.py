from django import template
from django.template.defaultfilters import urlencode

register = template.Library()

TWITTER_ENDPOINT = 'https://twitter.com/intent/tweet?text=%s'
FACEBOOK_ENDPOINT = 'https://www.facebook.com/sharer/sharer.php?u=%s'
GPLUS_ENDPOINT = 'https://plus.google.com/share?url=%s'
MAIL_ENDPOINT = 'mailto:?subject=%s&body=%s'
LINKEDIN_ENDPOINT = 'https://www.linkedin.com/shareArticle?mini=true&title=%s&url=%s'
REDDIT_ENDPOINT = 'https://www.reddit.com/submit?title=%s&url=%s'
TELEGRAM_ENDPOINT = 'https://t.me/share/url?text=%s&url=%s'
WHATSAPP_ENDPOINT = 'https://api.whatsapp.com/send?text=%s'
PINTEREST_ENDPOINT = 'https://www.pinterest.com/pin/create/button/?url=%s'


@register.simple_tag()
def facebook(url):
    url = FACEBOOK_ENDPOINT % urlencode(url)
    return url

@register.simple_tag()
def twitter(url):
    url = TWITTER_ENDPOINT % urlencode(url)
    return url