# AI-health-hackthon: MRI Brain Tumor Classification

This project implements a medical-grade AI pipeline for classifying brain tumors from MRI scans using Swin Transformers and ensemble techniques.

## Dataset Overview
The dataset contains 7,200 MRI images categorized into four classes:
- **Glioma**: A type of tumor that starts in the glial cells of the brain or the spine.
- **Meningioma**: A tumor that arises from the meninges — the membranes that surround your brain and spinal cord.
- **Pituitary**: Tumors that develop in the pituitary gland.
- **No Tumor**: Healthy brain scans for baseline comparison.

## Project Structure
- `datasets/`: Extracted MRI data (Training/Testing).
- `data_audit.py`: Script for initial dataset analysis.
- `requirements.txt`: Python dependencies.

## Clinical Relevance
This audit ensures that the model is built on high-quality, balanced data, replicating real-world radiology AI workflows for maximum clinical reliability.