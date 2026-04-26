from pages.inventory_page import InventoryPage

def test_ver_productos(logged_in):
    inventory = InventoryPage(logged_in)
    assert inventory.obtener_cantidad_productos() > 0

def test_ordenar_por_nombre_za(logged_in):
    inventory = InventoryPage(logged_in)
    inventory.ordenar_por("za")
    nombres = inventory.obtener_nombres_productos()
    assert nombres == sorted(nombres, reverse=True)

