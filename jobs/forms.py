from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
# from phonenumber_fields import PhoneNumberField

class NewUserForm(UserCreationForm):
    firstname = forms.CharField(max_length = 30, label = 'First Name', required = True)
    middlename = forms.CharField(max_length = 30, label = 'Middle Name', required = False, help_text = "Optional")
    lastname = forms.CharField(max_length = 30, label = 'Last Name', required = True)
    email = forms.EmailField(max_length = 256, label = 'Email Address', required=False, help_text = "Please use a frequently checked email")
    dateofbirth = forms.DateField(widget = AdminDateWidget, label = 'Date of Birth', required = False, help_text = 'MM/DD/YYYY or Select From Calendar')
    university = forms.CharField(max_length = 100, label = 'University/College Name', required = False, help_text = 'Optional')
    degree = forms.CharField(max_length = 50, label = 'Degree/Highest Level of Education', required = False, help_text = 'Optional')
    major = forms.CharField(max_length = 50, label = 'University Major', required = False, help_text = 'Optional')
    yearinschool = forms.CharField(max_length = 10, label = 'Current Year in School', required = False, help_text = 'Optional')
    personalwebsite = forms.URLField(max_length = 256, label = 'Personal Website Link', required = False, help_text = 'Optional')
    github = forms.URLField(max_length = 256, label = 'GitHub Link', required = False, help_text = 'Optional')
    linkedin = forms.URLField(max_length = 256, label = 'LinkedIn Link', required = False, help_text = 'Optional')
    workexperience = forms.CharField(max_length = 1000, label = 'Past Work Experience', required = False, help_text = 'Optional')

    class Meta:
        User = get_user_model()
        model = User
        fields = ("username", "password1", "password2", "firstname", "middlename", "lastname", "email", "dateofbirth", 
        "degree", "major", "university", "yearinschool", "personalwebsite", "github", "linkedin", "workexperience")

    #to implement 
    #"address1", "zipcode1", "city1", "country1", "address2", "zipcode2", "city2", "country2", "phonenumber", 

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.firstname = self.cleaned_data['firstname']
        user.email = self.cleaned_data['email']
        
        user.middlename = self.cleaned_data['middlename']
        user.lastname = self.cleaned_data['lastname']
        user.dateofbirth = self.cleaned_data['dateofbirth']
        user.university = self.cleaned_data['university']
        user.degree = self.cleaned_data['degree']
        user.major = self.cleaned_data['major']
        user.yearinschool = self.cleaned_data['yearinschool']
        user.personalwebsite = self.cleaned_data['personalwebsite']
        user.github = self.cleaned_data['github']
        user.linkedin = self.cleaned_data['linkedin']
        user.werkexperience = self.cleaned_data['workexperience']

        if commit:
            user.save()
        return user