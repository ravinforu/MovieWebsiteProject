import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toy comes to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

transformers = media.Movie("Transformers",
                           "The Autobots and Decepticons, two intergalactic races of robots, crash land on Earth in order to battle for the ultimate power source, AllSpark, which is held by Sam",
                           "https://upload.wikimedia.org/wikipedia/en/6/66/Transformers07.jpg",
                           "https://www.youtube.com/watch?v=XnwmUZuF5OY")

rocky = media.Movie("Rocky",
                    "Is a boxing saga of popular films",
                    "https://upload.wikimedia.org/wikipedia/en/8/84/Rocky_anthology_dvd_cover.jpg",
                    "https://www.youtube.com/watch?v=3VUblDwa648")
commando = media.Movie("Commando",
                       "An Ex-Army man fighting as one-man army against his ex-army colleague turned enemy to take back his kidnapped daughter",
                       "https://upload.wikimedia.org/wikipedia/en/d/d9/Commandoposter.jpg",
                       "https://www.youtube.com/watch?v=pPhISgw3I2w")
predator = media.Movie("Predator",
                       "The leader of an elite special forces team on a mission to rescue hostages fights against an extraterrestrial life which secretly hunts the rescue group",
                       "https://upload.wikimedia.org/wikipedia/en/9/95/Predator_Movie.jpg",
                       "https://www.youtube.com/watch?v=Y1txEAywdiw")

movies = [toy_story, avatar, transformers, rocky, commando, predator]
fresh_tomatoes.open_movies_page(movies)
