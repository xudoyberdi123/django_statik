from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Category, News, Suggestion
# from django.db import connection
# from contextlib import closing

from random import randint


# def baza():
#     with closing(connection.cursor()) as cur:
#         cur.execute(""" SELECT * FROM news_news """)
#


def index(requests):
    news = News.objects.all().order_by("-created_at")
    l1 = []
    for i in news:
        l1.append(i)
    states = {
        "ctg": news,
        "xabar": l1[randint(0, len(l1)-1)]

    }
    # baza()
    return render(requests, "index.html", states)


def category(requests, category_id):
    ctg = get_object_or_404(Category, pk=category_id)
    fo = get_list_or_404(News, category_id=category_id)
    # foa = News.objects.all().filter(category_id=category_id)
    # ctg = Category.objects.get(pk = category_id)
    new_rand = News.objects.all().order_by("-created_at")
    new_ra = News.objects.all().order_by("created_at")

    states = {
        "category_id": category_id,
        "ctg": ctg,
        "fo": fo,
        "a": new_rand,
        "b": new_ra
    }

    return render(requests, "category.html", states)


def contact(requests):
    suggest = Suggestion()
    if requests.POST:
        suggest.user_name = requests.POST.get("user_name")
        suggest.email = requests.POST.get("email")
        suggest.text = requests.POST.get("text")
        suggest.save()
    return render(requests, "contact.html")


def view(requests, news_id):
    new = get_object_or_404(News, pk=news_id)
    new_rand = News.objects.all().order_by("-created_at")
    new_ra = News.objects.all().order_by("created_at")
    states = {
        "news_id": news_id,
        "new": new,
        "a": new_rand,
        "b": new_ra
    }
    return render(requests, "view.html", states)


def search(requests):
    print("asdasdasdad")
    var = requests.POST.get("search")
    news = News.objects.all().order_by("-created_at")
    l1 = []
    if requests.POST:
        srch_where = News.objects.all()
        for i in srch_where:
            if var.lower() in str(i.title).lower():
                l1.append(i)
    print("asdasd", l1)
    ctx = {
        "complated_search": l1,
        "length": len(l1),
        "result": var,
        "news": news
    }

    return render(requests, "search.html", ctx)
