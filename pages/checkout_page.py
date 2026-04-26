class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def completar_formulario(self, nombre, apellido, zip_code):
        self.page.fill("[data-test='firstName']", nombre)
        self.page.fill("[data-test='lastName']", apellido)
        self.page.fill("[data-test='postalCode']", zip_code)
        self.page.click("[data-test='continue']")

    def obtener_total(self):
        return self.page.inner_text(".summary_total_label")

    def confirmar_compra(self):
        self.page.click("[data-test='finish']")

    def obtener_mensaje_confirmacion(self):
        return self.page.inner_text(".complete-header")
