import matplotlib.pyplot as plt

def plot_subspace_decomposition():
    fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(aspect="equal"))
    
    subspaces = ['Active Transition Channels\n($N_{active} = 9$)', 
                 'Diagonal Norm-Conservation\n($V_{diag}^{(4)} = 4$)', 
                 'Gauge-Constraint Sector\n($V_{gauge}^{(3)} = 3$)']
    dims = [9, 4, 3]
    colors = ['#2ca02c', '#aec7e8', '#ffbb78']
    
    wedges, texts, autotexts = ax.pie(dims, labels=subspaces, autopct='%1.1f%%',
                                      startangle=140, colors=colors, 
                                      textprops=dict(color="black", fontsize=11))
    
    plt.setp(autotexts, size=10, weight="bold")
    ax.set_title("Matrix Space $\\mathcal{M}_4(\\mathbb{C})$ Subspace Decomposition ($Total = 16$)", fontsize=13, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('subspace_decomposition.png', dpi=300)
    plt.show()

if __name__ == '__main__':
    plot_subspace_decomposition()
