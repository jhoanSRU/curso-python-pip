
import reader_csv
import charts

def run():
    data = reader_csv.read_csv('popular_songs.csv')
    artist = input("type Artist's name:") 
    print(artist)
    data = list(filter(lambda art : art['artist(s)_name']==artist,data))
    
    songs = list(map(lambda so: so['track_name'],data))
    streams = list(map(lambda st: st['streams'], data))
    charts.bar_chart(artist, songs, streams)

if __name__ == '__main__':
     run()