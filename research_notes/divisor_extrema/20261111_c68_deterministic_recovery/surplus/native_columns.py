"""Replay stock-variable lifted tail columns on the original positive three-state kernel."""
from argparse import ArgumentParser
from fractions import Fraction as F
from pathlib import Path
import json
import sys
from terminal_words import column,matrix_value,y_next

def run(native):
    sys.path.insert(0,str(native.resolve()))
    from enterprise_math import brc_histogram as brc
    rates=(F(1,4),F(1),F(4))
    branch_count=0
    controls=[]
    for word in [(0,), (2,0),(0,1,2),(1,0,1,0),(0,0,1,0,0)]:
        for c in (sum(word)+2,11,23):
            y=F(1)
            for n in range(3,c+1):y=y_next(y,n)
            body=''.join('5'*m+'23' for m in word)+'5'*(c-sum(word)-2)
            for j,tail in enumerate(('557','575','755')):
                masses=[]
                for u in (F(0),F(1)):
                    prob=(F(7,8),u/8,(1-u)/8)
                    rows=[brc.weight_histogram([p] if p else []) for p in prob]
                    ns=[len(word),len(word),c,1]
                    for a in body+tail:
                        ix='2357'.index(a)
                        new=[brc.weight_histogram([]) for _ in range(3)]
                        for i,h in enumerate(rows):
                            if h.is_zero:continue
                            q=(rates[i] if a=='5' else 1)*ns[ix]/(ns[0]+ns[1]+rates[i]*ns[2]+ns[3])
                            dests=((0,F(7,8)),(i,F(1,8))) if a=='3' else ((min(i+1,2) if a=='2' else i,F(1)),)
                            for d,p in dests:
                                w=brc.histogram_serial(h,brc.weight_histogram([p*q]))
                                new[d]=brc.histogram_recoalesce(new[d],w)
                        ns[ix]-=1
                        rows=new
                    assert ns==[0,0,0,0]
                    branches=sum(x.count for x in rows)
                    assert branches==2**(len(word)+1)
                    branch_count+=branches
                    masses.append(sum(x.total_mass for x in rows))
                z=matrix_value(column(word,j),c,y)
                assert z==masses[1]/masses[0]
                controls.append(dict(word=word,c=c,tail=tail,ratio=str(z)))
    return dict(probabilities=2*len(controls),positive_branches_with_multiplicity=branch_count,controls=controls)

if __name__=='__main__':
    p=ArgumentParser(description=__doc__)
    p.add_argument('--native-root',type=Path,required=True)
    print(json.dumps(run(p.parse_args().native_root),indent=2))
