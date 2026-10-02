#!/usr/bin/env python3
"""Optional visualization; floats here are display only, never proof inputs."""
import csv
from fractions import Fraction
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
with (HERE/'residuals.csv').open() as f:
    rows = list(csv.DictReader(f))
fig, axes = plt.subplots(1, 3, figsize=(13, 3.9), layout='constrained')
names = [('decay', 'Linear decay'), ('diffusion', 'Drift diffusion'), ('oscillator', 'Rational rotation')]
for ax, (name, label) in zip(axes, names):
    data = [r for r in rows if r['model'] == name]
    t = [int(r['n']) for r in data]
    if name == 'oscillator':
        y = [float(Fraction(r['radial_fourth_cumulant'])/(2*Fraction(r['variance_x']))**2) for r in data]
        ylabel = 'Radial cumulant / (trace covariance)^2'
    else:
        y = [float(Fraction(r['excess_kurtosis_x'])) for r in data]
        ylabel = 'Fourth cumulant / variance^2'
    ax.axvspan(0, 8, color='#e6e9ee', label='Calibration 1–8')
    ax.axhline(0, color='#9a4960', linestyle='--', label='Gaussian reference')
    ax.plot(t, y, color='#245fc0', linewidth=2, label='BRC branch residual')
    ax.set(title=label, xlabel='Step', ylabel=ylabel, xlim=(1,64))
    ax.grid(alpha=.15)
    ax.spines[['top','right']].set_visible(False)
axes[0].legend(fontsize=8, loc='lower right')
fig.suptitle('Equal means and covariances do not fix the residual shape', fontsize=15)
fig.savefig(HERE/'residual_laws.png', dpi=160)
fig.savefig(HERE/'residual_laws.svg')
