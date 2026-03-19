# Intelligent Architecture 🏠

A computer vision project that uses instance segmentation to analyse residential architectural floor plans and verify room compliance with Lithuanian construction regulations (STR 2.02.01:2004).

---

## About

This project trains a **YOLOv8 segmentation model** to detect, classify, and measure rooms in residential floor plans. Once rooms are identified and their areas calculated, the system checks them against minimum size requirements defined in Lithuanian building regulations.

### What it does

1. Takes a floor plan image as input
2. Segments and classifies each room (bedroom, kitchen, bathroom, living room, etc.)
3. Calculates room areas in square metres using a user-provided scale reference
4. Validates rooms against construction rulesets and reports passes, failures, and warnings

### Room classes detected

The model is trained to identify 14 room types:

- `space_bedroom`
- `space_kitchen`
- `space_living_room`
- `space_toilet`
- `space_bathroom`
- `space_balconi`
- `space_front`
- `space_dressroom`
- `space_staircase`
- `space_elevator`
- `space_elevator_hall`
- `space_outdoor_room`
- `space_multipurpose_space`
- `space_other`

### Construction rules checked

Based on **STR 2.02.01:2004 "Gyvenamieji pastatai"** (Lithuanian Residential Building Regulations):

| Rule | Minimum |
|---|---|
| Total habitable area per resident | 14 m² |
| Living room area | 16 m² |
| Kitchen area | 7 m² |
| Bathroom area | 2.89 m² |
| Bedroom area | 6.5 m² |
| Any room (minimum) | 4 m² |

---

## Installation

### Prerequisites

- Python 3.8+
- CUDA-compatible GPU recommended (NVIDIA GTX 1070 or better)
- PyTorch with CUDA support

### Steps

```bash
# Clone the repository
git clone https://github.com/LinaVysnia/Intelligent-Architecture.git
cd Intelligent-Architecture

# Install dependencies
pip install ultralytics opencv-python numpy
```

> **Note:** This project uses **PyTorch** with the Ultralytics YOLOv8 library. Make sure your PyTorch installation matches your CUDA version. See [PyTorch installation guide](https://pytorch.org/get-started/locally/).

---

## Configuration

### Image preprocessing options

The preprocessing pipeline accepts the following image formats: `.png`, `.jpg`, `.jpeg`, `.bmp`

Optional preprocessing flags can be set before running predictions:

| Option | Description |
|---|---|
| `desaturate` | Converts image to greyscale to match training data style |
| `adjust_contrast` | Enhances contrast to improve wall/room distinction |
| `threshold` | Forces a black-and-white binary image |

### Scale input

The area calculation requires a scale reference. You will be prompted to:

1. Specify a line length in **pixels** (e.g. a known wall on the plan)
2. Specify the corresponding real-world length in **metres**

The system uses this ratio to convert segmented pixel areas into square metres.

---

## Usage

### Running predictions

```bash
python run.py
```

You will be prompted to provide the path to your floor plan image and the scale reference values.

### Example output

```
Validating the minimum habitable space...
Pass — There is enough habitable space in the residence (75.32 m²)

Validating living room total area...
Pass — There is enough space in the living room (23.79 m²)

Validating kitchen area...
Fail — The kitchen area of 3.98 m² is smaller than the required minimum of 7 m²

Validating bathroom total area...
Pass — There is enough space in the bathroom (4.04 m²)
```

---

## Model

The final model used is **YOLOv8s-seg** (small, segmentation variant), trained on the [BuilderFormer-4 dataset](https://universe.roboflow.com/builderformer/builderformer-4/dataset/4) from Roboflow.

### Training summary

| Model | Epochs | Training time | Notes |
|---|---|---|---|
| YOLOv8n | 30 | ~1h (Colab GPU) | Baseline, ~0.9 precision |
| YOLOv8m | 50 | 5.2h | Good results, precision near 1 |
| YOLOv8l | 50 | 22h | Marginal gain over medium |
| YOLOv8s | 300 | 7.1h | Best balance of speed and accuracy |
| YOLOv8s-seg | 100 | ~2h | Used for final mask extraction |

**Best performing configuration:** `YOLOv8s` with 300 epochs — strong accuracy across most room types, with the exception of `space_multipurpose_space` which is inherently ambiguous.

### Dataset

- **Source:** [BuilderFormer-4 on Roboflow](https://universe.roboflow.com/builderformer/builderformer-4/dataset/4)
- **Size:** ~1,968 images, 99,257 annotations across 14 classes
- **Preprocessing:** Auto-orient, resize to 640×640

> ⚠️ The training dataset consists primarily of Korean floor plans. Performance on Lithuanian plans may vary, particularly for rooms without typical furniture markings.

---

## Known Limitations

- Model performance on real-world Lithuanian floor plans is lower than validation metrics suggest, likely due to dataset/validation overlap and the absence of furniture in many training images.
- `space_multipurpose_space` and `space_other` are frequently confused with each other — their visual appearance is highly variable by design.
- Scale input is manual — a future improvement would be automatic scale detection from plan annotations.
- Rules currently cover area minimums only; fire safety, ventilation ratios, and stairwell checks are identified as future work.

---

## Future Improvements

- Label a custom dataset of Lithuanian residential plans
- Add automatic scale detection from floor plan text/annotations
- Expand rulesets to cover fire safety exits, corridor widths, and window-to-room ratios
- Explore ensemble approaches (e.g. a dedicated wall detector + a room classifier)

---

## References

- [STR 2.02.01:2004 Lithuanian Residential Building Regulations](https://lrs.lt)
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [BuilderFormer-4 Dataset](https://universe.roboflow.com/builderformer/builderformer-4/dataset/4)
- [Deep Floor Plan Recognition Using a Multi-Task Network (2019)](https://arxiv.org/pdf/1908.11025)
- [Room Classification on Floor Plan Graphs using GNNs (2021)](https://arxiv.org/pdf/2108.05947)

---

## More

The full project documentation can be found [here](https://docs.google.com/document/d/1UkhhtIs63hSMtFtOdrl_XOZLH1OMUwXIU_sdPuVnaow/edit?usp=sharing)
