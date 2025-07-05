from osu import Client, Path
from dotenv import load_dotenv
import os


load_dotenv()


CLIENT_ID = int(os.getenv("OSU_CLIENT_ID"))
CLIENT_SECRET = os.getenv("OSU_CLIENT_SECRET")

client = Client.from_credentials(CLIENT_ID, CLIENT_SECRET, None)

beatmap_id = 5175021 # miku farm xd


beatmap = client.get_beatmap(beatmap_id)
beatmapset_id = beatmap.beatmapset_id

resp = client.http.make_request(
    Path("get", f"beatmapsets/{beatmapset_id}", "public"),
    limit=10
)
print(", ".join([x['name'] for x in resp['related_tags']]))

