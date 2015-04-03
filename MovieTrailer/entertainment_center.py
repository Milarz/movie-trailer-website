import media
import fresh_tomatoes

movies = []  #list of films to be displayed
#Instantiate each movie object and add it to the film list.
donnie_darko = media.Movie("Donnie Darko",
                     "A teenager is plagued by visions of a large bunny rabbit.",
                      "http://upload.wikimedia.org/wikipedia/en/d/db/Donnie_Darko_poster.jpg",
                      "https://www.youtube.com/watch?v=ZZyBaFYFySk")
movies.append(donnie_darko)
princess_bride = media.Movie("The Princess Bride",
                     "A grandfather reads a fairy tale to a sick boy.",
                      "http://upload.wikimedia.org/wikipedia/en/d/db/Princess_bride.jpg",
                      "https://www.youtube.com/watch?v=O3CIXEAjcc8")
movies.append(princess_bride)
blade_runner = media.Movie("Blade Runner",
                     "A police officer must retire four replicants.",
                      "http://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",
                      "https://www.youtube.com/watch?v=eogpIG53Cis")
movies.append(blade_runner)
patton = media.Movie("Patton",
                     "Follows General Patton's WW2 exploits.",
                      "http://upload.wikimedia.org/wikipedia/en/f/f2/70_patton.jpg",
                      "https://www.youtube.com/watch?v=g-0dTpzNzwo")
movies.append(patton)
brazil = media.Movie("Brazil",
                     "A bureaucrat becomes a state fugative.",
                     "http://upload.wikimedia.org/wikipedia/en/e/e9/Brazil_%281985_film%29_poster.jpg", 
                     "https://www.youtube.com/watch?v=4Wh2b1eZFUM")
movies.append(brazil)
tender_mercies = media.Movie("Tender Mercies",
                     "A drifter is redeemed by a kind woman.",
                      "http://upload.wikimedia.org/wikipedia/en/1/10/Tender_mercies.jpg",
                      "https://www.youtube.com/watch?v=m-ZawEDsop4")
movies.append(tender_mercies)

#Invoke canned functionality to display web page, provided in Fresh Tomatoes module 
fresh_tomatoes.open_movies_page(movies)

