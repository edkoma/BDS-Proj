import unicodecsv as ucsv
import csv
import json
import glob
import codecs
#from io import open

def write_file():
	header = ['ROI', 'movie_title', 'plot', 'plot_keywords', 'genre', 'release_date', 'duration', 'director_name', \
	'actor_1', 'actor_1_followers', 'actor_2', 'actor_2_followers', 'actor_3', 'actor_3_followers', \
	'IMDB_Score', 'num_IMDB_reviews', 'metacritic_score', 'budget', 'gross', 'language', 'country', 'rating', \
	'aspect_ratio']

	print(header)
	merged_file = open('./merged_data.csv', 'w+b')
	merged_writer = ucsv.writer(merged_file, encoding='utf-8')
	merged_writer.writerow(header)
	#merged_writer.writerow([s.decode('utf-8')for s in header])
	#merged_writer.writerow([unicode(s) for s in header])

	kaggle_file = open('./movie_metadata.csv', 'rb')
	kaggle_csv = ucsv.reader(kaggle_file, delimiter=',', encoding='utf-8')
	twitter_file = open('twitter_data.csv', 'rb')
	twitter_data = [row for row in csv.reader(twitter_file.read().splitlines())]
	twitter_iter = iter(twitter_data)
	#twitter_csv = csv.reader(twitter_file, delimiter=',', encoding='utf-8')
	i = 0
	for movie in kaggle_csv:
		#skip the first line
		if i > 0:
			row = [None] * 23
			twitter_row = next(twitter_iter)
			#From the scheme I used to save the movie json files, search for the id at the
			#beginning of the file name to find the right file. glob will let you use re to
			#find the file
			file_id = '%04d' % i
			json_file = glob.glob('./movies/' + file_id + '*.json')[0]
			json_file = open(json_file, 'rb')
			json_data = json.load(json_file)
			json_dict = json.loads(json_data)

			row[1] = json_dict['Title']
			row[2] = json_dict['Plot']
			#plot keywords
			row[3] = movie[16]
			row[4] = json_dict['Genre']
			row[5] = json_dict['Released']
			row[6] = json_dict['Runtime']
			#director name
			row[7] = movie[1]
			#actor 1 name
			row[8] = movie[10]
			#actor 1 followers
			row[9] = twitter_row[3]
			#actor 2
			row[10] = movie[6]
			#actor 2 followers
			row[11] = twitter_row[1]
			#actor 3
			row[12] = movie[14]
			#actor 3 followers
			row[13] = twitter_row[5]
			row[14] = json_dict['imdbRating']
			row[15] = json_dict['imdbVotes']
			row[16] = json_dict['Metascore']
			#row[17] = json_dict['Writer']
			#budget
			if movie[22]:
				budget = int(movie[22])
				row[17] = movie[22]
			else:
				row[17] = '?'
			#gross
			if movie[8]:
				gross = int(movie[8])
				row[18] = movie[22]
			else:
				row[18] = '?'
			# roi = gross - budget / budget
			if movie[22] and movie[8]:
				roi = 1.0 * (gross - budget) / budget
				row[0] = "%.2f" % round(roi, 2)
			else:
				row[0] = '?'
			#language
			row[19] = movie[19]
			#country
			row[20] = movie[20]
			row[21] = json_dict["Rated"]
			row[22] = movie[26]

			#unicode_row = [unicode(s, errors='replace').encode('utf-8').strip() for s in row]
			merged_writer.writerow(row)
			json_file.close()

		i += 1
		print("Progress: " + str(i) +  "/5043")

	kaggle_file.close()
	twitter_file.close()
	merged_file.close()

if __name__ == "__main__":
	write_file()
