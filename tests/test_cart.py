from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_agregar_al_carrito(logged_in):
    inventory = InventoryPage(logged_in)
    inventory.agregar_primer_producto()
    inventory.ir_al_carrito()
    cart = CartPage(logged_in)
    assert cart.obtener_cantidad_items() > 0

def test_carrito_vacio(logged_in):
    inventory = InventoryPage(logged_in)
    inventory.ir_al_carrito()
    cart = CartPage(logged_in)
    assert cart.obtener_cantidad_items() == 0
