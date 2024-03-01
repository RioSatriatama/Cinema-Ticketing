class Movie:
    """A class to represent a movie playing at the cinema."""

    def __init__(self, title, price):
        """Initialize the movie with a title and price."""
        self.title = title
        self.price = price

class Cinema:
    """A class to represent a cinema with a list of movies."""

    def __init__(self, name):
        """Initialize the cinema with a name and an empty list of movies."""
        self.name = name
        self.movies = []

    def add_movie(self, movie):
        """Add a movie to the cinema's list of movies."""
        self.movies.append(movie)

class TicketOrder:
    """A class to represent a ticket order for a movie at a cinema."""

    def __init__(self, cinema, movie, num_tickets):
        """Initialize the ticket order with a cinema, movie, and number of tickets."""
        self.cinema = cinema
        self.movie = movie
        self.num_tickets = num_tickets

    def calculate_cost(self):
        """Calculate the cost of the ticket order."""
        return self.movie.price * self.num_tickets

    def print_order(self):
        """Print the details of the ticket order."""
        print(f"Cinema: {self.cinema.name}")
        print(f"Movie: {self.movie.title}")
        print(f"Number of tickets: {self.num_tickets}")
        print(f"Cost: {self.calculate_cost()}")

# Example usage:

cinema = Cinema("Cineplex")
movie1 = Movie("The Avengers", 15)
movie2 = Movie("The Matrix", 12)

cinema.add_movie(movie1)
cinema.add_movie(movie2)

order = TicketOrder(cinema, movie1, 2)
order.print_order()