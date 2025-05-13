Database Testing with MongoDB and Python
Setup and Installation
Clone this repository to local machine: 
bash
Copy
git clone mongodb+srv://durjoy:Kzifub0X9e2u4RlC@cluster0.jx0fabg.mongodb.net/
cd database-testing
Install the required Python packages by running:

bash
Copy
pip install -r requirements.txt
Testing results below:
![datatest1](https://github.com/user-attachments/assets/02b60c84-f499-4f71-b48b-5919edbbdd16)
![datatest2](https://github.com/user-attachments/assets/650c7bbe-0bb5-4d1b-beb7-83a04864b6e6)
![datatest3](https://github.com/user-attachments/assets/3ce197c1-7c90-4395-947d-fcf712b6a23d)
![datatest4](https://github.com/user-attachments/assets/dafbe960-8e04-4000-a8c8-cdd5d973aced)

Checking for Duplicates
python:
duplicate_query = collection.aggregate([
    { "$group": { "_id": "$email", "count": { "$sum": 1 } } },
    { "$match": { "count": { "$gt": 1 } } }
])

for duplicate in duplicate_query:
    print(f"Duplicate found for email: {duplicate['_id']}")
