from django import template
from student.models import *
from taggit.models import Tag, TaggedItem

register = template.Library()

@register.filter
def question_downvote_check(question, student):
    temp = question.action_set.filter(student = student).first()
    if not temp:
        return 0
    return 0 if temp.action_type == 1 else 1

@register.filter
def question_upvote_check(question, student):
    temp = question.action_set.filter(student = student).first()
    if not temp:
        return 0
    return 0 if temp.action_type == 0 else 1


@register.filter
def comment_downvote_check(comment, student):
    temp = comment.action_set.filter(student = student).first()
    if not temp:
        return 0
    return 0 if temp.action_type == 1 else 1

@register.filter
def comment_upvote_check(comment, student):
    temp = comment.action_set.filter(student = student).first()
    if not temp:
        return 0
    return 0 if temp.action_type == 0 else 1