# import necessary libraries
from bs4 import BeautifulSoup
import requests
from csv import writer

try:
    # send a GET request to the IMDB Top 250 movies page
    url = requests.get("https://www.imdb.com/chart/top/")
    url.raise_for_status()   # check if the response status code is 200, raise an error if not

    # create a BeautifulSoup object with the HTML content of the page
    soup = BeautifulSoup(url.text, "html.parser")

    # find the tbody element with class "lister-list" that contains the movie list
    movies = soup.find("tbody", class_="lister-list")
    movies = movies.find_all("tr")  # find all the tr elements within the tbody element

    # create a new CSV file and write the header row
    with open("IMDB_Top_Rating.csv", "w", encoding="utf-8") as f:
        thewriter = writer(f)
        header = ["name", "rank", "year", "rating"]
        thewriter.writerow(header)

        # loop through each movie and extract its name, rank, year, and rating
        for movie in movies:
            name = movie.find("td", class_="titleColumn").a.text
            rank = movie.find("td", class_="titleColumn").get_text(strip=True).split(".")[0]
            year = movie.find("span", class_="secondaryInfo").text.strip("()")
            rating = movie.find("td", class_="ratingColumn imdbRating").strong.text

            # create a list of the extracted information and write it to the CSV file
            info = [name, rank, year, rating]
            thewriter.writerow(info)

except Exception as e:
    # handle any errors that occur during the execution of the program
    print(e)
