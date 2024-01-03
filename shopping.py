from typing import List


class ShoppingCart:
    def __init__(self, max_item: int):
        self.items: List[str] = []
        self.max_item = max_item

    def add(self, item: str):
        if self.size_of_cart() == self.max_item:
            raise OverflowError("Cannot add more item")
        self.items.append(item)

    def size_of_cart(self) -> int:
        return len(self.items)

    def get_items(self) -> List[str]:
        return self.items

    def get_total_price(self, price_map):
        total_price = 0
        for item in self.items:
            print(item)
            total_price += price_map.get(item)
        return total_price