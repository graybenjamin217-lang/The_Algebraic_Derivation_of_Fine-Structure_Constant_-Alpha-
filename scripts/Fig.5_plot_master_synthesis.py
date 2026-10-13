import matplotlib.pyplot as plt

def plot_master_synthesis():
    fig, ax = plt.subplots(figsize=(9, 6))
    
    components = ['UV Ground State\n($\\lambda_{phys}$)', 
                  'Active Channels\n($Tr(\\hat{\\Pi}_{active})$)', 
                  'Dilation Shift\n($\\eta_{D_k}$)', 
                  'Model Total\n($\\alpha_{lab}^{-1}$)', 
                  'CODATA-2022\n(Empirical)']
    values = [128.00, 9.00, 0.036071168, 137.036071168, 137.035999084]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#7f7f7f']
    
    bars = ax.bar(components, values, color=colors, alpha=0.85, width=0.55)
    
    # Customizing axis limits to zoom in on the precision decimal values
    ax.set_ylim(120, 140)
    ax.set_ylabel('Inverse Coupling Value ($\\alpha^{-1}$)', fontsize=12)
    ax.set_title('Master Operator Synthesis vs. CODATA-2022 Benchmark', fontsize=13, fontweight='bold')
    
    # Add exact text labels above bars
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.5f}' if height > 10 else f'{height:.3f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5),  # 5 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9, fontweight='bold')

    plt.tight_layout()
    plt.savefig('master_synthesis_codata.png', dpi=300)
    plt.show()

if __name__ == '__main__':
    plot_master_synthesis()
