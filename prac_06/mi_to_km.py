from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class MiToKm(App):
    def build(self):
        Window.size = (350,150)
        self.title = 'Convert Mi to Km'
        self.root = Builder.load_file('mi_to_km.kv')
        return self.root

    def increment_up(self, value):
        result_up = value + 1
        self.root.ids.input_mi.text = str(result_up)

    def increment_down(self, value):
        result_down = value - 1
        self.root.ids.input_mi.text = str(result_down)

    def handle_calculate(self, value):
        result_calculate = value * 1.61
        result_disp = '{:.2f} mi = {:.2f} km'.format(value, result_calculate)
        self.root.ids.output_label.text = result_disp

MiToKm().run()