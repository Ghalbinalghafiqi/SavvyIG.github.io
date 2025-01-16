import instaloader
import json
import os

def download_instagram_post(url, base_directory="."):
    """
    Download feed atau reels Instagram menggunakan URL.

    Args:
        url (str): URL dari postingan feed atau reels.
        base_directory (str): Folder dasar tempat semua folder post akan disimpan.

    Returns:
        None
    """
    loader = instaloader.Instaloader(download_videos=True, save_metadata=False)
    
    try:
        # Mengambil shortcode dari URL
        shortcode = url.split("/")[-2]
        target_directory = os.path.join(base_directory, f"instagram_{shortcode}")
        
        # Membuat folder khusus untuk setiap post jika belum ada
        os.makedirs(target_directory, exist_ok=True)
        
        # Mendownload post ke folder tersebut
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        loader.dirname_pattern = target_directory
        loader.download_post(post, target=target_directory)
        
        print(f"Postingan berhasil didownload di folder: {target_directory}")
    except Exception as e:
        print(f"Error: {e}")
        print("Pastikan URL valid atau akun tidak private.")

def load_media_urls(file_path):
    """
    Load URL dari file JSON.

    Args:
        file_path (str): Path ke file JSON yang berisi daftar URL.

    Returns:
        list: Daftar URL yang akan didownload.
    """
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return [item["media_url"] for item in data]
    except Exception as e:
        print(f"Error membaca file JSON: {e}")
        return []

if __name__ == "__main__":
    # Path ke file media.json
    json_file_path = "media.json"
    
    # Folder dasar tempat penyimpanan semua post
    base_download_directory = "img"
    os.makedirs(base_download_directory, exist_ok=True)
    
    # Load URL dari media.json
    urls = load_media_urls(json_file_path)
    
    if urls:
        print(f"Menemukan {len(urls)} URL untuk didownload.")
        for url in urls:
            print(f"Mendownload: {url}")
            download_instagram_post(url, base_directory=base_download_directory)
    else:
        print("Tidak ada URL yang ditemukan dalam file media.json.")