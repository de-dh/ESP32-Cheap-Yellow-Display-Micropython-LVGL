from PIL import Image
import os
import sys


def read_metadata(meta_file):
    """
    Liest eine Metadatendatei im Format
        width=320
        height=480
        cf=RGB565
        size=307200
    ein und gibt ein Dictionary zurück.
    """
    meta = {}

    with open(meta_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or "=" not in line:
                continue
            key, value = line.split("=", 1)
            meta[key.strip()] = value.strip()

    return meta



def rgb565_raw_to_png(raw_file, out_file=None, meta_file=None):
    """
    Wandelt eine RAW-Datei im RGB565-Format anhand einer zugehörigen
    Metadatendatei in ein PNG-Bild um.

    Erwartete Metadatei (Standard): <raw_file>.txt
    Beispiel:
        screen.raw
        screen.raw.txt

    Parameter:
        raw_file  : Pfad zur .raw-Datei
        out_file  : Pfad zur auszugebenden PNG-Datei (optional)
        meta_file : Pfad zur Metadatendatei (optional)
    """
    if meta_file is None:
        meta_file = raw_file + ".txt"

    if out_file is None:
        base, _ = os.path.splitext(raw_file)
        out_file = base + ".png"

    if not os.path.exists(raw_file):
        raise FileNotFoundError(f"RAW-Datei nicht gefunden: {raw_file}")

    if not os.path.exists(meta_file):
        raise FileNotFoundError(f"Metadatendatei nicht gefunden: {meta_file}")

    meta = read_metadata(meta_file)

    try:
        width = int(meta["width"])
        height = int(meta["height"])
        color_format = meta["cf"]
        expected_size = int(meta["size"])
    except KeyError as e:
        raise ValueError(f"Fehlender Metadaten-Eintrag: {e}")

    if color_format.upper() != "RGB565":
        raise ValueError(
            f"Nicht unterstütztes Farbformat: {color_format}. "
            "Dieses Skript unterstützt derzeit nur RGB565."
        )

    with open(raw_file, "rb") as f:
        data = f.read()

    if len(data) != expected_size:
        raise ValueError(
            f"Dateigröße passt nicht zu den Metadaten: "
            f"erwartet {expected_size} Bytes, erhalten {len(data)} Bytes"
        )

    if len(data) != width * height * 2:
        raise ValueError(
            f"Breite/Höhe und Größe passen nicht zusammen: "
            f"width*height*2 = {width * height * 2}, size = {len(data)}"
        )

    img = Image.new("RGB", (width, height))
    pixels = []

    for i in range(0, len(data), 2):
        pixel = data[i] | (data[i + 1] << 8)

        r = (pixel >> 11) & 0x1F
        g = (pixel >> 5) & 0x3F
        b = pixel & 0x1F

        # Auf 8 Bit pro Farbkanal skalieren
        r = (r * 255) // 31
        g = (g * 255) // 63
        b = (b * 255) // 31

        pixels.append((r, g, b))

    img.putdata(pixels)
    img.save(out_file)
    return out_file


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Verwendung:")
        print("  python raw_to_png.py <datei.raw> [<datei.raw.txt>] [<ausgabe.png>]")
        print("")
        print("Beispiel:")
        print("  python raw_to_png.py screen.raw")
        print("  python raw_to_png.py screen.raw screen.raw.txt")
        print("  python raw_to_png.py screen.raw screen.raw.txt screen.png")
        sys.exit(1)

    raw_file = sys.argv[1]
    meta_file = sys.argv[2] if len(sys.argv) >= 3 else None
    out_file = sys.argv[3] if len(sys.argv) >= 4 else None

    try:
        out = rgb565_raw_to_png(raw_file, out_file=out_file, meta_file=meta_file)
        print(f"PNG gespeichert: {out}")
    except Exception as e:
        print(f"Fehler: {e}")
        sys.exit(1)
