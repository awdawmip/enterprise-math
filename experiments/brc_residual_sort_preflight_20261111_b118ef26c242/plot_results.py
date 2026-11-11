from pathlib import Path
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

root=Path(__file__).resolve().parent
with (root/'theory3/child_gate_exact.csv').open() as f:
    probabilities=[r for r in csv.DictReader(f) if int(r['training_misses'])==0 and int(r['n'])==400000 and int(r['total_misses'])%4000==0 and int(r['total_misses'])<=232000]
with (root/'phase6/results/all_methods.csv').open() as f:
    times={(r['family'],r['method']):float(r['median_us'])/1000 for r in csv.DictReader(f)}
with (root/'phase6/results/comparisons.csv').open() as f:
    winners={r['family']:r['reference'] for r in csv.DictReader(f) if r['comparison']=='fastest_29'}
fig,axes=plt.subplots(1,2,figsize=(11.4,4.35),gridspec_kw={'width_ratios':[1,1.22]})
a,b=axes
for k,color in [(64,'#517998'),(1024,'#a8441d')]:
    rows=sorted([r for r in probabilities if int(r['probe_size'])==k],key=lambda r:int(r['total_misses']))
    a.plot([int(r['total_misses'])/400000 for r in rows],[float(r['p_trigger_given_complete']) for r in rows],
           marker='o',ms=4.3,color=color,lw=2.5,label=f'{k:,} probes')
a.yaxis.set_major_formatter(PercentFormatter(1))
a.xaxis.set_major_formatter(PercentFormatter(1,decimals=0))
a.set(xlabel='True residual fraction',ylabel='Probability of early fallback',ylim=(-.025,1.05))
a.set_title('Detection on a 400,000-value node',loc='left',fontweight='bold',fontsize=12)
a.legend(frameon=False,loc='upper left')
labels=['Million, 40/30/30','125k, 37/33/30','150k, shifted bands']
families=['new_balanced_million','new_three_37_33_30','new_wider_shifted']
for method,delta,color,label in [('deep_gate',-.22,'#a8441d','1,024 probes'),('radix',0,'#24685b','Direct child radix'),('winner',.22,'#5f6977','Fastest of 29 controls')]:
    vals=[]
    for family in families:
        key=winners[family] if method=='winner' else method
        vals.append(times[family,'certified_combined_1024']/times[family,key])
    b.barh([i+delta for i in range(3)],vals,.19,color=color,label=label)
b.axvline(1,lw=1,color='#53575a',ls='--')
b.set_yticks(range(3),labels)
b.invert_yaxis()
b.set_xlabel('Speed ratio to fourth-round sorter (higher is faster)')
b.set_title('Families with large residual children',loc='left',fontweight='bold',fontsize=12)
b.legend(loc='lower center',bbox_to_anchor=(.46,-.46),ncol=2,frameon=False,fontsize=9)
for ax in axes:
    ax.spines[['top','right']].set_visible(False)
    ax.grid(color='#c4c8c8',alpha=.35,axis='y' if ax==a else 'x')
    ax.set_axisbelow(True)
fig.subplots_adjust(left=.075,right=.98,bottom=.27,top=.86,wspace=.48)
fig.savefig(root/'results.png',dpi=170,bbox_inches='tight')
