"""Direct rational evaluation of the original model and every offset cell for c=8."""
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path
import json
import subprocess

# The next function is reproduced from C80 check_native.py at 441853d82f262cceb29b631c737d67b9b79910f9.
def native_tail_ratios(c, v, w):
    def consume(masses, stock, symbol):
        weights = []
        for rate, mass in zip((Q(1,4), Q(1), Q(4)), masses):
            den = stock[0] + stock[1] + rate*stock[2] + stock[3]
            weights.append(mass * stock[symbol] * (rate if symbol == 2 else 1) / den)
        stock[symbol] -= 1
        if symbol == 0:
            return [Q(0), weights[0], weights[1]+weights[2]]
        if symbol == 1:
            return [(7*sum(weights)+weights[0])/8, weights[1]/8, weights[2]/8]
        return weights

    body = [2]*(c-v) + [0,1] + [2]*(v-w) + [0,1] + [2]*(w-2)
    tails = ((2,2,3),(2,3,2),(3,2,2))
    rows = []
    for prep in (0, 1):
        state = [Q(7),Q(prep),Q(1-prep)]
        stock = [2,2,c,1]
        for symbol in body:
            state = consume(state,stock,symbol)
        vals = []
        for tail in tails:
            copy_stock, copy_state = stock.copy(), state.copy()
            for symbol in tail:
                copy_state = consume(copy_state,copy_stock,symbol)
            vals.append(sum(copy_state))
        assert sum(vals) == sum(state)
        rows.append(vals)
    return [b/a for a,b in zip(*rows)]


def verify(c=8):
    p=((c**9).bit_length()-1)//4
    points=[]
    for v in range(2,c+1):
        for w in range(2,v+1):
            row=[]
            for stock in (c,c+1):
                values=native_tail_ratios(stock,v,w)
                row.append((max(values)/min(values)-1)*2**p)
            points.append(row)
    axes=[sorted({Q(0),Q(1),*((-row[k])%1 for row in points)}) for k in (0,1)]
    areas=[Q(0)]*len(points)
    for x0,x1 in zip(axes[0],axes[0][1:]):
        for y0,y1 in zip(axes[1],axes[1][1:]):
            labels=[((x+x0)//1,(y+y0)//1) for x,y in points]
            counts=Counter(labels)
            for i,k in enumerate(labels):
                if counts[k]==1:
                    areas[i]+=(x1-x0)*(y1-y0)
    scale=2**40
    keys=[sorted({row[k]+u for row in points for u in (0,1)}) for k in (0,1)]
    ranks=[{v:i for i,v in enumerate(key)} for key in keys]
    lines=[f'{len(points)} {len(keys[0])} {len(keys[1])}']
    lines.extend(' '.join(str((v*scale+Q(1,2))//1) for v in key) for key in keys)
    for x,y in points:
        lines.append(' '.join(map(str,(ranks[0][x],ranks[0][x+1],ranks[1][y],ranks[1][y+1]))))
    base=Path(__file__).resolve().parent
    out=subprocess.check_output([str(base/'individual')],input='\n'.join(lines)+'\n',text=True)
    for area,line in zip(areas,out.splitlines()):
        rounded,possible,robust=map(int,line.split())
        assert abs(area-Q(rounded,scale**2))<=Q(4*len(points),scale)
        assert (area>0,area==1)==(bool(possible),bool(robust))
    profile=next(r for r in json.loads((base/'individual_profiles.json').read_text()) if r['c']==c)
    mean=sum(areas)/len(areas)
    second=sum(a*a for a in areas)/len(areas)
    for label,value in [('mean_q_1e12',mean),('mean_q_squared_1e12',second),
                        ('independent_offsets_switch_1e12',2*(mean-second))]:
        low,high=profile[label]
        assert low<=value*10**12<=high
    for cutoff in (1,25,50,75,99):
        low,high=profile[f'q_ge_{cutoff}pct']
        assert low<=sum(a*100>=cutoff for a in areas)<=high
    return len(points),(len(axes[0])-1)*(len(axes[1])-1)

if __name__=='__main__':
    print('exact native labeled templates and phase rectangles:',*verify())
