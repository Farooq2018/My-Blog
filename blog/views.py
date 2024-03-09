from datetime import date
from django.shortcuts import render


all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Farooq",
        "date" : date(2024,8,10),
        "title": "Hiking",
        "excerpt": "There is nothing like the views in the vally",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illo amet iste nulla officia perferendis aliquam,
            ipsum maiores sequi nisi maxime ex aliquid eligendi doloribus iure, molestias fuga, error recusandae ullam?

            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illo amet iste nulla officia perferendis aliquam,
            ipsum maiores sequi nisi maxime ex aliquid eligendi doloribus iure, molestias fuga, error recusandae ullam?

            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illo amet iste nulla officia perferendis aliquam,
            ipsum maiores sequi nisi maxime ex aliquid eligendi doloribus iure, molestias fuga, error recusandae ullam?
"""
    },
    {
        "slug": "delicious-meal",
        "image": "mountains.jpg",
        "author": "Farooq",
        "date" : date(2021,7,15),
        "title": "Delicious Meal",
        "excerpt": "There is nothing like the views in the vally",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illo amet iste nulla officia perferendis aliquam,
            ipsum maiores sequi nisi maxime ex aliquid eligendi doloribus iure, molestias fuga, error recusandae ullam?

            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illo amet iste nulla officia perferendis aliquam,
            ipsum maiores sequi nisi maxime ex aliquid eligendi doloribus iure, molestias fuga, error recusandae ullam?

            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illo amet iste nulla officia perferendis aliquam,
            ipsum maiores sequi nisi maxime ex aliquid eligendi doloribus iure, molestias fuga, error recusandae ullam?
"""
    },
    {
        "slug": "office-view",
        "image": "mountains.jpg",
        "author": "Farooq",
        "date" : date(2022,10,25),
        "title": "Nice view from Office",
        "excerpt": "There is nothing like the views in the vally",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illo amet iste nulla officia perferendis aliquam,
            ipsum maiores sequi nisi maxime ex aliquid eligendi doloribus iure, molestias fuga, error recusandae ullam?

            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illo amet iste nulla officia perferendis aliquam,
            ipsum maiores sequi nisi maxime ex aliquid eligendi doloribus iure, molestias fuga, error recusandae ullam?

            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illo amet iste nulla officia perferendis aliquam,
            ipsum maiores sequi nisi maxime ex aliquid eligendi doloribus iure, molestias fuga, error recusandae ullam?
"""
    }
]

def get_date(post):
    return post.get('date')
# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    indentified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": indentified_post
    })
