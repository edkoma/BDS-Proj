import csv
import numpy as np

cluster_map = {}
cluster_map[0] = []
cluster_map[1] = []
cluster_map[2] = []
cluster_map[3] = []
cluster_map[4] = []
cluster_map[5] = []
cluster_map[6] = []
cluster_map[7] = []
cluster_map[8] = []
cluster_map[9] = []

def get_dataset():
    data = open("../merged_data.csv", "rb")
    clusters = open("../clusters.txt", "rb")

    movies = [row for row in csv.reader(data.read().splitlines())]
    clusters = [int(row) for row in clusters]

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
            cluster_map[clusters[i]].append(movie[1])
            roi = avg_roi if movie[0] == "?" else float(movie[0])
            duration = avg_duration if movie[6] == "?" else int(movie[6])
            actor1_followers = avg_actor1 if movie[9] == "?" else int(movie[9])
            actor2_followers = avg_actor2 if movie[11] == "?" else int(movie[11])
            actor3_followers = avg_actor3 if movie[13] == "?" else int(movie[13])
            budget = avg_budget if movie[17] == '?' else int(movie[17])
            c0 = 1 if clusters[i] == 0 else 0
            c1 = 1 if clusters[i] == 1 else 0
            c2 = 1 if clusters[i] == 2 else 0
            c3 = 1 if clusters[i] == 3 else 0
            c4 = 1 if clusters[i] == 4 else 0
            c5 = 1 if clusters[i] == 5 else 0
            c6 = 1 if clusters[i] == 6 else 0
            c7 = 1 if clusters[i] == 7 else 0
            c8 = 1 if clusters[i] == 8 else 0
            c9 = 1 if clusters[i] == 9 else 0
            labeled_points.append(np.array([roi, duration, actor1_followers, actor2_followers, actor3_followers, budget,
                                            c0, c1, c2, c3, c4, c5, c6, c7, c8, c9]))
        i += 1
    return cluster_map

def toCSVLine(data):
    return ','.join(str(d) for d in data)

