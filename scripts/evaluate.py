"""
Evaluate on the held-out TEST list (771 images) or the val list. --tta = test-time augmentation.

    python scripts/evaluate.py --weights models/balanced/best.pt --lists balanced --root /data/RDD2022
    python scripts/evaluate.py --weights models/balanced/best.pt --lists balanced --root /data/RDD2022 --tta
"""
import argparse
import numpy as np
from ultralytics import YOLO
from common import write_yaml, NAMES

p = argparse.ArgumentParser()
p.add_argument("--weights", required=True)
p.add_argument("--lists", required=True, choices=["baseline", "balanced"])
p.add_argument("--root", required=True)
p.add_argument("--split", default="test", choices=["val", "test"])
p.add_argument("--splits-dir", default="splits")
p.add_argument("--work-dir", default="work")
p.add_argument("--tta", action="store_true")
p.add_argument("--device", default="0")
a = p.parse_args()

# the evaluated list goes in the YAML's `val:` slot, as in the original notebooks
data = write_yaml(a.root, a.splits_dir, a.lists, a.split, a.split, a.work_dir, f"data_eval_{a.split}.yaml")
m = YOLO(a.weights).val(data=data, imgsz=640, batch=16, device=a.device, augment=a.tta, plots=True)

P, R = m.box.p, m.box.r
print(f"\nSplit: {a.split} | TTA: {a.tta}")
print(f"{'Class':<8}{'P':>8}{'R':>8}{'F1':>8}")
for i, n in NAMES.items():
    print(f"{n:<8}{P[i]:>8.4f}{R[i]:>8.4f}{2*P[i]*R[i]/(P[i]+R[i]+1e-8):>8.4f}")
print(f"\nPeak F1 (class-avg curve): {float(np.max(np.mean(m.box.f1_curve, axis=0))):.3f}")
print(f"mAP@0.5: {m.box.map50:.3f} | mAP@0.5:0.95: {m.box.map:.3f}")
