# parent class
class Book:
  def __init__(self, title, author, pages, genre):
    self.title = title
    self.author = author
    self.pages = pages  # 'pages' is required by the parent constructor
    self.genre = genre

# child class
class BlogPost(Book):
  def __init__(self, website, title, author, word_count, genre, page_views):
    # We still call super() with title, author, and genre
    super().__init__(title, author, 0, genre)  # Pass '0' for pages since it's not required in BlogPost
    self.website = website
    self.word_count = word_count
    self.page_views = page_views

my_post = BlogPost("Vogue", "Hot Summer Trends", "Amy Gutierrez", 2319, "fashion", 2748)

print(my_post.website)
print(my_post.title)		
print(my_post.author)	
print(my_post.word_count)	
print(my_post.genre)	
print(my_post.page_views)
