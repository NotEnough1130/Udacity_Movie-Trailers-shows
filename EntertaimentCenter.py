import media
import fresh_tomatoes

best_movie_1 = media.Movie("Three Billboards Outside Ebbing, Missouri,", 
                        "Mildred Hayes, a hard-nosed mother is seeking justice for her murdered daughter. With no arrests after seven months, Mildred puts up three roadside signs to goad Ebbing police chief into action. But the law - and especially Sam Rockwell's hot-headed deputy - don't take kindly to the provocation. And the townsfolk are on their side. But Mildred doesn't care about ruffling a few feathers. In fact, she's happy to pluck the whole bird.",
                        "https://plymouthartscentre.org/wp-content/uploads/2018/02/three-billboards-outside-ebbing-missouri-2696_8-1024x576.jpg",
                        "https://www.youtube.com/watch?v=Jit3YhGx5pU")

#print(best_movie_1.title)

best_movie_2 = media.Movie("The Big Sick", 
                        "Kumail is a Pakistani comic who meets an American graduate student named Emily at one of his stand-up shows. As their relationship blossoms, he soon becomes worried about what his traditional Muslim parents will think of her. When Emily suddenly comes down with an illness that leaves her in a coma, Kumail finds himself developing a bond with her deeply concerned mother and father.",
                        "https://upload.wikimedia.org/wikipedia/en/6/69/The_Big_Sick.jpg",
                        "https://www.youtube.com/watch?v=jcD0Daqc3Yw")

best_movie_3 = media.Movie("Lady Bird", 
                        "Marion McPherson, a nurse, works tirelessly to keep her family afloat after her husband loses his job. She also maintains a turbulent bond with a teenage daughter who is just like her: loving, strong-willed and deeply opinionated.",
                        "https://upload.wikimedia.org/wikipedia/en/6/61/Lady_Bird_poster.jpeg",
                        "https://www.youtube.com/watch?v=cNi_HC839Wo")

#best_movie_1.show_trailer()
movies = [best_movie_1, best_movie_2, best_movie_3]
fresh_tomatoes.open_movies_page(movies)
