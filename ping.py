import requests
import time

# VPS URL
vps_url = "https://idx.google.com/24x7-63926321"  # yahan apna VPS link daalo

# Ping interval (seconds)
interval = 300  # har 5 minute ping karega

while True:
    try:
        response = requests.get(vps_url)
        if response.status_code == 200:
            print(f"✅ VPS is alive at {time.ctime()}")
        else:
            print(f"⚠️ VPS returned status {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    time.sleep(interval)
