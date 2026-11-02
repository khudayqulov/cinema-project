from movie import Movie
from ticket import Ticket


class Cinema:
    """Kinoteatrning asosiy boshqaruvi (ATM analogi)."""

    def __init__(self, name):
        self.name = name
        self.__movies = []
        self.__tickets = []
        self.__customer = None
        self.__load_movies()

    def __load_movies(self):
        self.__movies = [
            Movie(1, "Interstellar", "Fantastika", 169, 45000, "18:00"),
            Movie(2, "Avatar", "Sarguzasht", 162, 40000, "20:30"),
            Movie(3, "Titanic", "Drama", 195, 35000, "15:00"),
            Movie(4, "Joker", "Triller", 122, 38000, "22:00"),
        ]

    # ---------- Yordamchi metodlar ----------
    def __find_movie(self, movie_id):
        for m in self.__movies:
            if m.movie_id == movie_id:
                return m
        return None

    def __choose_movie(self):
        self.show_movies()
        try:
            movie = self.__find_movie(int(input("Film raqamini kiriting: ")))
        except ValueError:
            movie = None
        if movie is None:
            print("❌ Bunday film topilmadi!")
        return movie

    # ---------- Kirish ----------
    def login(self):
        print(f"\n🎥 {self.name} kinoteatriga xush kelibsiz!")
        name = ""
        while not name:
            name = input("Ismingizni kiriting: ").strip()
        self.__customer = name
        print(f"✅ Salom, {name}!")

    # ---------- Amallar ----------
    def show_movies(self):
        print("\n📽️  Bugungi afisha:")
        for m in self.__movies:
            m.show_info()

    def show_seats(self):
        movie = self.__choose_movie()
        if movie:
            movie.show_seats()

    def buy_ticket(self):
        movie = self.__choose_movie()
        if not movie:
            return
        movie.show_seats()
        seat = input("O'rindiqni tanlang (masalan, B4): ").strip().upper()
        if not movie.book_seat(seat):
            print("❌ Bu o'rindiq band yoki mavjud emas!")
            return
        ticket = Ticket(self.__customer, movie.title, seat,
                        movie.price, movie.session_time)
        self.__tickets.append(ticket)
        print("✅ Chipta muvaffaqiyatli sotib olindi!")
        print(ticket)

    def cancel_ticket(self):
        active = [t for t in self.__tickets if t.is_active()]
        if not active:
            print("ℹ️  Bekor qilish uchun faol chipta yo'q.")
            return
        for t in active:
            print(t)
        try:
            tid = int(input("Bekor qilinadigan chipta ID: "))
        except ValueError:
            print("❌ Noto'g'ri ID!")
            return
        for t in active:
            if t.ticket_id == tid:
                movie = next(m for m in self.__movies if m.title == t.movie_title)
                movie.cancel_seat(t.seat)
                t.cancel()
                print(f"✅ Chipta #{tid} bekor qilindi. "
                      f"{t.price:,} so'm qaytariladi.")
                return
        print("❌ Bunday faol chipta topilmadi!")

    def show_history(self):
        print("\n🧾 Chiptalar tarixi:")
        if not self.__tickets:
            print("Hozircha chipta yo'q.")
            return
        for t in self.__tickets:
            print(t)
        total = sum(t.price for t in self.__tickets if t.is_active())
        print(f"💰 Jami (faol chiptalar): {total:,} so'm")

    # ---------- Menyu ----------
    def menu(self):
        print("""
========== MENYU ==========
1. Afishani ko'rish
2. Zal sxemasini ko'rish
3. Chipta sotib olish
4. Chiptani bekor qilish
5. Chiptalar tarixi
0. Chiqish
===========================""")

    def run(self):
        self.login()
        actions = {
            "1": self.show_movies,
            "2": self.show_seats,
            "3": self.buy_ticket,
            "4": self.cancel_ticket,
            "5": self.show_history,
        }
        while True:
            self.menu()
            choice = input("Tanlovingiz: ").strip()
            if choice == "0":
                print(f"👋 Xayr, {self.__customer}! Yaxshi dam oling!")
                break
            action = actions.get(choice)
            if action:
                action()
            else:
                print("❌ Noto'g'ri tanlov, qaytadan urinib ko'ring.")
