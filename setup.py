from cx_Freeze import setup, Executable

base = None    

executables = [Executable("App.py", base=base)]

from login import Logging, cs, cur
from searching import Search
import db_connect as db
import os
import socket
import pickle
import datetime 


packages = ["idna", "os", "socket", "pickle", "datetime", "fpdf", "psycopg2", ]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "App",
    options = options,
    version = "2.0.0",
    description = "Aplikacja zrobiona w architekturze KLIENT - SERWER. Podłączona do bazy danych PostgreSQL 11",
    executables = executables
)