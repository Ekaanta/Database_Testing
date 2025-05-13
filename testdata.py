from pymongo import MongoClient
import pandas as pd
from pandasgui import show


client = MongoClient("mongodb+srv://durjoy:Kzifub0X9e2u4RlC@cluster0.jx0fabg.mongodb.net/")
db = client['test_db']  
collection = db['test']  


query = { "status": "active" }
users = collection.find(query)


user_data = []


for user in users:
    user_data.append({
        "_id": str(user["_id"]),
        "fullName": user.get("fullName", ""),
        "email": user.get("email", ""),
        "phone": user.get("phone", ""),
        "profession": user.get("profession", ""),
        "isEmailVerified": user.get("isEmailVerified", False),
        "roles": ', '.join(user.get("roles", [])),
        "status": user.get("status", ""),
        "image": user.get("image", ""),
        "cords": str(user.get("cords", {})),
        "address": user.get("address", ""),
        "role": user.get("role", ""),
        "createdAt": str(user.get("createdAt", "")),
        "updatedAt": str(user.get("updatedAt", ""))
    })


df = pd.DataFrame(user_data)


show(df)


print(df)


duplicate_query = collection.aggregate([
    { "$group": { "_id": "$email", "count": { "$sum": 1 } } },
    { "$match": { "count": { "$gt": 1 } } }
])


for duplicate in duplicate_query:
    print(f"Duplicate found for email: {duplicate['_id']}")
