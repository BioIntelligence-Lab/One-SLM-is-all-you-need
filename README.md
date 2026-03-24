# One SLM is All You Need: Multi-Task Clinical NLP with Privacy-Preserving Small Language Models

[![Paper](https://img.shields.io/badge/Paper-JIIM%202026-blue)](https://link.springer.com/article/10.1007/s10278-026-01912-4)

## TL;DR
We show that a single fine-tuned small language model (OPT-350M + LoRA) can outperform GPT-4o across multiple clinical NLP tasks, while being:

- ✅ 25x–100x smaller
- ✅ Deployable on local hardware
- ✅ Privacy-preserving (no cloud required)
- ✅ Multi-task capable (no need for multiple models)

This challenges the assumption that larger models are necessary for clinical AI.


## Key Results

| Task | Multi-task SLM | GPT-4o |
|------|---------------|--------|
| Report Labeling (F1) | **0.894** | 0.728 |
| DICOM Harmonization (Accuracy) | **0.975** | 0.878 |
| Impression Generation (Likert) | **4.39 ± 1.00** | 3.65 ± 1.00 |

- Outperforms GPT-4o across all tasks
- Requires no prompt engineering
- Runs on standard hospital hardware


## Method Overview

We propose a **multi-task small language model (SLM)** framework:

- Backbone: OPT-350M
- Fine-tuning: LoRA (Low-Rank Adaptation)
- Training: Multi-task instruction tuning

### Tasks:
1. Medical report labeling (multi-label classification)
2. DICOM metadata harmonization (standardization)
3. Impression generation (text generation)

### Key Idea:
Instead of training one model per task:
→ Train ONE model for ALL tasks

This reduces:
- Engineering overhead
- Deployment complexity
- Maintenance burden


## Experiments

### Models Compared
- OPT-350M (single-task)
- OPT-350M (multi-task)
- Phi-4-mini (4B)
- LLaMA-3.2-1B
- Mistral-7B
- Qwen3-4B
- GPT-4o (zero-shot + prompt engineered)

### Training Setup
- Epochs: 100
- Batch size: 4
- Learning rate: 8e-4
- Hardware: NVIDIA A40
