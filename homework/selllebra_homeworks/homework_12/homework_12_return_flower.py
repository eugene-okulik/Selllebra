class Flowers:
    def __init__(self, name, color, alive, price):
        self.name = name
        self.color = color
        self.alive = alive
        self.price = price


class Wildflowers(Flowers):
    def __init__(self, name, color, alive, price, size):
        super().__init__(name, color, alive, price)
        self.size = size


class WeddingFlowers(Flowers):
    def __init__(self, name, color, alive, price, flavor):
        super().__init__(name, color, alive, price)
        self.flavor = flavor


flower1 = WeddingFlowers('Rose', "red", 7, 100, "high")
flower2 = WeddingFlowers('Tulip', "yellow", 6, 45, "low")
flower3 = Wildflowers('Poppy', "blue", 4, 25, "medium")
flower4 = Wildflowers('Camomile', "green", 14, 10, "small")


class Bouquet:

    def __init__(self, flowers):
        self.flowers = flowers

    def bouquet_price(self):
        return sum(flower.price for flower in self.flowers)

    def bouquet_alive(self):
        avg = sum(flower.alive for flower in self.flowers) / len(self.flowers)
        return round(avg)

    def __lt__(self, obj):
        return self.bouquet_price() < obj.bouquet_price()

    def sort_by_price(self):
        sorted_flowers = sorted(self.flowers, key=lambda flower: flower.price)
        return {flower for flower in sorted_flowers}

    def sort_by_color(self):
        sorted_flowers = sorted(self.flowers, key=lambda flower: flower.color)
        return [flower for flower in sorted_flowers]

    def find_by_color(self, color):
        return [flower for flower in self.flowers if flower.color == color]


bouquet_order1 = Bouquet([flower1, flower2, flower3])
bouquet_order2 = Bouquet([flower3, flower4])

print(bouquet_order1.bouquet_price())
print(bouquet_order1.bouquet_alive())
print(bouquet_order1 < bouquet_order2)
print(bouquet_order1.sort_by_price())
print(bouquet_order1.sort_by_color())
print(bouquet_order1.find_by_color('red'))
