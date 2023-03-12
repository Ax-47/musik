import os
import asyncio
import motor.motor_asyncio
from dotenv import load_dotenv


def chack_database(clinent):
    try:
        clinent.admin.command("ismaster")
        print("!error")
    except Exception as e:
        print("error")


if __name__ != "__main__":
    load_dotenv()
    SPOTIFY_ID = os.getenv("SPOTIFY_ID")
    SPOTIFY_SECRET = os.getenv("SPOTIFY_SECRET")

    CLINENT = motor.motor_asyncio.AsyncIOMotorClient(
        os.getenv("MONGOURI"), serverSelectionTimeoutMS=5000)
    CLINENT.get_io_loop = asyncio.get_running_loop
    DATABASE = CLINENT.ngan_song_kru
    GUILD = DATABASE.Guild
    CAPTCHA = DATABASE.captcha
    TONTON = DATABASE.tonton
    FEEDBACK = DATABASE.feedback
