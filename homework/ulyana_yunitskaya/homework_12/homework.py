class Flower:
    stem = True
    leaves = True

    def __init__(self, freshness, color, stem_length, cost, life_time):
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length
        self.cost = cost
        self.life_time = life_time

class Hibiscus(Flower):
    def __init__(self, freshness, color, stem_length, cost, life_time, smell):
        super().__init__(freshness, color, stem_length, cost, life_time)
        self.smell = smell

class Rose(Flower):
    def __init__(self, freshness, color, stem_length, cost, life_time, thorns):
        super().__init__(freshness, color, stem_length, cost, life_time)
        self.thorns = thorns

class Aster(Flower):
    def __init__(self, freshness, color, stem_length, cost, life_time, core):
        super().__init__(freshness, color, stem_length, cost, life_time)
        self.core = core


flower_h = Hibiscus(True, 'orange', 7, 15, 5, False)
flower_r = Rose(False, 'white', 16, 22, 3, True)
flower_a = Aster(True, 'blue', 10, 7, 6, True)
print(flower_h.cost)
print(flower_r.color)
print(flower_a.stem_length)

class Bouquet:
    def __init__(self, flowers: list):
        self.bouquet_list = flowers

    def price_bouquet(self):
        return sum([flower.cost for flower in self.bouquet_list])

    def time_of_fading(self):
        return sum([flower.life_time for flower in self.bouquet_list]) / len(self.bouquet_list)

    def sorted_flower_freshness(self):
        return sorted(self.bouquet_list, key=lambda flower: flower.freshness)

    def sorted_flower_color(self):
        return sorted(self.bouquet_list, key=lambda flower: flower.color)

    def sorted_flower_stem_length(self):
        return sorted(self.bouquet_list, key=lambda flower: flower.stem_length)

    def sorted_flower_color_cost(self):
        return sorted(self.bouquet_list, key=lambda flower: flower.cost)

    def search_flower_life_time(self):
        new_list_search = []
        for flower in self.bouquet_list:
            if flower.life_time > 4:
                new_list_search.append(flower)

        return new_list_search
