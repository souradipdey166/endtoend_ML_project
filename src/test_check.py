
from check import (
    calculate_subtotal,
    calculate_discount,
    calculate_final_price,
    apply_tax,
    checkout,
)


def test_calculate_subtotal():
    items = [
        {"price": 100, "quantity": 2},
        {"price": 50, "quantity": 1},
    ]

    assert calculate_subtotal(items) == 250


def test_premium_discount():
    assert calculate_discount(1000, "premium") == 200


def test_regular_discount():
    assert calculate_discount(1000, "regular") == 100


def test_no_discount():
    assert calculate_discount(1000, "guest") == 0


def test_final_price_premium():
    items = [
        {"price": 500, "quantity": 2},
    ]

    # subtotal = 1000
    # premium discount = 20%
    # final = 800
    assert calculate_final_price(items, "premium") == 800


def test_final_price_regular():
    items = [
        {"price": 500, "quantity": 2},
    ]

    # subtotal = 1000
    # regular discount = 10%
    # final = 900
    assert calculate_final_price(items, "regular") == 900


def test_tax():
    assert apply_tax(100, 0.10) == 110


def test_checkout():
    items = [
        {"price": 100, "quantity": 2},
        {"price": 50, "quantity": 2},
    ]

    # subtotal = 300
    # premium discount = 60
    # discounted price = 240
    # 10% tax = 264
    assert checkout(items, "premium", 0.10) == 264
