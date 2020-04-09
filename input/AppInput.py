class AppInput:

    def __init__(self, input_list):
        self.input_list = input_list

    def begin_input(self):
        for sub_input in self.input_list:
            sub_input.begin_input()

    def get_button(self):
        for sub_input in self.input_list:
            button = sub_input.get_button()
            if button is not None:
                return button
        return None

    def set_callback(self, button_callback):
        for sub_input in self.input_list:
            sub_input.set_callback(button_callback)
