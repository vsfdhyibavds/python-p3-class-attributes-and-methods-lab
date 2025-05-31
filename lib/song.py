class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Set current artist and genre for class methods to access
        self.__class__._current_artist = artist
        self.__class__._current_genre = genre

        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls):
        if cls.genres is None:
            cls.genres = []
        if cls._current_genre not in cls.genres:
            cls.genres.append(cls._current_genre)

    @classmethod
    def add_to_artists(cls):
        if cls.artists is None:
            cls.artists = []
        if cls._current_artist not in cls.artists:
            cls.artists.append(cls._current_artist)

    @classmethod
    def add_to_genre_count(cls):
        if cls._current_genre not in cls.genre_count:
            cls.genre_count[cls._current_genre] = 0
        cls.genre_count[cls._current_genre] += 1

    @classmethod
    def add_to_artist_count(cls):
        if cls._current_artist not in cls.artist_count:
            cls.artist_count[cls._current_artist] = 0
        cls.artist_count[cls._current_artist] += 1
