# Generated by Django 4.1.2 on 2022-11-16 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("details", "0002_alter_doctor_user_alter_nurse_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="speciality",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="doctor",
                to="details.speciality",
            ),
        ),
        migrations.CreateModel(
            name="PatientConsultation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Complete", "Complete"),
                            ("In Progress", "In Progress"),
                            ("Pending", "Pending"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="details.doctor"
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="details.patient",
                    ),
                ),
            ],
        ),
    ]
