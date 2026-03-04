from django.shortcuts import render, redirect
from .models import Vote
from django.db.models import Count

def vote_view(request):
    if request.method == "POST":
        choice = request.POST.get("choice")
        if choice in ["cat", "dog"]:
            Vote.objects.create(choice=choice)
        return redirect("results")

    return render(request, "vote.html")


def results_view(request):
    total_votes = Vote.objects.count()

    vote_counts = Vote.objects.values("choice").annotate(count=Count("choice"))

    cat_votes = 0
    dog_votes = 0

    for item in vote_counts:
        if item["choice"] == "cat":
            cat_votes = item["count"]
        elif item["choice"] == "dog":
            dog_votes = item["count"]

    winner = "Tie"

    if cat_votes > dog_votes:
        winner = "Cat 🐱"
    elif dog_votes > cat_votes:
        winner = "Dog 🐶"

    context = {
        "total_votes": total_votes,
        "cat_votes": cat_votes,
        "dog_votes": dog_votes,
        "winner": winner,
    }

    return render(request, "results.html", context)