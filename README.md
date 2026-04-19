<h1 style="display: flex; justify-content: center; align-items: center; gap: 10px; margin: 0;">
  MathIF: Instruction-Following Benchmark for Large Reasoning Models (ACL 2026)
</h1>

[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-brightgreen)]() [![CUDA 12.4](https://img.shields.io/badge/CUDA-12.4-red)]() [![License](https://img.shields.io/badge/license-MIT-blue)]()

MathIF is a dedicated benchmark for evaluating the instruction-following capabilities of large reasoning models (LRMs) on mathematical reasoning tasks. It exposes a fundamental trade-off between a model’s problem-solving strength and its ability to comply with user-specified constraints.


<div align="center" style="font-family: Arial, sans-serif; font-size: 16px;">
  <p>
    <!-- <a href="#news" style="text-decoration: none; font-weight: bold;">🎉 News</a> • -->
    <!-- <a href="#links" style="text-decoration: none; font-weight: bold;">🔗 Links</a> --> • 
     <a href="https://arxiv.org/abs/2505.14810" style="text-decoration: none; font-weight: bold;"> 📖 Paper</a> •
<!--     <a href="#getting-started" style="text-decoration: none; font-weight: bold;"> ✨ Getting Started</a> • -->
  <!-- </p>
  <p> -->
    <a href="#usage" style="text-decoration: none; font-weight: bold;">🔧 Usage</a>
    <!-- <a href="#evaluation" style="text-decoration: none; font-weight: bold;">📃 Evaluation</a> • -->
    <!-- <a href="#citation" style="text-decoration: none; font-weight: bold;">🎈 Citation</a> • --> •
    <a href="#leaderboard" style="text-decoration: none; font-weight: bold;"> 📊 Leaderboard</a> •
    <a href="https://huggingface.co/datasets/TingchenFu/MathIF" style="text-decoration: none; font-weight: bold;">🤗 Data</a> •
    <a href="https://x.com/yafuly/status/1925753754961236006" style="text-decoration: none; font-weight: bold;"> 🐦 Twitter</a>
    
  </p>
</div>


# 📖Features

- **Compositional Constraints**  
  15 Python-verifiable constraint types in four categories (length, lexical, format, affix), combined into single, dual, and triple constraints.

- **Diverse Math Sources**  
  Problems drawn from GSM8K, MATH-500, Minerva, Olympiad, and AIME, totaling 420 high-quality evaluation samples.

- **Fine-Grained Metrics**  
  - **Hard Accuracy (HAcc):** fraction of examples satisfying _all_ constraints  
  - **Soft Accuracy (SAcc):** average fraction of satisfied constraints per example

- **vLLM-Powered Inference**  
  Efficient decoding with nucleus sampling (T=1.0, p=0.95) and up to 16k token generation.

# ✨Getting Started

## Prerequisites

- Python 3.9 or later  
- CUDA 12.4  
- `git`, `bash`

## Installation

```bash
git clone https://github.com/TingchenFu/MathIF.git
cd MathIF

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
````



# 🔧Usage

## Inference

```bash
bash code/scripts/vllm_if.sh
```

## Evaluation

```bash
bash code/scripts/eval_if.sh
```

## Dataset Format

Each line in the JSONL file contains:

| Field             | Description                       |
| ----------------- | --------------------------------- |
| `source`          | Original data source              |
| `id`              | Unique example identifier         |
| `question`        | Math problem statement            |
| `answer`          | Ground-truth solution             |
| `constraint_desc` | Human-readable constraint summary |
| `constraint_name` | Constraint category               |
| `constraint_args` | Arguments used for verification   |

## Project Structure

```
.
├── data/                # MathIF JSONL files
├── code/
│   ├── scripts/         # Inference & evaluation scripts
│   └── ...              # Model wrappers and utilities
├── output/              # Generated predictions & logs
├── requirements.txt     # Python dependencies
└── README.md            # This overview
```

<!-- ## Citation

If you use MathIF, please cite:

```bibtex
@inproceedings{fu2025MathIF,
  title={MathIF: Instruction‐Following Benchmark for Large Reasoning Models},
  author={Fu, Tingchen and Gu, Jiawei and Li, Yafu and Qu, Xiaoye and Cheng, Yu},
  booktitle={NeurIPS},
  year={2025}
}
```

## License

Released under the MIT License. See [LICENSE](LICENSE) for details.

```
``` -->

Here's your LaTeX table transformed into a clean and readable GitHub-flavored Markdown table, **keeping only HAcc, SAcc, and correctness with constraint** (`w/ const.`). For clarity, the models are grouped by size, but LaTeX-specific formatting (bold/underline) is omitted since GitHub tables do not support rich styling.


# 📊Leaderboard
📢 **Showcase Your Model’s Instruction-Following Capability**

Feel free to contribute results from your own models—we welcome community submissions!
We currently support evaluation of newly added models on our platform. To be included on the leaderboard, please provide the Hugging Face model link for verification and testing.

## **≤ 4B Models**              

| Model                         | HAcc  | SAcc  | Correctness |
| ----------------------------- | ----- | ----- | ----------------------- |
| [Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B)                      | 44.05 | 61.43 | 58.57                   |
| [Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B)                    | 30.24 | 50.24 | 51.19                   |
| [Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B)                    | 27.86 | 50.44 | 32.14                   |
| [L1-Qwen-1.5B-Exact](https://huggingface.co/l3lab/L1-Qwen-1.5B-Exact)            | 19.76 | 39.60 | 42.86                   |
| [L1-Qwen-1.5B-Max](https://huggingface.co/l3lab/L1-Qwen-1.5B-Max)              | 19.76 | 39.40 | 45.71                   |
| [DeepSeek-R1-Distill-Qwen-1.5B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B) | 17.14 | 36.62 | 31.67                   |
| [DeepScaler-1.5B-Preview](https://huggingface.co/agentica-org/DeepScaleR-1.5B-Preview)       | 14.52 | 34.52 | 36.19                   |
| [Qwen2.5-1.5B-SimpleRL-Zoo](https://huggingface.co/hkust-nlp/Qwen-2.5-1.5B-SimpleRL-Zoo)     | 9.05  | 24.33 | 22.38                   |
| [Qwen2.5-Math-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Math-1.5B-Instruct)    | 7.62  | 21.39 | 44.29                   |

## **7B–14B Models**
| Model                         | HAcc  | SAcc  | Correctness |
| ----------------------------- | ----- | ----- | ----------------------- |
| [Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B)                          | 50.71  | 67.06  | 64.29                   |
| [DeepSeek-R1-Distill-Qwen-14B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B)      | 39.28  | 60.55  | 50.95                   |
| [Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B)                       | 37.86  | 57.34  | 66.43                   |
| [DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B)       | 26.43  | 44.96  | 48.57                   |
| [DeepSeek-R1-Distill-Llama-8B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-8B)      | 22.14  | 44.04  | 36.43                   |
| [Open-Reasoner-Zero-7B](https://huggingface.co/Open-Reasoner-Zero/Open-Reasoner-Zero-7B)             | 13.57  | 32.26  | 51.90                   |
| [Qwen2.5-Math-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Math-7B-Instruct)          | 9.05   | 25.60  | 37.14                   |


## **≥ 32B Models**
| Model                         | HAcc  | SAcc  | Correctness |
| ----------------------------- | ----- | ----- | ----------------------- |
| [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B)                          | 43.81  | 62.82  | 70.00                   |
| [DeepSeek-R1-Distill-Qwen-32B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B)      | 42.62  | 60.91  | 57.62                   |
| [DeepSeek-R1-Distill-Llama-70B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-70B)     | 41.43  | 61.07  | 54.05                   |
| [QwQ-32B](https://huggingface.co/Qwen/QwQ-32B)                            | 40.24  | 59.99  | 68.81                   |
| [OlympicCoder-32B](https://huggingface.co/open-r1/OlympicCoder-32B)                  | 35.95  | 57.97  | 54.52                   |
| [s1-32B](https://huggingface.co/simplescaling/s1-32B)                             | 20.95  | 41.78  | 60.95                   |
| [Open-Reasoner-Zero-32B](https://huggingface.co/Open-Reasoner-Zero/Open-Reasoner-Zero-32B)            | 15.47  | 35.52  | 67.62                   |




# 🌻Acknowledgements

MathIF is inspired by prior work on [IFEval](https://huggingface.co/datasets/google/IFEval) and [ComplexBench](https://github.com/thu-coai/ComplexBench), and leverages [vLLM](https://github.com/vllm-project/vllm) for efficient inference.

# 📖Citation

```
@article{fu2025scaling,
  title={Scaling Reasoning, Losing Control: Evaluating Instruction Following in Large Reasoning Models},
  author={Fu, Tingchen and Gu, Jiawei and Li, Yafu and Qu, Xiaoye and Cheng, Yu},
  journal={arXiv preprint arXiv:2505.14810},
  year={2025}
}
```

# 📬Contact

For questions, feedback, or collaboration inquiries, please contact:  
- **Tingchen Fu**: lucas.futingchen@gmail.com
- **Yafu Li**: yafuly@gmail.com
