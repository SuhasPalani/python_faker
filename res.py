from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Create a list to store the generated data
customer_data = []
status = ['failed', 'confirmed']

# Define a start and end date for your timestamp range
start_date = datetime(2023, 10, 1)
end_date = datetime(2023, 12, 31)

# Generate 20 customer records
for _ in range(15):
    res_id = _ + 230  # Primary key, incrementing by 1 for each record
    cust_id = random.randint(101, 118)
    spot_id = random.randint(200, 229)
    start_time = start_date + timedelta(seconds=random.randint(0, (end_date - start_date).total_seconds()))

    # Ensure that the difference between checkin_at and checkout_at is less than 24 hours
    max_checkout_diff = min(24 * 60 * 60, (end_date - start_time).total_seconds())
    checkout_diff = random.randint(0, max_checkout_diff)
    expire_time = start_time + timedelta(seconds=checkout_diff)

    vehicle_type = random.choice(status)

    checkin_at = start_time.strftime("%Y-%m-%d %H:%M:%S")
    checkout_at = expire_time.strftime("%Y-%m-%d %H:%M:%S")

    customer_record = (res_id, cust_id, spot_id, checkin_at, checkout_at, vehicle_type)
    customer_data.append(customer_record)

# Print the generated data
for record in customer_data:
    print(record)
    print(",")
