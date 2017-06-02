import media
import fresh_tomatoes

# Add movie data
toy_story = media.Movie("Toy Story", """A story of a boy and his toys that come
                        to life""",
                        "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "http://www.impawards.com/2009/posters/avatar_xlg.jpg",
                     "https://www.youtube.com/watch?v=uZNHIU3uHT4")
crash = media.Movie("Crash", """The lives of several strangers become intertwi
                     ned over a single event""",
                    "http://i41.tinypic.com/3358pav.jpg",
                    "https://www.youtube.com/watch?v=durNwe9pL0E")
guardians = media.Movie("Guardians of the Galaxy", """An adventure through
                        space""",
                        "http://cdn.collider.com/wp-content/uploads/guardians-of-the-galaxy-poster-star-lord.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=B16Bo47KS2g")
interstellar = media.Movie("Interstellar", "A mindblowing scifi epic",
                           "http://halifaxbloggers.ca/flawintheiris/wp-content/uploads/sites/7/2014/11/Interstellar-Poster-HD-Wallpapers-Images-Pics-24.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=ePbKGoIGAXY")
district9 = media.Movie("District 9", """A realistic look of how humanity migh
                        t interect with aliens if they ever joined our
                        society""",
                        "http://img.moviepostershop.com/district-9-movie-poster-2009-1020502468.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=DyLUwOcR5pk")

# List movies to display
movies = [toy_story, avatar, crash, guardians, interstellar, district9]

# Launch website
fresh_tomatoes.open_movies_page(movies)
