#
# File: songlist.py
# Description:
#       The Class represents a list of songs
#
# Last Modified:
#       May 17, 2018
# Owner:
#       Felix Widyanto Oetomo
#
#

from a2_sample.song import Song

class SongList:
    """

    The Class SongList stores a list of songs

    """
    def __init__(self):
        """

        The constructor of the SongList.
        Initialize the list to store the song objects belonging to this list

        """
        self.songs = []

    def add_song(self, song):
        """

        The method will add a song to the list of the songs by reading

        :param song: the song object which is to be added

        """
        if song is not None:
            self.songs.append(song)

    def load_songs(self, csv_input_file):
        """

        The method will populate the list of the songs by reading
        a csv formatted file. The format of the csv file is:
        TITLE_OF_THE_SONG,ARTIST,YEAR,REQUIRED_OR_NOT

        :param csv_input_file: the cvs file from which the data of the song
                                is read

        """
        with open(csv_input_file, "r") as in_csv_f:
            for line in in_csv_f:
                words = line.split(",")
                artist = words[0]
                title = words[1]
                year = int(words[2])
                is_learned = (words[3].strip() == 'y')
                new_song = Song(title, artist, year, True)
                if is_learned is True:
                    new_song.mark_learned()
                self.songs.append(new_song)
        in_csv_f.close()

    def save_songs(self, csv_output_file):
        """

        The method will store the list of the songs by writing (to the file system)
        a csv formatted file. The format of the csv file is:
        TITLE_OF_THE_SONG,ARTIST,YEAR,REQUIRED_OR_NOT

        :param csv_output_file: the path of the cvs file to which the data of the list of the song is
                                written

        """
        # open the output file, wipe out the content if the file already exists
        with open(csv_output_file, "w") as out_csv_f:
            for song in self.songs:
                out_csv_f.write(str(song)+'\n')
        out_csv_f.close()


    def get_song_by_title(self, title):
        """

        The method retrieves the song based on the title

        :param title: the title of the song to be found
        :return: the song with the title if found, otherwise it will return None

        """
        for song in self.songs:
            if song.title == title:
                return song
        return None


    def get_required_songs(self):
        """

        The method returns the required number of the songs
        in the list

        :return: the number of the required songs

        """
        required_songs = 0
        for song in self.songs:
            if song.is_required is True:
                required_songs += 1
        return required_songs

    def get_learned_songs(self):
        """

        The method returns the learned number of the songs
        in the list

        :return: the number of the learned songs

        """
        learned_songs = 0
        for song in self.songs:
            if song.is_learned is True:
                learned_songs += 1
        return learned_songs

    def sort_songs(self, key):
        """

        The method will sort the list of the songs according to the given key
        and then by the title

        :param key: the key to sort the list of the songs

        """
        f = None
        if key == "artist":
            f = lambda x: (x.artist.lower(), x.title.lower())
        elif key == "title":
            f = lambda x: x.title.lower()
        elif key == "year":
            f = lambda x: (x.year, x.title.lower())
        elif key == "is_required":
            f = lambda x: (x.is_required, x.title.lower())
        elif key == "is_learned":
            f = lambda x: (x.is_learned, x.title.lower())
        self.songs.sort(key=f)

    def __str__(self):
        ret_str = ""
        for song in self.songs:
            ret_str += str(song) + '\n'
        return ret_str
