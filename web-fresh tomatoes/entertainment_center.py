import media
import fresh_tomatoes

toys_story = media.Movie("Toys Story",
                        "A story of a boy and his toys that come to life.",
                        "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0%2C0%2C300%2C450",
                        "https://www.youtube.com/watch?v=Bj4gS1JQzjk")

avatar = media.Movie("Avatar",
                        "A marine in an alien planet.",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("School of Rock",
                        "A substitute teacher of a strict elementary private school, tries to turn it into a rock band.",
                        "http://www.gstatic.com/tv/thumb/movieposters/33094/p33094_p_v8_aa.jpg",
                        "https://www.youtube.com/watch?v=3PsUJFEBC74")

#print (toys_story.storyline)
#avatar.show_trailer()
#school_of_rock.show_poster()

movies = [toys_story, avatar, school_of_rock]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__) # reads the comment section of the Movie documentations
#print(media.Movie.__dict__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
