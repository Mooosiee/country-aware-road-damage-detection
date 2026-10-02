"""
Train one experiment on the India subset (hyperparameters recovered from the saved checkpoints
and the balanced Kaggle notebook).

    python scripts/train.py --exp baseline         --lists baseline --root /data/RDD2022
    python scripts/train.py --exp balanced         --lists balanced --root /data/RDD2022
    python scripts/train.py --exp architecture_mod --lists balanced --root /data/RDD2022 \
                            --model configs/yolo11s_p2.yaml

--root is the folder that CONTAINS India/ (list entries look like India/train/images/xxx.jpg).
"""
import argparse
from ultralytics import YOLO
from common import write_yaml

p = argparse.ArgumentParser()
p.add_argument("--exp", required=True, choices=["baseline", "balanced", "architecture_mod"])
p.add_argument("--lists", required=True, choices=["baseline", "balanced"],
               help="which split lists to train/validate on")
p.add_argument("--root", required=True)
p.add_argument("--splits-dir", default="splits")
p.add_argument("--model", default="yolo11s.pt")
p.add_argument("--init-weights", default=None, help="optional yolo11s.pt transfer into a custom-YAML model")
p.add_argument("--work-dir", default="work")
p.add_argument("--device", default="0")
a = p.parse_args()

data = write_yaml(a.root, a.splits_dir, a.lists, "train", "val", a.work_dir, f"data_{a.exp}.yaml")

model = YOLO(a.model)
if a.init_weights:
    model = model.load(a.init_weights)

model.train(
    data=data,
    epochs=150, imgsz=640, batch=32,
    optimizer="SGD", lr0=0.01, momentum=0.937, weight_decay=0.0005,
    warmup_epochs=3, warmup_momentum=0.8,
    patience=50, seed=0,
    val=True, save=True, save_period=5,
    device=a.device,
    project="runs", name=a.exp, exist_ok=True,
)
