// Path ke file JSON archive
const jsonFile = "./media.json";

// Fungsi untuk load dan render data
fetch(jsonFile)
  .then((response) => response.json())
  .then((data) => {
    const gallery = document.getElementById("gallery");
    data.forEach((item) => {
      // Buat card untuk setiap media
      const card = document.createElement("div");
      card.className = "card";

      // Buat embed iframe untuk media
      const iframe = document.createElement("iframe");
      iframe.src = `${item.media_url}embed`;
      iframe.width = "100%";
      iframe.height = "400px";
      iframe.style.border = "none";
      iframe.allow = "encrypted-media";

      // Tambahkan caption
      const caption = document.createElement("div");
      caption.className = "caption";
      caption.textContent = item.caption || "No caption";

      // Gabungkan elemen ke card
      card.appendChild(iframe);
      card.appendChild(caption);

      // Tambahkan card ke gallery
      gallery.appendChild(card);
    });
  })
  .catch((error) => console.error("Error loading JSON:", error));
