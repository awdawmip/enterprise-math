#!/usr/bin/env python3
"""R743: exact stock-2, four-PASS, arc-preserving BRC scheduler certificate."""
from collections import defaultdict
from itertools import product
import json

LOOPS = {
 'A': {'I':('012','014','013','012'), 'P':('012','023','013','012'), 'Q':('012','023','123','012')},
 'B': {'I':('012','123','124','012'), 'P':('012','023','013','012'), 'Q':('012','123','013','012')},
}
CODE = {
 'A': {'012>014':'F', '012>023':'R', '014>013':'R', '023>013':'F', '023>123':'R', '013>012':'F', '123>012':'F'},
 'B': {'012>023':'F', '012>123':'R', '023>013':'R', '123>124':'R', '123>013':'F', '013>012':'F', '124>012':'F'},
}
PERM = {
 'A': {'I':(0,1,2), 'P':(0,2,1), 'Q':(1,0,2)},
 'B': {'I':(0,1,2), 'P':(0,2,1), 'Q':(2,1,0)},
}
EARLY = {'A':'Q', 'B':'I'}
NAMED = {
 'A': {'III':'012','IIP':'021','IIQ':'102','IPQ':'201','IQP':'120','PQP':'210'},
 'B': {'III':'012','IIP':'021','IIQ':'210','IPQ':'120','IQP':'201','PQP':'102'},
}

def arc_word(carrier, symbol):
    p=LOOPS[carrier][symbol]
    return ''.join(CODE[carrier][p[j]+'>'+p[j+1]] for j in range(3))

def event_word(carrier,symbol):
    w=arc_word(carrier,symbol)
    return w[0]+'F'+w[1:] if symbol==EARLY[carrier] else w+'R'

def execute_pulses(w):
    x,y=1,1
    for ch in w:
        if ch=='F': x-=1;y+=1
        else: x+=1;y-=1
        assert 0<=x<=2 and 0<=y<=2,(w,ch,x,y)
    return x,y

def safe_prefix(w):
    x,y=1,1
    for ch in w:
        if ch=='F':x-=1;y+=1
        else:x+=1;y-=1
        if min(x,y)<0 or max(x,y)>2:return False
    return True

def relation(carrier,word):
    h=(0,1,2)
    for symbol in word: h=tuple(h[i] for i in PERM[carrier][symbol])
    return ''.join(map(str,h))

def certify():
    result={'schema':'R743_EARLY_COMPENSATION_V1','status':'PASS','root_stock':[1,1],
            'local_port_capacity':2,'events_per_generator':4,
            'exhaustive_generators_up_to':8,'carriers':{}}
    for carrier in ('A','B'):
        d=CODE[carrier];loops=LOOPS[carrier]
        bysrc=defaultdict(list)
        for e,s in d.items(): bysrc[e.split('>')[0]].append(s)
        assert all(len(set(v))==len(v) for v in bysrc.values())
        words={g:event_word(carrier,g) for g in 'IPQ'}
        assert len(set(words.values()))==3
        for g,w in words.items():
            assert len(w)==4 and w.count('F')==w.count('R')==2
            assert execute_pulses(w)==(1,1)
            assert loops[g][0]==loops[g][-1]=='012'
        assert set(words.values())=={'FRFR','RFFR','RFRF'}
        arcs=sorted(d);root_only_good=0;injective=0
        for bits in product('FR',repeat=len(arcs)):
            trial=dict(zip(arcs,bits));sources=defaultdict(list)
            for e,s in trial.items():sources[e.split('>')[0]].append(s)
            if any(len(set(v))!=len(v) for v in sources.values()):continue
            injective+=1
            raw=[''.join(trial[loops[g][j]+'>'+loops[g][j+1]] for j in range(3)) for g in 'IPQ']
            if all(safe_prefix(w) for w in raw):root_only_good+=1
        assert root_only_good==0 and injective==32
        for k in range(9):
            n=0;seen=set()
            for letters in product('IPQ',repeat=k):
                word=''.join(letters);pulses=''.join(words[g] for g in letters)
                assert len(pulses)==4*k and pulses.count('F')==pulses.count('R')==2*k
                assert execute_pulses(pulses)==(1,1)
                seen.add(relation(carrier,word));n+=1
            assert n==3**k
            assert len(seen)==(1 if k==0 else 3 if k==1 else 5 if k==2 else 6)
        for w,name in NAMED[carrier].items():assert relation(carrier,w)==name
        result['carriers'][carrier]={
          'codebook':d,'generator_arc_codes':{g:arc_word(carrier,g) for g in 'IPQ'},
          'generator_event_words':words,'early_helper_generator':EARLY[carrier],
          'root_only_injective_codebooks_checked':injective,
          'root_only_stock2_feasible_codebooks':root_only_good,
          'history_count_each_carrier':sum(3**k for k in range(9)),
          'six_relation_witness':NAMED[carrier]}
    return result

if __name__=='__main__':
    print(json.dumps(certify(),ensure_ascii=False,sort_keys=True,indent=2))
