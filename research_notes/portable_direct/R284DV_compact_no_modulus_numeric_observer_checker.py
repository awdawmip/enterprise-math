#!/usr/bin/env python3
"""R284DV: exact compact arithmetic numeric Port observer without modulo or arcs."""
import itertools, json
from collections import Counter
from pathlib import Path
from R284DT_seven_window_affine_checker import P,det,lower,residue,arcs,dist,WINDOWS
from R284DU_boolean_winner_classifier_checker import classify

COEFF={label:(s,c) for label,lo,hi,s,c,margin in WINDOWS}
QUOTIENT={(0,0):3992,(0,1):3846,(1,0):3847,(1,1):3593}

def compact_det(v,B):
    X,Y,Z,U2,U1,U0,W,R=v
    x,y,z,w,r=1+X,1+Y,1+Z,1+W,1+R
    u=44-x*w
    p1,p2=11+x,4+w
    v0=-r*u-z*(4+x)-y*(w+11)
    q1=-r*p1+X*z+12*y
    q2=-r*p2+5*z+y*W
    k0=1651128*u+v0
    k1=1651128*p1+q1
    k2=1651128*p2+q2
    k3=60-X*W
    return (1120831-U2)*k0-(390140+U1)*k1-(394466+U0)*k2-(1497640+B)*k3

def quotient(X,W):return 3992-145*X-146*W-108*X*W

def observe(v,B):
    X,Y,Z,U2,U1,U0,W,R=v
    d=compact_det(v,B)
    t=d-quotient(X,W)*P
    label=classify(*v)
    s,c=COEFF[label]
    return s*t+c,label

def verify():
    A=arcs();assert len(A)==64
    vals={pair:[] for pair in QUOTIENT}
    labels=Counter(); gaps=Counter()
    num_calls=0
    for v in itertools.product((0,1),repeat=8):
        X,Y,Z,U2,U1,U0,W,R=v
        low=1056+(X<<9)+(Y<<8)+(Z<<4)+(W<<6)+R
        for B in (0,1):
            up=(U2<<3)+(U1<<2)+(U0<<1)+B
            idx=(up<<12)|low
            top=sum(((up>>(3-j))&1)<<j for j in range(4))
            old=det(lower(low),top)
            d=compact_det(v,B)
            assert d==old
            q=quotient(X,W)
            assert q==QUOTIENT[X,W] and q*P<=d<(q+1)*P
            assert d-q*P==residue(idx)
            value,label=observe(v,B)
            direct=[dist(d-q*P,a) for a in A]
            assert value==max(direct) and direct.index(value)==label and direct.count(value)==1
            num_calls+=len(A)
            vals[X,W].append(d)
            if B==0:labels[label]+=1
        d0,_=observe(v,0);d1,_=observe(v,1)
        assert abs(d0-d1)==60-X*W
        gaps[abs(d0-d1)]+=1
    assert num_calls==32768
    assert labels==Counter({21:45,32:21,44:37,45:19,55:64,56:43,63:27})
    assert gaps==Counter({60:192,59:64})
    bounds={}
    for (X,W),seq in sorted(vals.items()):
        mn,mx=min(seq),max(seq);q=QUOTIENT[X,W]
        assert len(seq)==128 and q*P<=mn<=mx<(q+1)*P
        bounds[f'{X}{W}']={'q':q,'states':128,'min_det':mn,'max_det':mx,
                           'min_residue':mn-q*P,'max_residue':mx-q*P,
                           'lower_slack':mn-q*P,'upper_slack':(q+1)*P-1-mx}
    return {'schema':'R284DV_COMPACT_INTEGER_NO_MODULUS_OBSERVER_V1',
            'status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
            'domain':'R284DQ/R284DT frozen 512 witness states, 9 input bits',
            'source_pin':'R284CO@acba2d8667903434aaa2a10720f43637fcc2421b',
            'q_expression':'3992-145X-146W-108XW',
            'quotient_bounds':bounds,'states_checked':512,
            'original_det_equal_compact_expression':True,
            'no_modulus_numeric_output_matches_direct_64_arc':True,
            'verification_point_arc_calls':num_calls,
            'witness_pair_gap_counts':dict(sorted(gaps.items())),
            'winner_label_counts':dict(sorted(labels.items())),
            'construction_modulo_calls':0,'construction_arc_calls':0,'construction_event_queries':0,
            'review':'NOT_REVIEWED'}

if __name__=='__main__':
    c=verify()
    Path(__file__).with_name('R284DV_compact_no_modulus_numeric_observer_certificate.json').write_text(json.dumps(c,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print(json.dumps(c,indent=2,ensure_ascii=False))
