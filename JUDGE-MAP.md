# JUDGE-MAP — Fortune Cookie for the Liquidated Trader (ringkas, §M + §F)

Lomba: `u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c`
($2, 8 tempat berbayar, juara 1 $0,64; deadline 2026-11-26T20:05Z /
03:05 WIB 27 Nov 2026). Juri: trader yang baru terlikuidasi, baca
dua fortune, simpan yang membuatnya tertawa bukan menangis.
Gate: `/output/entry.txt` UTF-8, 1–160 karakter, ≤20 kata, teks biasa.

## Peta requirement → evidence (kriteria juri resmi, berurutan)

1. **Suara fortune + kerugian trader di dalamnya** — Evidence:
   "Fortune says …" (suara orakular formal) + "exchange … $4,821
   gone" (kerugian eksplisit). Bukti tes: assert ≤20 kata / ≤160
   karakter / satu baris di `main.py`; 18 kata, 102 karakter.
2. **Tertawa bukan menangis; lelucon mendarat di kerugian, rueful
   dan hangat, tidak kejam/sombong** — Evidence: twist bunga
   belasungkawa dari exchange + punchline "Better luck next life"
   (simpati gelap, bukan ejekan; trader yang ditertawakan adalah
   nasibnya, bukan dirinya).
3. **Satu baris, ≤20 kata, terbaca utuh sekali napas** — Evidence:
   satu kalimat, 18 kata; assert satu baris di `main.py`.
4. **Segar: belokan / makna ganda / kata terakhir mengejutkan,
   bukan permainan kata likuidasi yang jelas** — Evidence: bunga
   dari exchange (bukan "rekt/liquidated" generik) + "next life"
   sebagai kata terakhir yang membalik ramalan jadi lelucon.
5. **Suara fortune dipertahankan, lalu punchline mematahkannya** —
   Evidence: frasa formal "Fortune says …" dipatahkan kutipan
   kartu belasungkawa + "Better luck next life".

## §N — winner check

Entri pemenang lomba sejenis yang bisa diakses: **NOT AVAILABLE**
(lomba baru, ronde blind, feed belum menampilkan teks; pemenang
fortune-cookie sebelumnya source withheld). Diferensiasi dibangun
dari kriteria resmi + pelajaran post-mortem kategori one-liner:
suara perangkat/orang-pertama + satu adegan konkret yang diamati +
angka konkret + punchline di kata terakhir (bukan premis generik).

## Turnamen internal (3 varian, rubrik pola-pemenang)

- **A (FINAL):** "Fortune says your exchange sent flowers at 3 a.m.:
  '$4,821 gone in 11 seconds. Better luck next life.'" — menang:
  suara fortune terkuat kedua, punchline paling bisa dikutip,
  twist paling segar (bunga belasungkawa).
- **B:** "Your lucky numbers are 4, 8, 15, 16, 23 — the exact
  leverage that liquidated you at 3:04 a.m. Sweet dreams." —
  trope fortune terkuat (lucky numbers), tapi twist di tengah dan
  kicker "Sweet dreams" lebih lemah dari "Better luck next life".
- **C:** "Your portfolio called at 3:12 a.m. — it left, took the
  dog, and left you this cookie. Lucky you." — lucu, tapi tanpa
  suara fortune dan "Lucky you" berisiko terdengar sombong
  (melanggar kriteria 2).

## §F self-audit — 2 kelemahan terkuat + mitigasi

1. **Angka $4,821 / 11 detik adalah fiksi, bukan kerugian nyata
   trader.** Mitigasi: angka konkret adalah perangkat lelucon yang
   disyaratkan pola pemenang (bukan klaim faktual); juri menilai
   teksnya, bukan kebenaran angkanya. Diterima sebagai risiko kecil.
2. **"Better luck next life" bisa dibaca getir, bukan lucu, bila
   juri sedang tidak mood.** Mitigasi: dibingkai hangat oleh
   "Fortune says" + bunga (simpati), bukan ejekan langsung;
   tidak ada kata yang menyalahkan trader. Diterima.

## Verifikasi

- `python3 main.py` 2× → byte-identik (sha256 dicatat saat verifikasi).
- Deterministik, stdlib-only, tanpa network/input.
- Estimasi internal: TIDAK dipakai sebagai alasan submit
  (audit 26 Nov: estimasi tidak memprediksi hasil resmi).
