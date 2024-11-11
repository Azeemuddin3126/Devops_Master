import tkinter # Do not erase this line of code

class Post:
  """Create a post object for the fictitious social network Photogram"""
  def __init__(self, username, user_id, media, avatar, comment_button, caption, likes, comments, like_button):
    self.username = username
    self.user_id = user_id
    self.media = media
    self.avatar = avatar
    self.comment_button = comment_button
    self.caption = caption
    self.likes = likes
    self.comments = comments
    self.like_button = like_button

username = "Sally_17"
user_id = 112010
media = "student_folder/img/photogram/waterfall.png"
avatar = "student_folder/img/photogram/avatar_icon.png"
comment_button = "student_folder/img/photogram/add_comment.png"
caption = "First time at Yosemite. It has surpassed all of my expectations."
likes = 23
comments = ["Beautiful!", "I wish I was there too.", "Is that Nevada Falls?", "Love it!", 
            "Can't wait for the Halfdome pictures", "More pics please"]
like_button = "student_folder/img/photogram/likes_icon.png"

post1 = Post(username, user_id, media, avatar, comment_button, caption, likes, comments, like_button)

window = tkinter.Tk()
window.title("Photogram")
window.geometry("800x500")
window.configure(background="white")

window.grid_columnconfigure(1, weight=0)
window.grid_columnconfigure(2, weight=1)

photo = tkinter.PhotoImage(file=post1.media)
comment_button = tkinter.PhotoImage(file=post1.comment_button)
avatar = tkinter.PhotoImage(file=post1.avatar)
like_button = tkinter.PhotoImage(file=post1.like_button)

# Big photo on the left
image = tkinter.Label(
  window,
  image=photo,
  bg="white")

image.grid(
  row=0,
  column=0,
  rowspan=10,
  stick="W")

# Gray user avatar
user_avatar = tkinter.Label(
  window,
  image=avatar,
  width=30,
  bg="white")

user_avatar.grid(
  row=0,
  column=1,
  sticky="W")

# Username to the right of the avatar
user_name = tkinter.Label(
  window,
  text=post1.username,
  font="DejaVuSans 14 bold",
  justify="left",
  bg="white")

user_name.grid(
  row=0,
  column=2,
  sticky="W")

# User caption for the photo
caption = tkinter.Label(
  window,
  text=post1.caption,
  font="DejaVuSans 14",
  wraplength=300,
  justify="left",
  bg="white")

caption.grid(
  row=1,
  column=1,
  columnspan=2,
  sticky="NW")

# Add comment icon
comment_icon = tkinter.Label(
  window,
  image=comment_button,
  bg="white",
  justify="center")

comment_icon.grid(
  row=2,
  column=1,
  columnspan=2)

# Loop to add all of the comments
for comment in post1.comments:
  tkinter.Label(
  window,
  text=comment,
  font="DejaVuSans 14",
  wraplength=300,
  justify="left",
  bg="white").grid(
  row=post1.comments.index(comment) + 3,
  column=1,
  columnspan=5,
  sticky="NW")

# Add likes icon
likes = tkinter.Label(
  window,
  image=like_button,
  bg="white",
  justify="center")

likes.grid(
  row=9,
  column=1)

# Add likes count
likes_count = tkinter.Label(
  window,
  font="DejaVuSans 14",
  text=post1.likes,
  bg="white",
  justify="left")

likes_count.grid(
  row=9,
  column=2,
  sticky="W",
  columnspan=2)

window.mainloop() # This should be the last line of code in your program