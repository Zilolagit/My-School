# Generated by Django 4.2.9 on 2024-02-08 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_subject_teacher_subject_teacher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['class_degree']},
        ),
        migrations.AlterField(
            model_name='createclass',
            name='primary_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_teacher', to='core.teacher'),
        ),
        migrations.AlterField(
            model_name='group',
            name='subjects',
            field=models.ManyToManyField(related_name='subject_groups', to='core.subject'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject_teacher', to='core.teacher'),
        ),
    ]
