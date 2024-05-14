from django.shortcuts import render
from .models import Topic
from .froms import TopicForm

def index(request):
    return render(request, 'learning_logs/index.html')


def topics(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = Topic.entry_set.order_by('-date_added')
    context = {'Topic': topic, 'entries' : entries}
    return render(request, 'learning_logs/topics.html', context)


def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
# Create your views here.
