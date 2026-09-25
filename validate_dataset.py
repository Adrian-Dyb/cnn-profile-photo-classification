from pathlib import Path
from collections import Counter
import sys

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/content/drive/MyDrive/dataset_cv")
TRAIN = ROOT / "train"
TEST = ROOT / "test"
IMG_EXT = {".jpg",".jpeg",".png",".webp",".bmp",".tif",".tiff",".jfif"}

def infer_domain(path: Path):
    parts = {x.lower() for x in path.parts}
    name = path.name.lower()
    if "real" in parts or "_real_" in name or name.startswith("real_"):
        return "real"
    if "synthetic" in parts or "synth" in parts or "_synthetic_" in name or "_synth_" in name:
        return "synthetic"
    return "unknown"

def class_counts(split):
    out = {}
    for d in sorted(p for p in split.iterdir() if p.is_dir()):
        out[d.name] = sum(1 for p in d.rglob("*") if p.is_file() and p.suffix.lower() in IMG_EXT)
    return out

if not TRAIN.exists() or not TEST.exists():
    raise SystemExit(f"Missing train/test under: {ROOT}")

train_counts = class_counts(TRAIN)
test_counts = class_counts(TEST)

train_files = [p for p in TRAIN.rglob("*") if p.is_file() and p.suffix.lower() in IMG_EXT]
test_files = [p for p in TEST.rglob("*") if p.is_file() and p.suffix.lower() in IMG_EXT]

domains = Counter(infer_domain(p) for p in train_files)

print("Dataset root:", ROOT)
print("Train per class:", train_counts)
print("Train total:", len(train_files))
print("Train domains:", domains)
print("Test per class:", test_counts)
print("Test total:", len(test_files))

warnings = []
if len(train_files) != 200:
    warnings.append(f"Expected 200 training images, found {len(train_files)}.")
if len(test_files) != 20:
    warnings.append(f"Expected 20 test images, found {len(test_files)}.")
if any(v != 4 for v in test_counts.values()) or len(test_counts) != 5:
    warnings.append("Expected exactly 5 test classes with 4 images each.")
if domains["unknown"]:
    warnings.append(f"{domains['unknown']} training images have unknown domain labels.")
if domains["synthetic"] and domains["real"] and (domains["synthetic"] + domains["real"] != 200):
    warnings.append("Recognized real + synthetic counts do not sum to 200.")

if warnings:
    print("\nWARNINGS:")
    for w in warnings:
        print("-", w)
else:
    print("\nDataset structure matches the project requirements.")
