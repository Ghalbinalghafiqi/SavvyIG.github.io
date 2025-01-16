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
        dict: Informasi tentang file yang di-download.
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
        
        # Mengembalikan informasi post yang telah didownload
        downloaded_files = [os.path.join(target_directory, file) for file in os.listdir(target_directory)]
        return {"url": url, "downloaded_files": downloaded_files}
    except Exception as e:
        print(f"Error: {e}")
        print("Pastikan URL valid atau akun tidak private.")
        return None

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

def save_downloaded_files_to_json(downloaded_data, output_file="downloaded_media.json"):
    """
    Simpan informasi tentang file yang telah didownload ke file JSON.

    Args:
        downloaded_data (list): Daftar informasi file yang telah didownload.
        output_file (str): Nama file output JSON.
    
    Returns:
        None
    """
    try:
        with open(output_file, "w") as file:
            json.dump(downloaded_data, file, indent=4)
        print(f"Informasi file yang didownload telah disimpan di {output_file}")
    except Exception as e:
        print(f"Error menyimpan file JSON: {e}")

if __name__ == "__main__":
    # Path ke file media.json
    json_file_path = "media.json"
    
    # Folder dasar tempat penyimpanan semua post
    base_download_directory = "img"
    os.makedirs(base_download_directory, exist_ok=True)
    
    # Load URL dari media.json
    urls = load_media_urls(json_file_path)
    
    # Menyimpan data tentang file yang didownload
    downloaded_data = []

    if urls:
        print(f"Menemukan {len(urls)} URL untuk didownload.")
        for url in urls:
            print(f"Mendownload: {url}")
            result = download_instagram_post(url, base_directory=base_download_directory)
            if result:
                downloaded_data.append(result)
        
        # Simpan informasi file yang didownload ke dalam file JSON
        if downloaded_data:
            save_downloaded_files_to_json(downloaded_data)
    else:
        print("Tidak ada URL yang ditemukan dalam file media.json.")