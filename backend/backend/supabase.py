
from supabase import create_client, Client
from dotenv import dotenv_values
config = dotenv_values(".env") 
import psycopg2 

def get_supabase_connection():
    conn = psycopg2.connect(
    dbname='postgres',
    user='postgres.zzcdmpkeauuozbnvxdxv',
    password=config.get("SUPABASE_DEV_ENV"),
    host='aws-0-ap-south-1.pooler.supabase.com',
    port='5432'
    )
    return conn 

# using raw sql query

# cur = supabase_connction.cursor()
# cur.execute("SELECT * FROM public.vendor_vendor")
# rows = cur.fetchall()

# data = []
# # print(cur.description)
# # print(type(cur.description))
# # (Column(name='id', type_code=20), Column(name='name', type_code=1043), Column(name='details', type_code=1043))
# # <class 'tuple'>
# for row in rows:
## each row is a tuple (1, 'tvs', 'vendor details')
#row_dict = {}
# for i, field in enumerate(cur.description):
# field_name = field.name
# row_dict[field_name] = row[i]
# data.append(row_dict)
# cur.close()
# supabase_connction.close()
# return Response({"data": data})