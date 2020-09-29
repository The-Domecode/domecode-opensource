from django.shortcuts import render


def FusionHomeView(requests):
    return render(requests, "fusion/fusion.html", {"title": "Fusion"})


def FusionDetailView(requests):
    return render(requests, "fusion/fusion_detail.html",
                  {"title": "Fusion Immerse"})
