# Generated by Django 4.1.5 on 2023-01-10 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Enterprise",
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
                ("name", models.CharField(max_length=50)),
                (
                    "owner",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Collaborator",
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
                ("name", models.CharField(default="", max_length=50)),
                ("phone", models.CharField(default="", max_length=15)),
                ("date_of_birth", models.DateField(max_length=8, null=True)),
                (
                    "address1",
                    models.CharField(
                        default="", max_length=1024, verbose_name="Address line 1"
                    ),
                ),
                (
                    "address2",
                    models.CharField(
                        default="", max_length=1024, verbose_name="Address line 2"
                    ),
                ),
                (
                    "zip_code",
                    models.CharField(
                        default="", max_length=12, verbose_name="ZIP / Postal code"
                    ),
                ),
                (
                    "city",
                    models.CharField(default="", max_length=1024, verbose_name="City"),
                ),
                (
                    "country",
                    models.CharField(default="", max_length=50, verbose_name="Country"),
                ),
                (
                    "degree",
                    models.CharField(
                        choices=[
                            ("AA", "Associate of Arts"),
                            ("AS", "Associate of Science"),
                            ("AAA", "Associate of Applied Arts"),
                            ("AAS", "Associate of Applied Science"),
                            ("BA", "Bachelor of Arts"),
                            ("BS", "Bachelor of Science"),
                            ("BFA", "Bachelor of Fine Arts"),
                            ("MA", "Masters of Arts"),
                            ("MS", "Master of Science"),
                            ("MFA", "Master of Fine Arts"),
                            ("MBA", "Master of Business"),
                            ("MLS", "Master of Library Science"),
                            ("MPH", "Master of Public Health"),
                            ("MSW", "Master of Social Work"),
                            ("LLM", "Master of Laws"),
                            ("MLS", "Master of Arts in Liberal Studies"),
                            ("MM", "Master of Music"),
                            ("MEd", "Master of Education"),
                            ("MEng", "Master of Engineering"),
                            ("MArch", "Master of Architecture"),
                            ("PhD", "Doctor of Philosophy (PhD)"),
                            ("DBA", "Doctor of Business Administration"),
                            ("DHA", "Doctor of Health Administration"),
                            ("EdD", "Doctor of Education"),
                            ("DNP", "Doctor of Nurse Practice"),
                        ],
                        default="AA",
                        max_length=5,
                    ),
                ),
                ("major", models.CharField(default="", max_length=50)),
                ("university", models.CharField(default="", max_length=50)),
                ("college_email", models.CharField(default="", max_length=50)),
                (
                    "year_in_school",
                    models.CharField(
                        choices=[
                            ("FR", "Freshman"),
                            ("SO", "Sophomore"),
                            ("JR", "Junior"),
                            ("SR", "Senior"),
                            ("GR", "Graduate"),
                        ],
                        default="FR",
                        max_length=2,
                    ),
                ),
                ("personal_website", models.URLField(blank=True)),
                ("github", models.URLField(blank=True)),
                ("linkedin", models.URLField(blank=True)),
                ("work_experience", models.TextField(default="")),
                (
                    "owner",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
