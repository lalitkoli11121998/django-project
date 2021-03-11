# first register the custom template filter
# this class is called itself because we use __init_py as module
from django import template

register = template.Library()


def cut(value,arg): 

    """
    this cuts out all the values of "arg" from the string!

    """
    return value.replace(arg,'')

def add50(value):

    return value +50

register.filter('cut',cut)

#  we can also register the filter by decorators
# @register.filter(name='cut')
# register.filter('add50', add50)