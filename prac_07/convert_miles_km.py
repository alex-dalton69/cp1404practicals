from kivy.app import App
from kivy.lang import Builder

__author__ = 'Alexander Dalton'

MILES_TO_KM = 1.60934


class MilesConversionApp(App):
    def build(self):
        """build app from kivy file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """handles the calculation to convert m to km"""
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """changes the number of miles up or down depending on input"""
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """error checking for input type errors and convert input to float"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConversionApp().run()
