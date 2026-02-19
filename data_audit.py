import os
import cv2
import matplotlib.pyplot as plt
import pandas as pd

def audit_dataset(data_dir):
    print(f"Auditing dataset at: {data_dir}")
    
    phases = [d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))]
    print(f"Phases found: {phases}")
    
    audit_results = []
    
    for phase in phases:
        phase_path = os.path.join(data_dir, phase)
        classes = [d for d in os.listdir(phase_path) if os.path.isdir(os.path.join(phase_path, d))]
        print(f"\nPhase: {phase}")
        for c in classes:
            class_path = os.path.join(phase_path, c)
            num_samples = len(os.listdir(class_path))
            print(f"  {c}: {num_samples} samples")
            audit_results.append({'Phase': phase, 'Class': c, 'Count': num_samples})
            
    # Visualize Sample
    if phases:
        first_phase = phases[0]
        first_class = [d for d in os.listdir(os.path.join(data_dir, first_phase)) if os.path.isdir(os.path.join(data_dir, first_phase, d))][0]
        sample_folder = os.path.join(data_dir, first_phase, first_class)
        sample_files = [f for f in os.listdir(sample_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]
        
        if sample_files:
            sample_path = os.path.join(sample_folder, sample_files[0])
            img = cv2.imread(sample_path)
            if img is not None:
                plt.figure(figsize=(10, 6))
                plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                plt.title(f"Sample MRI - {first_phase}/{first_class}")
                plt.axis("off")
                plt.savefig("sample_mri_check.png")
                print("\nSaved sample MRI check to 'sample_mri_check.png'")
            else:
                print(f"\nFailed to load image: {sample_path}")
        else:
            print("\nNo image files found for visualization.")

    df = pd.DataFrame(audit_results)
    print("\nSummary Table:")
    print(df)
    
if __name__ == "__main__":
    dataset_path = "datasets"
    if os.path.exists(dataset_path):
        audit_dataset(dataset_path)
    else:
        print(f"Dataset path '{dataset_path}' not found.")
