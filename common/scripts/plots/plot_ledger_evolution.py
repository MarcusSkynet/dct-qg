import numpy as np
import matplotlib.pyplot as plt

def plot_entropy_staircase(filename="figs/tdt3_staircase.pdf",
                           snap_times=(2.0, 4.0, 6.0),
                           S0=0.0,
                           ln2=np.log(2.0),
                           use_tex=False):
    """
    Make the TDT-3 staircase figure.
    - snap_times: times at which snaps occur (strictly increasing)
    - S0: initial Ledger entropy (nats)
    - Each snap adds ln(2) nats to S_L (capacity = payload at snaps)
    """

    if use_tex:
        plt.rcParams["text.usetex"] = True

    # Build time grid: piecewise-constant then jumps
    t0 = 0.0
    times = [t0]
    ent   = [S0]

    S = S0
    for ts in snap_times:
        # flat (unitary) segment up to just before snap
        times += [ts]
        ent   += [S]
        # jump: write one bit => + ln 2 nats
        S += ln2
        times += [ts]
        ent   += [S]

    # Extend a little after last snap for a flat tail
    tail = (snap_times[-1] + 0.9) if snap_times else 1.0
    times += [tail]
    ent   += [S]

    fig, ax = plt.subplots(figsize=(8, 5))

    # True staircase
    ax.step(times, ent, where="post", linewidth=2)

    # Vertical jump markers at snaps
    for ts, k in zip(snap_times, range(1, len(snap_times)+1)):
        ax.plot([ts, ts], [S0+(k-1)*ln2, S0+k*ln2], linestyle="--",color='red', linewidth=2)

    # Labels and title
    ax.set_xlabel("Time (arb. units)")
    ax.set_ylabel(r"Ledger entropy $S_{\mathcal{L}}(t)$ (nats)")
    ax.set_title("TDT–3: Episodic Growth of Ledger Entropy", pad=12)

    # Y ticks aligned with steps
    kmax = len(snap_times)
    yticks = [S0 + k*ln2 for k in range(0, kmax+1)]
    yticklabels = [r"$S_0$"] + [rf"$S_0 + {k}\ln 2$" for k in range(1, kmax+1)]
    ax.set_yticks(yticks)
    ax.set_yticklabels(yticklabels)

    ax.text(3, 0.85, r'Quiet Phase:' '\n' r'Unitary Evolution' '\n' r'($\nabla_a s^a = 0$)', 
            ha='center', va='bottom', fontsize=11, color='blue')
    ax.text(5, 0.85, r'Snap Event:' '\n' r'Irreversible Write' '\n' r'($\delta S_{\mathcal{L}} = \delta S_{\mathrm{info}}$)', 
            ha='center', va='bottom', fontsize=11, color='red')

    # Cosmetics
    ax.set_xlim(times[0], times[-1])
    ax.set_ylim(S0 - 0.2*ln2, S0 + (kmax+1)*ln2)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Generated: {filename}")

if __name__ == '__main__':
    OUTPUT_DIR = 'dct_figures'
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created directory: {OUTPUT_DIR}")

    plot_entropy_staircase(os.path.join(OUTPUT_DIR, 'fig_tdt_staircase.pdf'))
    
    print("\n--- All TDT figures generated successfully. ---")