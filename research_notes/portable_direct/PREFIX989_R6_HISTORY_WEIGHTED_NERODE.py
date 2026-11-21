"""PREFIX-989 reproducible exact finite typed positive-branch observer.
Pure Python 3, standard library, exact integers only.
The input is an auxiliary named-source residual observer, not native X6 dynamics.
"""
from collections import defaultdict, deque
from functools import lru_cache
import json

WORDS=((6,24,6,-3),(6,24,8,40))


def build(word, p):
    L=len(word)
    src={q:tuple((q,i,j,s) for i in range(p) for j in range(1,p)
                     for s in (1,-1) if (1<<i)-s*(1<<j)==c)
         for q,c in enumerate(word)}
    ports=tuple(sorted({a[2] for group in src.values() for a in group}))
    assert ports and 0 not in ports
    def nextstate(state, a):
        q, x, prev=state
        if q!=a[0] or (x>>a[2])&1 != (1-a[3])//2:
            return None
        return ((q+1)%L, x^(1<<a[2]), a[2])
    # A new experiment begins at phase zero with undefined previous port.
    states0=tuple((0,1+sum((1<<j) for k,j in enumerate(ports) if mask>>k&1),0)
                  for mask in range(1<<len(ports)))
    known=set(states0); todo=deque(states0)
    edges={}
    while todo:
        z=todo.popleft()
        edges[z]=[]
        for a in src[z[0]]:
            t=nextstate(z,a)
            if t is not None:
                wt={0:1,1:2,2:3,3:5,4:7,5:11,6:13}.get(z[2], 17+z[2])
                edges[z].append((a,wt,t))
                if t not in known:
                    known.add(t);todo.append(t)
    return ports, src, states0, edges


def min_quotient(edges):
    """Terminal ε=1; exact weighted Nerode via finite partition refinement."""
    zs=sorted(edges)
    cls={z:0 for z in zs}
    iterations=0
    while True:
        signatures={z:tuple((a,wt,cls[t]) for (a,wt,t) in edges[z]) for z in zs}
        unique={sig:k for k,sig in enumerate(sorted(set(signatures.values())))}
        nxt={z:unique[signatures[z]] for z in zs}
        iterations+=1
        # Only compare induced equivalence, not potentially renumbered labels
        if all((cls[a]==cls[b])==(nxt[a]==nxt[b]) for ia,a in enumerate(zs)
               for b in zs[ia+1:]):
            return nxt,iterations
        cls=nxt


def counts(edges, starts, nmax):
    # Backward DP gives exact number and sum of weights from each state for n steps.
    N={z:1 for z in edges}; W=N.copy()
    ans=[(sum(N[z] for z in starts),sum(W[z] for z in starts))]
    for n in range(1,nmax+1):
        N={z:sum(N[t] for _a,wt,t in edges[z]) for z in edges}
        W={z:sum(wt*W[t] for _a,wt,t in edges[z]) for z in edges}
        ans.append((sum(N[z] for z in starts),sum(W[z] for z in starts)))
    return ans


def quotient_counts(edges,starts,cls,nmax):
    reps={}
    for z,c in cls.items():reps.setdefault(c,z)
    qedges={c:tuple((a,wt,cls[t]) for a,wt,t in edges[rep]) for c,rep in reps.items()}
    mult=defaultdict(int)
    for z in starts:mult[cls[z]]+=1
    n={c:1 for c in reps}; v=n.copy()
    out=[(sum(mult[c]*n[c] for c in reps),sum(mult[c]*v[c] for c in reps))]
    for t in range(1,nmax+1):
        n={c:sum(n[dst] for _a,wt,dst in qedges[c]) for c in reps}
        v={c:sum(wt*v[dst] for _a,wt,dst in qedges[c]) for c in reps}
        out.append((sum(mult[c]*n[c] for c in reps),sum(mult[c]*v[c] for c in reps)))
    return out


def independent_forward(edges,starts,nmax):
    curr=defaultdict(int)
    for z in starts:curr[z]+=1
    out=[(sum(curr.values()),sum(curr.values()))]
    count=dict(curr);mass=dict(curr)
    for n in range(1,nmax+1):
        nc=defaultdict(int);nm=defaultdict(int)
        for z in count:
            for a,wt,t in edges[z]:
                nc[t]+=count[z]
                nm[t]+=wt*mass[z]
        count,mass=nc,nm
        out.append((sum(nc.values()),sum(nm.values())))
    return out


def port_histogram(edges,starts,n):
    # Explicit positive weighted branch histogram N[Q_{>0}], no total-only collapse.
    H=defaultdict(int)
    for z in starts:H[(z,1)]+=1
    for step in range(n):
        J=defaultdict(int)
        for (z,weight),multiplicity in H.items():
            for a,wt,t in edges[z]: J[(t,weight*wt)]+=multiplicity
        H=J
    out=defaultdict(int)
    for (z,w),mul in H.items():out[w]+=mul
    return dict(sorted(out.items()))


def witness(edges):
    # Search the same odd initial x for histories reaching same (q,x)
    # with different last ports and a common next label.
    for s in sorted(z for z in edges if z[0]==0 and z[2]==0):
        curr={s:()}
        for n in range(1,18):
            nxt={}
            for z,path in curr.items():
                for a,wt,t in edges[z]:nxt.setdefault(t,path+(a,))
            curr=nxt
            pools=defaultdict(list)
            for z,path in curr.items():pools[z[:2]].append((z,path))
            for key,L in sorted(pools.items()):
                for ia,(a_state,path_a) in enumerate(L):
                    for b_state,path_b in L[ia+1:]:
                        if a_state[2]==b_state[2]:continue
                        adict={a:wt for a,wt,t in edges[a_state]}
                        bdict={a:wt for a,wt,t in edges[b_state]}
                        for label in sorted(set(adict)&set(bdict)):
                            if adict[label]!=bdict[label]:
                                return dict(start=s,steps=n,shared_q_x=key,
                                    first=dict(last_port=a_state[2],path=path_a,next_weight=adict[label]),
                                    second=dict(last_port=b_state[2],path=path_b,next_weight=bdict[label]),
                                    common_next_source=label)
    return None


def main():
    ans={"model":"auxiliary signed-source observer / Markov-one strictly positive integer branch weights", "weight_rule":"g(h,a)= {0:1,1:2,2:3,3:5,4:7,5:11,6:13}; h previous port (0 before start)", "families":[]}
    for word in WORDS:
        p0=max(abs(c) for c in word).bit_length()+1
        ports,src,starts,edges=build(word,p0)
        cls,it=min_quotient(edges)
        full=counts(edges,starts,24)
        quotient=quotient_counts(edges,starts,cls,24)
        direct=independent_forward(edges,starts,16)
        assert full==quotient and full[:17]==direct
        h8=port_histogram(edges,starts,8)
        assert sum(h8.values())==full[8][0] and sum(k*v for k,v in h8.items())==full[8][1]
        # Exact source-alphabet stabilization across every width to 19.
        for p in range(p0,20):
            P,S,_,_=build(word,p)
            assert P==ports and S==src
        scale=1<<(19-1-len(ports))
        data=dict(word=word,p0=p0,ports=ports,source_count=sum(len(s) for s in src.values()),
                  initial_active_states=len(starts),reachable_augmented_states=len(edges),
                  weighted_nerode_classes=len(set(cls.values())),refinement_rounds=it,
                  finite_path_counts={str(n):list(full[n]) for n in (0,1,4,7,8,13,18,19,20,24)},
                  p19_spectator_factor=scale,
                  p19_n8=[scale*k for k in full[8]],p19_n19=[scale*k for k in full[19]],
                  histogram_n8=[{'mass':w,'multiplicity':cnt} for w,cnt in h8.items()],
                  witness=witness(edges),
                  independent_forward_verified="n=0..16",quotient_verified="n=0..24",source_width_stability_verified=f"p={p0}..19")
        ans['families'].append(data)
    with open('/mnt/data/PREFIX989_R6_EXACT_RESULTS.json','w') as f:json.dump(ans,f,indent=2,ensure_ascii=False)
    for d in ans['families']:
        print('WORD',d['word'],'p0',d['p0'],'ports',d['ports'],'states',d['reachable_augmented_states'],'classes',d['weighted_nerode_classes'])
        print('phase0 counts',d['finite_path_counts'],'19bit length8',d['p19_n8'],'19bit length19',d['p19_n19'])
        print('witness',d['witness'])
        print('hist_n8 distinct',len(d['histogram_n8']))
    print('PASS exact DP/quotient/forward/histogram/stability')

if __name__=='__main__':main()
