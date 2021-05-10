from django.template import Library, loader

register = Library()


@register.inclusion_tag('hierarchical/rowitem.html')
def rowitem(section, color=None):
    return {
        'section': section,
        'color': color
    }