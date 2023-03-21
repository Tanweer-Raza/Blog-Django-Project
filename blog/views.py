from django.shortcuts import render
from datetime import date

all_posts = [
        {
        "slug":"hike-in-the-mountains",
        "image": "mountains.jpg",
        "author":'T.Raza',
        "date" : date(2023, 3, 16),
        "title" : " 2.Mountain Hiking",
        "excerpt" : """
                    There's nothing like the views you get when hiking in the mountains! 
                    And I wasn't even prepared for what happened whilst I was enjoying the view!
                    """ ,
        "content" : """
                    INNER JOIN will fetch only those records which are present in both the joined tables.
                    The matching of the records is only based on the columns used for joining these two tables.
                    INNER JOIN can also be represented as JOIN in your SELECT query.

                    INNER JOIN will fetch only those records which are present in both the joined tables.
                    The matching of the records is only based on the columns used for joining these two tables.
                    INNER JOIN can also be represented as JOIN in your SELECT query.

                    INNER JOIN will fetch only those records which are present in both the joined tables.
                    The matching of the records is only based on the columns used for joining these two tables.
                    INNER JOIN can also be represented as JOIN in your SELECT query.

                    INNER JOIN will fetch only those records which are present in both the joined tables.
                    The matching of the records is only based on the columns used for joining these two tables.
                    INNER JOIN can also be represented as JOIN in your SELECT query.
                    """

        },

        {
        "slug":"hike-in-the-woods",
        "image": "woods.jpg",
        "author":'T.Raza',
        "date" : date(2023, 6, 18),
        "title" : "4.Mountain Hiking",
        "excerpt" : """
                    There's nothing like the views you get when hiking in the mountains! 
                    And I wasn't even prepared for what happened whilst I was enjoying the view!
                    """ ,
        "content" : """
                    INNER JOIN will fetch only those records which are present in both the joined tables.
                    The matching of the records is only based on the columns used for joining these two tables.
                    INNER JOIN can also be represented as JOIN in your SELECT query.

                    INNER JOIN will fetch only those records which are present in both the joined tables.
                    The matching of the records is only based on the columns used for joining these two tables.
                    INNER JOIN can also be represented as JOIN in your SELECT query.

                    INNER JOIN will fetch only those records which are present in both the joined tables.
                    The matching of the records is only based on the columns used for joining these two tables.
                    INNER JOIN can also be represented as JOIN in your SELECT query.

                    INNER JOIN will fetch only those records which are present in both the joined tables.
                    The matching of the records is only based on the columns used for joining these two tables.
                    INNER JOIN can also be represented as JOIN in your SELECT query.
                    """

         },
        {
        "slug":"hike-in-max-world",
        "image": "max.png",
        "author":'T.Raza',
        "date" : date(2023, 5, 26),
        "title" : "3.Mountain Hiking",
        "excerpt" : """
                    There's nothing like the views you get when hiking in the mountains! 
                    And I wasn't even prepared for what happened whilst I was enjoying the view!
                    """ ,
        "content" : """
                    INNER JOIN will fetch only those records which are present in both the joined tables.
                    The matching of the records is only based on the columns used for joining these two tables.
                    INNER JOIN can also be represented as JOIN in your SELECT query.

                    INNER JOIN will fetch only those records which are present in both the joined tables.
                    The matching of the records is only based on the columns used for joining these two tables.
                    INNER JOIN can also be represented as JOIN in your SELECT query.

                    INNER JOIN will fetch only those records which are present in both the joined tables.
                    The matching of the records is only based on the columns used for joining these two tables.
                    INNER JOIN can also be represented as JOIN in your SELECT query.

                    INNER JOIN will fetch only those records which are present in both the joined tables.
                    The matching of the records is only based on the columns used for joining these two tables.
                    INNER JOIN can also be represented as JOIN in your SELECT query.
                    """

         },
        {
        "slug":"hike-in-the-tan-world",
        "image": "tan.jpg",
        "author":'T.Raza',
        "date" : date(2023, 1, 23),
        "title" : "1.Mountain Hiking",
        "excerpt" : """
                    There's nothing like the views you get when hiking in the mountains! 
                    And I wasn't even prepared for what happened whilst I was enjoying the view!
                    """ ,
        "content" : """
                    INNER JOIN will fetch only those records which are present in both the joined tables.
                    The matching of the records is only based on the columns used for joining these two tables.
                    INNER JOIN can also be represented as JOIN in your SELECT query.

                    INNER JOIN will fetch only those records which are present in both the joined tables.
                    The matching of the records is only based on the columns used for joining these two tables.
                    INNER JOIN can also be represented as JOIN in your SELECT query.

                    INNER JOIN will fetch only those records which are present in both the joined tables.
                    The matching of the records is only based on the columns used for joining these two tables.
                    INNER JOIN can also be represented as JOIN in your SELECT query.

                    INNER JOIN will fetch only those records which are present in both the joined tables.
                    The matching of the records is only based on the columns used for joining these two tables.
                    INNER JOIN can also be represented as JOIN in your SELECT query.
                    """

        }
]


def get_date(post):
    return post['date']
# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date , reverse = True)
    latest_posts = sorted_posts[:3]
    return render(request, "blog/index.html" ,{
        "posts" : latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts" : all_posts
    })

def post_details(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html" ,{
        "post" : identified_post
    })
