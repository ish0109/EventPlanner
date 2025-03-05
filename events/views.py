from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, RSVP
from .forms import EventForm
from .forms import RSVPForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    form = RSVPForm()

    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            rsvp = form.save(commit=False)
            rsvp.event = event
            rsvp.save()

            return redirect('event-list')

    return render(request, 'events/event_detail.html', {'event': event, 'form': form})

def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('event-list')
    else:
        form = EventForm()
    
    return render(request, 'events/event_form.html', {'form': form, 'title': 'Create Event'})

def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event-list')
    else:
        form = EventForm(instance=event)
    
    return render(request, 'events/event_form.html', {'form': form, 'title': 'Update Event'})

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        event.delete()
        return redirect('event-list')
    
    return render(request, 'events/event_confirm_delete.html', {'event': event})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    form = RSVPForm()
    return render(request, 'events/event_detail.html', {'event': event, 'form': form})

def home(request):
    return render(request, 'home.html', {'events': event_list})

