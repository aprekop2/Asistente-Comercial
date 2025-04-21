from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def guardar_interaccion(usuario, mensaje, respuesta):
    data = {
        "usuario": usuario,
        "mensaje": mensaje,
        "respuesta": respuesta,
    }
    supabase.table("interacciones").insert(data).execute()
