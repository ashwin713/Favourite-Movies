import media

shawshank_redemption = media.Movie("The Shawshank Redemption", "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.", "https://en.wikipedia.org/wiki/The_Shawshank_Redemption#/media/File:ShawshankRedemptionMoviePoster.jpg", "https://www.youtube.com/watch?v=6hB3S9bIaco")
the_dark_knight = media.Movie("The Dark Knight", "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.", "https://en.wikipedia.org/wiki/The_Dark_Knight_(film)#/media/File:Dark_Knight.jpg", "https://www.youtube.com/watch?v=EXeTwQWrcwY")
lord_of_the_rings = media.Movie("The Lord of the Rings: The Fellowship of the Ring", "A meek Hobbit and eight companions set out on a journey to destroy the One Ring and the Dark Lord Sauron.", "https://en.wikipedia.org/wiki/The_Lord_of_the_Rings:_The_Fellowship_of_the_Ring#/media/File:The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_(2001)_theatrical_poster.jpg", "https://www.youtube.com/watch?v=V75dMMIW2B4") 

print "Which Trailer do you want to watch ? \n(1) : The Shawshank Redemption \n(2) : The Dark Knight \n(3) : The Lord of the Rings \n"
choice = int(raw_input("Input your choice : "))
if choice == 1:
	shawshank_redemption.show_trailer()
elif choice == 2:	
	the_dark_knight.show_trailer()
elif choice == 3:
	lord_of_the_rings.show_trailer()
else:
	print "Wrong choice"