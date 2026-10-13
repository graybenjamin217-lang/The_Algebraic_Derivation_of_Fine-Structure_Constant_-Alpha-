import matplotlib.pyplot as plt
import numpy as np

def plot_core_coupling():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # 4 binary orientation axes {P, T, A, S}
    generators = ['Parity (P)', 'Time-Rev (T)', 'Abs Phase (A)', 'Spatial Shift (S)']
    dimensions = [2, 2, 2, 2]
    
    y_pos = np.arange(len(generators))
    ax.barh(y_pos, dimensions, align='center', color='#1f77b4', alpha=0.8)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(generators, fontsize=11)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Binary State Dimension ($2^1 = 2$)', fontsize=12)
    ax.set_title('Master Field Algebra $\\mathcal{A}_G$ Core Architecture ($dim = 2^4 = 16$)', fontsize=13, fontweight='bold')
    
    # Annotation for 1/16 baseline
    ax.text(1.2, 1.5, 'Core Coupling:\n$\\alpha_{core} = 1 / 16$', fontsize=12, 
            bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.3))
    
    plt.tight_layout()
    plt.savefig('core_coupling_baseline.png', dpi=300)
    plt.show()

if __name__ == '__main__':
    plot_core_coupling()
