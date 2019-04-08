from django import template

register = template.Library()

@register.filter(name='pending')
def pending(value):
	if value.status == 0:
		return True
	else:
		return False