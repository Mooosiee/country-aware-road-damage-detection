Split lists for the India subset (70/20/10), one path per line, relative to the RDD2022 root (the folder containing `India/`).

- `_Balanced_India_{train,val,test}.txt`: train 5842 (5394 original + 448 augmented `aug_India_D10_*`), val 1541, test 771.
  Provided by the author (originally absolute Kaggle paths, rewritten to relative).
- `_Baseline_India_{train,val,test}.txt`: DERIVED, not the original files. Train = balanced train minus the 448 augmented images
  (5394); val/test identical to the balanced ones. Replace with the original baseline lists if you still have them.

The augmented images must exist at `India/train/images/aug_India_D10_*.jpg` under the root.
