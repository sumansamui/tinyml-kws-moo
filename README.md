# Keyword Spotting via Multi-Objective Optimization

This repository accompanies the research paper:

**Keyword Spotting via Multi-Objective Optimization: Balancing Accuracy and Model Size for Efficient TinyML Deployment**

## 📄 Abstract
This work presents a hardware-aware neural architecture search (NAS) framework using multi-objective optimization (MOO) to deploy keyword spotting (KWS) models on resource-constrained TinyML hardware. Three optimization techniques—NSGA-II (Non-dominated Sorting Genetic Algorithm II), MOSA (Multi-Objective Simulated Annealing), and MOBO (Multi-Objective Bayesian Optimization)—are employed to generate Pareto-optimal models balancing accuracy and model size across CNN, CRNN, and DS-CNN architectures. The results are evaluated using standard metrics such as Hypervolume (HV) and Generational Distance (GD). Additionally, a scalarization-based model ranking approach (Tchebycheff method) is introduced to assist in deployment decisions under specific hardware constraints.

## 🧪 Experiments
- Dataset: [Google Speech Commands v2](http://download.tensorflow.org/data/speech_commands_v0.02.tar.gz)
- Target Classes: `["yes", "no", "up", "down", "left", "right", "on", "off", "go", "stop"]`
- Models: CNN, CRNN, DS-CNN
- Feature Extraction: Log-Mel Spectrograms (MFCC optional)
- Deployment: TFLite quantization (INT8) for TinyML readiness

## 📊 Optimization Techniques
| Technique | Description |
|-----------|-------------|
| **NSGA-II** | Genetic algorithm-based MOO method for diverse Pareto fronts. |
| **MOSA**    | Probabilistic annealing-based MOO with temperature control. |
| **MOBO**    | Surrogate model-based Bayesian optimization for efficient sampling. |

## 📈 Evaluation Metrics
- Hypervolume (HV)
- Generational Distance (GD)
- Inverted GD (IGD)
- C-Metric
- Tchebycheff Scalarization Score


## 📌 Key Contribution
- First application of MOO to hyperparameter tuning for SF-KWS.
- Comparative analysis of three MOO strategies on TinyML-suitable architectures.
- A flexible model selection strategy via scalarization scoring.

## 🔗 Citation
If you use this repository, please cite our paper:


## 📜 License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

