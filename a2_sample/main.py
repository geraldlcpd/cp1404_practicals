"""
Name: Felix Widyanto Oetomo
Date: May 17, 2018
Brief Project Description: XXXXXXXXXXXXXXXXXXXX
GitHub URL: XXXXXXXXXXXXXXXXXXXX
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import ListProperty
import datetime
import atexit

from a2_sample.songlist import SongList
from a2_sample.song import Song

__author__ = 'Felix Widyanto Oetomo'

SONG_CSV_FILE='songs.csv'

class SongsToLearnApp(App):
    """

    The class to start the App:
        - Initialize the GUI and load KV file
        - Initialize and load the songs stored in the object song_list

    """
    current_sort = StringProperty()
    sorting_types = ListProperty()

    def build(self):
        # initialize variables
        self.learned_number = 0
        self.tolearned_number = 0
        # Load all the songs into the song list instance
        self.all_song_widgets = []
        self.song_list = SongList()
        self.load_songs()
        # Initialize GUI
        self.title = "Song to learn 1.0 (c) Felix Widyanto Oetomo"
        self.root = Builder.load_file('app.kv')
        self.sorting_types = ["year", "artist", "title", "is_required", "is_learned"]
        self.current_sort = self.sorting_types[0]
        atexit.register(self.saved_all_songs)
        return self.root

    def reset_songs(self):
        """

        the method destroy all the buttons which holds each song

        """
        for song_id in self.all_song_widgets:
            self.root.ids.song_containers.remove_widget(song_id)
            print(song_id)
        self.all_song_widgets = []
        self.learned_number = 0
        self.tolearned_number = 0

    def _add_displayed_song(self, song):
        learned_color = (1, 1, 0, 1)
        unlearned_color = (0, 1, 1, 1)
        # create a button for each song entry, specifying the song title and id
        # song title on the GUI is "title" by artist (year) (learned or empty)
        # song id is title
        song_title = '"{0}" by {1} ({2}){3}'.format(song.title,
                                                    song.artist,
                                                    song.year,
                                                    "(learned)" if song.is_learned is True else "")
        song_color = None
        if song.is_learned is True:
            song_color = learned_color
            self.learned_number += 1
        else:
            song_color = unlearned_color
            self.tolearned_number += 1
        song_id = song.title
        temp_button = Button(text=song_title, id=song_id, color=song_color)
        self.all_song_widgets.append(temp_button)
        temp_button.bind(on_release=self.press_entry)
        # add the button to the "entries_box" using add_widget()
        self.root.ids.song_containers.add_widget(temp_button)
        self.root.ids.title_win.text = "To learn: {0}, Learned: {1}".format(
            self.tolearned_number, self.learned_number)

    def display_songs(self):
        for song in self.song_list.songs:
            self._add_displayed_song(song)

    def load_songs(self):
        self.song_list.load_songs(SONG_CSV_FILE)
        self.song_list.sort_songs(self.current_sort)

    def change_sort(self, sort_type):
        self.current_sort = sort_type
        self.song_list.sort_songs(sort_type)
        self.reset_songs()
        self.display_songs()

    def press_entry(self, instance):
        """
        Handle pressing entry buttons.
        :param instance: the Kivy button instance representing a song
        :return: None
        """
        # get name (dictionary key) from the id of Button we clicked on
        song_title = instance.id  # or name = instance.text
        # update status text
        self.root.ids.program_status.color = (0, 1, 0, 1)
        self.root.ids.program_status.text = "{0} is selected".format(song_title)

    def add_song(self):
        title = self.root.ids.title_input.text
        year = self.root.ids.year_input.text
        artist = self.root.ids.artist_input.text
        if title == "" or year == "" or artist == "":
            self.root.ids.program_status.color = (1, 0, 0, 1)
            self.root.ids.program_status.text = "All fields must be completed"
            return
        year_int = int(year)
        now = datetime.datetime.now()
        if year_int <= 1900 or year_int > now.year:
            self.root.ids.program_status.color = (1, 0, 0, 1)
            self.root.ids.program_status.text = "Please enter a valid year " \
                                                "(greater than 1900 and less than this year)"
            return
        new_song = Song(title, artist, year_int, True)
        self.song_list.add_song(new_song)
        self._add_displayed_song(new_song)

    def clear(self):
        """
        Handle pressing cler buttons.
        :param instance: the Kivy button instance
        :return: None
        """
        self.root.ids.artist_input.text = ''
        self.root.ids.title_input.text = ''
        self.root.ids.year_input.text = ''
        self.root.ids.program_status.text = ''

    def saved_all_songs(self):
        self.song_list.save_songs(SONG_CSV_FILE)

SongsToLearnApp().run()

