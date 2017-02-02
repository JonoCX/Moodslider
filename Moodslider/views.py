from django.shortcuts import render

from .forms import UploadFileForm
from .models import Programme

from xml.dom import minidom


def index(request):
    data = Programme.objects.all()
    if data:
        return render(request, 'index.html', {'content': data})
    else:
        return render(request, 'index.html', {'content': 'no-content'})

def file_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            xml_file = minidom.parse(file)
            prog_list = xml_file.getElementsByTagName("programme")
            objs = []
            for prog in prog_list:
                pid = prog.getAttribute('id')
                name = prog.getElementsByTagName('name')[0].firstChild.data
                image = prog.getElementsByTagName('image')[0].firstChild.data
                mood = prog.getElementsByTagName('mood')[0].firstChild.data

                objs.append(Programme(
                    programme_id=pid,
                    name=name,
                    image=image,
                    mood=mood)
                )

            Programme.objects.bulk_create(objs)
            return render(request, 'index.html', {'content': objs})
    else:
        form = UploadFileForm()

    return render(request, 'file-upload.html', {'form': form})


def process_mood(request):
    mood = request.GET.get('mood')
    slider_id = request.GET.get('slider_id')

    data = Programme.objects.all()
    if slider_id == 'one':
        if mood == '2':
            data = Programme.objects.filter(mood='Agitated')
        elif mood == '0':
            data = Programme.objects.filter(mood='Calm')
    elif slider_id == 'two':
        if mood == '2':
            data = Programme.objects.filter(mood='Happy')
        elif mood == '0':
            data = Programme.objects.filter(mood='Sad')
    elif slider_id == 'three':
        if mood == '2':
            data = Programme.objects.filter(mood='Tired')
        elif mood == '0':
            data = Programme.objects.filter(mood='Wide Awake')
    elif slider_id == 'four':
        if mood == '2':
            data = Programme.objects.filter(mood='Scary')
        elif mood == '0':
            data = Programme.objects.filter(mood='Fearless')

    return render(request, 'suggestions.html', {'content': data})
