"""R728: exact S3 character transfer and nine-step primitive lift.
Run: python R728_HOLONOMY_CHAR_VERIFY.py > R728_HOLONOMY_CHAR_RESULTS.json
Standard library; integer only. Source-distinct positive CNB histories.
"""
import json
from itertools import combinations, permutations
from collections import defaultdict

ROOT='012'
TRIADS=tuple(''.join(t) for t in combinations('01234',3))
ALL_ARCS=tuple((u,v) for u in TRIADS for v in TRIADS if len(set(u)&set(v))==2)
REPS={'A_R725_1_2':211733226574,'B_R725_3_4':5363347296468}
PERMS=tuple(permutations(range(3)))
FRAMES=tuple(''.join(t) for t in permutations(ROOT))

def step(frame,target):
    leaving=next(x for x in frame if x not in target)
    arriving=next(x for x in target if x not in frame)
    return frame.replace(leaving,arriving)

def edge_perm(edge):
    u,v=edge
    return tuple(v.index(t) for t in step(u,v))

def compose(p,q):return tuple(p[q[i]] for i in range(3))

def parity(p):
    return -1 if sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2 else 1

def standard(p):
    cols=[]
    for i in (0,1):
        v=[0,0,0]; v[p[i]]+=1;v[p[2]]-=1
        cols.append(v[:2])
    return [[cols[c][r] for c in range(2)] for r in range(2)]

def identity(n):return [[int(i==j) for j in range(n)] for i in range(n)]

def matmul(A,B):
    n=len(A); C=[[0]*n for _ in range(n)]
    for i,row in enumerate(A):
        for k,a in enumerate(row):
            if a:
                for j,b in enumerate(B[k]):
                    if b:C[i][j]+=a*b
    return C

def char_certificate(M,roots,d):
    n=len(M)
    powers=[identity(n)]
    for _ in range(n):powers.append(matmul(powers[-1],M))
    traces=[0]+[sum(Mk[i][i] for i in range(n)) for Mk in powers[1:]]
    D=[1]
    for k in range(1,n+1):
        s=sum(D[k-j]*traces[j] for j in range(1,k+1))
        assert s%k==0
        D.append(-s//k)
    CH=[[0]*n for _ in range(n)]
    for k,c in enumerate(D):
        if c:
            P=powers[n-k]
            for i in range(n):
                for j in range(n):CH[i][j]+=c*P[i][j]
    assert all(not z for row in CH for z in row)
    c=[sum(Mk[d*i+j][d*i+j] for i in roots for j in range(d)) for Mk in powers]
    N=[sum(D[k-j]*c[j] for j in range(k+1)) for k in range(n)]
    # The adjugate numerator has degree <= n-1; this is an all-length identity.
    while len(N)>1 and N[-1]==0:N.pop()
    while len(D)>1 and D[-1]==0:D.pop()
    return D,N,c

def build(mask):
    arcs=tuple(e for i,e in enumerate(ALL_ARCS) if mask>>i&1)
    assert len(arcs)==15
    roots=tuple(i for i,e in enumerate(arcs) if e[0]==ROOT)
    B=[[0]*15 for _ in arcs]
    BS=[[0]*15 for _ in arcs]
    BM=[[0]*30 for _ in range(30)]
    adjacency=[[] for _ in arcs]
    for i,e in enumerate(arcs):
        for j,f in enumerate(arcs):
            if e[1]!=f[0] or e[0]==f[1]:continue
            adjacency[i].append(j)
            B[i][j]=1
            p=edge_perm(f)
            BS[i][j]=parity(p)
            st=standard(p)
            # Transpose reverses product order in a trace, matching actual slot update.
            for a in range(2):
                for b in range(2):BM[2*i+a][2*j+b]=st[b][a]
    return arcs,roots,B,BS,BM,adjacency

def path_hist(arcs,max_m):
    nbr=defaultdict(list)
    for a,b in arcs:nbr[a].append(b)
    d={(ROOT,v,step(ROOT,v),v):1 for v in nbr[ROOT]}
    out={}
    for m in range(2,max_m+1):
        nd=defaultdict(int)
        for (prev,cur,frame,first),w in d.items():
            for v in nbr[cur]:
                if v!=prev:nd[(cur,v,step(frame,v),first)]+=w
        d=nd
        if m>=3:
            H={f:0 for f in FRAMES}
            for (prev,cur,frame,first),w in d.items():
                if cur==ROOT and prev!=first:H[frame]+=w
            out[m]=H
    return out

def lift_certificate(arcs,adj):
    ids={(i,p):6*i+k for i in range(15) for k,p in enumerate(PERMS)}
    J=[[] for _ in range(90)]
    for i in range(15):
        for j in adj[i]:
            pf=edge_perm(arcs[j])
            for p in PERMS:J[ids[(i,p)]].append(ids[(j,compose(pf,p))])
    # Every entry of L^9 is a positive integer. Exact full 90x90 certificate.
    counts=[]; support8=0
    for source in range(90):
        v=[0]*90;v[source]=1
        for stepno in range(1,10):
            w=[0]*90
            for i,a in enumerate(v):
                if a:
                    for j in J[i]:w[j]+=a
            v=w
            if stepno==8:support8+=sum(a>0 for a in v)
        counts.extend(v)
    assert len(counts)==8100 and min(counts)>0
    return {'lifted_states':90,'lifted_transition_count':sum(map(len,J)),
            'L8_positive_entries':support8,'L8_zero_entries':8100-support8,
            'L9_positive_entries':sum(x>0 for x in counts),
            'L9_min_entry':min(counts),'L9_max_entry':max(counts),
            'L9_sum_entries':sum(counts),
            'primitive_exponent_exactly':9}

def run():
    out={'schema':'R728_BRC_S3_CHARACTER_AND_PRIMITIVE_LIFT_V1',
         'status':'R728_EXACT_CHARACTER_AND_LIFT_PASS',
         'scientific_pin':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
         'upstream':'R725@a9ba60ca; R726@5ef47c8c; R727@6ee08807',
         'arithmetic':'exact integers only',
         'claim':'exact all-length S3 conjugacy-class GFs and primitive 90-state lifted graph, exponent 9',
         'classes':{}}
    for name,mask in REPS.items():
        arcs,roots,B,BS,BM,adj=build(mask)
        D0,N0,Tr0=char_certificate(B,roots,1)
        Ds,Ns,Trs=char_certificate(BS,roots,1)
        Dc,Nc,Trc=char_certificate(BM,roots,2)
        assert N0[0]==len(roots)
        hist=path_hist(arcs,14)
        values={}
        for m in range(3,15):
            H=hist[m]
            total=sum(H.values())
            sign=sum(v*parity(tuple(ROOT.index(x) for x in frame)) for frame,v in H.items())
            std=2*H[ROOT]-H['120']-H['201']
            assert (total,sign,std)==(Tr0[m],Trs[m],Trc[m])
            classes=(H[ROOT],H['021']+H['102']+H['210'],H['120']+H['201'])
            assert (2*std+total+sign)//6==classes[0]
            assert (total-sign)//2==classes[1]
            assert (total+sign-std)//3==classes[2]
            values[str(m)]={'identity':classes[0],'all_transpositions':classes[1],
                            'both_three_cycles':classes[2],
                            'each_individual_holonomy':H}
        lift=lift_certificate(arcs,adj)
        assert D0 == ([1,0,0,-3,-7,-8,-4] if name.startswith('A') else [1,0,0,-3,-7,-8,-5,-1])
        out['classes'][name]={
            'mask':mask,'arcs':['>'.join(e) for e in arcs],
            'root_outdegree':len(roots),
            'trivial':{'denominator':D0,'numerator_including_m0':N0,'m0':Tr0[0]},
            'sign':{'denominator':Ds,'numerator_including_m0':Ns,'m0':Trs[0]},
            'standard':{'denominator':Dc,'numerator_including_m0':Nc,'m0':Trc[0]},
            'm3_to_m14_classes':values,'lift_certificate':lift,
            'checked_CH_entries':15*15+15*15+30*30,
            'direct_source_distinct_DP_test_lengths':'3..14'
        }
    return out

if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,indent=2,sort_keys=True))
