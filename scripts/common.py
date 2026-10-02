"""Shared helpers: turn the relative split lists into absolute lists + an Ultralytics data YAML."""
import os

NAMES = {0: "D00", 1: "D10", 2: "D20", 3: "D40"}
PREFIX = {"baseline": "_Baseline_India", "balanced": "_Balanced_India"}


def absolute_list(src, dst, root):
    with open(src) as f:
        lines = [l.strip() for l in f if l.strip()]
    # entries may be relative (India/train/images/x.jpg) or absolute Kaggle paths; keep the part from "India/"
    paths = [os.path.join(root, l[l.index("India/"):] if "India/" in l else l) for l in lines]
    missing = [p for p in paths[:50] if not os.path.exists(p)]
    if missing:
        raise FileNotFoundError(f"Images not found under --root, e.g. {missing[0]}")
    with open(dst, "w") as f:
        f.write("\n".join(paths))
    return dst, len(paths)


def write_yaml(root, splits_dir, lists, train_split, val_split, work_dir, yaml_name):
    """lists: 'baseline' | 'balanced'. train_split/val_split: 'train' | 'val' | 'test'."""
    os.makedirs(work_dir, exist_ok=True)
    pre = PREFIX[lists]
    out = {}
    for key, split in (("train", train_split), ("val", val_split)):
        src = os.path.join(splits_dir, f"{pre}_{split}.txt")
        dst = os.path.join(work_dir, f"{lists}_{split}_abs.txt")
        out[key], n = absolute_list(src, dst, root)
        print(f"{key}: {split} list, {n} images")
    names = "\n".join(f"  {k}: {v}" for k, v in NAMES.items())
    yaml_path = os.path.join(work_dir, yaml_name)
    with open(yaml_path, "w") as f:
        f.write(f"path: /\ntrain: {out['train']}\nval: {out['val']}\n\nnames:\n{names}\n")
    return yaml_path
