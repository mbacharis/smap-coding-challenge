# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
#Bokeh is used to create the plots
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components
from bokeh.embed import file_html
from consumption.models import User,Summary
#for removing the timezone information
import pytz

def summary(request):
  #the x_axis_type='datetime' is added to 
  #allow Bokeh to correctly render the datetime
  #the data can't have timezone information
  plot = figure(width=700,height=300, responsive=True,x_axis_type='datetime')
  xData=[]
  yData=[]
  for i in Summary.objects.all():
      xData.append(i.summary_time.replace(tzinfo=None))#removes the timezone information
      yData.append(i.summary_use)
  plot.circle(xData, yData)
  #Formating the plot
  #Remove Bokeh logo and toolbars
  plot.toolbar.logo = None
  plot.toolbar_location = None
  #adds axis labels
  plot.xaxis.axis_label='Date'
  plot.yaxis.axis_label='Total Consumption / Wh'
  script, div = components(plot)	  
  context={"the_script": script, "the_div": div,"the_user":User.objects.all(),}
  return render(request, 'consumption/summary.html', context)

def detail(request, dUser_key):
  #the x_axis_type='datetime' is added to 
  #allow Bokeh to correctly render the datetime
  #the data can't have timezone information
  plot = figure(width=700,height=300, responsive=True,x_axis_type='datetime')
  dUser=User.objects.all()[int(dUser_key)-1]
  xData=[]
  yData=[]
  for i in dUser.energyuse_set.all():
      xData.append(i.EnergyUse_time.replace(tzinfo=None))#removes the timezone information
      yData.append(i.EnergyUse_consumption)
  plot.circle(xData, yData)
  #Formating the plot
  #Remove Bokeh logo and toolbars
  plot.toolbar.logo = None
  plot.toolbar_location = None
  #adds axis labels
  plot.xaxis.axis_label='Date'
  plot.yaxis.axis_label='Consumption / Wh'
  script, div = components(plot)	  
  context={"the_script": script, "the_div": div,"the_user":dUser,}
  return render(request, 'consumption/detail.html', context)