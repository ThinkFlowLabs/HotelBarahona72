import os, re, urllib.request, traceback
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = r"C:/Users/JimAn/Desktop/ThinkFlowLabs/Websites Builder/Projects/Hotel Barahona 72"
ENV = r"C:/Users/JimAn/Desktop/ThinkFlowLabs/Websites Builder/Projects/mb-clean-solutions/site/.env"
for line in open(ENV, encoding="utf-8"):
    m = re.match(r"\s*FAL_KEY\s*=\s*(.+)\s*", line)
    if m:
        os.environ["FAL_KEY"] = m.group(1).strip().strip('"').strip("'")
import fal_client

REAL = ("Ultra photorealistic candid photograph, natural skin texture with pores and subtle imperfections, "
        "realistic natural lighting, shot on a full-frame camera 50mm lens, shallow depth of field, "
        "authentic documentary style, not a render, no CGI, no text, no watermark, no logo.")

JOBS = {
 "life-guest": ({"width":1024,"height":1536},
   "A stylish, friendly young Colombian woman traveler in her late twenties smiling softly, standing in a "
   "bright clean hotel lobby with warm daylight, wearing a light casual summer blouse, holding a woven straw "
   "handbag, relaxed and welcoming, tasteful and elegant. " + REAL),
 "life-business": ({"width":1536,"height":1024},
   "A Colombian businesswoman in her thirties working calmly on a laptop at a wooden desk inside a clean, tidy "
   "hotel room, wearing a smart casual blazer, focused and content, warm natural light from a side window, "
   "professional and aspirational. " + REAL),
 "life-family": ({"width":1536,"height":1024},
   "A happy young Colombian family, mother father and two small children, hugging and smiling warmly together "
   "in a bright modern hotel lobby with teal armchairs, casual everyday clothes, genuine joyful expressions, "
   "soft natural window light, wholesome and warm. " + REAL),
 "life-carnaval": ({"width":1536,"height":1024},
   "A joyful Afro-Colombian young woman celebrating Carnaval de Barranquilla, wearing a vibrant colorful "
   "traditional flowered ruffled dress, dancing gracefully on a sunny colorful colonial street of Barranquilla, "
   "flowers in her hair, big genuine smile, festive Caribbean atmosphere, motion and joy, positioned toward the "
   "left of the frame with colorful bokeh background. " + REAL),
}

logp = os.path.join(BASE, "assets", "lifestyle", "_gen.log")
os.makedirs(os.path.dirname(logp), exist_ok=True)
def log(m):
    with open(logp, "a", encoding="utf-8") as f: f.write(m+"\n")
    print(m, flush=True)

def gen(name):
    size, prompt = JOBS[name]
    dst = os.path.join(BASE, "assets", "lifestyle", name + ".png")
    r = fal_client.subscribe("openai/gpt-image-2", arguments={
        "prompt": prompt, "image_size": size, "num_images": 1, "quality": "high"})
    url = r["images"][0]["url"]
    urllib.request.urlretrieve(url, dst)
    return f"ok {name} ({os.path.getsize(dst)//1024} KB)"

log(f"=== lifestyle gen start: {len(JOBS)} images ===")
done=0
with ThreadPoolExecutor(max_workers=4) as ex:
    futs = {ex.submit(gen, n): n for n in JOBS}
    for fut in as_completed(futs):
        n = futs[fut]
        try: log(fut.result()); done+=1
        except Exception as e: log(f"FAIL {n}: {str(e)[:180]}")
log(f"=== lifestyle gen done: {done}/{len(JOBS)} ===")
