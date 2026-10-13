import matplotlib.pyplot as plt
import numpy as np

def plot_clifford_spectrum():
    fig, ax = plt.subplots(figsize=(9, 5))
    
    # Eigenvalue bins and degeneracies from characteristic polynomial
    eigenvalues = [-1.0, -0.125, 0.125, 1.0]
    degeneracies = [2, 6, 6, 2]
    labels = ['$\\lambda = -1$ (Deg: 2)', '$\\lambda = -1/8$ (Deg: 6)', '$\\lambda = +1/8$ (Deg: 6)', '$\\lambda = +1$ (Deg: 2)']
    colors = ['#d62728', '#ff7f0e', '#2ca02c', '#1f77b4']
    
    bars = ax.bar(labels, degeneracies, color=colors, alpha=0.85, width=0.5)
    
    ax.set_ylabel('Degeneracy Multiplicity', fontsize=12)
    ax.set_title('Clifford Orientation Pair Spectrum ($\hat{O}_{pair}$) & Mass Gap ($1/8$)', fontsize=13, fontweight='bold')
    ax.set_ylim(0, 8)
    
    # Highlight the 1/8 spectral mass gap
    ax.annotate('Spectral Mass Gap\n$\\Delta E_0 / E_0 = 1/8$', xy=(1.5, 6), xytext=(1.5, 7.2),
                ha='center', fontsize=11, fontweight='bold',
                arrowstyle='->', lw=1.5)

    plt.tight_layout()
    plt.savefig('clifford_spectrum_gap.png', dpi=300)
    plt.show()

if __name__ == '__main__':
    plot_clifford_spectrum()
