import csv, operator

movie_csv = "student_folder/.labs/movie_data.csv"

def fetch_movie_data(movie_csv):
    """Return movie data from a CSV file"""
    with open(movie_csv, "r") as movie_file:
        reader = csv.reader(movie_file)
        movie_info = []
        for row in reader:
          movie_info.append(row)
        return movie_info

def get_money(gross):
    return float(gross[3])

def print_movie_data(data):
    """Print the movie data in easy to read columns"""
    for title, genre, rotten, gross, year in data:
        print("{:36} {:10} {:18} ${:16} {}".format(title, genre, rotten, gross, year))
    
def sort_movie_data(data, index, descending):
    """Sort movie data based on the column data"""
    header = data[0]
    sorted_movies = data[1:]
    if index == 3:
        sorted_movies.sort(key=get_money)
    else:
        sorted_movies.sort(key=operator.itemgetter(index))
    if descending:
        sorted_movies.reverse()
    sorted_movies.insert(0, header)
    return sorted_movies

def ask_column():
    """Ask the user by which criteria they want to sort the data"""
    column = input("""How do you want to sort the movie data? Enter '6' to exit the program.
        1) By Film Title
        2) By Genre
        3) By Rotten Tomatoes Score
        4) By Worldwide Gross
        5) By Year
        6) Quit\n""")
    return column

def sanitize_column(column):
    """Return True if the user entered a valid number, else return False"""
    try:
        int(column)
        return int(column) >= 1 and int(column) <= 5
    except ValueError:
        return False

def ask_order():
    """Ask the user how they want the data sorted: ascending or descending"""
    order = input("""How do you want the movie data ordered?
          1) Ascending Order
          2) Descending Order\n""")
    return order

def sanitize_order(order):
    """Return True if the user entered a valid number, else return False"""
    try:
        int(order)
        return int(order) >= 1 and int(order) <= 2
    except ValueError:
        return False

def user_interface():
    """Ask user how they want to sort the movie data"""
    while True:
        column = ask_column()
        if column == "6":
            break
        if sanitize_column(column):
            order = ask_order()
            if sanitize_order(order):
                movie_data = fetch_movie_data(movie_csv) 
                print_movie_data(sort_movie_data(movie_data, int(column) - 1, int(order) == 2))
            else:
                print("Enter a number 1 or 2.\n")
        else:
            print("Enter a number 1 to 6.\n")

user_interface()

#-------------------------------------------------------

import csv, operator

def fetch_movie_data(file):
    with open(file, "r") as f:
        return list(csv.reader(f))

def print_movie_data(data):
    for title, genre, rotten, gross, year in data:
        print(f"{title:36} {genre:10} {rotten:18} ${gross:16} {year}")

def sort_movie_data(data, idx, desc):
    header, movies = data[0], data[1:]
    movies.sort(key=(lambda x: float(x[3]) if idx == 3 else operator.itemgetter(idx)), reverse=desc)
    return [header] + movies

def get_input(prompt, valid_func):
    while True:
        inp = input(prompt)
        if valid_func(inp): return inp

def user_interface(file):
    while True:
        col = get_input(
            "Sort by:\n1) Film Title 2) Genre 3) Rotten Score 4) Worldwide Gross 5) Year 6) Quit\n",
            lambda x: x.isdigit() and 1 <= int(x) <= 6
        )
        if col == "6": break
        order = get_input("Order:\n1) Ascending 2) Descending\n", lambda x: x in ("1", "2"))
        data = fetch_movie_data(file)
        print_movie_data(sort_movie_data(data, int(col) - 1, int(order) == 2))

user_interface("student_folder/.labs/movie_data.csv")
