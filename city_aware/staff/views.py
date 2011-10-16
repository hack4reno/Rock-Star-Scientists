# -*- coding: utf-8 -*
from django.shortcuts import render

from livereno.models import Venues, Sponsors, EventCategories, Events

def staff_home(request):
    #TODO direct to template
    a = {}
    return render(request, 'staff/staff_home.html', a)
    
def view_event_categories(request):
    #TODO direct to template
    a = {}
    #return render(request, 'staff/event_categories_main.html', a)
    return render(request, 'staff/event_categories_table.html', a)
    
def view_venues(request):
    #TODO direct to template
    a = {}
    return render(request, 'staff/venues_main.html', a)

    
def list_venues(request):
    #TODO direct to template
    a = {}
    a['items'] = Venues.objects.all()
    return render(request, 'staff/list_venues.html', a)

def edit_sponsors(request):
    #TODO direct to template
    a = {}
    return render(request, 'staff/edit_sponsors.html', a)
    
def list_sponsors(request):
    #TODO direct to template
    a = {}
    a['items'] = Sponsors.objects.all()
    return render(request, 'staff/list_sponsors.html', a)

def list_categories(request):
    #TODO direct to template
    a = {}
    a['items'] = EventCategories.objects.all()
    return render(request, 'staff/list_categories.html', a)
    
def list_events(request):
    #TODO direct to template
    a = {}
    a['items'] = Events.objects.all()
    return render(request, 'staff/list_events.html', a)
