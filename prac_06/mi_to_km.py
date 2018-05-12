from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase

LabelBase.register(name='SourceCodePro', fn_regular='SourceCodePro-Regular.ttf', fn_bold='SourceCodePro-Semibold.ttf')

class MiToKm(App):
    def build(self):
        Window.size = (350,150)
        self.title = 'Convert Mi to Km'
        self.root = Builder.load_file('mi_to_km.kv')
        return self.root

    def increment_up(self, value):
        try:
            float(value)
        except ValueError:
            value = 0.0
            self.root.ids.input_mi.text = 'Invalid'

        number = float(value)
        result_up = number + 1
        self.root.ids.input_mi.text = str(result_up)

    def increment_down(self, value):
        valid_input = False
        if valid_input == False:
            try:
                float(value)
                valid_input = True
            except ValueError:
                pass
        if valid_input == True:
            number = float(value)
            if number <= 0.0:
                result_down = 0.0
                self.root.ids.input_mi.text = str(result_down)
            else:
                result_down = number - 1
                self.root.ids.input_mi.text = str(result_down)


    def handle_calculate(self, value):
        valid_input = False
        if valid_input == False:
            try:
                float(value)
                valid_input = True
            except ValueError:
                pass

        if valid_input == True:
            number = float(value)
            result_calculate = number * 1.61
            result_display = '{:.2f} mi = {:.2f} km'.format(number, result_calculate)
            self.root.ids.output_label.text = result_display
        else:
            result_display = '-.-- mi = -.-- km'
            self.root.ids.output_label.text = result_display
MiToKm().run()