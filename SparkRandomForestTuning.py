import csv
import numpy as np
from pyspark import SparkContext, SparkConf
from pyspark.mllib.util import MLUtils
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.tree import DecisionTree, DecisionTreeModel
from pyspark.mllib.evaluation import RegressionMetrics

conf = SparkConf().setAppName('baseline roi')
sc = SparkContext(conf=conf)
sc.setLogLevel("OFF")

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
        i += 1

    avg_roi = total_roi / roi_count
    avg_duration = total_duration / duration_count
    avg_actor1 = total_actor1 / actor1_count
    avg_actor2 = total_actor2 / actor2_count
    avg_actor3 = total_actor3 / actor3_count

    labeled_points = []
    i = 0
    for movie in movies:
        if i > 0:
            roi = avg_roi if movie[0] == "?" else float(movie[0])
            duration = avg_duration if movie[6] == "?" else int(movie[6])
            actor1_followers = avg_actor1 if movie[9] == "?" else int(movie[9])
            actor2_followers = avg_actor2 if movie[11] == "?" else int(movie[11])
            actor3_followers = avg_actor3 if movie[13] == "?" else int(movie[13])
            labeled_points.append(LabeledPoint(roi, np.array([duration, actor1_followers, actor2_followers, actor3_followers])))
        i += 1
    return sc.parallelize(labeled_points)

def train_model():
    data = get_dataset()
    (trainingData, testData) = data.randomSplit([0.7, 0.3])
    metrics_combos = []

    bins = [x for x in range(50, 500, 10)]
    depths = [x for x in range(4, 12)]
    for numBin in bins:
        for depth in depths:
            model = DecisionTree.trainRegressor(trainingData, categoricalFeaturesInfo={},
                                    impurity='variance', maxDepth=depth, maxBins=numBin)

            predictions = model.predict(testData.map(lambda x: x.features))
            labelsAndPredictions = testData.map(lambda lp: lp.label).zip(predictions)
            metrics = RegressionMetrics(labelsAndPredictions)
            metrics_combos.append(((numBin, depth), metrics.meanSquaredError))

    print(sorted(metrics_combos, key=lambda s: s[1]))
    #testMSE = labelsAndPredictions.map(lambda (v, p): (v - p) * (v - p)).sum() /\
    #    float(testData.count())

if __name__ == "__main__":
    train_model()
