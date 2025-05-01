class HomePage:

    def __init__(self, page):
        self.page = page
        self.search_input = "#search_query_top"
        self.search_button = "button[name='submit_search']"

    def abrir(self):
        self.page.goto("http://automationpractice.pl/index.php")

    def buscar_producto(self, texto):
        self.page.fill(self.search_input, texto)
        self.page.click(self.search_button)
