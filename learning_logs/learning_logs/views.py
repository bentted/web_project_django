from django.shortcuts import render
from .models import Topic

def index(request):
    return render(request, 'learning_logs/index.html')


def topics(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = Topic.entry_set.order_by('-date_added')
    context = {'Topic': topic, 'entries' : entries}
    return render(request, 'learning_logs/topics.html', context)

# Create your views here.
