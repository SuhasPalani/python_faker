from faker import Faker
import random

fake = Faker()

# Create a list to store the generated data
customer_data = []
spot_types=['standard','disabled','motor cycle','charging','valet','reserved','truck']
status_type=['available','occupied']
# Generate 20 customer records
for _ in range(20):
    spot_id = _ + 230  # Primary key, incrementing by 1 for each record
    lot_id = random.randint(1001,1015)
    spot_type = random.choice(spot_types)
    status = random.choice(status_type)
    customer_record = (spot_id,lot_id, spot_type, status)
    customer_data.append(customer_record)

# Print the generated data
for record in customer_data:
    print(record)
    print(",")
