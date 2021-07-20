# 1
from newapp.models import *

user1 = User.objects.create_user(username="Aron")
user2 = User.objects.create_user(username="Tom")

# 2
Author.objects.create(user=user1)
Author.objects.create(user=user2)

# 3
Category.objects.create(name="IT")
Category.objects.create(name="Mathematics")
Category.objects.create(name="Python")
Category.objects.create(name="Java")

# 4
x1 = Author.objects.get(id=1)
x2 = Author.objects.get(id=2)
Post.objects.create(author=x1, type="AR", title="Python code", text="Text about Python.")
Post.objects.create(author=x2, type="AR", title="Java code", text="Text about Java.")
Post.objects.create(author=x2, type="NE", title="Mathematical research", text="Text about mathematical research")

# 5
Post.objects.get(id=1).categories.add(Category.objects.get(id=1))
Post.objects.get(id=1).categories.add(Category.objects.get(id=3))

Post.objects.get(id=2).categories.add(Category.objects.get(id=1))
Post.objects.get(id=2).categories.add(Category.objects.get(id=4))

Post.objects.get(id=3).categories.add(Category.objects.get(id=1))
Post.objects.get(id=3).categories.add(Category.objects.get(id=2))

# 6
Comment.objects.create(post=Post.objects.get(id=1), user=Author.objects.get(id=2).user, text="Comment for 'Python code' 1")
Comment.objects.create(post=Post.objects.get(id=2), user=Author.objects.get(id=1).user, text="Comment for 'Java code'")
Comment.objects.create(post=Post.objects.get(id=3), user=Author.objects.get(id=1).user, text="Comment for 'Mathematical research'")
Comment.objects.create(post=Post.objects.get(id=1), user=Author.objects.get(id=1).user, text="Comment for 'Python code' 2")

# 7
Post.objects.get(id=1).like()
Post.objects.get(id=1).like()
Post.objects.get(id=1).like()
Post.objects.get(id=2).like()
Post.objects.get(id=3).like()
Post.objects.get(id=3).like()
Post.objects.get(id=3).dislike()
Comment.objects.get(id=1).like()
Comment.objects.get(id=1).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).dislike()
Comment.objects.get(id=4).like()
Comment.objects.get(id=4).like()
Comment.objects.get(id=4).like()

# 8
x1.update_rating()
x2.update_rating()

# 9
bestUser = Author.objects.all().order_by("-rating")[:1]
for el in bestUser:
    print("Best user:")
    print(f"name: {el.user.username}")
    print(f"rating: {el.rating}")
    print("---------------")

# 10
bestArticle = Post.objects.all().order_by("-rating")[:1]
for el in bestArticle:
    print("Best post:")
    el.timeCreation.isoformat(sep="/")
    print(f"author: {el.author.user.username}")
    print(f"rating: {el.rating}")
    print(f"title: {el.title}")
    print(f"text preview: {el.preview()}")
    print("---------------")

# 11
comments_of_bestArticle = Comment.objects.filter(post=bestArticle)
for i, el in enumerate(comments_of_bestArticle):
    print(f"Comment №{i+1}")
    el.timeCreation.isoformat(sep="/")
    print(f"author: {el.user.username}")
    print(f"rating: {el.rating}")
    print(f"text: {el.text}")
    print("---------------")
