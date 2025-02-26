import os
import shutil
import yt_dlp

# 🔧 Konfigurasi
USERNAME = "timothyronaldclip"  # Ganti dengan username TikTok yang diinginkan
MAX_VIDEOS = 2  # Jumlah maksimal video yang ingin diambil

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
    }

    with yt_dlp.YoutubeDL(ydl_opts_single) as ydl:
        ydl.download([video_url])

# 📦 Buat file ZIP dari semua video
zip_filename = "tiktok_videos.zip"
shutil.make_archive(zip_filename.replace(".zip", ""), 'zip', "videos")

print(f"📁 Semua video telah diarsipkan dalam: {zip_filename}")
print("🎉 Semua proses selesai! File ZIP siap diunduh.")
