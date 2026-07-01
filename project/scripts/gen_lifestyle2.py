import os, re, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
BASE = r"C:/Users/JimAn/Desktop/ThinkFlowLabs/Websites Builder/Projects/Hotel Barahona 72"
ENV = r"C:/Users/JimAn/Desktop/ThinkFlowLabs/Websites Builder/Projects/mb-clean-solutions/site/.env"
for line in open(ENV, encoding="utf-8"):
    m = re.match(r"\s*FAL_KEY\s*=\s*(.+)\s*", line)
    if m: os.environ["FAL_KEY"] = m.group(1).strip().strip('"').strip("'")
import fal_client
REAL = ("Ultra photorealistic candid lifestyle photograph, natural realistic skin texture, natural warm "
        "Caribbean daylight, shot on a full-frame camera 50mm lens, shallow depth of field, authentic, "
        "not a render, no CGI, no text, no watermark, no logo.")
# Barranquilla is a hot coastal Caribbean city: summer / resort attire, curvy costena look, tasteful.
JOBS = {
 "life-guest": ({"width":1024,"height":1536},
   "A beautiful warm Colombian woman in her late twenties with golden-tan skin and long wavy dark brown hair, "
   "radiant genuine smile, natural curvy build, wearing an elegant colorful summer dress, standing in a bright "
   "modern hotel lobby with green plants and teal armchairs, holding a woven straw bag, welcoming and friendly. " + REAL),
 "life-lounge": ({"width":1536,"height":1024},
   "A cheerful Colombian woman in her late twenties with warm tan skin and wavy dark hair, relaxing and laughing "
   "on a grey sofa in a bright hotel lobby lounge with teal armchairs and plants, wearing a casual summer blouse "
   "and light jeans, natural curvy build, warm daylight, candid and inviting. " + REAL),
 "life-terrace": ({"width":1024,"height":1536},
   "A confident Colombian woman in her early thirties with warm tan skin and wavy hair, standing on a sunny hotel "
   "terrace with tropical plants and a bright sky, wearing a light flowy summer dress, relaxed genuine smile, "
   "natural curvy build, golden afternoon light. " + REAL),
}
logp = os.path.join(BASE, "assets", "lifestyle", "_gen2.log")
def log(m):
    with open(logp, "a", encoding="utf-8") as f: f.write(m+"\n")
    print(m, flush=True)
def gen(name):
    size, prompt = JOBS[name]
    dst = os.path.join(BASE, "assets", "lifestyle", name + ".png")
    r = fal_client.subscribe("openai/gpt-image-2", arguments={"prompt":prompt,"image_size":size,"num_images":1,"quality":"high"})
    urllib.request.urlretrieve(r["images"][0]["url"], dst)
    return f"ok {name} ({os.path.getsize(dst)//1024} KB)"
open(logp,"w").close()
log(f"=== gen2 start: {len(JOBS)} ===")
done=0
with ThreadPoolExecutor(max_workers=3) as ex:
    futs={ex.submit(gen,n):n for n in JOBS}
    for f in as_completed(futs):
        try: log(f.result()); done+=1
        except Exception as e: log(f"FAIL {futs[f]}: {str(e)[:160]}")
log(f"=== gen2 done: {done}/{len(JOBS)} ===")
