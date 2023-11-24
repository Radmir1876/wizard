class Wizard:
    def init(self, name, rating, age):
        self.name = name
        self.rating = rating
        self.age = age

    def change_rating(self, value):
        self.rating += value
        if self.rating > 100:
            self.rating = 100
        elif self.rating < 1:
            self.rating = 1

        if value > 0:
            self.age -= abs(value) // 10
            if self.age < 18:
                self.age = 18
        elif value < 0:
            self.age -= abs(value) // 10

    def iadd(self, string):
        self.rating += len(string)
        self.age -= len(string) // 10
        if self.rating > 100:
            self.rating = 100
        if self.age < 18:
            self.age = 18
        return self

    def call(self, value):
        return self.age * self.rating

    def str(self):
        return f"Wizard {self.name} with {self.rating} rating looks {self.age} years old"

    def lt(self, other):
        if self.rating != other.rating:
            return self.rating < other.rating
        elif self.age != other.age:
            return self.age < other.age
        return self.name < other.name

    def le(self, other):
        return self < other or self == other

    def eq(self, other):
        return self.rating == other.rating and self.age == other.age and self.name == other.name

    def ne(self, other):
        return not self == other

    def gt(self, other):
        return not self <= other

    def ge(self, other):
        return not self < other