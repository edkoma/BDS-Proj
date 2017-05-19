import csv
import numpy as np

def get_dataset():
    data = open("../merged_data.csv", "rb")

    movies = [row for row in csv.reader(data.read().splitlines())]

    total_roi = 0
    roi_count = 0
    total_duration = 0
    duration_count = 0
    total_actor1 = 0
    actor1_count = 0
    total_actor2 = 0
    actor2_count = 0
    total_actor3 = 0
    actor3_count = 0
    total_budget = 0
    budget_count = 0

    i = 0
    for movie in movies:
        if i > 0:
            total_roi += float(movie[0]) if movie[0] != '?' else 0
            roi_count += 1 if movie[0] != '?' else 0
            total_duration += int(movie[6]) if movie[6] != '?' else 0
            duration_count += 1 if movie[6] != '?' else 0
            total_actor1 += int(movie[9]) if movie[9] != '?' else 0
            actor1_count += 1 if movie[9] != '?' else 0
            total_actor2 += int(movie[11]) if movie[11] != '?' else 0
            actor2_count += 1 if movie[11] != '?' else 0
            total_actor3 += int(movie[13]) if movie[13] != '?' else 0
            actor3_count += 1 if movie[13] != '?' else 0
            total_budget += int(movie[17]) if movie[17] != '?' else 0
            budget_count += 1 if movie[17] != '?' else 0

        i += 1

    avg_roi = total_roi / roi_count
    avg_duration = total_duration / duration_count
    avg_actor1 = total_actor1 / actor1_count
    avg_actor2 = total_actor2 / actor2_count
    avg_actor3 = total_actor3 / actor3_count
    avg_budget = total_budget / budget_count


    labeled_points = []
    i = 0
    for movie in movies:
        if i > 0:
            roi = avg_roi if movie[0] == "?" else float(movie[0])
            duration = avg_duration if movie[6] == "?" else int(movie[6])
            actor1_followers = avg_actor1 if movie[9] == "?" else int(movie[9])
            actor2_followers = avg_actor2 if movie[11] == "?" else int(movie[11])
            actor3_followers = avg_actor3 if movie[13] == "?" else int(movie[13])
            budget = avg_budget if movie[17] == '?' else int(movie[17])
            genres = movie[4]
            scifi = 1 if "Sci-Fi" in genres else 0
            crime = 1 if "Crime" in genres else 0
            romance = 1 if "Romance" in genres else 0
            animation = 1 if "Animation" in genres else 0
            music = 1 if "Music" in genres else 0
            comedy = 1 if "Comedy" in genres else 0
            war = 1 if "War" in genres else 0
            horror = 1 if "Horror" in genres else 0
            adventure = 1 if "Adventur" in genres else 0
            thriller = 1 if "Thriller" in genres else 0
            western = 1 if "Western" in genres else 0
            mystery = 1 if "Mystery" in genres else 0
            short = 1 if "Short" in genres else 0
            drama = 1 if "Drama" in genres else 0
            action = 1 if "Action" in genres else 0
            documentary = 1 if "Documentary" in genres else 0
            musical = 1 if "Musical" in genres else 0
            history = 1 if "History" in genres else 0
            family = 1 if "Family" in genres else 0
            fantasy = 1 if "Fantasy" in genres else 0
            sport = 1 if "Sport" in genres else 0
            biography = 1 if "Biography" in genres else 0
            labeled_points.append(np.array([roi, duration, actor1_followers, actor2_followers, actor3_followers, budget, scifi,
                                            crime, romance, animation, music, comedy, war, horror, adventure, thriller,
                                            western, mystery, short, drama, action, documentary, musical, history, family,
                                            fantasy, sport, biography]))
        i += 1
    return labeled_points

def toCSVLine(data):
    return ','.join(str(d) for d in data)

if __name__ == "__main__":
    out = open("genre.csv", "w+")
    data = get_dataset()
    for datum in data:
        csvLine = toCSVLine(datum)
        out.write(csvLine)
        out.write('\n')
