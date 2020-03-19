class AppInput:

    def __init__(self, input_list):
        self.input_list = input_list

    def get_button(self, event):
        for sub_input in self.input_list:
            button = sub_input.get_button(event)
            if button is not None:
                return button
        return None
