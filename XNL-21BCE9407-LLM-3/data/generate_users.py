from faker import Faker
import pandas as pd
import random

faker = Faker()
def generate_users(n=100000):
    data = []
    for _ in range(n):
        data.append({
            'user_id': faker.uuid4(),
            'age': random.randint(18, 70),
            'region': faker.country(),
            'credit_score': random.randint(300, 850),
            'behavioral_history': faker.sentence()
        })

    df = pd.DataFrame(data)
    df.to_csv('users.csv', index=False)

if __name__ == "__main__":
    generate_users()
