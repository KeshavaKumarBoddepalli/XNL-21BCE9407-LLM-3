from faker import Faker
import pandas as pd
import random

faker = Faker()

def generate_transaction_data(n=1000000):
    data = []
    for _ in range(n):
        data.append({
            'user_id': faker.uuid4(),
            'amount': round(random.uniform(1.0, 10000.0), 2),
            'merchant': faker.company(),
            'timestamp': faker.date_time_this_year(),
            'device': faker.user_agent(),
            'location': faker.address(),
            'label': random.choice(['normal', 'suspicious', 'fraudulent'])
        })

    df = pd.DataFrame(data)
    df.to_csv('transactions.csv', index=False)

if __name__ == "__main__":
    generate_transaction_data()
