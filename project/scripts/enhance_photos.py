import os, re, urllib.request, traceback, sys
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = r"C:/Users/JimAn/Desktop/ThinkFlowLabs/Websites Builder/Projects/Hotel Barahona 72"
ENV = r"C:/Users/JimAn/Desktop/ThinkFlowLabs/Websites Builder/Projects/mb-clean-solutions/site/.env"
for line in open(ENV, encoding="utf-8"):
    m = re.match(r"\s*FAL_KEY\s*=\s*(.+)\s*", line)
    if m:
        os.environ["FAL_KEY"] = m.group(1).strip().strip('"').strip("'")
import fal_client

PROMPT = ("Enhance this real hotel interior photograph for the hotel website. "
 "Improve lighting, white balance, sharpness, contrast and color so it looks like clean, bright, "
 "professional real-estate / hospitality photography. Keep the room, furniture, layout, materials, "
 "proportions and every object EXACTLY the same. Do NOT add, remove, move or invent any furniture, "
 "windows, doors, views, decorations or text. Brighten shadows, remove color cast, make it crisp, "
 "inviting and magazine-quality. Photorealistic. No new text, no watermark.")

PROMPT_03 = ("Enhance this real hotel reception photograph for the hotel website. Improve lighting, "
 "white balance, sharpness and color to clean professional hospitality photography. Keep the reception "
 "desk, the brand logo and ALL signage text EXACTLY as in the original and fully legible, and keep any "
 "person's face and appearance unchanged. Do NOT add, remove, move or invent anything. Photorealistic, "
 "no new text, no watermark.")

# remaining images (01 and 22 already enhanced in the pilot)
NUMS = ["02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","20","21"]

logp = os.path.join(BASE, "assets", "enhanced", "_batch.log")
def log(msg):
    with open(logp, "a", encoding="utf-8") as f:
        f.write(msg + "\n")
    print(msg, flush=True)

def enhance(n):
    src = os.path.join(BASE, "assets", "drive", f"barahona-{n}.jpg")
    dst = os.path.join(BASE, "assets", "enhanced", f"barahona-{n}-gpt.png")
    if os.path.exists(dst):
        return f"skip {n} (exists)"
    prompt = PROMPT_03 if n == "03" else PROMPT
    url = fal_client.upload_file(src)
    args = {"prompt": prompt, "image_urls": [url], "num_images": 1, "quality": "high", "image_size": "auto"}
    try:
        r = fal_client.subscribe("openai/gpt-image-2/edit", arguments={**args, "input_fidelity": "high"})
    except Exception as e:
        r = fal_client.subscribe("openai/gpt-image-2/edit", arguments=args)
    out = r["images"][0]["url"]
    urllib.request.urlretrieve(out, dst)
    return f"ok {n} ({os.path.getsize(dst)//1024} KB)"

log(f"=== batch start: {len(NUMS)} images ===")
done = 0
with ThreadPoolExecutor(max_workers=4) as ex:
    futs = {ex.submit(enhance, n): n for n in NUMS}
    for fut in as_completed(futs):
        n = futs[fut]
        try:
            log(fut.result()); done += 1
        except Exception as e:
            log(f"FAIL {n}: {str(e)[:160]}")
log(f"=== batch done: {done}/{len(NUMS)} succeeded ===")
