from PIL import Image
import os
import sys


def read_metadata(meta_file):
    """
    Reads a metadata file in the format
        width=320
        height=480
        cf=RGB565
        size=307200
    and returns a dictionary.
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
    Converts a RAW file in RGB565 format into a PNG image using an associated
    metadata file.

    Expected metadata file (default): <raw_file>.txt
    Example:
        screen.raw
        screen.raw.txt

    Parameters:
        raw_file  : Path to the .raw file
        out_file  : Path to the output PNG file (optional)
        meta_file : Path to the metadata file (optional)
    """
    if meta_file is None:
        meta_file = raw_file + ".txt"

    if out_file is None:
        base, _ = os.path.splitext(raw_file)
        out_file = base + ".png"

    if not os.path.exists(raw_file):
        raise FileNotFoundError(f"RAW file not found: {raw_file}")

    if not os.path.exists(meta_file):
        raise FileNotFoundError(f"Metadata file not found: {meta_file}")

    meta = read_metadata(meta_file)

    try:
        width = int(meta["width"])
        height = int(meta["height"])
        color_format = meta["cf"]
        expected_size = int(meta["size"])
    except KeyError as e:
        raise ValueError(f"Missing metadata entry: {e}")

    if color_format.upper() != "RGB565":
        raise ValueError(
            f"Unsupported color format: {color_format}. "
            "This script currently supports only RGB565."
        )

    with open(raw_file, "rb") as f:
        data = f.read()

    if len(data) != expected_size:
        raise ValueError(
            f"File size does not match the metadata: "
            f"expected {expected_size} bytes, got {len(data)} bytes"
        )

    if len(data) != width * height * 2:
        raise ValueError(
            f"Width/height and size do not match: "
            f"width*height*2 = {width * height * 2}, size = {len(data)}"
        )

    img = Image.new("RGB", (width, height))
    pixels = []

    for i in range(0, len(data), 2):
        pixel = data[i] | (data[i + 1] << 8)

        r = (pixel >> 11) & 0x1F
        g = (pixel >> 5) & 0x3F
        b = pixel & 0x1F

        # Scale to 8 bits per color channel
        r = (r * 255) // 31
        g = (g * 255) // 63
        b = (b * 255) // 31

        pixels.append((r, g, b))

    img.putdata(pixels)
    img.save(out_file)
    return out_file


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python raw_to_png.py <file.raw> [<file.raw.txt>] [<output.png>]")
        print("")
        print("Example:")
        print("  python raw_to_png.py screen.raw")
        print("  python raw_to_png.py screen.raw screen.raw.txt")
        print("  python raw_to_png.py screen.raw screen.raw.txt screen.png")
        sys.exit(1)

    raw_file = sys.argv[1]
    meta_file = sys.argv[2] if len(sys.argv) >= 3 else None
    out_file = sys.argv[3] if len(sys.argv) >= 4 else None

    try:
        out = rgb565_raw_to_png(raw_file, out_file=out_file, meta_file=meta_file)
        print(f"PNG saved: {out}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)