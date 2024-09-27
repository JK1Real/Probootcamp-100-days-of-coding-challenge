class User():
    def __init__(self, name):
        self.name=name
        self.logged = False

def is_authenticatted(function):
    def wrapper(*args, **kargs):
        if args[0].logged ==True:
            function(args[0])
    return wrapper

@is_authenticatted
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post")

user = User("Jerom")
print(user.name)
print(user.logged)
create_blog_post(user)

user.logged=True
print(user.logged)
create_blog_post(user)
