# Image Processing & Computer Vision — CAPTCHA-Style Character Recognition

Classical OpenCV pipeline for CAPTCHA-like character recognition:
**preprocess → binarize (Otsu / Adaptive Gaussian) → morphology (3×3) → template match (with small rotation sweep).**

> This repo contains small, focused modules that demonstrate each stage and can be stitched into an end-to-end workflow.

---

## ✨ What this project shows (resume alignment)

- Built a **CAPTCHA recognition** workflow in OpenCV for efficient image processing and decoding tasks.
- Employed **Otsu** and **Adaptive Gaussian** thresholding to obtain clean binary masks under both uniform and locally varying illumination.
- Applied **morphological transforms** (erosion/dilation, open/close with a **3×3** kernel via `morphologyEx`) to remove specks and normalize stroke thickness.
- Used **template matching** (`matchTemplate`) with a **small angle sweep** to match rotated test glyphs to a reference alphabet.
- Included a **synthetic dot-matrix digit generator** to create quick, controlled test images for pipeline tuning.

---

## 🧱 Repository structure

- `preprocess.py` — grayscale + (optional) histogram leveling/CLAHE hooks to stabilize contrast before thresholding.
- `thresholding.py` — Otsu and Adaptive Gaussian thresholding utilities with sensible defaults.
- `augmentation.py` — lightweight image tweaks (flips, simple geometric/photometric changes) for robustness checks.
- `synthesize_dot_digits.py` — produces a small set of dot-matrix digits (0–9) to sanity-check the pipeline.

> Optional future modules (mentioned in the write-up, add when ready):
> - `morphology.py` — wrappers around `cv2.morphologyEx` for 3×3 open/close/erode/dilate.
> - `template_match.py` — normalized cross-correlation matching with angle sweep and top-k reporting.

---

## 🔄 Pipeline overview

1. **Preprocessing**
   - Convert to grayscale and stabilize local contrast (optional CLAHE).
   - Goal: make foreground–background separation easier and less sensitive to lighting.

2. **Thresholding**
   - **Otsu** for globally consistent backgrounds.
   - **Adaptive Gaussian** when there are shadows/gutters; preserves thin strokes.
   - Output: clean binary mask of characters.

3. **Morphology (3×3)**
   - **Open/Close** to remove isolated noise and bridge small gaps.
   - **Erode/Dilate** to normalize stroke thickness across characters.

4. **Template Matching**
   - `matchTemplate` with normalized cross-correlation.
   - Evaluate a **small rotation range** (e.g., −15°…+15°) to handle skew.
   - Return top candidates with simple thresholding on correlation scores.

5. **Synthetic Data (optional but handy)**
   - Generate dot-matrix digits to quickly validate each stage before moving to noisy, real-world images.

---

## 📏 Evaluation mindset

- Visual checks at each stage (mask quality, morphology effect).
- Correlation scores from template matching used as a basic confidence signal.
- Sanity tests on synthetic digits first; then on real/scan images with varied lighting and rotation.

---

## 🧠 Design choices (brief)

- **Keep it classical:** deterministic, easy to reason about, fast on CPU.
- **Two thresholding strategies:** switch based on background variability.
- **Small kernels (3×3):** avoid over-smoothing strokes; retain character shape.
- **Angle sweep:** pragmatic fix for skew without full keypoint matching.

---

## ⚠️ Limitations

- Sensitive to heavy perspective distortion, complex backgrounds, and severe occlusions.
- Template matching requires a good reference alphabet; performance drops if fonts differ substantially.
- For production-grade robustness, consider feature-based matching or a small CNN for glyph classification.

---

## 📚 Acknowledgments

- Uses **OpenCV** for all image operations.
- The dot-digit idea is included to support quick iteration and debugging of the classical pipeline.

---
