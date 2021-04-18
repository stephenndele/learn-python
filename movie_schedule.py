current_movies = {
    'The Grinch': '11:00am',
    'Rudolph':'1:00pm',
    'Frosty the Snowman':'3.00pm',
    'Christmas Vacation': '5:00pm',
}

print("we are showing the following movies:")

for key in current_movies:
    print(key)

movie = input("what movies would you like to watch?\n")

showtime = current_movies.get(movie)

if showtime == None:
    print ("The requested movies is not there")

else:
    print(movie, 'is playing at ', showtime)
