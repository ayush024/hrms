from django import template

register = template.Library()

@register.filter(name='processing')
def processing(value):
	if value.status == 1:
		return True
	else:
		return False