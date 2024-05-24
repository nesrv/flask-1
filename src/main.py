import asyncio
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

# from queries.core import create_tables, insert_data
# from queries.orm import create_tables, insert_data

# from queries.core import  SyncCore
from queries.orm import SyncORM

# SyncCore.create_tables()
# SyncCore.insert_workers()
# SyncCore.select_workers()


SyncORM.create_tables()
SyncORM.insert_workers()
SyncORM.select_workers()
SyncORM.update_worker()
SyncORM.insert_resumes()

# create_tables()
# asyncio.run(insert_data())
# insert_data()