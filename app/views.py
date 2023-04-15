from django.shortcuts import render
from translate import Translator


# Create your views here.

def index(request):
    if request.method == 'POST':
        text = request.POST['translate']
        lang = request.POST['language']
        translator = Translator(to_lang=lang)
        translation = translator.translate(text)
        word1 = wordCount(text)
        word2 = wordCount(translation)
        context = {
            'translation': translation,
            'word1': word1,
            'word2': word2
        }
        return render(request,'index.html', context)
    return render(request, 'index.html')



def wordCount(text):
    if text != '':
        word = len(text.split())
        return word

