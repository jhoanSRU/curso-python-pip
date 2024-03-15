import csv
def read_csv(path):
    with open(path, encoding = 'latin-1') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        #print(header)
        data = []
        for row in reader:
            iterable = zip(header, row)
            #spotify_dict = {key: value for key, value in iterable}
            spotify_dict = dict(iterable)
            data.append(spotify_dict)
       
            #print(data)
        return data
if __name__ == '__main__':
    data = read_csv('./popular_songs.csv')
    #read_csv('./popular_songs.csv')
    print(data)