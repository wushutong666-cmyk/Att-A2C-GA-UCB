# Att-A2C+GA-UCB: Collaborative Test Data Generation for Mutation Testing

This is the official PyTorch implementation of the paper: **"Att-A2C+GA-UCB: Collaborative Test Data Generation via Multidimensional Path Similarity for Mutation Testing"**.

---

## 💡 Overview

Traditional evolutionary algorithms for mutation testing suffer from structural-semantic gaps and premature convergence. We propose **Att-A2C+GA-UCB**, a tightly coupled framework that:
1. Constructs a **four-dimensional path similarity metric** (integrating rule semantics, operator similarity, operand context, and structural characteristics).
2. Uses an **Attention-enhanced Advantage Actor-Critic (Att-A2C)** model to dynamically adjust Genetic Algorithm (GA) parameters and multi-dimensional UCB coefficients.
3. Alleviates path starvation and eliminates redundant search overhead across complex program paths.

