# Generated by Django 5.1.4 on 2025-01-10 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='category',
            field=models.CharField(choices=[('00', '코미디'), ('01', 'SF'), ('02', '액션'), ('03', '공포'), ('04', '다큐멘터리'), ('05', '로맨스')], default='00', max_length=2),
        ),
    ]
