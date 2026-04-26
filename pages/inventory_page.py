class InventoryPage:
    def __init__(self, page):
        self.page = page

    def obtener_cantidad_productos(self):
        return self.page.locator(".inventory_item").count()

    def agregar_primer_producto(self):
        self.page.locator(".btn_inventory").first.click()

    def ir_al_carrito(self):
        self.page.click(".shopping_cart_link")

    def ordenar_por(self, criterio):
        self.page.select_option(".product_sort_container", criterio)

    def obtener_nombres_productos(self):
        return self.page.locator(".inventory_item_name").all_inner_texts()

    def obtener_precios_productos(self):
        precios = self.page.locator(".inventory_item_price").all_inner_texts()
        return [float(p.replace('$'', ''')) for p in precios]
