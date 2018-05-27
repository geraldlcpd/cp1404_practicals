#
# File: test_song.py
# Description:
#       The File to test song.py
#
# Last Modified:
#       May 17, 2018
# Owner:
#       Felix Widyanto Oetomo
#
#

from song import Song

# test empty song (defaults)
song = Song()
print(song)
assert song.artist == ""
assert song.title == ""
assert song.year == 0
assert song.is_required
assert song.is_learned is False

# test initial-value song
song2 = Song("Amazing Grace", "John Newton", 1779, True)
print(song2)
# This is how to test the initial-value song above
assert song2.artist == "Amazing Grace"
assert song2.title == "John Newton"
assert song2.year == 1779
assert song2.is_required
assert song2.is_learned is False

# test mark_learned()
song2.mark_learned()
# This is how to test the song whether it is now learned or not
assert song2.is_learned is True

# test mark_unlearned()
song2.mark_unlearned()
# This is how to test the song whether it is now being reset to unlearned or not
assert song2.is_learned is False

# test __str__()
assert "Amazing Grace,John Newton,1779,n" == str(song2)
# test mark_learned()
song2.mark_learned()
assert "Amazing Grace,John Newton,1779,y" == str(song2)