
import pyrebase
from django.http import HttpResponse
from django.shortcuts import render
from .forms import *

config = {
    'apiKey': "AIzaSyB6AIIq0bpkVyBe0thCPJ68sd35RWzsOQk",
    'authDomain': "pictures-6b720.firebaseapp.com",
    'databaseURL': "https://pictures-6b720.firebaseio.com",
    'projectId': "pictures-6b720",
    'storageBucket': "pictures-6b720.appspot.com",
    'messagingSenderId': "419981868746",
    'appId': "1:419981868746:web:4109a439cbbd4728af3e33",
    'measurementId': "G-1X1JG83079"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


def signIn(request):
    return render(request, "signIn.html")


def postsign(request):
    email=request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        auth.sign_in_with_email_and_password(email, passw)
    except:
        message = "invalid credentials"
        return render(request,"signIn.html", {"msg" : message})
    return render(request, "welcome.html")


def signUp(request):
    return render(request, "signUp.html")


def home(request):
    if auth.current_user is None:
        return render(request, "signIn.html")
    return render(request, "welcome.html")


def postSignUp(request):
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    try:
        auth.create_user_with_email_and_password(email, passw)
        auth.sign_in_with_email_and_password(email, passw)
    except:
        message = "error with user creation"
        return render(request,"signUp.html",{"msg" : message})
    return render(request, "welcome.html")


def uploadPicture(request):
    if auth.current_user is None:
        return render(request, "signIn.html")
    elif request.method == 'POST':
        form = PictureForm(auth.current_user['localId'], request.POST, request.FILES)

        if form.is_valid():
            photo = form.save()
            photo.user_id = auth.current_user['localId']
            if form.cleaned_data['album']:
                photo.album_id = form.cleaned_data['album'].id
            else:
                photo.album_id = 0
            photo.save()
            return render(request, "uploadPicture.html",
                {"msg" : "Upload Successful !", "form": form})
    else:
        form = PictureForm(auth.current_user['localId'])
    return render(request, "uploadPicture.html", {'form' : form})


def picturesGallery(request):
    if auth.current_user is None:
        return render(request, "signIn.html")
    pictures = Picture.objects.filter(user_id=auth.current_user['localId'])
    return render(request, "picturesFeed.html", {"gallery" : pictures})


def createAlbum(request):
    if auth.current_user is None:
        return render(request, "signIn.html")
    elif request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)

        if form.is_valid():
            album = form.save(commit=False)
            album.user_id = auth.current_user['localId']
            album.save()
            return render(request, "createAlbum.html",
                {"msg" : "Album Created !", "form": form})
    else:
        form = AlbumForm()
    return render(request, "createAlbum.html", {'form' : form})


def albumGallery(request):
    if auth.current_user is None:
        return render(request, "signIn.html")
    albums = Album.objects.filter(user_id=auth.current_user['localId'])
    return render(request, "albumsGallery.html", {"albums": albums})


def albumContent(request, id):
    if auth.current_user is None:
        return render(request, "signIn.html")
    album = Album.objects.get(id=id, user_id=auth.current_user['localId'])
    photos = Picture.objects.filter(album_id=id, user_id=auth.current_user['localId'])
    return render(request, "albumContent.html", {"album": album, "photos": photos})