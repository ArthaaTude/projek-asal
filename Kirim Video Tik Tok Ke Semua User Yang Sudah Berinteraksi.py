import os
import shutil
import yt_dlp
import requests

# 🔧 Konfigurasi
USERNAME = "timothyronaldclip"  # Ganti dengan username TikTok yang diinginkan
MAX_VIDEOS = 1  # Jumlah maksimal video yang ingin diambil
BOT_TOKEN = "7964693110:AAEKBCfQfVSsKkA_ScmijTvRlsxpw3ZGek0"  # Ganti dengan token bot Telegrammu

# 📂 Buat folder penyimpanan
os.makedirs("videos", exist_ok=True)

# 🎬 Ambil daftar video
URL = f"https://www.tiktok.com/@{USERNAME}"

ydl_opts = {
    "quiet": False,  # Tampilkan proses di terminal
    "extract_flat": True,  # Ambil daftar video tanpa download langsung
}

print(f"🔍 Mencari video dari @{USERNAME}...")

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(URL, download=False)  # Hanya ambil info video

# Ambil URL semua video yang ditemukan
video_urls = [entry["url"] for entry in info.get("entries", [])]
total_videos = len(video_urls)

# 🔎 Cek apakah jumlah video lebih sedikit dari yang diminta
if total_videos < MAX_VIDEOS:
    print(f"⚠️ Hanya ditemukan {total_videos} video (dari {MAX_VIDEOS} yang diminta).")
    confirm = input("❓ Apakah ingin melanjutkan download? (y/n): ").strip().lower()
    if confirm != "y":
        print("❌ Download dibatalkan.")
        exit()

# Batasi jumlah video yang akan di-download
video_urls = video_urls[:MAX_VIDEOS]

# 🎬 Download video satu per satu
print(f"📥 Mengunduh {len(video_urls)} video...")

for index, video_url in enumerate(video_urls):
    print(f"▶ Downloading video {index+1}/{len(video_urls)}: {video_url}")

    ydl_opts_single = {
        "outtmpl": f"videos/%(id)s.%(ext)s",  # Simpan ke folder videos
        "format": "bestvideo+bestaudio/best",  # Mengunduh video dan audio terbaik
        # Hapus bagian "postprocessors" untuk menonaktifkan konversi
    }

    with yt_dlp.YoutubeDL(ydl_opts_single) as ydl:
        ydl.download([video_url])

# 📦 Buat file ZIP dari semua video
zip_filename = "tiktok_videos.zip"
shutil.make_archive(zip_filename.replace(".zip", ""), 'zip', "videos")

# 🧹 Hapus semua video setelah kompresi
for video_file in os.listdir("videos"):
    video_path = os.path.join("videos", video_file)
    if os.path.isfile(video_path):
        os.remove(video_path)
        print(f"🗑️ Video {video_file} telah dihapus setelah dikompres.")

# 📨 Fungsi untuk mendapatkan semua chat_id yang berinteraksi dengan bot
def get_chat_ids():
    chat_ids = []
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    response = requests.get(url)
    if response.status_code == 200:
        updates = response.json()
        if updates["result"]:
            for update in updates["result"]:
                chat_id = update["message"]["chat"]["id"]
                if chat_id not in chat_ids:  # Pastikan chat_id unik
                    chat_ids.append(chat_id)
            print(f"Chat ID yang ditemukan: {chat_ids}")
        else:
            print("Tidak ada pembaruan yang ditemukan.")
    else:
        print(f"❌ Gagal mengambil updates. Status code: {response.status_code}")
    return chat_ids

# 📨 Kirim file ZIP ke semua pengguna yang telah berinteraksi dengan bot
def send_file_to_telegram(file_path, chat_ids):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    for chat_id in chat_ids:
        with open(file_path, "rb") as file:
            payload = {
                "chat_id": chat_id
            }
            files = {
                "document": file
            }
            response = requests.post(url, data=payload, files=files)
            if response.status_code == 200:
                print(f"✅ File berhasil dikirim ke chat_id {chat_id}")
            else:
                print(f"❌ Gagal mengirim file ke chat_id {chat_id}. Status code: {response.status_code}, Response: {response.text}")

# Ambil chat_ids yang sudah berinteraksi
chat_ids = get_chat_ids()

# Pastikan chat_ids ditemukan sebelum mengirim file
if chat_ids:
    # Mengirim file ZIP ke semua chat_id
    send_file_to_telegram(zip_filename, chat_ids)
    # 🧹 Hapus file ZIP setelah berhasil mengirim
    os.remove(zip_filename)  # Menghapus file ZIP dari PC
    print("🗑️ File ZIP berhasil dihapus dari PC!")
else:
    print("❌ Tidak ada chat_id ditemukan. File tidak dikirim.")
