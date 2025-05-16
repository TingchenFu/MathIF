# MathIF:  Instruction-Following Benchmark for LRMs.

This repository contains code for working with the MathIF dataset, which focuses on instruction following of LRMs.

## Setup

### 1. Environment Setup

```bash
# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 2. Data Download

The dataset can be downloaded from Hugging Face: https://huggingface.co/datasets/TingchenFu/MathIF and should be put in data/ directory.

## Usage

### Inference

To run inference on the MathIF dataset:

```
bash code/scripts/vllm_if.sh
```

### Evaluation

To evaluate model predictions:

```
bash code/scripts/eval_if.sh
```

## Data Format

The dataset is in JSONL format, where each line contains:
- `source`: Dataset source
- `id`: Unique identifier
- `question`: Mathematical question
- `answer`: Ground truth answer
- `constraint_desc`: Description of constraints
- `constraint_name`: Type of constraint
- `constraint_args`: Constraint arguments

## Project Structure

```
.
├── data/               # Dataset files
├── code/               # Source code
│   ├── scripts/        # Scripts for inference and evaluation
│   └── ...             # Other code files
├── output/           # Output directory
└── README.md         # This file
```

## Requirements

Key dependencies include:
- Python 3.9+
- CUDA 12.4
