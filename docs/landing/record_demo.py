"""데모 HTML(window.seek)을 프레임 캡처해 mp4 + poster로 굽는다.

데모 HTML은 녹화 전용이라 공개 사이트(site/)가 아니라 docs/landing/demo/에 둔다.
docs/landing/assets는 site/assets를 가리키는 심볼릭 링크다.
사용: python3 docs/landing/record_demo.py [search|research]
      (녹화용 서버를 스크립트가 직접 띄웠다가 끈다)"""
import os, shutil, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor
from playwright.sync_api import sync_playwright

PORT = 18432
BASE = f"http://127.0.0.1:{PORT}/demo"
MEDIA = os.path.join(os.path.dirname(__file__), "..", "..", "site", "assets", "media")
JOBS = [(d, l, dur) for d, dur in (("search", 11), ("research", 11.5)) for l in ("en", "ko", "zh")]
FPS = 30

def rec(job):
    demo, lang, dur = job
    out = os.path.abspath(os.path.join(MEDIA, f"{demo}-{lang}.mp4"))
    fr = tempfile.mkdtemp(prefix=f"frames-{demo}-{lang}-")
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1280, "height": 720})
        pg.goto(f"{BASE}/{demo}.html?lang={lang}"); pg.wait_for_function("window.__ready===true"); pg.wait_for_timeout(800)
        for i in range(int(dur * FPS)):
            pg.evaluate(f"seek({i / FPS})"); pg.screenshot(path=f"{fr}/{i:05d}.png")
        b.close()
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", f"{fr}/%05d.png", "-c:v", "libx264",
                    "-pix_fmt", "yuv420p", "-crf", "22", "-movflags", "+faststart", out], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(dur - 0.5), "-i", out, "-frames:v", "1",
                    out.replace(".mp4", "-poster.png")], check=True)
    shutil.rmtree(fr)
    return out

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    srv = subprocess.Popen([sys.executable, "-m", "http.server", str(PORT), "--bind", "127.0.0.1", "--directory", here],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    import time, urllib.request
    for _ in range(50):
        try:
            urllib.request.urlopen(f"{BASE}/search.html", timeout=1); break
        except Exception:
            time.sleep(0.2)
    only = sys.argv[1:]
    jobs = [j for j in JOBS if not only or j[0] in only]
    with ThreadPoolExecutor(6) as ex:
        try:
            for o in ex.map(rec, jobs): print("done", o)
        finally:
            srv.terminate()
