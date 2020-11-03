class Part:
    def __init__(self, category, part_str, price, url):
        self.category = category
        self.part_str = part_str
        self.price = price
        self.url = url

    def __str__(self):
        return f"{self.category}, {self.part_str}, {self.price}, {self.url}"

    def __eq__(self, other):
        if self.url == other.url:
            return True
        return False
