#!/usr/bin/env python3
"""R749SNH: Fraction-only complete joint-vertex certificate.
No dependencies beyond Python standard library; no project/native X6 operation.
"""
from fractions import Fraction as Q
from itertools import combinations, product
import json

AD = list(product((1, -1), repeat=2))
SIGNS = list(product((1, -1), repeat=2))


def solve(rows, rhs):
    n = len(rhs)
    a = [[Q(x) for x in row] + [Q(v)] for row, v in zip(rows, rhs)]
    for j in range(n):
        pivot = next((k for k in range(j, n) if a[k][j] != 0), None)
        if pivot is None:
            return None
        a[j], a[pivot] = a[pivot], a[j]
        scale = a[j][j]
        a[j] = [x / scale for x in a[j]]
        for k in range(j + 1, n):
            scale = a[k][j]
            if scale:
                a[k] = [a[k][i] - scale * a[j][i] for i in range(n + 1)]
    ans = [Q(0)] * n
    for j in reversed(range(n)):
        ans[j] = a[j][-1] - sum(a[j][i] * ans[i] for i in range(j+1,n))
    return tuple(ans)


def constraints(lo, hi):
    # joint variables x = (s, h, U+, U-, W+, W-); all affine >= inequalities.
    L = []
    for a,d in AD:
        row=[Q(d), Q(a*d), Q(-int(a==1)), Q(-int(a==-1)), Q(-int(d==1)), Q(-int(d==-1))]
        L.append((row, -1-Q(a,2)))
    for j in range(2,6):
        row = [Q(0)]*6
        row[j]=Q(1)
        L.append((row,Q(0)))
    L.append(([Q(1),0,0,0,0,0], Q(lo)))
    L.append(([-Q(1),0,0,0,0,0], -Q(hi)))
    return L


def vertices(lo, hi):
    C=constraints(lo,hi)
    verts={}
    nonsingular=feasible=0
    for inds in combinations(range(len(C)),6):
        v=solve([C[i][0] for i in inds],[C[i][1] for i in inds])
        if v is None:
            continue
        nonsingular+=1
        if all(sum(a*x for a,x in zip(row,v)) >= rhs for row,rhs in C):
            feasible+=1
            verts[v]=True
    return sorted(verts),{"six_facet_combinations":210,"nonsingular_bases":nonsingular,"feasible_bases":feasible,"distinct_vertices":len(verts),"endpoint_counts":{str(lo):sum(v[0]==lo for v in verts),str(hi):sum(v[0]==hi for v in verts)}}


def TV(s,v,kind):
    _,h,up,un,wp,wn=v
    if kind=='free':
        tau=(1-s)/2; sigma=Q(1); eta=tau
    elif kind=='cal_left':
        tau=Q(1,2); sigma=s; eta=Q(3,10)-s/5
    elif kind=='cal_right':
        tau=Q(1,2); sigma=s; eta=s-Q(1,2)
    else:
        raise ValueError(kind)
    loss=Q(0)
    for a,d in AD:
        base=1 + Q(a,2)+s*d+h*a*d
        center=1 + tau*a+sigma*d+eta*a*d
        assert center >= 0, (kind,s,v,center)
        U=up if a==1 else un
        W=wp if d==1 else wn
        for P,T in SIGNS:
            x=base+P*U+T*W
            assert x>=0, (s,v,a,d,P,T)
            loss+=abs(x-center)/32
    return loss


def check_slab(lo,hi,kinds):
    V,info=vertices(lo,hi)
    assert V, 'No joint vertices'
    info.update({'slab':[str(lo),str(hi)],'checks':{}})
    for kind in kinds:
        eq=0; maxgap=Q(-1)
        for v in V:
            s=v[0]
            rho = (2-s)/4 if kind in ('free','cal_right') else (3-2*s)/5
            gap=TV(s,v,kind)-rho
            maxgap=max(maxgap,gap)
            eq+=gap==0
            assert gap<=0, (kind,s,v,gap)
        info['checks'][kind]={'equality_vertices':eq,'max_gap':str(maxgap),'violations':0}
    return info


def src(t,s,h,Uplus,Uminus,Wplus,Wminus):
    return [(1+t*a+s*d+h*a*d+P*(Uplus if a==1 else Uminus)+T*(Wplus if d==1 else Wminus))/16 for a,d in AD for P,T in SIGNS]


def check_lower():
    vals=[]
    for s in (Q(1,2),Q(3,5),Q(5,8),Q(2,3),Q(3,4),Q(1)):
        a=src(Q(1,2),s,s-Q(1,2),2*(1-s),0,1,0)
        b=src(Q(1,2),s,s-Q(1,2),-2*(1-s),0,-1,0)
        assert min(a+b)>=0 and sum(a)==sum(b)==1
        dist=sum(abs(x-y) for x,y in zip(a,b))/2
        assert dist == (2-s)/2
        Ea=(0,2,4,5,8,10); Eb=(0,1,2,3,12,13,14,15)
        alpha=src(Q(1,2),s,s-Q(1,2),2*(1-s),0,1,0)
        beta=src(Q(1,2),s,Q(3,2)-s,0,0,2*s-1,0)
        assert min(beta)>=0 and sum(beta)==1
        for eta in (Q(-1,10),Q(0),Q(1,6),Q(1,3)):
            q=[(1+Q(a,2)+s*d+eta*a*d)/16 for a,d in AD for _ in SIGNS]
            l_a=sum(alpha[i]-q[i] for i in Ea)
            l_b=sum(beta[i]-q[i] for i in Eb)
            assert l_a == (9-6*s+2*eta)/16
            assert l_b == (3-2*s-2*eta)/4
            assert (4*l_a+l_b)/5 == (3-2*s)/5
        vals.append({'s':str(s),'distance':str(dist),'rho_lower':str(dist/2)})
    return vals


def main():
    reports=[check_slab(Q(3,5),Q(2,3),('free','cal_left')),
             check_slab(Q(2,3),Q(1),('free','cal_right'))]
    lower=check_lower()
    result={'name':'R749SNH_OFF_DIAGONAL_T_HALF_S_SWEEP','scope':'fixed t=1/2, all real s in [3/5,1]',
      'free_rho':'(2-s)/4 on [3/5,1]',
      'calibrated_rho':'(3-2*s)/5 for [3/5,2/3]; (2-s)/4 for [2/3,1]',
      'proof': 'source witness pair gives diameter lower; calibrated event inequalities give stronger lower; complete joint vertex enumeration and convexity give universal upper',
      'slabs':reports,'lower_sample_checks':lower,'status':'PASS'}
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()
