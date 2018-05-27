"""
(incomplete) Tests for SongList class
"""
from songlist import SongList
from song import Song

# test empty SongList
song_list = SongList()
print(song_list)
assert len(song_list.songs) == 0

# test loading songs
song_list.load_songs('songs.csv')
print(song_list)
original_length = len(song_list.songs)
assert original_length > 0  # assuming CSV file is not empty

# all tests below are to show the various required methods work as expected
# test sorting songs
song_list.sort_songs("artist")
print(song_list)
song_list.sort_songs("year")
print(song_list)
song_list.sort_songs("title")
print(song_list)
song_list.sort_songs("is_required")
print(song_list)
song_list.sort_songs("is_learned")
print(song_list)

# test adding a new Song

new_song = Song( "New Title", "New Artist",2018, True)
song_list.add_song(new_song)
new_song1 = Song("New Title1", "New Artist1", 2018, True)
song_list.add_song(new_song1)
new_song2 = Song("New Title2", "New Artist2", 2018, False)
song_list.add_song(new_song2)
# adding 3 new songs, so the length must be the original length (above) plus 3
assert (original_length + 3) == len(song_list.songs)

# test get_song()
# get the song with the title New Title1
found_songs = song_list.get_song_by_title("New Title1")
assert found_songs is not None
# trying to get a song that does NOT exist
found_songs = song_list.get_song_by_title("New Title111111")
assert found_songs is None


# test getting the number of required and learned songs (separately)

required_songs = song_list.get_required_songs()
assert required_songs == 8
learned_songs = song_list.get_learned_songs()
assert learned_songs == 4

# test saving songs (check CSV file new_songs.csv manually to see results)
song_list.save_songs("new_songs.csv")