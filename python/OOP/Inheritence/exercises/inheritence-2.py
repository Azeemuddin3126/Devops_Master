# Parent class: Book
class Book:
    def __init__(self, title, author, word_count, genre):
        self.title = title
        self.author = author
        self.word_count = word_count
        self.genre = genre

# Child class: BlogPost
class BlogPost(Book):
    def __init__(self, website, title, author, word_count, genre, page_views):
        super().__init__(title, author, word_count, genre)  # Calling Book's __init__
        self.website = website
        self.word_count = word_count
        self.page_views = page_views

# Object Instantiation
my_post = BlogPost("Vogue", "Hot Summer Trends", "Amy Gutierrez", 2319, "fashion", 2748)

# Print attributes of the BlogPost
print(my_post.website)      # Output: Vogue
print(my_post.title)        # Output: Hot Summer Trends
print(my_post.author)       # Output: Amy Gutierrez
print(my_post.word_count)   # Output: 2319
print(my_post.genre)        # Output: fashion
print(my_post.page_views)   # Output: 2748
