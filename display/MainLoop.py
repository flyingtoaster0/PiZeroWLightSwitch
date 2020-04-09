class MainLoop:

    def __init__(self, app_input, renderer, menu_manager, breadcrumb_printer):
        self.renderer = renderer
        self.app_input = app_input

        self.menu_manager = menu_manager
        self.breadcrumb_printer = breadcrumb_printer
        pass

    def run(self):
        self.renderer.init_renderer()

        lines_to_render = self.menu_manager.get_renderable_text()
        self.renderer.render(lines_to_render)
        self.app_input.set_callback(self.handle_input)
        self.app_input.begin_input()

    def handle_input(self, input_button):
        self.menu_manager.handle_input(input_button)
        lines_to_render = self.menu_manager.get_renderable_text()
        self.renderer.render(lines_to_render)
