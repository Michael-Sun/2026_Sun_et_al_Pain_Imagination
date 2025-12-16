# Precision Functional Mapping of Imagined and Experienced Pain

This repository contains analysis code associated with:

**Sun, Petre, Bo, Bango, Hershkop, Shohan, Jung, and Wager. (2026)**  
*Precision Functional Mapping of Imagined and Experienced Pain*

The code implements univariate, multivariate, and representational similarity analyses used to compare neural responses to experienced and imagined pain within individuals using deep-phenotyping fMRI data.

---

## Repository Structure

- **BehavioralSelfReport/**  
  Scripts for processing and summarizing behavioral and self-report measures collected alongside fMRI data.

- **UnivariateGLM/**  
  Subject-level and group-level univariate general linear model (GLM) analyses for Hot, Warm, and Imagine conditions.

- **PrecisionFunctionalSVM/**  
  Precision functional mapping using cross-validated support vector machines (SVMs) to identify subject- and body site–specific nociceptive representations and test their generalization across conditions and sessions.

- **RepresentationalSimilarity/**  
  Representational similarity analyses (RSA) assessing multivariate pattern similarity between experienced and imagined pain across cortical and subcortical regions.

---

## Software Requirements

Analyses were conducted primarily in **MATLAB**, using:
- CANlab neuroimaging tools  
- RSA toolbox  
- SPM (for preprocessing and GLM estimation)  

Exact software versions and parameters are reported in the manuscript and Supplementary Methods (COBIDAS-compliant).

---

## Data Availability

Neuroimaging and behavioral data used in this study will be made publicly available upon acceptance of the manuscript, consistent with institutional guidelines and journal policy.  
Until that time, this repository provides all analysis code required to reproduce the reported results once the data are released.

---

## Notes

This repository is intended to support transparency and reproducibility.  
Scripts are organized to reflect the analysis workflow described in the manuscript but are not designed as a turn-key pipeline.

For questions, please contact the corresponding author.
