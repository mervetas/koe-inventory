import qrcode, os, csv
from pathlib import Path
from dotenv import load_dotenv 

# Load environment variables from .env file
load_dotenv()

# Read from environment variable, otherwise use localhost
BASE_URL = os.environ.get("BASE_URL","http://localhost:5000/asset/")
OUT_DIR = Path(__file__).resolve().parent / "qrs"
OUT_DIR.mkdir(exist_ok=True)

print(f"🔗 QR Base URL: {BASE_URL}")  

# Simple CSV sample describing assets (id, tag, name)
assets = [
    ("asset-1","KOE-001","Lenovo Laptop"),
    ("asset-2","KOE-002","iPhone 12"),
    ("asset-3","KOE-003","Logitech Mouse"),
    ("asset-4","KOE-004","Dell Monitor"),
    ("asset-5","KOE-005","HP Keyboard"),
]

for aid, tag, name in assets:
    url = BASE_URL + aid
    img = qrcode.make(url)
    fname = OUT_DIR / f"{tag}.png"
    img.save(fname)
    print(f"✅ {tag}.png → {url}")  # ← More detailed