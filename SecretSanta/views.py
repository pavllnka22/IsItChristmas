import random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from SecretSanta.forms import SecretForm



def santa_page(request):
    if "participants" not in request.session:
        request.session["participants"] = []

    participants = request.session["participants"]
    form = SecretForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        name = form.cleaned_data["name"]
        if name not in participants:
            participants.append(name)
            request.session["participants"] = participants
            return HttpResponseRedirect(reverse('santa_page'))
        else:
            form.add_error("name", "Name already in use!")

    return render(request, 'santa.html', {
        "form": form,
        "participants": participants
    })

def make_pairs(participants):
    if len(participants) < 2:
        return None
    givers = participants.copy()
    receivers = participants.copy()
    pairs = {}
    random.shuffle(receivers)
    for giver in givers:
        if giver == receivers[0]:  # якщо даємо сам собі
            receivers.append(receivers.pop(0))  # переміщаємо в кінець
        pairs[giver] = receivers.pop(0)
    return pairs

def generate_pairs(request):
    participants = request.session.get("participants", [])
    pairs = make_pairs(participants)
    request.session["pairs"] = pairs  # зберігаємо в сесії
    if not pairs:
        return render(request, 'pairs.html',
            {"pairs": None,  "error": "at least 2 participants needed"})
    return render(request, "pairs.html", {"pairs": pairs})

def remove_participant(request, name):
    participants = request.session.get("participants", [])
    if name in participants:
        participants.remove(name)
        request.session["participants"] = participants
    return HttpResponseRedirect(reverse('santa_page'))

def clear_participants(request):
    request.session["participants"] = []
    return HttpResponseRedirect(reverse('santa_page'))