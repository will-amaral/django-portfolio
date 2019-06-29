from django.shortcuts import render, redirect
from wordcount.forms import CountForm
import operator

def count_index(request):
    if 'text' in request.session:
        request.session.flush() 
    form = CountForm()
    if request.method == 'POST':
        form = CountForm(request.POST)
        if form.is_valid():
            request.session['text'] = form.cleaned_data["body"]
            return redirect('count_result')
    context = {
        "form": form
    }
    
    return render(request, "count_index.html", context)

def  count_result(request):
    if 'text' in request.session:
        text = request.session['text']
        numText = text.lower().split()
        numWords = len(set(numText))
        wordList = {}
        for word in numText:
            wordList[word] = numText.count(word)
        wordList = dict(sorted(wordList.items(), key=operator.itemgetter(0)))
        wordList = dict(sorted(wordList.items(), key=operator.itemgetter(1), reverse=True))
        context = {
            "text": text,
            "numWords": numWords,
            "wordList": wordList
        }
    else:
        return redirect('count_error')

    return render(request, "count_result.html", context)

def count_error(request):
    return render(request, "count_error.html")




# Create your views here.
