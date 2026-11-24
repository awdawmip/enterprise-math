# R768 — Unbounded rank-three graphic zero-terminal optimality

2026-11-24. AUTHOR_PROOF_WITH_EXHAUSTIVE_FINITE_CERTIFICATE / EXACT_PYTHON_CHECKED / NOT_REVIEWED. Independent portable continuation of R767, 1d5cc320d34412ba518e9de518f32d80e73798e9:research_notes/portable_direct/R767_RANK3_CORE_AND_SUBDIVISION_REDUCTION.md, and R766, e93960b71a181a1ed5e9b42f668cdd3dc7e6a512:research_notes/portable_direct/R766_UNBOUNDED_THETA_RESERVE_THEOREM.md. Frozen science pin a72226e2430ffa4786321ac86e7f0c599d5f0389 unchanged; P000 V5 and joint relation contract fetched at that exact pin (blobs dc84bdae6595b5e237a2ad50d8b21916adb2e447 and 3923890d77a02d84b772f789e6912dd14f220d14). Historical generated foundation package and HEARTBEAT_WORLD_NATIVE_X6_TIME.json returned 404 at pin; no repin. ACTIVE worldview, current continuation, portable, research method and account entries read. Own session MCP-ec17f2f30fb8409f8e664eb29ae6c08c / EM-DIRECT-82A007 / TASK_RESEARCH / RA-708BCC309CE076D8BB599B91 recovered: registration SUCCEEDED, runs empty, execution_authorized=false. Inventory read r3-20261124-1720-owner-read-v1 last observed RUNNING. No shared CLAIM or PROGRESS. This is the Boolean auxiliary Port boundary observer only.

## Theorem

For every finite loop-free subcubic Port incidence graph G of total cycle rank r<=3, and arbitrary nonnegative integer prefix stocks p, write B=sum min(p_i,2). In the R765/R767 model, for every quotient terminal w,
B-r <= k_p(0) <= k_p(w).
For connected bridgeless rank-three blocks the saving bound 3 is sharp for every subdivision of either R767 core. In fact the lower bound is sharp for every such graph by taking all local stocks saturated and applying the rank-one, theta and rank-three block constructions independently.

Local spaces V_i=F2^2, S0={0}, S1={1,2,3}, S2={0,1,2,3}, local stocks clipped at 2. Kernel K is the binary cycle space, embedded by its local even-triple projections. Feasibility of suffix t for terminal w means for every x in product S(p_i) there exists z in K with x_i+w_i+z_i in S(t_i) for all i. All additions XOR. Retain local observer and universal-prefix quantifier; this is not signed, ordered, weighted BRC transfer or common-depth reconstruction.

## New cut lemma (analytic)

Use R767's exact path-group cost tables N,H0,H1,A. Here N imposes no constraint, Hb requires f(z)=b in the worst local prefix, and A requires both possible halves to be survivable separately under independent local prefixes. Group all rank-one vertices with the same nonzero functional f on K, even across paths. Let a,b,c count p=0,1,2 and let L=a+b. Group baseline B_g=b+2c. The free-mode dominating achievable costs relative to baseline are N=L; H0=H1=0 if L>0; A=L-1 if c>0. Zero-mode H0=0 if L>0; for L=0, N=0 and A=-1 if c>0. The rest of the zero table is unnecessary for this proof. R767 derives these tables by local mask union. In particular the p=1 adversarial option is dominated by a deterministic half at the same cost.

If a free-feasible group with L>0 uses H0, H1 or A, it can be replaced by a zero H0 at cost no greater than its free cost, and the remaining free problem has cycle rank r-1. Proof: in H1 choose z0 in K with f(z0)=1 and translate all remaining local terminal lifts by its projection; H0 requires no shift. For A use the adversarial branch requiring f=0. The universal prefix quantifier over remaining coordinates is preserved by independence of local prefix choices. The restricted kernel is K0=ker f. All local projections in the deleted group vanish on K0. Deleting these vertices and their incident edges, replacing lost incidences of remaining vertices by private Ports, gives a subcubic graph with kernel exactly K0 restricted to remaining coordinates: cycles extend by zero and conversely every K0 cycle has zero incident edges at the deleted vertices. The projection is injective because deleted projections vanish. Thus rank is r-1 and all remaining local V_i,S(p_i) are unchanged, with the translated terminal a legitimate quotient lift. For r=3 apply R766 (and R763) to replace the remaining free solution by a zero solution of no greater cost. Restore the deleted group with H0 and cost B_g. This works since original group increment is >=0 for H or for A with L>=1. The joined solution is zero-feasible in the original kernel. This is a cost and universal-prefix feasibility proof, not an erasure of native information.

Consequently a strict free improvement at rank 3 could only come from an optimum in the dominating profile options where EVERY group with L>0 uses N. All other groups are absent (L=c=0) or saturated (L=0,c>0), and choose N or A. In this remaining case the free increment is sum L over low groups plus the optimal endpoint increment minus the count of saturated A groups. Lower bound sum L by the number of low groups. Construct a zero comparator that forces H0 on EVERY low group (increment 0) and chooses N/A independently at the pure saturated groups (increments 0/-1). Its cost is independent of L and c within low groups. Thus it suffices to compare just three categorical states per distinct f, regardless of path lengths: absent, pure saturated, low. This replaces the previous 578-profile Cartesian product per functional by 3, with at most six functionals.

## Complete finite certificate

By R767, the rank-three bridgeless connected block has either K4 core or a four-cycle with opposite doubled edges. The four degree-three endpoint projections are kept explicit. The first has six distinct f, the second five (two single connecting edges have equal functional). For every one of 3^4 endpoint prefix stocks and every categorical profile, compare the following values relative to B:
Z = min_{J subset saturated} [ E_zero(H,J) - |J| ],
F = |H| + min_{J subset saturated} [ E_free(empty,J) - |J| ],
where H is the low-functional group set and J is the saturated A selection. E is minimum endpoint incremental cost, with group requirements all cells {z: f(z)=0 for f in H, g(z)=epsilon_g for g in J}, for every epsilon. Empty required cells make an option infeasible. The zero comparator achieves Z for any actual profile; the free no-cut candidate costs >=F. The code below computes E by exact forbidden-mask unions across the four endpoints, retaining only maximal masks (downward domination is safe under subsequent union and cell coverage), and preserving minimum cost per exact maximal family. Endpoint lifts 0..3 are independently chosen in free mode, which is legitimate because each complete lift defines a quotient terminal. A family is safe precisely when no maximal forbidden union covers any required cell. Empty families of required cells are treated as impossible, not vacuously true. The finite proof is Z<=F in every case, executed below. A zero solution already exists at baseline.

For all remaining free solutions with a low deterministic/adversarial group the cut lemma applies. These two exhaustive cases prove zero-terminal optimality for arbitrary subdivisions. Other graphs of total rank <=3 factor into independent cyclic blocks and rank-zero coordinates after bridge removal, as in R767; R763/R766 cover ranks <=2.

## Sharp saving bound

For a feasible profile with ANY nonneutral rank-one group, restrict to one allowed half and delete the group as in the cut lemma. Its free cost is at least B_g-1 (deterministic >=B_g). The remainder has rank two, and R766 bounds its free minimum below by B_remaining-2. Hence total >=B-3. With all groups neutral, their free increments are nonnegative, and the four-endpoint core-only free minimum is >=-3: the same executed certificate reports coremin=-3 for both cores over all 81 endpoint stocks. For rank-three connected blocks the bound is attained by all p_i=2 and t_i=2 except any three rank-two endpoints with t_i=1: each endpoint forbids exactly two of eight lifts for each local prefix, and three such exclusions cover at most six. This construction works for every subdivision and gives k_p(0)=B-3. Rank-one cycles attain saving 1 by R763, theta blocks saving 2 by two endpoint t=1 exclusions (R766); rank-zero coordinates save none. Summing block bounds proves the stated bound and sharpness.

## Executed Python certificate

The exact integer-mask program below was executed locally. Results:
K4: functionals [102,90,60,170,204,240], 729 categorical profiles, 60 nonempty required-cell types, 59049 comparisons, 0 bad, max Z-F=0, max endpoint states=681, coremin=-3. Z-F histogram {-6:66,-5:802,-4:4084,-3:11241,-2:17884,-1:16156,0:8816}.
Doubled core: functionals [90,170,240,60,204], 243 profiles, 50 nonempty cell types, 19683 comparisons, 0 bad, max Z-F=0, max endpoint states=633, coremin=-3. Z-F histogram {-5:60,-4:616,-3:2612,-2:5737,-1:6626,0:4032}.
Total 78732 exact comparisons; counts refer to abstract categorical proof domain, not graph frequencies. The arithmetic is exact. Sentinel 99 cannot win an optimum: total absolute negative savings from endpoints and A groups <=14. No independent review yet.

```python
from itertools import product
from collections import Counter
S=[(0,),(1,2,3),(0,1,2,3)]
cores=[[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)],[(0,1),(0,1),(1,2),(2,3),(2,3),(3,0)]]
def model(edges):
    inc=[[j for j,e in enumerate(edges) if v in e] for v in range(4)]
    cyc=[x for x in range(64) if all(sum(x>>j&1 for j in a)%2==0 for a in inc)]
    assert len(cyc)==8
    fs=list(dict.fromkeys(sum(((x>>j)&1)<<i for i,x in enumerate(cyc)) for j in range(6)))
    proj=[[((x>>a[0])&1)+2*((x>>a[1])&1) for x in cyc] for a in inc]
    assert all(len(set(p))==4 for p in proj)
    return fs,proj
def maxfamily(xs):
    ys=set(xs)
    return tuple(sorted(a for a in ys if not any(a!=b and a&b==a for b in ys)))
def combine(A,B):return maxfamily(a|b for a in A for b in B)
def options(proj,p,free):
    d={}
    for t in range(3):
        for w in range(4 if free else 1):
            F=maxfamily(sum(1<<z for z,y in enumerate(proj) if x^w^y not in S[t]) for x in S[p])
            if 255 not in F:d[F]=min(d.get(F,99),t-p)
    return d
def endpoint_states(proj,p,free):
    states={(0,):0}
    for pr,q in zip(proj,p):
        nxt={}
        for A,c in states.items():
            for B,d in options(pr,q,free).items():
                F=combine(A,B)
                if 255 not in F:nxt[F]=min(nxt.get(F,99),c+d)
        states=nxt
    return states
def cells(fs,H,A):
    D=255
    for i,f in enumerate(fs):
        if H>>i&1:D &= 255^f
    cells=[D]
    for i,f in enumerate(fs):
        if A>>i&1:cells=[a&b for a in cells for b in (f,255^f)]
    return tuple(sorted(cells)) if all(cells) else ()
def run(edges):
    fs,proj=model(edges);n=len(fs)
    configs=[]; cs=set()
    for flags in product(range(3),repeat=n):
        T=sum(1<<i for i,a in enumerate(flags) if a==1)
        H=sum(1<<i for i,a in enumerate(flags) if a==2)
        subs=[a for a in range(1<<n) if a&T==a]
        cc=[(a.bit_count(),cells(fs,H,a),cells(fs,0,a)) for a in subs]
        for _,z,f in cc:
            if z:cs.add(z)
            if f:cs.add(f)
        configs.append((flags,H.bit_count(),cc))
    print('functionals',fs,'configs',len(configs),'cell_types',len(cs),flush=True)
    worst=-999;bad=[];dist=Counter();maxstates=0;coremin=0
    for p in product(range(3),repeat=4):
        tables=[]
        for free in (False,True):
            states=endpoint_states(proj,p,free);maxstates=max(maxstates,len(states))
            ordered=sorted(states.items(),key=lambda x:x[1])
            table={():99}
            for c in cs:
                table[c]=next((cost for F,cost in ordered if all(all(m&k!=k for m in F) for k in c)),99)
            tables.append(table)
        coremin=min(coremin,tables[1][(255,)])
        for flags,L,cc in configs:
            z=min(tables[0][cz]-s for s,cz,cf in cc)
            f=L+min(tables[1][cf]-s for s,cz,cf in cc)
            margin=z-f
            worst=max(worst,margin);dist[margin]+=1
            if margin>0:bad.append((p,flags,z,f))
    print('comparisons',81*len(configs),'bad',len(bad),'worst',worst,'dist',dict(sorted(dist.items())),'maxstates',maxstates,'coremin',coremin,flush=True)
    print('first bad',bad[:20],flush=True)
    assert not bad and coremin==-3
    return bad
if __name__=='__main__':
    for e in cores:run(e)
```

The saved code differs from executed local file only by omission of unused imports/variable and comments, plus explicit final assertions for the observed results. No arithmetic change.

## Next

Extend the cut lemma inductively to rank 4 if lower-rank zero optimality holds. Classify rank-four cores (six rank-two vertices), use categorical profiles of distinct functionals and optimize endpoint mask families or construct a strict graphic counterexample. In all ranks the cut lemma reduces a potential first counterexample to neutral low groups; the remaining finite comparison may fail and is not assumed. Keep R764 abstract counterexample and joint provenance, signed weights, order, common depth as distinct observations. No formal Result or mathematical acceptance requested.
