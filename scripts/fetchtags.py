from osu import Client
from dotenv import load_dotenv
import os


load_dotenv()


CLIENT_ID = int(os.getenv("OSU_CLIENT_ID"))
CLIENT_SECRET = os.getenv("OSU_CLIENT_SECRET")
REDIRECT_URI = os.getenv("OSU_REDIRECT_URI")

client = Client.from_client_credentials(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)

beatmap_id = 221777


beatmap = client.get_beatmap(beatmap_id)
beatmapset_id = beatmap.beatmapset_id

beatmapset = client.get_beatmapset(beatmapset_id)


tags_string = beatmapset.tags
tags = tags_string.split() if tags_string else []

print(f"Tags for beatmapset {beatmapset_id}: {tags}")
