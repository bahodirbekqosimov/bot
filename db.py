from psycopg2 import connect
from environs import Env





from utils import writer


env = Env()
env.read_env()

print(env.str("TOKEN"))