#!/usr/bin/env python3
"""R284DW, exact frozen-Port 4096-state extension, standard library only.

All arithmetic is integer.  The displayed affine windows are certified for
EVERY integer in each window by checking endpoints of each arc-affine slab.
"""
import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path

P = 17179869143
D = (1120832, 6, 13, 1651128)
Z0 = (0, 390139, 394465, 1497639)
SELECT = (0, 1, 2, 4, 5, 6)
FROZEN_SHA = 'b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4'

# (X,W,lo,hi,winning labels,slope,intercept); slope/intercept null for ties.
WINDOWS = (
 (0,0,8199694214,8215340596,(53,),1,197360345),
 (0,0,8215340597,8238895431,(53,),-1,16628041538),
 (0,0,8238895432,8242919833,(2,),1,150250675),
 (0,0,8242919834,8294927059,(2,),-1,16636090342),
 (0,0,8294927060,8319365309,(44,),1,46236223),
 (0,0,8319365310,8434887417,(44,),-1,16684966842),
 (0,0,8434887418,8434887418,(44,63),None,None),
 (0,0,8434887419,8507286428,(63,),1,-184807994),
 (0,1,14508253482,14761913799,(21,),-1,22929044144),
 (0,1,14761913800,14818876290,(45,),1,-6594783455),
 (1,0,4471172719,4676263589,(32,),-1,12686611854),
 (1,0,4676263590,4676263590,(32,56),None,None),
 (1,0,4676263591,4781786875,(56,),1,3334084674),
 (1,1,15577040133,15706587425,(8,),-1,23778878722),
 (1,1,15706587426,15886415284,(55,),1,-7634296129),
)

def det(L, top):
    u1,a,x,y,u2,w,b,z,u3,g,h,r = L
    t,s = 6-a, 13-b
    u=t*s-x*w
    v=-r*u-z*(t*h+x*g)-y*(w*h+s*g)
    p1,p2=s*u1+x*u2,t*u2+w*u1
    q1=-r*p1-u1*z*h+x*z*u3+y*(u2*h+s*u3)
    q2=-r*p2+t*z*u3+u1*z*g+y*(w*u3-u2*g)
    q3=u*u3+p1*g+p2*h
    k=(u*D[3]+v,p1*D[3]+q1,p2*D[3]+q2,q3)
    base=D[0]*k[0]-Z0[1]*k[1]-Z0[2]*k[2]-Z0[3]*k[3]-sum(k)
    return base-sum(k[j] for j in range(4) if top & (1<<j))

def arcs():
    out=[]
    for label in range(64):
        lo=[1]*12; hi=[2]*12
        for j,pos in enumerate(SELECT):
            lo[pos]=hi[pos]=1+((label>>(5-j))&1)
        high=det(hi,15)
        out.append((high%P,det(lo,0)-high))
    assert len(out)==64 and all(0<w<P//2 for a,w in out)
    return out

def dist(x,arc):
    a,w=arc
    d=(x-a)%P
    return 0 if d<=w else min(d-w,P-d)

def q(X,W):
    return 3992-145*X-146*W-108*X*W

def source(X,Y,Z,U2,U1,U0,W,R,u3,g,h,B):
    lo=(1,2,1+X,1+Y,1,1+W,2,1+Z,u3,g,h,1+R)
    return lo,U2+2*U1+4*U0+8*B

def critical_integer_cuts(L,H,arc):
    # On integer x, each arc distance has slope -1,0,+1 between cuts.
    a,w=arc
    middle=(P+w)//2
    return [x for j in range(-2,3)
            for x in (a+j*P,a+w+1+j*P,a+middle+1+j*P)
            if L<x<=H]

def certify_windows(A):
    check_count=0; slab_count=0
    by_pair={}
    for X,W,lo,hi,ids,slope,intercept in WINDOWS:
        by_pair.setdefault((X,W),[]).append((lo,hi))
        if len(ids)>1:
            vals=[dist(lo,a) for a in A]
            assert tuple(i for i,d in enumerate(vals) if d==max(vals))==ids
            check_count+=64
            continue
        cuts=sorted({lo,hi+1} | {k for a in A for k in critical_integer_cuts(lo,hi,a)})
        for s,e in zip(cuts,cuts[1:]):
            slab_count+=1
            for x in {s,e-1}:
                values=[dist(x,a) for a in A]
                assert values[ids[0]]==slope*x+intercept
                assert all(values[ids[0]]>values[j] for j in range(64) if j!=ids[0])
                check_count+=64
    for pair,parts in by_pair.items():
        assert all(parts[i][1]+1==parts[i+1][0] for i in range(len(parts)-1)), pair
    return check_count,slab_count

def main():
    A=arcs()
    edge_checks,slabs=certify_windows(A)
    stats={key:{'min_det':10**30,'max_det':-1,'min_residue':P,'max_residue':-1,'n':0}
           for key in itertools.product((0,1),repeat=2)}
    counts=Counter(); labels=Counter(); gapped=Counter(); hashout=hashlib.sha256()
    min_margin=10**30; min_margin_witness=None; max_gap=0
    for bits in itertools.product((0,1),repeat=8):
        X,Y,Z,U2,U1,U0,W,R=bits
        for u3,g,h in itertools.product((1,2),repeat=3):
            low,top=source(*bits,u3,g,h,0)
            q3=(44-(1+X)*(1+W))*u3+(12+X)*g+(5+W)*h
            min_signed=None; winning_label=None
            for B in (0,1):
                T=det(low,top+8*B)
                residue=T-q(X,W)*P
                assert 0<=residue<P
                assert residue==T%P
                vals=[dist(residue,a) for a in A]
                ordered=sorted(vals,reverse=True)
                value=ordered[0]
                assert ordered[0]>ordered[1]
                win=vals.index(value)
                matches=[(ids,sl,c) for xx,ww,a,b,ids,sl,c in WINDOWS
                         if (xx,ww)==(X,W) and a<=residue<=b]
                assert len(matches)==1
                ids,slope,intercept=matches[0]
                assert ids==(win,)
                assert value==slope*residue+intercept
                if B==0:
                    winning_label=win; min_signed=slope
                    margin=value-ordered[1]
                    if margin<min_margin:
                        min_margin=margin;min_margin_witness=(bits,u3,g,h,residue)
                else:
                    assert win==winning_label
                    assert value==previous_value-min_signed*q3
                previous_value=value
                bucket=stats[(X,W)]
                bucket['min_det']=min(bucket['min_det'],T)
                bucket['max_det']=max(bucket['max_det'],T)
                bucket['min_residue']=min(bucket['min_residue'],residue)
                bucket['max_residue']=max(bucket['max_residue'],residue)
                bucket['n']+=1
                labels[win]+=1
                counts['direct_arc_calls']+=64
                counts['states']+=1
                hashout.update(residue.to_bytes(8,'big'))
                hashout.update(bytes([win]))
                hashout.update(value.to_bytes(8,'big'))
            assert q3<=120
            assert q3>=59
            gapped[q3]+=1
            max_gap=max(max_gap,q3)
            counts['B_flip_pairs']+=1
    assert counts['states']==4096 and counts['B_flip_pairs']==2048
    assert min_margin==37469 and min_margin>2*max_gap
    assert len(labels)==10 and sum(labels.values())==4096
    assert len(gapped)==19 and gapped[59]==64 and gapped[120]==192
    for k,st in stats.items():
        assert st['n']==1024 and st['min_det']>=q(*k)*P and st['max_det']<(q(*k)+1)*P
    # Independent sharp coordinate-free-cube obstruction: one original-base counterexample each.
    changes={}
    for name,pos,newval in (('u1',0,2),('a',1,1),('u2',4,2),('b',6,1)):
        v=[1,2,1,1,1,1,2,1,1,1,1,1]
        v[pos]=newval
        changes[name]=det(v,0)//P-q(0,0)
    assert changes=={'u1':-450,'a':1147,'u2':-189,'b':393}
    return {'schema':'R284DW_FROZEN_4096_QUOTIENT_STABILITY_V1',
            'source':'R284CO@acba2d8667903434aaa2a10720f43637fcc2421b',
            'frozen_SHA256':FROZEN_SHA,'P':P,
            'scientific_status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
            'state_count':counts['states'],'B_flip_pairs':counts['B_flip_pairs'],
            'arc_distance_checks':counts['direct_arc_calls'],
            'exact_band_endpoints':{f'{X}{W}':st for (X,W),st in sorted(stats.items())},
            'all_integer_windows':len(WINDOWS),
            'unique_affine_windows':sum(len(ids)==1 for *_,ids,sl,c in WINDOWS),
            'tied_integer_positions':[(xx,ww,a,ids) for xx,ww,a,b,ids,sl,c in WINDOWS if len(ids)>1],
            'window_slab_count':slabs,'window_endpoint_arc_checks':edge_checks,
            'winner_label_counts':dict(sorted(labels.items())),
            'B_flip_gap_histogram':dict(sorted(gapped.items())),
            'B_flip_gap_min':min(gapped),'B_flip_gap_max':max(gapped),
            'B_flip_margin_min':min_margin,
            'B_flip_margin_min_witness':min_margin_witness,
            'free_coordinate_obstructions_quotient_delta':changes,
            'ordered_state_residue_label_value_sha256':hashout.hexdigest(),
            'all_exact_checks_passed':True,'review':'NOT_REVIEWED'}

if __name__=='__main__':
    report=main()
    path=Path(__file__).with_name('R284DW_eightfold_port_extension_certificate.json')
    path.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2,ensure_ascii=False))
