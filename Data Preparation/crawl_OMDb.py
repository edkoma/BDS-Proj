#dependency - use pip insatll unicodecsv
import unicodecsv as csv
import json
import urllib2
import re
import time

def crawl():
    with open('movie_metadata.csv', 'rb') as csvfile:
        movie_reader = csv.reader(csvfile, delimiter=',')
        i = 1
        for movie in movie_reader:
            imdb_id = re.search('tt[0-9]+', movie[17])
            if imdb_id:
                #Extract the IMDB id, get the response from OMDB, and parse the json response
                movie_id = imdb_id.group(0)
                movie_metadata = urllib2.urlopen("http://www.omdbapi.com/?i=" + movie_id, timeout=5).read()
                row_id = '%04d' % i 
                json_file = open("./movies/" + row_id + '-' +  movie_id + ".json", 'w')
                json.dump(movie_metadata, json_file, ensure_ascii=False)
                json_file.close()
                
                print("Progress: " + str(i) +  "/5043")
                i += 1
                #be nice and don't bombard the OMDB server with 5000 requests in a second
                time.sleep(5)

def main():
    crawl()

if __name__ == "__main__":
    main()
