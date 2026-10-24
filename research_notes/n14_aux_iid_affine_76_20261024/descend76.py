#!/usr/bin/env python3
"""Exact ordered suffix terminal provenance after the new A76 state."""
from fractions import Fraction as F
from collections import defaultdict,Counter
import json,verify_n14_76 as m

def audit():
    records=defaultdict(lambda:[0,F(),F()])
    def visit(state,p,q,length):
        z=m.act(state)
        if z!='C':
            r=records[(state,z,length)];r[0]+=1;r[1]+=p;r[2]+=q
            return
        assert state[0]<m.N
        for i in range(3):
            visit(m.child(state,i),p*m.P[i],q*m.Q[i],length+1)
    visit(m.A,F(1),F(1),0)
    Psum=sum((v[1] for v in records.values()),F())
    Qsum=sum((v[2] for v in records.values()),F())
    eP=sum((v[1] for (_,z,_),v in records.items() if z=='Q'),F())
    eQ=sum((v[2] for (_,z,_),v in records.items() if z=='P'),F())
    tP=sum((length*v[1] for (_,_,length),v in records.items()),F())
    tQ=sum((length*v[2] for (_,_,length),v in records.items()),F())
    assert (Psum,Qsum)==(F(1),F(1))
    assert (eP,eQ,tP,tQ)==m.suffix(m.A)
    lengths={str(i):sum(v[0] for (_,_,k),v in records.items() if k==i) for i in range(1,5)}
    suffix_words=sum(v[0] for v in records.values())
    assert (len(records),suffix_words,lengths)==(12,21,{'1':2,'2':0,'3':4,'4':15})
    first=m.firsthit(m.A)[2]
    assert first==210
    return {'status':'AUTHOR_ORDERED_PROVENANCE_EXACT_PASS',
            'firsthit_A':first,'suffix_terminal_classes':len(records),
            'distinct_terminal_states':len(set(k[0] for k in records)),
            'suffix_words':suffix_words,
            'truncated_terminal_ordered_histories':first*suffix_words,
            'suffix_length_distribution':lengths,
            'weighted_suffix_risks':list(map(str,(eP,eQ,tP,tQ))),
            'terminal_evidence':[{'state':list(state),'decision':z,'suffix_length':k,
               'word_count':v[0],'P_mass':str(v[1]),'Q_mass':str(v[2])}
                for (state,z,k),v in sorted(records.items())]}
if __name__=='__main__':print(json.dumps(audit(),indent=2))
