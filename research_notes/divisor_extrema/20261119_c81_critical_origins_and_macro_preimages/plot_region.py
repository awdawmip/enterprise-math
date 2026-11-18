"""Draw the disputed and certified macroregions in the original source triangle."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
from matplotlib.patches import Patch

root=Path(__file__).resolve().parent
record=json.loads((root/'region_cells.json').read_text())[-1]
n=record['n']
fig,ax=plt.subplots(figsize=(7.5,4.6))
fig.subplots_adjust(left=.10,right=.67,bottom=.15,top=.91)
ax.fill([0,1,1],[0,0,1],color='#edeff0')
for low,high,color in [(0,(2/11)**(4/9),'#c38a58'),
                       ((2/11)**(4/9),4**(-4/9),'#edcc9e')]:
    ax.fill([0,1,1],[0,low,high],color=color)
# Additional almost-everywhere triple region where the d=0 endpoint is physical.
xcut=(3/10)**(4/15)
ax.fill([0,xcut,xcut],[0,xcut*(2/11)**(4/9),xcut*4**(-4/9)],color='#c38a58')
cells=[]
for i,j,k in record['row_runs']:
    x0,x1=(i/n)**(4/15),((i+1)/n)**(4/15)
    r0,r1=(j/n)**(4/9),(k/n)**(4/9)
    cells.append([(x0,x0*r0),(x1,x1*r0),(x1,x1*r1),(x0,x0*r1)])
ax.add_collection(PolyCollection(cells,facecolors='#167767',edgecolors='none',
                                  antialiaseds=False))
ax.set(xlim=(0,1),ylim=(0,1),aspect='equal',xlabel=r'$v/c$',ylabel=r'$w/c$')
ax.spines[['top','right']].set_visible(False)
colors=['#c38a58','#edcc9e','#167767','#edeff0']
labels=['At least three (a.e.)','At least two','Exactly one (certified)','Unclassified here']
ax.legend([Patch(color=c) for c in colors],labels,title='Macroscopic preimages',
          loc='center left',bbox_to_anchor=(1.03,.52),frameon=False,
          borderpad=0.2,labelspacing=1.1)
fig.suptitle('Arrangements with the same limiting pair of readings',
             x=.08,horizontalalignment='left',fontsize=14)
matplotlib.rcParams['svg.fonttype']='none'
matplotlib.rcParams['svg.hashsalt']='c81-region'
fig.savefig(root/'macro_regions.svg',metadata={'Date':None})
