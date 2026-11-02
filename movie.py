class Movie:
    """Film ma'lumotlari va zal o'rindiqlarini boshqaradi (Account analogi)."""

    ROWS = "ABCDE"
    COLS = 8

    def __init__(self, movie_id, title, genre, duration, price, session_time):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.duration = duration          # daqiqada
        self.price = price                # so'mda
        self.session_time = session_time
        # Encapsulation: o'rindiqlar faqat metodlar orqali o'zgaradi
        self.__seats = {
            f"{r}{c}": False
            for r in self.ROWS
            for c in range(1, self.COLS + 1)
        }

    def is_available(self, seat):
        return seat in self.__seats and not self.__seats[seat]

    def book_seat(self, seat):
        if not self.is_available(seat):
            return False
        self.__seats[seat] = True
        return True

    def cancel_seat(self, seat):
        if seat in self.__seats and self.__seats[seat]:
            self.__seats[seat] = False
            return True
        return False

    def free_count(self):
        return sum(1 for taken in self.__seats.values() if not taken)

    def show_info(self):
        print(f"[{self.movie_id}] {self.title} | {self.genre} | "
              f"{self.duration} daq | {self.session_time} | "
              f"{self.price:,} so'm | Bo'sh joy: {self.free_count()}")

    def show_seats(self):
        print(f"\n🎬 {self.title} — zal sxemasi (X = band)")
        print("        EKRAN")
        print("    " + "  ".join(f"{c:>2}" for c in range(1, self.COLS + 1)))
        for r in self.ROWS:
            row = []
            for c in range(1, self.COLS + 1):
                row.append(" X" if self.__seats[f"{r}{c}"] else " .")
            print(f" {r}  " + "  ".join(row))
        print()
