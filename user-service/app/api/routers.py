from app.models.models import *
from .general_api import get_router

routers = []
key = "Table"
for w in dir():
    if key in w and len(w) > len(key):
        print(w)
        # 表中增加字段
        t = globals()[w]
        t.user = Column(String)
        t.syncTime = Column(Integer)
        routers.append(get_router(t))
