from django.shortcuts import render
from .models import Song
from .utils import detect_moods_from_text
from django.db.models import Q

def home(request):
    songs = []
    moods = []
    confession = ""

    if request.method == "POST":
        confession = request.POST.get("confession")
        moods = detect_moods_from_text(confession)
        print("Confession:", confession)
        print("Detected Moods:", moods)

        # Filter songs by any of the detected moods
        query = Q()
        for mood in moods:
            query |= Q(moods__icontains=mood) | Q(lyrics__icontains=mood) | Q(name__icontains=mood)
        songs = list(Song.objects.filter(query))  # Convert queryset to list

        print("Songs found:", len(songs))

    return render(request, "player/home.html", {
        "songs": songs,
        "mood": moods[0] if moods else "No mood detected",  # Pass the first mood or fallback
        "confession": confession
    })

