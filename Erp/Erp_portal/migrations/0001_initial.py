# Generated by Django 4.2.9 on 2024-02-07 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_Name', models.CharField(max_length=10)),
                ('course_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dept_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Staff_name', models.CharField(max_length=20)),
                ('Contact', models.CharField(max_length=20)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=20)),
                ('Date_Employed', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Reg_No', models.CharField(max_length=30, unique=True)),
                ('Student_Email', models.CharField(max_length=30)),
                ('Student_Number', models.CharField(max_length=30)),
                ('Courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Erp_portal.courses')),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Erp_portal.department')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='Staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Erp_portal.staff'),
        ),
        migrations.AddField(
            model_name='courses',
            name='Dept_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Erp_portal.department'),
        ),
        migrations.CreateModel(
            name='Course_unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unit_Name', models.CharField(max_length=25)),
                ('Unit_Code', models.CharField(max_length=20)),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Erp_portal.department')),
                ('Staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Erp_portal.staff')),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Erp_portal.courses')),
            ],
        ),
    ]
