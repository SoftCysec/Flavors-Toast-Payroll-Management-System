# Generated by Django 2.2.28 on 2022-11-10 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0002_auto_20200529_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deductions',
            name='deduct',
            field=models.FloatField(verbose_name='Deduction'),
        ),
        migrations.AlterField(
            model_name='deductions',
            name='deductDesc',
            field=models.CharField(max_length=50, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='deductions',
            name='deductID',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Deduction ID'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='jobDesc',
            field=models.CharField(max_length=50, verbose_name='Job Description'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='jobID',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Job ID'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='salary',
            field=models.FloatField(verbose_name='Salary'),
        ),
    ]