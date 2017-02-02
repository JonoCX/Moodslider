from django.shortcuts import render

from .forms import UploadFileForm
from .models import Programme

from xml.dom import minidom

'''
Index function in order to parse the html for the
landing page.
'''
def index(request):
    data = Programme.objects.all()
    if data:  # if there is data in the database
        return render(request, 'index.html', {'content': data})
    else:
        return render(request, 'index.html', {'content': 'no-content'})

'''
Function present and parse the file upload form
on the file-upload html file.
'''
def file_upload(request):
    if request.method == 'POST':  # if a POST has been passed from the front end
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():  # if the content of the form meets what is expected
            file = request.FILES['file']
            xml_file = minidom.parse(file)
            prog_list = xml_file.getElementsByTagName("programme")
            objs = []

            # iterate over the entire contents and append the objects
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

            # batch commit for a performance increase
            Programme.objects.bulk_create(objs)
            return render(request, 'index.html', {'content': objs})
    else:
        form = UploadFileForm()

    return render(request, 'file-upload.html', {'form': form})


'''
Process the mood of the user.
'''
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
