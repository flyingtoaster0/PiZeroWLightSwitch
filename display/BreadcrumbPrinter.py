

class BreadcrumbPrinter:

    def get_breadcrumb_str(self, menu_stack):
        breadcrumb_str = ''
        for menu in menu_stack:
            breadcrumb_str = breadcrumb_str + menu.get_title_text() + ' > '
        return breadcrumb_str
