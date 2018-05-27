#
# File: song.py
# Description:
#       The Class represents a single song
#
# Last Modified:
#       May 17, 2018
# Owner:
#       Felix Widyanto Oetomo
#
#

class Song:
    """

    A class representing a song containing artist name, title, year of publication
    and is it required or not

    """
    def __init__(self, artist="", title="", year=0, is_required=True):
        # type: (str, str, int, bool) -> object
        """

        Constructor for the song

        :param artist: string identifies the artist/singer of the song, default is empty
        :param title: string identifies the title of the song, default is empty
        :param year: string identifies the year of the song, default is empty
        :param is_required: True or False

        """
        self.artist = artist
        self.title = title
        self.year = year
        self.is_required = is_required
        self.is_learned = False

    def mark_learned(self):
        """

        A Method to mark a song being learned

        """
        self.is_learned = True

    def mark_unlearned(self):
        """

        A Method to reset a song being not yet learned

        """
        self.is_learned = False

    def __str__(self):
        """

        A string representation of the song to be used with print function
        :return a string of the concatination of the artist name,
                title, the year, requirement and being learned separated by _
        """
        return "{0},{1},{2},{3}".format(self.artist, self.title, self.year,
                                       'y' if self.is_learned is True else 'n')

