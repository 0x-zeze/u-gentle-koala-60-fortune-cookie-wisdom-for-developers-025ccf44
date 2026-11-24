# Varian Fortune Cookie Wisdom for Developers

Semua varian memakai struktur 3 ketukan: **(1)** setup dengan alat/artefak konkret dunia developer, **(2)** eskalasi, **(3)** punchline berupa *category error* / pembalikan dengan hantaman di kata terakhir.

---

## Varian 1
> `Your test suite will mock the database, stub the clock, and quietly draft your alibi.` (85 karakter)

- **Ketukan 1 (Setup):** `Your test suite will mock the database,` — alat konkret (`test suite`, `mock`) pada aktivitas harian penulisan tes.
- **Ketukan 2 (Eskalasi):** `stub the clock,` — eskalasi dari memalsukan penyimpanan ke memalsukan waktu itu sendiri.
- **Ketukan 3 (Punchline):** `and quietly draft your alibi.` — *category error* (pengujian perangkat lunak → pembelaan hukum); punch di kata terakhir `alibi`.
- **Kriteria Judge:**
  1. *Fortune cookie asli:* Ya, bernada ramalan tenang khas fortune cookie, bukan nasihat atau slogan.
  2. *Satu tarikan napas:* Seimbang dan mengalir, meski ada satu adverbia (`quietly`).
  3. *Kebenaran hari developer:* Sangat nyata—tes penuh mock lolos di CI tetapi gagal menjaga produksi.
  4. *Putaran orisinal:* Segar, bebas klise/pepatah lama.
  5. *Twist bacaan kedua:* `alibi` berarti alasan saat postmortem ("tesnya hijau semua!") sekaligus makna literalnya ("berada di tempat lain"—tes membuktikan kode berjalan di dunia palsu, bukan di produksi).

---

## Varian 2 (PEMENANG)
> `Your next LGTM will clear the queue, unblock the release, and transfer custody.` (79 karakter)

- **Ketukan 1 (Setup):** `Your next LGTM will clear the queue,` — artefak konkret review kode (`LGTM`, antrean PR) dengan nada positif seolah keberuntungan biasa.
- **Ketukan 2 (Eskalasi):** `unblock the release,` — eskalasi dampak dari kotak masuk pribadi ke peluncuran produksi.
- **Ketukan 3 (Punchline):** `and transfer custody.` — pembalikan total dan *category error* (persetujuan review → hukum perwalian/penahanan); punch tepat di kata terakhir `custody`.
- **Kriteria Judge:**
  1. *Fortune cookie asli:* Paling kuat; pembuka `Your next...` persis seperti ramalan kertas fortune cookie, tanpa menggurui atau berlagak slogan.
  2. *Satu tarikan napas:* 13 kata, 79 karakter, nol kata pengisi. Pola paralel `clear the queue` / `unblock the release` lalu dipatahkan secara ritmis oleh `transfer custody`.
  3. *Kebenaran hari developer:* Sangat dekat dengan realitas *tired senior engineer*—menyetujui PR demi mengosongkan antrean dan melancarkan rilis, lalu berakhir menanggung bug-nya.
  4. *Putaran orisinal:* Tidak mengulang klise review (seperti "10 baris banyak komentar, 500 baris LGTM"), melainkan membingkai `LGTM` sebagai serah-terima hak asuh.
  5. *Twist bacaan kedua:* Dua lapis langsung terasa tanpa perlu referensi obscure: (a) pembalikan makna `transfer`—niatnya melepas beban dari antrean, nyatanya justru menerima beban permanen dari penulis asli; (b) makna ganda `custody`—*hak asuh* (merawat kode orang lain seumur hidupnya) sekaligus *tahanan* (ikut bertanggung jawab penuh saat rilis pecah).

---

## Varian 3
> `Your git rebase will tidy the branch, squash the panic, and commit perjury.` (75 karakter)

- **Ketukan 1 (Setup):** `Your git rebase will tidy the branch,` — alat konkret (`git rebase`) dalam rutinitas merapikan PR.
- **Ketukan 2 (Eskalasi):** `squash the panic,` — memakai kata kerja git nyata (`squash`) untuk eskalasi dari kerapian teknis ke penghapusan jejak kepanikan debugging.
- **Ketukan 3 (Punchline):** `and commit perjury.` — *category error* (operasi git → sumpah palsu di pengadilan); punch di kata terakhir `perjury` dengan permainan kata `commit`.
- **Kriteria Judge:**
  1. *Fortune cookie asli:* Cukup baik, namun permainan kata `commit perjury` sedikit lebih condong ke *one-liner* jenaka daripada nada orakular fortune cookie.
  2. *Satu tarikan napas:* Sangat ringkas dan tajam (75 karakter).
  3. *Kebenaran hari developer:* Benar tentang riwayat git linear yang dipoles agar terlihat selalu tahu arah sejak awal.
  4. *Putaran orisinal:* Segar, menghindari klise `git blame`.
  5. *Twist bacaan kedua:* `commit` bermakna ganda (`git commit` + melakukan pelanggaran) sambil menyindir hilangnya konteks sejati bagi maintainer berikutnya.

---

## Varian 4
> `Your sprint estimate will size the ticket, pad the risk, and measure your amnesia.` (82 karakter)

- **Ketukan 1 (Setup):** `Your sprint estimate will size the ticket,` — artefak konkret estimasi sprint dan tiket.
- **Ketukan 2 (Eskalasi):** `pad the risk,` — eskalasi ke kebiasaan senior engineer menambahkan buffer demi keamanan.
- **Ketukan 3 (Punchline):** `and measure your amnesia.` — *category error* (mengukur usaha kerja → mengukur lupa ingatan); punch di kata terakhir `amnesia`.
- **Kriteria Judge:**
  1. *Fortune cookie asli:* Sangat baik, tenang, dan aporistik.
  2. *Satu tarikan napas:* 14 kata, 82 karakter, ritme seimbang tanpa kata pengisi.
  3. *Kebenaran hari developer:* Sangat tepat untuk keseharian estimasi sprint.
  4. *Putaran orisinal:* Menghindari klise "estimasi berubah jadi deadline".
  5. *Twist bacaan kedua:* Buffer risiko yang dikira buah pengalaman ternyata hanya bukti bahwa kita sudah cukup lupa betapa kacaunya modul lama itu. Makna ganda pada kata terakhirnya tidak sekuat Varian 2 karena `amnesia` bermakna tunggal.

---

## Varian 5
> `Your /healthz endpoint will return 200, keep the pager quiet, and work purely as a placebo.` (91 karakter)

- **Ketukan 1 (Setup):** `Your /healthz endpoint will return 200,` — alat konkret produksi (`/healthz`, status HTTP 200).
- **Ketukan 2 (Eskalasi):** `keep the pager quiet,` — eskalasi dari respons HTTP ke membungkam alarm on-call.
- **Ketukan 3 (Punchline):** `and work purely as a placebo.` — *category error* (liveness probe → obat kosong medis); punch di kata terakhir `placebo`.
- **Kriteria Judge:**
  1. *Fortune cookie asli:* Baik, tetapi sedikit lebih teknis/deskriptif dibanding nada ramalan Varian 2.
  2. *Satu tarikan napas:* Terpanjang di antara kelima varian (91 karakter) dan memakai adverbia `purely`.
  3. *Kebenaran hari developer:* Nyata tentang health check dangkal yang tetap hijau saat sistem sebenarnya sekarat.
  4. *Putaran orisinal:* Metafora `placebo` segar dan tidak klise.
  5. *Twist bacaan kedua:* Placebo hanya menenangkan kecemasan operator tanpa menyembuhkan penyakit di produksi.

---

## Pemenang: Varian 2

> **`Your next LGTM will clear the queue, unblock the release, and transfer custody.`** (79 karakter)

**Alasan memilih Varian 2:**
1. **Paling otentik sebagai fortune cookie (Kriteria #1):** Frasa `Your next...` mendarat tepat seperti ramalan pendek di dalam kue keberuntungan—tanpa menggurui, tanpa berbunyi seperti slogan atau lelucon panggung.
2. **Paling tak terduga di ketukan ketiga:** Ketukan 1 dan 2 sengaja terdengar 100% positif dan produktif (tidak membocorkan punchline dengan kata sifat seperti "hasty"), sehingga pembalikan `transfer custody` menghantam keras di kata terakhir.
3. **Ekonomi kata terbaik (Kriteria #2):** 79 karakter, nol adverbia pengisi, dan pematahan ritme (`the queue` → `the release` → `custody`) mengunci mendaratnya kalimat dalam satu tarikan napas.
4. **Makna ganda paling dalam pada bacaan kedua (Kriteria #5):** `custody` bekerja secara alami di dua register sekaligus—hak asuh (merawat kode orang lain setelah disetujui) dan penahanan/tanggung jawab (ikut ditahan saat rilis bermasalah)—diperkuat oleh ironi kata `transfer` saat niat awalnya justru mengosongkan antrean.

---

## Revisi

- **Baris lama:** `Your next LGTM will clear the queue, unblock the release, and transfer custody.` (79 karakter)
- **Baris baru:** `Your next LGTM will clear the queue, free the author, and transfer custody.` (75 karakter)
- **Kelemahan yang ditemukan:** Ketukan kedua (`unblock the release`) memakai jargon manajemen rilis yang generik dan berdiri di domain terpisah dari `transfer custody`, sehingga tidak menjelaskan secara implisit *dari siapa* hak asuh berpindah dan membuat eskalasi tengah terasa datar.
- **Alasan perubahan:** Mengganti `unblock the release` menjadi `free the author` memberi tiga perbaikan sekaligus dalam satu edit konkret: (1) memadatkan kalimat dari 79 menjadi 75 karakter dengan ritme simetris (`clear the queue` / `free the author`, masing-masing 4 suku kata); (2) tetap terdengar wajar dan positif pada bacaan pertama tanpa membocorkan punchline; (3) mengunci twist bacaan kedua—menyetujui PR benar-benar *membebaskan* penulisnya sementara `custody` (hak asuh pemeliharaan sekaligus tanggung jawab hukum/on-call) berpindah ke reviewer.
