import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "28432968"))
API_HASH = getenv("API_HASH", "428d4a60ab657a4c901693140101e424")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7431327628:AAFYBX_ple-ofDBW2J640kl7ex5S08fnauI")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://aydanmsc:dahumyG5@cluster0.i2vt3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 5400))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002179110868"))

# Get this value from @Hot_Girl_Robot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7250739004"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Hesenovhuseyn/FidanMusicBot-v2",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/VenomOwners")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Venom_Chatz")


AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "false")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "5400"))
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @Venom_string_robot on Telegram
STRING1 = getenv("STRING_SESSION", "AgGx2kgAGGcg5NMOC-HA_ZvpZkJ6BOCQOsAhe_oLt9yEM5JaomWFwN1qiwU9_gGiZKWf_3RedaWRKCme9Dq4t7iGLE7mbbq94RllPdvUYzrJ1uI_Bwi_lIJlD6USPmhoqVnRSAx5Q1SGgh4_N3mfL0tJNhOClfyZKE-8GWCdnoK0AC6xgXIq1TqNMHBrwvzn9JdPVE1w1f-AwFmOdZe3RK6lTykQ-gmWPd0Kg7ljvm55farYLWj_W81rT2CPQxn8OFqGN1v9p5zEv2PEJlwBE3r_Ah30kMw8bmRL02TR_CCmp0HQpi_HVRzmfl4nUnV12PLbTQ2MVEk1yhN6TVmu1Er8_6aA5QAAAAG2y3H9AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/754e95311eccb48b7aafc.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
