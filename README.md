# The Algebraic Derivation of Fine-Structure Constant ($\alpha$) via Non-Scalar Operator Mechanics

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22999751.svg)](https://doi.org/10.5281/zenodo.22999751).

## Overview
This repository hosts technical artifacts, scripts, and supporting documentation for the paper **"The Algebraic Derivation of Fine-Structure Constant $\alpha$ via Non-Scalar Operator Mechanics"**, authored by Benjamin Edward Gray. 

The immutable, citable preprint version of this manuscript is permanently published on Zenodo:  
👉 **[Zenodo DOI: 10.5281/zenodo.22999751](https://doi.org/10.5281/zenodo.22999751)**.

---

## Core Theoretical Framework
Operating under the strict mandate of **Algebraic Primacy**, this framework derives the fine-structure constant *a priori* from the internal symmetries of the master field algebra $\mathcal{A}_G$ without introducing any empirical fitting parameters or scalar adjustments.

### Key Architectural Layers
1. **Primary Core Coupling ($\alpha_{\text{core}} = 1/16$):** Established directly from the four orientation generators $\{P, T, A, S\}$ across the fundamental binary axes of the master algebra $\mathcal{A}_G$.
2. **GNS Representation Sector ($1/128$):** Projecting the algebra into the 16-dimensional Hilbert space $\mathcal{H}_\omega \cong \mathbb{C}^{16}$ contracts the spectral gap to $\Delta E_0 = \frac{1}{8}E_0$ via the Clifford orientation pair operator $\hat{O}_{\text{pair}}$, yielding the unshielded high-energy baseline $\alpha_{sector} = 1/128$.
3. **Topological Dual-Dilation Impedance ($\alpha_{\text{lab}}^{-1} \approx 137.036071168$):** The low-energy asymptotic value is evaluated via the sum of the discrete diagonal weight, active transition channels, and boundary shift.:
   $$\alpha_{\text{lab}}^{-1} = 128 + 9 + \eta_{D_k} \approx 137.036071168$$
   where $N_{\text{active}} = 9$ represents active off-diagonal transition channels and $\eta_{D_k} \approx 0.036071168$ is the continuous operator expectation value under dual-dilation boundary limits.

---

## Repository Structure
* `/docs` — Comprehensive technical notes, nomenclature breakdowns, and auxiliary proofs.
* `/scripts` — Numerical verification routines and spectral calculation scripts.
* `README.md` — Project overview and bidirectional navigation guide.

---

## Citation
If you utilize or reference the mathematical formalism in this repository, please cite the official Zenodo preprint:
```bibtex
@misc{gray2026alpha,
  author       = {Benjamin Edward Gray},
  title        = {The Algebraic Derivation of Fine-Structure Constant $\alpha$ via Non-Scalar Operator Mechanics},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.22999751},
  url          = {[https://doi.org/10.5281/zenodo.22999751](https://doi.org/10.5281/zenodo.22999751)}
}
