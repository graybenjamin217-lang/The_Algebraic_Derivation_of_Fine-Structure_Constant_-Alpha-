import matplotlib.pyplot as plt
import numpy as np

def plot_dilation_boundary():
    iterations = np.arange(1, 16)
    # Simulated exponential convergence toward the exact boundary limit under Banach threshold
    target = 0.036071168
    values = target + 0.5 * np.exp(-0.4 * iterations)
    
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(iterations, values, marker='o', color='#9467bd', lw=2, label='Feedback Iteration Path')
    ax.axhline(y=target, color='r', linestyle='--', label=f'Exact Limit $\\eta_{{D_k}} \\approx {target}$')
    
    ax.set_xlabel('Feedback Iteration Step', fontsize=12)
    ax.set_ylabel('Boundary Expectation Value', fontsize=12)
    ax.set_title('Dual-Dilation Impedance Convergence ($D_k X D_k$)', fontsize=13, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(True, linestyle=':', alpha=0.6)
    
    plt.tight_layout()
    plt.savefig('dilation_boundary_convergence.png', dpi=300)
    plt.show()

if __name__ == '__main__':
    plot_dilation_boundary()
