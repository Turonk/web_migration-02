# Generated by Django 2.2 on 2020-06-13 16:35

from django.db import migrations

def comment_to_postcomment(apps, schema_editor):
    Com_text= apps.get_model("posts", 'Comment')
    Postcom_text= apps.get_model("posts", 'PostComment')

    for comment in Com_text.objects.all():
        Postcom_text.objects.get_or_create(text = comment.text, post_id = 1)


def move_backward(apps, schema_editor):
    Postcom_text= apps.get_model("posts", 'PostComment')
    Postcom_text.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_postcomment'),
    ]

    operations = [
         migrations.RunPython(comment_to_postcomment, move_backward),
    ]
