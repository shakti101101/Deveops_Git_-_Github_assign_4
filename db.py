from pymongo import MongoClient

MONGO_URI = "mongodb+srv://shaktig101101_db_user:C1yoWqhkEj5muHcL@cluster0.sofmx8o.mongodb.net/"
#mongodb+srv://shaktig101101_db_user:6jjQ45uNyVBCUR@cluster0.sofmx8o.mongodb.net/
try:
    client = MongoClient(MONGO_URI)
    print("✅ Connected! Databases:", client.list_database_names())
except Exception as e:
    print("❌ Connection failed:", e)
