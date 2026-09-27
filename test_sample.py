# get the duplicate element :

from sqlalchemy import create_engine,text
from sqlalchemy.orm import declarative_base,sessionmaker
import json

DATABASE_URL = "postgresql://postgres:12345@localhost/Employee"

engine = create_engine(DATABASE_URL)
session = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit = False
)

Base = declarative_base()

db = session()
query = text("SELECT * FROM employees")
result = db.execute(query)
# results = result.fetchall()  ---> will get the result like (1, 'Alice', 'IT', 
# 'Software Engineer', Decimal('75000.00'), datetime.date(2022, 1, 15)) tuple and also access by the col name 

# results = result.mappings().all()
results = result.mappings()

for res in results:
    print(res)

result_data = [{k:str(v) for k,v in row.items()} 
               for row in result.mappings()]

print(result_data[:5])

