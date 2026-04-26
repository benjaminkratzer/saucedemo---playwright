from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_completo(logged_in):
    inventory = InventoryPage(logged_in)
    inventory.agregar_primer_producto()
    inventory.ir_al_carrito()
    cart = CartPage(logged_in)
    cart.ir_a_checkout()
    checkout = CheckoutPage(logged_in)
    checkout.completar_formulario("Benjamin", "Kratzer", "1234")
    assert "$" in checkout.obtener_total()
    checkout.confirmar_compra()
    assert checkout.obtener_mensaje_confirmacion() == "Thank you for your order!"
