import numpy as np
from kmodes import kmodes
import csv



def main():
    movie_file = open("merged_data.csv", "r")
    movies = [row for row in csv.reader(movie_file.read().splitlines())]
    genre_map = {}
    i = 0
    for movie in movies:
        if i > 0:
            genres = movie[4].split()
            for genre in genres:
                if genre not in genre_map:
                    genre_map[genre] = 1
                else:
                    genre_map[genre] += 1
        i += 1

    genre_list = []
    for genre in genre_map.keys():
        if genre_map[genre] > 5:
            genre_list.append(genre)

    print(genre_list)
    mat = np.zeros((5043, len(genre_list)))

    i = 0
    for movie in movies:
        if i > 0:
            genres = movie[4].split()
            for genre in genres:
                if genre in genre_list:
                    mat[i - 1][genre_list.index(genre)] = 1

        i += 1

    km = kmodes.KModes(n_clusters=10, init='Huang', n_init=10, verbose=1)
    clusters = km.fit_predict(mat)

    cluster_labels = open("clusters.txt", "w")
    cluster_labels.write("\n")
    for label in km.labels_:
        cluster_labels.write(str(label))
        cluster_labels.write("\n")
    print(km.labels_)

if __name__ == "__main__":
    main()

    
