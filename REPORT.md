M. Bacharis 

The adopted approach is detailed below:

models.py:

I have chosen to include 3 models. The first, "Summary", is for storing summary data for all users that will be presented in the summary page. These are processesed by the load.py file, see below. The User and EnergyUse models are for loading the user and consumption data.

load.py:

To load the initial data to the database I wrote the load.py script. To run this:
$python manage.py shell
>>>execfile("../load.py")

It also creates an error report as there are some additional elements in some of the files same timestamp repeated twice. These second instances are saved in the error report as error_report.csv

Also for test purposes there is a break in lines 67-68 that should be removed at full deployement. This was included as the loading process in my computer takes a long time, I should explore alternatives.

views.py: 

Bokeh is used to create the plot with the summary data. This is used as Bokeh can directly output in html and has also interactive features (to turn these off uncomment from views.py line 34).

User.objects.all() is passed to the template to provide the data for the creation of the table in the template. 

Templates - consumption/summary.html:

The template imports some styles for Bokeh and splits the screen in two for the plot and the table. 

In the first implementation the hyperlinks for the table just point to "/detail/"  
