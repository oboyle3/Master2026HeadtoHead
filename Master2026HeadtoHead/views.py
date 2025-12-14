from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import UserTrackedGolfers, AllGolfers
from Master2026HeadtoHead.utils import user_team_total

def landing(request):
    return render(request, 'landing.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('landing')

@login_required
def dashboard(request):
    lineup, _ = UserTrackedGolfers.objects.get_or_create(user=request.user)

    ROUNDS_COMPLETED = 3  # 🔧 manually change this as admin

    # Debug: show lineup slots
    slots = [
        lineup.selection1,
        lineup.selection2,
        lineup.selection3,
        lineup.selection4,
        lineup.selection5,
    ]
    for i, golfer in enumerate(slots, start=1):
        print(f"Slot {i}:", golfer)

    # User's average score
    average_score = (
        user_team_total(lineup) / ROUNDS_COMPLETED
        if ROUNDS_COMPLETED > 0 else 0
    )

    # 🔥 Build leaderboard
    leaderboard = []
    for l in UserTrackedGolfers.objects.select_related(
        "selection1", "selection2", "selection3", "selection4", "selection5", "user"
    ):
        avg = (
            user_team_total(l) / ROUNDS_COMPLETED
            if ROUNDS_COMPLETED > 0 else 0
        )
        leaderboard.append({
            "user": l.user.username,
            "average_score": avg
        })

    # Lower score is better
    leaderboard.sort(key=lambda x: x["average_score"])

    return render(request, 'dashboard.html', {
        'lineup': lineup,
        'average_score': average_score,
        'leaderboard': leaderboard,
        'rounds_completed': ROUNDS_COMPLETED
    })

@login_required
def updateslot1(request):
    golfers = AllGolfers.objects.filter(rating__gte=9, rating__lte=10)
    if request.method == "POST":
        golfer_id = request.POST.get("golfer")
        if golfer_id:
            lineup, _ = UserTrackedGolfers.objects.get_or_create(user=request.user)
            lineup.selection1_id = golfer_id
            lineup.save()
        return redirect("dashboard")
    return render(request, 'update_slot1.html', {'golfers': golfers})


@login_required
def updateslot2(request):
    golfers = AllGolfers.objects.filter(rating__gte=7, rating__lte=8)
    if request.method == "POST":
        golfer_id = request.POST.get("golfer")
        if golfer_id:
            lineup, _ = UserTrackedGolfers.objects.get_or_create(user=request.user)
            lineup.selection2_id = golfer_id
            lineup.save()
        return redirect("dashboard")
    return render(request, 'update_slot2.html', {'golfers': golfers})


@login_required
def updateslot3(request):
    golfers = AllGolfers.objects.filter(rating__gte=5, rating__lte=6)
    if request.method == "POST":
        golfer_id = request.POST.get("golfer")
        if golfer_id:
            lineup, _ = UserTrackedGolfers.objects.get_or_create(user=request.user)
            lineup.selection3_id = golfer_id
            lineup.save()
        return redirect("dashboard")
    return render(request, 'update_slot3.html', {'golfers': golfers})


@login_required
def updateslot4(request):
    golfers = AllGolfers.objects.filter(rating__gte=3, rating__lte=4)
    if request.method == "POST":
        golfer_id = request.POST.get("golfer")
        if golfer_id:
            lineup, _ = UserTrackedGolfers.objects.get_or_create(user=request.user)
            lineup.selection4_id = golfer_id
            lineup.save()
        return redirect("dashboard")
    return render(request, 'update_slot4.html', {'golfers': golfers})


@login_required
def updateslot5(request):
    golfers = AllGolfers.objects.filter(rating__gte=1, rating__lte=2)
    if request.method == "POST":
        golfer_id = request.POST.get("golfer")
        if golfer_id:
            lineup, _ = UserTrackedGolfers.objects.get_or_create(user=request.user)
            lineup.selection5_id = golfer_id
            lineup.save()
        return redirect("dashboard")
    return render(request, 'update_slot5.html', {'golfers': golfers})


