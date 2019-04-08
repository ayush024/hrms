from django import template

register = template.Library()

@register.filter(name='accepted')
def accepted(value):
	if value.status == 2:
		return True
	else:
		return False