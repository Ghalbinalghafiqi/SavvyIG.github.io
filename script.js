// Path ke file JSON archive
const jsonFile = "./downloaded_media.json";

// Fungsi untuk load dan render data
fetch(jsonFile)
  .then((response) => response.json())
  .then((data) => {
    const gallery = document.getElementById("gallery");
    data.forEach((item) => {
      // Buat card untuk setiap media
      const card = document.createElement("div");
      card.className = "card";

      // Periksa apakah ada file media di dalam item
      item.downloaded_files.forEach((file) => {
        const fileExtension = file.split('.').pop().toLowerCase();

        let mediaElement;

        // Jika file adalah gambar (jpg, jpeg, png, gif)
        if (['jpg', 'jpeg', 'png', 'gif'].includes(fileExtension)) {
          mediaElement = document.createElement("img");
          mediaElement.src = file;
          mediaElement.alt = "Image";
          mediaElement.style.width = "100%";
        }
        // Jika file adalah video (mp4, webm)
        else if (['mp4', 'webm'].includes(fileExtension)) {
          mediaElement = document.createElement("video");
          mediaElement.src = file;
          mediaElement.controls = true;
          mediaElement.style.width = "100%";
        }

        // Jika ada elemen media, tambahkan ke dalam card
        if (mediaElement) {
          card.appendChild(mediaElement);
        }
      });

      // Tambahkan caption
      // const caption = document.createElement("div");
      // caption.className = "caption";
      // caption.textContent = item.caption || "No caption";

      // // Gabungkan elemen ke card
      // card.appendChild(caption);

      // Tambahkan card ke gallery
      gallery.appendChild(card);
    });
  })
  .catch((error) => console.error("Error loading JSON:", error));