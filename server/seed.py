# import app
# import model and db instance
from random import choice as rc
from random import randint

from app import app, db
from faker import Faker
from models import Sighting

# Define seeding functions (optional: use Faker to help generate fake data)
fake = Faker()


def clear_data():
    print("Clearing data...")
    Sighting.query.delete()


def gen_sightings():
    print("Generating sightings...")
    shapes = ["cigar", "saucer", "capsule", "sphere", "cylinder"]
    sightings = []
    for _ in range(10):
        s = Sighting(
            date=fake.date_this_decade(),
            time=fake.time(),
            location=fake.city(),
            shape_of_craft=rc(shapes),
            approximate_size=randint(1, 1000),
            approximate_speed=randint(0, 1000),
            description=fake.sentence(),
            reporter=fake.name(),
            reporter_reliable_witness=fake.boolean(),
        )
        sightings.append(s)
    db.session.add_all(sightings)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        # Call seeding functions
        clear_data()
        gen_sightings()
        print("Seeding complete...")
