#!/usr/bin/env python3
"""Deduplicate all 49 exact sharp-edge endpoints and classify their graph."""
from fractions import Fraction as Q
from itertools import combinations,permutations
from collections import Counter,defaultdict,deque
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
import COUNT_FIXED_FIBER_SHARP as z

def endpoint(w,t):
    tp,cons,slope,lo,hi,_=w
    x={(0,0):Q(z.E[(0,0)]),(6,6):Q(z.E[(6,6)])}
    for i,(j,k) in enumerate(tp):
        val=cons[i]+slope[i]*t
        assert 0<=val<=z.M[i]
        x[i,j]=val; x[i,k]=z.M[i]-val
    return tuple(x.get(d,Q()) for d in z.D)

def main():
    edges=[]; vertices={}; vkeys=[]
    for low in combinations(z.J,2):
        for labels in permutations(range(7)):
            if labels[5]>labels[6]:continue
            a,b,c,d,e,f,g=(z.R[i] for i in labels)
            ub=(c-a)*(d-e);ud=-(b-c)*(e-a)
            if -ub*(b-g)-ud*(d-g)==0 or -ub*(f-b)-ud*(f-d)==0:continue
            yes,w=z.solution_for_labels(low,labels)
            if not yes:continue
            tp,c,s,lo,hi,_=w
            ps=[endpoint(w,t) for t in (lo,hi)]
            for x in ps:
                if x not in vertices:
                    vertices[x]=len(vertices); vkeys.append(x)
            u,v=map(vertices.get,ps)
            edges.append((u,v,low,labels))
    assert len(edges)==49
    assert all(u!=v for u,v,_,_ in edges)
    G=defaultdict(set)
    for u,v,_,_ in edges:G[u].add(v);G[v].add(u)
    comp=[];seen=set()
    for v in range(len(vertices)):
        if v in seen:continue
        st=[v];seen.add(v);vv=[]
        while st:
            cur=st.pop(); vv.append(cur)
            for other in G[cur]:
                if other not in seen:
                    seen.add(other);st.append(other)
        comp.append(tuple(vv))
    comp_counts=Counter((len(cc),sum(len(G[v]) for v in cc)//2) for cc in comp)
    deg=Counter(map(len,G.values()))
    support=Counter(sum(x>0 for x in v) for v in vertices)
    print('EDGES',len(edges),'DISTINCT_VERTICES',len(vertices))
    print('COMPONENT_SIZE_AND_EDGES',sorted(comp_counts.items()))
    print('DEGREE_DISTRIBUTION',sorted(deg.items()))
    print('VERTEX_SUPPORT_DISTRIBUTION',sorted(support.items()))
    print('FIRST_EDGE_ENDPOINT_VERTEX_IDS',edges[0][:2], 'LOW',edges[0][2], 'LABELS',edges[0][3])
    assert sum(size*cnt for (size,_),cnt in comp_counts.items())==len(vertices)
    assert sum(e*cnt for (_,e),cnt in comp_counts.items())==len(edges)
    print('PASS_EXACT_49_EDGE_GRAPH_AND_ENDPOINT_DEDUP')

if __name__=='__main__':main()
