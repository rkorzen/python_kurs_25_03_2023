from faker import Faker

fake = Faker("pl_PL")

print(fake.name())
print(fake.first_name())
print(fake.last_name())
print(fake.job())
print(fake.address())
print(fake.text())
print(fake.date())
print(fake.isbn13())
print(fake.random_int(min=0, max=100))
print(fake.random_element(elements=("a", "b", "c")))
print(fake.random_element(elements=("a", "b", "c")))
