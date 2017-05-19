import csv
import numpy as np

def get_dataset():
    data = open("../merged_data_with_sentiment_score.csv", "rb")

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
            total_duration += int(movie[7]) if movie[7] != '?' else 0
            duration_count += 1 if movie[7] != '?' else 0
            total_actor1 += int(movie[10]) if movie[10] != '?' else 0
            actor1_count += 1 if movie[10] != '?' else 0
            total_actor2 += int(movie[12]) if movie[12] != '?' else 0
            actor2_count += 1 if movie[12] != '?' else 0
            total_actor3 += int(movie[14]) if movie[14] != '?' else 0
            actor3_count += 1 if movie[14] != '?' else 0
            total_budget += int(movie[18]) if movie[18] != '?' else 0
            budget_count += 1 if movie[18] != '?' else 0
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
            sentiment = movie[3]
            duration = avg_duration if movie[7] == "?" else int(movie[7])
            actor1_followers = avg_actor1 if movie[10] == "?" else int(movie[10])
            actor2_followers = avg_actor2 if movie[12] == "?" else int(movie[12])
            actor3_followers = avg_actor3 if movie[14] == "?" else int(movie[14])
            budget = avg_budget if movie[18] == '?' else int(movie[18])
            labeled_points.append(np.array([roi, sentiment, duration, actor1_followers, actor2_followers, actor3_followers, budget]))
        i += 1
    return labeled_points

def toCSVLine(data):
    return ','.join(str(d) for d in data)

if __name__ == "__main__":
    out = open("sentiment.csv", "w+")
    data = get_dataset()
    for datum in data:
        csvLine = toCSVLine(datum)
        out.write(csvLine)
        out.write('\n')
