# Django_Framework

## You can find different Django_Framework Projects in this repository.

This are the projects performed by me during the learning of django framework and anyone who is learning django as beginner or has already learned django can use this program for practice. If you have any questions or doubts regarding the program you can contact me:)

Thank You!!

# ********** DJANGO PROJECT STEPS ************
### 1. Open PyCharm ---> New Project ---> Choose Location

### 2. Install Django 

                "pip install django"

### 3. Start Django Project

                  "django-admin startproject PROJECTNAME"

### 4. Change Directory To PROJECTNAME 

                  "cd PROJECTNAME"

### 5. Run Django Project

                     "python manage.py runserver"

### 6. Stop Django Project 

                      "ctrl+c" (in terminal)

DJANGO PROJECT DJANGO_APP1 + DJANGO_APP2 + DJANGO_APP3…

ECOM_PROJECT = AUTH_APP + SELER_APP + BUYER_APP + LOGISTICS_APP + INVERTORY_APP + PAYMENT_APP

### 7. Create a Django App

                             "python manage.py startapp APPNAME"

### 8. Register a Django App

                 FOLDERNAME ---> PROJECTNAME ----> PROJECTNAME ---> settings.py
                  INSTALLED_APPS = [       
                                                              “__________________”,
                                                              “__________________”,
                                                              “__________________”,
                                                              “APPNAME”,
                                                        ]



### 9. Create a View

 FOLDERNAME --> PROJECTNAME---> APPNAME-->views.py
 
       from django.http import HttpResponse
       def VIEWNAME(request):
       ----------------------------------
       ----------------------------------
       resp obj =  HttpResponse("to be returned on browser")
       return resp obj



### 10. Create a App Level urls.py

FOLDERNME---> PROJECTNAME ---> APPNAME ---->urls.py


### 11. Register App Level urls.py to Project Level urls.py

  FOLDERNME ---> PROJECTNAME --->PROJECTNAME ---> urls.py

        from django.urls import path, include
		urlpatterns = [
		path("admin/",……………………...),
		………………………………………………..,
		path("project_lvl_url/", include("APPNAME.urls"))
		  ]


### 12. Create a URLPattern

  FOLDERNME ---> PROJECTNAME---> APPNAME ---> urls.py

			from django.urls import path
			urlpatterns = [
			path("/url", VIEWNAME)
			]

<img width="524" height="680" alt="image" src="https://github.com/user-attachments/assets/535f3d4a-8465-4c36-bd0f-d67bef74a670" />


### 13.Create a directory "templates"

FOLDERNAME ---> PROJECTNAME ---> templates

### 14. Create a sub-directory "APPNAME"

FOLDERNAME ---> PROJECTNAME ---> templates ---> APPNAME

### 15. Register/Configure the "templates" directory 
FOLDERNAME ---> PROJECTNAME ---> settings.py

		TEMPLATES = [ { k1:v1, k2:v2, "DIRS": ["templates"] } ]
		While deployment-
		TEMPLATES = [ { k1:v1, k2:v2, "DIRS": [ os.path.join(BASE_DIR, "templates")]}]

### 16. Create a template (HTML File)

FOLDERNAME ---> PROJECTNAME ---> templates ---> APPNAME ---> templ.html

### 17. Create a view to Render the template

 		from django.shortcuts import render

  FOLDERNAME ---> PROJECTNAME --> APPNAME ---> views.py

		def VIEWNAME(request):
		template_name = "APPNAME/template.html"
		context = {} 
		return render(request, template_name, context)

### 18. Create a AppLevel URL (Assuming that, we've the AppLevel urls.py file ready & registered) 

			from django.urls import path
			from. import views


# Django Template Language (DTL)

FOLDERNAME/PROJECTNAME/templates/APPNAME/templ.html

### ----> Variable

		{{ context_key }}

### -----> Conditional Statements

		{% if LHS CMP_OP RHS %}
		<tag> content1 </tag>
		<tag> content2 </tag>
		{% elif LHS CMP_OP RHS %}
		<tag> content1 </tag>
		<tag> content2 </tag>
		{% else %}
		<tag> content1 </tag>
		<tag> content2 </tag>
		{% endif %}

### -----> Control Flow Statements

		{% for VAR in CONTEXT_KEY %}
		<tag> {{VAR}} </tag>
		{% endfor %}


# Extrernal Static Files in Django

### 19. Create a directory to store the Static Files

FOLDERNAME -> PROJECTNAME --> static -> APPNAME

### 20. Register/Configure the directory

FOLDERNAME --> PROJECTNAME --> settings.py

		STATICFILES_DIRES = [ "static"]

### 21. Load static Files in Django Templates

FOLDERNAME --> PROJECTNAME --> templates --> AppNAME --> templ1.html

		{% load static %}
		<head>
		<link rel="stylesheet" href="{% static 'resource.css' %}">
		</head>
		<body>
		<img rel="stylesheet" src="{% static 'images/FILENAME.jpg' %}">
		</body>

### 22. ---> ConvertsPython Code into SQL (Generates SQL code)
		python manage.py makemigrations 

### 23.  ---> Executes the generated SQL code
		python manage.py migrate   

### 24. ---> superuser create
		python manage.py createsuperuser

### Create your models here.

### Django Models is a python class that inherits django.db.models.Model

### Each attribute of the model represents a database field/column.

### Django Models is used to create database tables and manipulate data in the database.

### 25. Create a Django Model

FOLDERNAME --> PROJECTNAME --> AppNAME --> models.py

		from django.db import models
		class MODELNAME (models. Model):
		field1 = models. FIELDCLASS()
		field2 = models. FIELDCLASS()
		field3= models. FIELDCLASS()

### 26. Register a Django Model

FOLDERNAME --> PROJECTNAME --> AppNAME -->admin.py

		from django.db import admin
		class MODELNAMEAdmin (admin. ModelAdmin):
		list_display = [10,20,30,40,50]

### 27. Visit

		---> http://127.0.0.1:8000/admin/

#DJANGO ORM QUERIES

### Retieval

 29.	 objs_qs = MODELNAME.objects.all()

 30.	 obj = MODELNAME.objects.get(col = val)

### Update

 31. 	obj MODELNAME.objects.get(col = val) 
      obj.member = NEWVAL 
      obj.save()

### Delete

32. 	obj = MODELNAME.objects.get(col = val) 
     obj.delete()

### Insert

33. 	obj MODELNAME(col1=vall, col2=val2,...) 
     obj.save()

### Retrieval

34. 	objs_qs = MODELNAME.objects.filter(col =  val)

35. 	objs_qs = MODELNAME.objects.filter(col_lt = val)

36. 	objs_qs = MODELNAME.objects.filter(col_lte = val)

37. 	objs_qs = MODELNAME.objects.filter(col_gt = val)

38. 	objs_qs = MODELNAME.objects.filter(col_gte = val)

39.	 objs_qs = MODELNAME.objects.filter(col_startswith = "L")

40.	 objs_qs = MODELNAME.objects.filter(col_endswith = "L")

41. 	objs_qs = MODELNAME.objects.filter(col_contains = "L")

42. 	objs_qs = MODELNAME.objects.order_by("col")

43. 	objs_qs = MODELNAME.objects.order_by("-col")

### Aggregate Functions

---->from diange.dk.models import Max, Min, Sum, Avg, Count

44.	 MODELNAME.objects.all().aggregate (Max("col"))

45. 	MODELNAME.objects.all().aggregate (Min("col"))
 
46. MODELNAME.objects.all().aggregate(Sum("col"))

47.	MODELNAME.objects.all().aggregate(Avg("col"))

48. MODELNAME.objects.all().aggregate(Count("col"))


### Django Forms

49. Create a Django Model

PROJECTAPP---->APPNAME--->models.py

from django.db import models 
class MODELNAME(models.Model):
field1 models. FieldName()
field2 models. FieldName()
.
.
fieldN models. FieldName()


50. Create a forms.py

PROJECTNAME----> APPNAME ------>forms.py

51. Create a ModelForm

PROJECTNAME----->APPNAME-------> forms.py

From. models import MODELNAME
from django import forms
class MODELNAMEModelFrom(forms.ModelForm):
class Meta:
model= "MODELNAME"
fields= ["field1", "field2",...) #OR "__all__"

52. Send the Model Form instance to the corresponding templates

PROJECTNAME-----> APPNAME------> VIEWS .py

def view1(request):

if request.method == "GET":
template_name = "to/path/template.html"
form= MODELNAMEModelFrom()
context = {}
return render(request, template_name, context)

elif request.method == "POST":
form =MORELNAMEModelFrom(request.POST)
if form.is_valid():
form.save()

53.Create a template to render the ModelForm 

PROJECTNAME-----> templates -----> APPNAME------> templ.html

<form method="POST">

{% csrf token %}

{{form}}

<input type="submit">

</form>


### Empty Form:

### Form ModelForm()
### Form filled with data from FrontEnd
### form= ModelForm(request.POST)
### Form filled with data from BackEnd
### obj = MODEL.objects.get(CONDITION)
### form= ModelForm(instance=obj)
### Form filled with data from FrontEnd (UI) to update it in the BackEnd(08)
### obj MODEL.objects.get(CONDITION)
### form = ModelForm(request.POST, instance=obj)

### URL Names

PROJECTNAME -----> APPNAME----->urls.py

from django.urls import path 
from . import views
urlpatterns = [
path("add/", views.add_course_view, name="addurl")
          ]
PROJECTNAME ---> templates ---> APPNAME ---> templ.html

<a href={%  url "addurl" %} >

<tag>Actual Content</tag>

</a>

### Dynamic URLs in Django

1. Create a Dynamic URL using DTL {{ VAR }}

PROJECTNAME-----> templates ----> APPNAME -----> templ.html

<a href="/project/app/{{VAR}}/">

<tag> content </tag>

</a>

2. Create a Dynamic URL Path

PROJECTNAME ----->APPNAME-------> urls.py

urlpatterns = [
path("app/<j>/", views. VIEWNAME),
]
3. Create a Dynamic view

PROJECTNAME-----> APPNAME--------> views.py

def VIEWNAME(request,j):
------------------------------------
-----------------------------------
-----------------------------------



### Django Crispy Forms

1. Install Django Crispy Forms

pip install crispy-bootstrap5

2. Register Django Crispy Forms

PROJECTNAME-----> PROJECTNAME ---> settings.py

INSTALLED_APPS = [
"APP1",
"APP2",
.
.
"crispy_forms",
"crispy_bootstrap5",
]


3. Configure Django Crispy Forms

PROJECTNAME -----> PROJECTNAME -----> settings.py

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

4. Load Django Crispy Form Tags

PROJECTNAME------> templates ---> APPNAME ------> templ.html

{% load crispy_forms_tags %}

5. Apply Django Crispy Form Filter

PROJECTNAME------> templates ------> APPNAME------> templ.html

{{ form|crispy }}


