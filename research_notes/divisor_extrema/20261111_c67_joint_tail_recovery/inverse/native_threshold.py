"""Direct positive three-state forward likelihoods at the new certificate's boundaries."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from pathlib import Path
import json
def native(k,gaps):
    tails=('557','575','755')
    rates=(Q(1,4),Q(1),Q(4))
    def forward(word,s):
        stock=dict(zip('2357',(k,k,k+1,1)))
        w=[Q(j==s) for j in range(3)]
        for t in word:
            nxt=[Q(0) for j in range(3)]
            for j,v in enumerate(w):
                den=stock['2']+stock['3']+stock['7']+stock['5']*rates[j]
                hit=v*stock[t]*(rates[j] if t=='5' else 1)/den
                if t=='3':
                    nxt[0]+=7*hit/8;nxt[j]+=hit/8
                else:
                    nxt[min(2,j+1) if t=='2' else j]+=hit
            stock[t]-=1
            w=nxt
        assert all(v==0 for v in stock.values()) and min(w)>0
        return sum(w)
    word='23'.join('5'*v for v in gaps)
    ratios=[forward(word+t,0)/forward(word+t,1) for t in tails]
    return max(ratios)/min(ratios)
if __name__=='__main__':
    parser=ArgumentParser(description=__doc__)
    parser.add_argument('--frontier',type=Path,required=True)
    parser.add_argument('--grid',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    grid=json.loads(args.grid.read_text());front=json.loads(args.frontier.read_text())
    samples=[]
    for k,word,target in [(z['k'],z['gaps'],1+Q(z['H_minus_one_exact'])) for z in front['records'] if 'H_minus_one_exact' in z]+[(8,[1]*7+[0,0],Q(grid['smallest_H']))]:
        value=native(k,word)
        assert value==target
        samples.append(dict(k=k,gaps=word,H=str(value)))
    args.output.write_text(json.dumps(dict(positive_native_three_tail_replays=samples),indent=2)+'\n')
