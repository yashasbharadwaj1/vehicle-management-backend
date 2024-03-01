
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