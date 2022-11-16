import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ducdn:220301@cluster0.1itnd0h.mongodb." \
                                   "net/students?retryWrites=true&w=majority")

MONGO_URL_LOCAL = os.getenv("MONGO_URL_LOCAL", "mongodb://localhost:27017")