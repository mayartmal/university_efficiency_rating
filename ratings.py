import csv

def get_list_row(opened_data_file):
    row = opened_data_file.readline()
    row = row.rstrip()
    list_row = row.split('\t')
    return list_row

def get_rating(rating_data):
    rating_dict = {}
    for i in range(100):
        list_row = get_list_row(rating_data)
        rating = list_row[0]
        university = list_row[1]
        rating_dict[university] = int(rating)
    return rating_dict

quality_data = open('quality_data.txt')
demand_data = open('demand_data.txt')
quality_rating = get_rating(quality_data)
demand_rating = get_rating(demand_data)

rating_distances = {}
for key in demand_rating:
    rating_distances[key] = abs(quality_rating[key] - demand_rating[key])

for key in rating_distances:
    print(key, rating_distances[key])

with open('dict.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for key, value in rating_distances.items():
       writer.writerow([key, value])
