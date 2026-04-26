class LoginPage:
    def __init__(self, page):
        self.page = page

    def abrir(self):
        self.page.goto("/")

    def login(self, usuario, password):
        self.page.fill("#user-name", usuario)
        self.page.fill("#password", password)
        self.page.click("#login-button")

    def obtener_error(self):
        return self.page.inner_text("[data-test='error']")
