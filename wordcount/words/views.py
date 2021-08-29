from django.shortcuts import render
from words.forms import text
# Create your views here.
def index(request):
    form = text()
    if request.method == 'POST':
        form = text(request.POST)
        if form.is_valid():
            total_count_words = form.cleaned_data['total_words']
            total_count_list = total_count_words.split(' ')
            word_count = len(total_count_list)
        return render(request,'total.html',{'total':word_count,'total_count_words':total_count_words}) 
    return render(request,'index.html',{'form':form})
