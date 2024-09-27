class Post:
    def __init__(self, posts) :
        self.posts = posts

    def get_title(self, id):
        self.id =id
        return self.posts[self.id-1]['title']
    
    def get_subtitle(self, id):
        self.id =id
        return self.posts[self.id-1]['subtitle']
    
    def get_body(self, id):
        self.id =id
        return self.posts[self.id-1]['body']

