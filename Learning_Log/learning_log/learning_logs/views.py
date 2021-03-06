from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Entry, Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    """home page app Learning_Log"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Print a list of topics"""
    
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """display the topic and all entries"""
    topic = Topic.objects.get(id=topic_id)
    # check that topic belongs current user
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """define new topic"""
    if request.method != 'POST':
        # data didn't send 
        form = TopicForm()
    else:
        # data 'POST' sent, new empty form creates
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            form.save()
            return redirect('learning_logs:topics')
    # display empty or error form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """add new entry to the specific topic"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # data didn't send
        form = EntryForm()
    else:
        # data POST sent, process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id = topic_id)

    # display empty or error form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404    

    if request.method != 'POST':
        # original request; the form fills in the data from the current entry
        form = EntryForm(instance=entry)
    else:
        # send POST data; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id = topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)



    
