

class BreadcrumbPrinter:

    def __init__(self, menu_stack):
        self.menu_stack = menu_stack

    def get_breadcrumb_str(self):
        breadcrumb_str = ''
        for menu in self.menu_stack:
            breadcrumb_str = breadcrumb_str + menu.get_title_text() + ' > '
        return breadcrumb_str

    def get_condensed_breadcrumb_str(self):
        tree_depth = len(self.menu_stack)

        breadcrumb_str = ''
        for i in range(0, tree_depth - 1):
            breadcrumb_str = breadcrumb_str + '> '

        return breadcrumb_str + self.menu_stack[-1].get_title_text()
