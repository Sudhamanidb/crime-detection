from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import cv2
import os
from django.utils.timezone import now
from django.conf import settings
from .models import EmergencyAlert
from django.core.files import File
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session["username"] = user.username  # Store in session
            return redirect("/admin/crime_prediction/userprofile/")
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')




# Save recorded video function
def save_recorded_video(user, video_filename):
    timestamp = now().strftime('%Y%m%d_%H%M%S')
    video_folder = os.path.join(settings.MEDIA_ROOT, 'emergency_videos', str(user.id), timestamp)
    os.makedirs(video_folder, exist_ok=True)

    video_file_path = os.path.join(video_folder, video_filename)

    cap = cv2.VideoCapture(0)  # Capture from webcam
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(video_file_path, fourcc, 30.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv2.imshow('Recording', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    return video_file_path

# Create emergency alert
def create_emergency_alert(user, location, description):
    video_filename = "alert_video.mp4"
    video_file_path = save_recorded_video(user, video_filename)

    with open(video_file_path, 'rb') as f:
        video_file = File(f)
        alert = EmergencyAlert.objects.create(
            user=user,
            location=location,
            description=description,
            video_file=video_file
        )

    return alert

# Emergency Alert view - save the emergency alert to the database
@login_required
def emergency_alert(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        video_url = request.POST.get('video_url')
        description = request.POST.get('description')

        alert = EmergencyAlert.objects.create(
            user=request.user,
            location=location,
            video_url=video_url,
            description=description
        )
        alert.save()

        return HttpResponse("Emergency alert recorded successfully!")
    return render(request, 'emergency_alert.html')

# Home view
def home(request):
    return render(request, 'home.html')

# About Us view
def about(request):
    return render(request, 'aboutus.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            # Redirect to the user profile or admin panel, passing the logged-in user's username
            return redirect('User profile')  # This should be the name of your profile view
        else:
            # Invalid login, show an error message
            messages.error(request, 'Invalid username or password.')
            return redirect('login')  # Redirect back to the login page

    return render(request, 'login.html')
# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Index view
def index(request):
    return render(request, 'index.html')
