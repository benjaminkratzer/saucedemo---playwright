class CartPage:
    def __init__(self, page):
        self.page = page

    def obtener_cantidad_items(self):
        return self.page.locator(".cart_item").count()

    def ir_a_checkout(self):
        self.page.click("[data-test='checkout']")
