import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

# Helper class for 3D arrows, which matplotlib's quiver can be tricky with.
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)

def create_npr_schematic_v2(filename="npr_projection_schematic.pdf"):
    """
    Generates a high-quality 3D schematic visualizing the NPR projection,
    with a 2D inset explaining the null basis of the normal plane.
    Revised based on user feedback.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8), subplot_kw=dict(projection='3d'))
    ax2.remove() # Remove the 3d projection from the second subplot
    ax2 = fig.add_subplot(1, 2, 2) # Add it back as a 2d plot

    # --- Main 3D Plot: The Projection ---
    # ax1 = fig.add_subplot(gs[:, :-1], projection='3d')
    ax1.set_title("\nNPR as an Orthogonal Projection (Analogy)", fontsize=16, pad=10)

    # 1. Define the Ledger plane (the "floor")
    xx, yy = np.meshgrid(np.linspace(-1, 2, 5), np.linspace(-1, 2, 5))
    zz = np.zeros_like(xx)
    ax1.plot_surface(xx, yy, zz, alpha=0.1, color='red', rstride=1, cstride=1, zorder=1)

    # 2. Define the "Before" vector
    V = np.array([1.5, 1.2, 1.8])
    
    # 3. Plot the "Before" vector (the "pen in the air")
    arrow_v = Arrow3D([0, V[0]], [0, V[1]], [0, V[2]], mutation_scale=20,
                      lw=2.5, arrowstyle="-|>", color="blue", zorder=10)
    ax1.add_artist(arrow_v)
    ax1.text(V[0]*-0.1, V[1]*-0.1, V[2]*0.8, r"$\mathbf{V}$ (Original Vector)", color="blue", fontsize=12)

    # 4. Define the "After" vector (the "shadow")
    V_proj = np.array([V[0], V[1], 0])

    # 5. Plot the "After" vector
    arrow_v_proj = Arrow3D([0, V_proj[0]], [0, V_proj[1]], [0, V_proj[2]], mutation_scale=20,
                           lw=2.5, arrowstyle="-|>", color="red", zorder=10)
    ax1.add_artist(arrow_v_proj)
    ax1.text(V_proj[0]*0.0, V_proj[1]*-0.15, V_proj[2]-0.2, r"$\mathbf{P}[V]$ (Projected Vector)", color="red", fontsize=12)

    # 6. Plot the projection lines
    ax1.plot([V[0], V_proj[0]], [V[1], V_proj[1]], [V[2], V_proj[2]], 'k--', lw=1, zorder=5)
    ax1.text((V[0]+V_proj[0])/2 + 0.1, (V[1]+V_proj[1])/2, (V[2]+V_proj[2])/2, "Projection", color='k', fontsize=10)

    ax1.scatter(0, 0, s=50, c='k', zorder=5)

    # Axis setup
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
    ax1.set_zticklabels([])
    ax1.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax1.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax1.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax1.set_xlabel("y (tangential)")
    ax1.set_ylabel("z (tangential)")
    ax1.set_zlabel("Normal Plane (Deleted)")
    ax1.set_xlim(-1.5, 2.5); ax1.set_ylim(-1.5, 2.5); ax1.set_zlim(0, 2.5)
    ax1.view_init(elev=20, azim=-50) # Set a nice viewing angle
    ax1.text(-2.65, 1.1, -0.1, r'Ledger Plane($\mathcal{L}$)', color='red')
    ax1.grid(True)

    # --- 2D Inset: The Null Basis ---
    ax2.set_title("\nThe Normal Plane Basis", fontsize=16, pad=10)
    ax2.axhline(0, color='k', lw=1.5, zorder=0)
    ax2.scatter(0, 0, s=100, c='k', zorder=5)
    ax2.text(-0.1, -0.05, r'Point on $\mathcal{L}$', ha='center', va='top')
    
    # Null vectors
    ax2.arrow(0, 0, 0.5, 0.5, head_width=0.04, head_length=0.06, fc='b', ec='b', ls='--', zorder=10)
    ax2.text(0.55, 0.55, r'$\mathbf{n}_+$', color='b', fontsize=14)
    ax2.arrow(0, 0, 0.5, -0.5, head_width=0.04, head_length=0.06, fc='r', ec='r', ls='--', zorder=10)
    ax2.text(0.55, -0.55, r'$\mathbf{n}_-$', color='r', fontsize=14)
    
    ax2.text(0, 0.8, 'This 2D null plane is the\nsubspace deleted by NPR.',
             ha='center', va='center', fontsize=12)
    
    ax2.set_xlim(-1, 1); ax2.set_ylim(-1, 1)
    ax2.set_aspect('equal', adjustable='box')
    ax2.axis('off')

    # # fig.tight_layout()
    plt.savefig(filename, bbox_inches='tight', dpi=300)
    plt.close(fig)
    print(f"Generated schematic: {filename}")

if __name__ == "__main__":
    create_npr_schematic_v2()