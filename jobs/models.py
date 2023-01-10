from django.db import models
from django.contrib.auth import get_user_model
from django import forms
from datetime import date


User = get_user_model()

# Create your models here.
class Collaborator(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]

    ASSOCIATE_OF_ARTS = "AA"
    ASSOCIATE_OF_SCIENCE = "AS"
    ASSOCIATE_OF_APPLIED_ARTS = "AAA"
    ASSOCIATE_OF_APPLIED_SCIENCE = "AAS"
    BACHELOR_OF_ARTS = "BA"
    BACHELOR_OF_SCIENCE = "BS"
    BACHELOR_OF_FINE_ARTS = "BFA"
    MASTER_OF_ARTS = "MA"
    MASTER_OF_SCIENCE = "MS"
    MASTER_OF_FINE_ARTS = "MFA"
    MASTER_OF_BUSINESS = "MBA"
    MASTER_OF_LIBRARY_SCIENCE = "MLS"
    MASTER_OF_PUBLIC_HEALTH = "MPH"
    MASTER_OF_SOCIAL_WORK = "MSW"
    MASTER_OF_LAWS = "LLM"
    MASTER_OF_ARTS_IN_LIBERAL_STUDIES = "MLS"
    MASTER_OF_MUSIC = "MM"
    MASTER_OF_EDUCATION = "MEd"
    MASTER_OF_ENGINEERING = "MEng"
    MASTER_OF_ARCHITECTURE = "MArch"
    DOCTOR_OF_PHILOSOPHY = "PhD"
    DOCTOR_OF_BUS_AD = "DBA"
    DOCTOR_OF_HEALTH_AD = "DHA"
    DOCTOR_OF_EDU = "EdD"
    DOCTOR_OF_NURS_PRAC = "DNP"



    DEGREE_LEVELS= [
        (ASSOCIATE_OF_ARTS, "Associate of Arts"),
        (ASSOCIATE_OF_SCIENCE, "Associate of Science"),
        (ASSOCIATE_OF_APPLIED_ARTS, "Associate of Applied Arts"),
        (ASSOCIATE_OF_APPLIED_SCIENCE, "Associate of Applied Science"),
        (BACHELOR_OF_ARTS, "Bachelor of Arts"),
        (BACHELOR_OF_SCIENCE, "Bachelor of Science"),
        (BACHELOR_OF_FINE_ARTS, "Bachelor of Fine Arts"),
        (MASTER_OF_ARTS, "Masters of Arts"),
        (MASTER_OF_SCIENCE, "Master of Science"),
        (MASTER_OF_FINE_ARTS, "Master of Fine Arts"),
        (MASTER_OF_BUSINESS, "Master of Business"),
        (MASTER_OF_LIBRARY_SCIENCE, "Master of Library Science"),
        (MASTER_OF_PUBLIC_HEALTH, "Master of Public Health"),
        (MASTER_OF_SOCIAL_WORK, "Master of Social Work"),
        (MASTER_OF_LAWS, "Master of Laws"),
        (MASTER_OF_ARTS_IN_LIBERAL_STUDIES, "Master of Arts in Liberal Studies"),
        (MASTER_OF_MUSIC, "Master of Music"),
        (MASTER_OF_EDUCATION, "Master of Education"),
        (MASTER_OF_ENGINEERING, "Master of Engineering"),
        (MASTER_OF_ARCHITECTURE, "Master of Architecture"),
        (DOCTOR_OF_PHILOSOPHY, "Doctor of Philosophy (PhD)"),
        (DOCTOR_OF_BUS_AD, "Doctor of Business Administration"),
        (DOCTOR_OF_HEALTH_AD, "Doctor of Health Administration"),
        (DOCTOR_OF_EDU, "Doctor of Education"),
        (DOCTOR_OF_NURS_PRAC, "Doctor of Nurse Practice"),
    ]


    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=15,default="")
    date_of_birth = models.DateField(max_length=8, null=True)
    address1 = models.CharField(
        "Address line 1",
        max_length=1024,
        default=""
    )

    address2 = models.CharField(
        "Address line 2",
        max_length=1024,
        default=""
    )

    zip_code = models.CharField(
        "ZIP / Postal code",
        max_length=12,
        default=""
    )

    city = models.CharField(
        "City",
        max_length=1024,
        default=""
    )

    country = models.CharField(
        "Country",
        max_length=50,
        default=""
    )


    degree = models.CharField(
        max_length=5,
        choices=DEGREE_LEVELS,
        default=ASSOCIATE_OF_ARTS
    )
    major = models.CharField(max_length=50, default="")
    university = models.CharField(max_length=50, default="")
    college_email = models.CharField(max_length=50, default="")
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )
    personal_website = models.URLField(blank = True)
    github = models.URLField(blank = True)
    linkedin = models.URLField(blank = True)

    work_experience = models.TextField(default="")



    def __str__(self):
        return f"{self.id} | {self.name}"

class Enterprise(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} | {self.name}"