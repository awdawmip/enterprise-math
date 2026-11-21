#!/usr/bin/env python3
"""R284CL: exact finite population Port-fiber k-fold support spectrum.
Independent of native BRC claims, on frozen Port observer only.
"""
import hashlib, json
from itertools import product
from collections import Counter

P=17179869143
D=(1120832,6,13,1651128)
Z=(0,390139,394465,1497639)
SELECT=(0,1,2,4,5,6)
FROZEN_SHA='b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4'

def determinant(lower, top):
    u1,a11,x,y,u2,w,a22,z,u3,g,h,r=lower
    t,s=6-a11,13-a22
    u=t*s-x*w
    v=-r*u-z*(t*h+x*g)-y*(w*h+s*g)
    p1,p2=s*u1+x*u2,t*u2+w*u1
    q1=-r*p1-u1*z*h+x*z*u3+y*(u2*h+s*u3)
    q2=-r*p2+t*z*u3+u1*z*g+y*(w*u3-u2*g)
    q3=u*u3+p1*g+p2*h
    k=(u*D[3]+v,p1*D[3]+q1,p2*D[3]+q2,q3)
    base=D[0]*k[0]-Z[1]*k[1]-Z[2]*k[2]-Z[3]*k[3]-sum(k)
    return base-sum(k[j] for j in range(4) if top & (1<<j))

def lower_state(key, fill):
    arr=[fill]*12
    for j,pos in enumerate(SELECT):
        arr[pos]=1+((key>>(5-j))&1)
    return arr

def arc_data():
    return [(determinant(lower_state(key,2),15)%P,
             determinant(lower_state(key,1),0)-determinant(lower_state(key,2),15))
            for key in range(64)]

def distance_point_arc(x, a, w):
    delta=(x-a)%P
    if delta<=w:return 0
    return min(delta-w, P-delta)

def generate_codewords():
    digest=hashlib.sha256()
    word_rows=[]
    for upper in product((1,2), repeat=4):
        top=sum((v-1)<<j for j,v in enumerate(upper))
        for lower in product((1,2),repeat=12):
            x=determinant(lower,top)%P
            digest.update(x.to_bytes(8,'big'))
            word_rows.append((x,upper,lower))
    assert digest.hexdigest()==FROZEN_SHA, (digest.hexdigest(),FROZEN_SHA)
    return word_rows

def main():
    arcs=arc_data()
    assert len(arcs)==64 and all(0<w<P//2 for a,w in arcs)
    words=generate_codewords()
    distribution=Counter()
    sums=[0]*64
    maxima=[(-1,None)]*64
    radii=(0,29,30,591,592,220306652,765828248,1260000000,3000000000,8400000000)
    profiles={str(q):Counter() for q in radii}
    exact_own_hit=0
    for idx,(x,top,lower) in enumerate(words):
        dists=sorted(distance_point_arc(x,a,w) for a,w in arcs)
        n0=sum(d==0 for d in dists)
        distribution[n0]+=1
        for k,d in enumerate(dists):
            sums[k]+=d
            if d>maxima[k][0]:maxima[k]=(d,idx)
        for q in radii:
            profiles[str(q)][sum(d<=q for d in dists)]+=1
        own_key=sum((lower[pos]-1)<<(5-j) for j,pos in enumerate(SELECT))
        if distance_point_arc(x,*arcs[own_key])==0:exact_own_hit+=1
        else:raise AssertionError(('own group missing',idx))
    assert exact_own_hit==65536
    radius=[m[0] for m in maxima]
    assert radius==sorted(radius)
    assert radius[0]==0
    record={
       'schema':'R284CL_FINITE_CODEWORD_SUPPORT_V1',
       'inputs':{'p':P,'D':D,'Z':Z,'SELECT':SELECT,'frozen_sha256':FROZEN_SHA},
       'codeword_count':len(words),'arcs_count':len(arcs),'own_group_membership':exact_own_hit,
       'zero_radius_multiplicity_distribution':{str(i):distribution[i] for i in sorted(distribution)},
       'kfold_population_radius':radius,
       'kfold_witnesses':[{'k':k+1,'radius':d,'codeword_index':idx,'codeword':words[idx][0]} for k,(d,idx) in enumerate(maxima)],
       'sum_kth_nearest_distance':sums,
       'candidate_profiles':{q:{str(i):c[i] for i in sorted(c)} for q,c in profiles.items()},
       'verification':{'arithmetic':'Python exact integer','scope':'all 65536 matrices times 64 closed arcs','distance_evaluations':65536*64,'certainty':'finite exhaustive; no independent review'}
    }
    print(json.dumps(record,indent=2,ensure_ascii=False))

if __name__=='__main__':main()
