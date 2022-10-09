from app.models.models import *
from .general_api import get_router

routers = []
key = "Table"
for w in dir():
    if key in w and len(w) > len(key):
        print(w)
        routers.append(get_router(globals()[w]))
