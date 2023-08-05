#Talking Data Starter Code

#Part 2 Setting up the program
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "The Hunger Games"

print("My favorite movie is " + favMovie + ".")


#Part 3 Investigate the data
#print(movieData.head())
#print(movieData["movie_title"])

#Part 4 Filter data
print("\nThe data for my favorite movie is:\n")
#Create a new variable to store your favorite movie information
favMovieBooleanList = movieData["movie_title"] == favMovie
#print(favMovieBooleanList)
favMovieData = movieData.loc[favMovieBooleanList]
print(favMovieData)

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

#Create a new variable to store a new data set with a certain genre
scifiMovieBooleanList = movieData["genres"].str.contains("Science Fiction & Fantasy")

scifiMovieData = movieData.loc[scifiMovieBooleanList]

numOfMovies = scifiMovieData.shape[0]

print("We will be comparing " + favMovie +
      " to other movies under the genre Science Fiction & Fantasy in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Science Fiction & Fantasy.")

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in this genre.\n")

#Part 5 Describe data
#min
min = scifiMovieData["audience_rating"].min()
print("The min audience rating of the data set is: " + str(min))
print(favMovie + " is rated 73 points higher than the lowest rated movie.")
print()

#find max
max = scifiMovieData["audience_rating"].max()
print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated 19 points lower than the highest rated movie.")
print()

#find mean
mean = scifiMovieData["audience_rating"].mean()
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " is higher than the mean movie rating.")
print()

#find median
median = scifiMovieData["audience_rating"].median()
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " is higher than the median movie rating.")

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Part 6 Create graphs
#Create histogram
plt.hist(scifiMovieData["audience_rating"], range = (0,100), bins = 20)

#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Science Fiction & Fantasy Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Science Fiction & Fantasy Movies")

#Prints interpretation of histogram
print(
  "According to the histogram, most science fiction and fantasy movies had an audience rating between 55 and 60."
)
print("\nClose the graph by pressing the 'X' in the top right corner.")

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

#Show histogram
plt.show()

#Create scatterplot
plt.scatter(data = scifiMovieData, label = "Animation Movies", x = "audience_rating", y = "critic_rating")

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Rating vs Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

plt.scatter(data = favMovieData, label = favMovie, x = "audience_rating", y = "critic_rating")
plt.legend()

#Prints interpretation of scatterplot
print(
  "According to the scatter plot, there is a positive correlation between the audience rating and the critic rating."
)

print(
  "\nThe Hunger Games follows the scatter plot's overall pattern."
)

print("Close the graph by pressing the 'X' in the top right corner.")

#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")
