from django import template
from student.models import *
from taggit.models import Tag, TaggedItem

register = template.Library()

@register.simple_tag
def student_tags(tag, id):
    ans = 0
    for question_id in TaggedItem.objects.filter(tag__id__in=[tag.id]):
        if Question.objects.filter(id=question_id.object_id).first().student.user.id == id:
            ans+=1
    return ans

# @register.filter
# def tag_check(a,b):
#     print(a, b)
#     return 0
