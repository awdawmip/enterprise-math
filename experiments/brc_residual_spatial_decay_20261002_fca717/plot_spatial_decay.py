#!/usr/bin/env python3
"""Display only: proof checks use exact rational arithmetic in main script."""
import csv
from fractions import Fraction as F
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
def read(name):
    with (HERE/name).open() as f:
        return list(csv.DictReader(f))

fig, axes = plt.subplots(1,3,figsize=(14,5.0),layout='constrained')
data = read('spatial_residuals.csv')
for d in (1,2,3,4):
    rows = [r for r in data if int(r['dimension'])==d and r['step']=='1']
    axes[0].loglog([float(F(r['radius'])) for r in rows],
                  [-float(F(r['normalized_radial_fourth'])) for r in rows],
                  marker='.',label=f'd={d}')
axes[0].set(title='Statistical width\nsame exponent across dimensions',xlabel='RMS width (ell)',ylabel='Absolute normalized radial fourth cumulant')
axes[0].legend(fontsize=8)

rows=[r for r in read('local_shell_transport.csv') if int(r['dimension'])==3]
radius=[int(r['radius']) for r in rows]
axes[1].loglog(radius,[float(F(r['mean_arrival_mass'])) for r in rows],marker='o',label='Shell average')
axes[1].loglog(radius,[float(F(r['corner_arrival_mass'])) for r in rows],marker='o',label='Corner site')
axes[1].loglog(radius,[1/(24*r*r) for r in radius],linestyle='--',color='black',label='1/(24 r^2)')
axes[1].set(title='Conserved local transport\nshell mean versus a corner',xlabel='Graph radius (r)',ylabel='Arrival mass')
axes[1].legend(fontsize=8)

ell=list(range(2,25,2))
for label,amp,p in [('Third cumulant',3,1),('Fourth cumulant',1,2),('Sixth cumulant',455,4)]:
    axes[2].loglog(ell,[amp/r**p for r in ell],marker='.',label=f'{label}: ell^-{p}')
axes[2].set(title='One iid process\nthree observers, three exponents',xlabel='RMS width (ell)',ylabel='Absolute standardized cumulant')
axes[2].legend(fontsize=8)
for ax in axes:
    ax.grid(alpha=.16,which='both')
    ax.spines[['top','right']].set_visible(False)
fig.suptitle('Inverse-square resemblance does not identify a force law',fontsize=15)
fig.savefig(HERE/'spatial_decay.png',dpi=160,bbox_inches='tight')
fig.savefig(HERE/'spatial_decay.svg',bbox_inches='tight')
