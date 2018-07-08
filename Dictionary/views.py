from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Word

count = 5
def index(request):
	word_list = Word.objects.order_by('date')
	# for i in webpages:
	# 	for top in topic:
	# 		print(i.topic == top)
	my_dict = {'word_list':word_list,
				'insert_me': "Mirkan Kilic, came from1 views.py!"
				}
	return render(request, 'Dictionary/index.html', context=my_dict)

def explain(request):
	global count
	count -= 1
	my_dict = {
	'insert_me': "Mirkan Kilic, came from1 views.py!",
	"count": count,
	}
	# print(count)
	if count == 0:
		count = 5
		return HttpResponse("You explained fast and counted bro XD<br><br><a href=\"other\">Click to return back</a><br><h1>(You see this because Count is %d )</h1>" % (count - count))
	return render(request, 'Dictionary/explain.html', context=(my_dict))

def other(request):
	return render(request, 'Dictionary/other.html')

def word_detail(request, pk):
	word = get_object_or_404(Word, pk=pk)
	return render(request, 'Dictionary/word_detail.html', {'word':word})