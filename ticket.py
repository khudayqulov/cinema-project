from datetime import datetime


class Ticket:
    """Sotib olingan chipta (Transaction analogi)."""

    _counter = 1000

    def __init__(self, customer, movie_title, seat, price, session_time):
        Ticket._counter += 1
        self.ticket_id = Ticket._counter
        self.customer = customer
        self.movie_title = movie_title
        self.seat = seat
        self.price = price
        self.session_time = session_time
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.status = "Faol"

    def cancel(self):
        self.status = "Bekor qilingan"

    def is_active(self):
        return self.status == "Faol"

    def __str__(self):
        return (f"#{self.ticket_id} | {self.customer} | {self.movie_title} | "
                f"O'rin: {self.seat} | {self.session_time} | "
                f"{self.price:,} so'm | {self.status} | {self.created_at}")
