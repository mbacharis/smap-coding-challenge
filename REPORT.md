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

Bokeh is used to create the plot with the summary data. This is used as Bokeh can directly output in html and has also interactive features (to turn these on comment from views.py line 34).

User.objects.all() is passed to the template to provide the data for the creation of the table in the template.

<Update> The detail view has been implemented based on the summary view with the addition of the variable dUser_key 

Templates - consumption/summary.html:

The template imports some styles for Bokeh and splits the screen in two for the plot and the table. 

In the first implementation the hyperlinks for the table just point to "/detail/"
 
<Update> with the full detail implementation they now point "/detail/'user_id'" 

Templates - consumption/detail.html:

The consumption/detail.html template was implemented based on the summary.html modifying the table to display details for one user and adding a line with a hypelink for returning back to the summary view.

consuption/urls.py:

the "url(r'^summary/$', views.summary)," was removed to simplify the url tree. The detail url modified to accept the dUser_key variable

admin.py:

Registered a basic form of the models. This needs to be improved.

No admin user has been created

To do list:

+ Explore better way of importing external data, experiment with build-in migrate functionality

+ Improve admin site

+ Develop testing scripts
