"""EC49CG: exact extension-safe X6 BRC halo/orbit certificate.
Derived from the validated EC49CF transfer recurrence, with a different
multi-horizon recurrence/test, no external numerical libraries.
"""
import json, time, sys
from pathlib import Path
from math import comb
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P))
from native_signed_brc import endpoint_weight,endpoint_multiplicity
S=(1,2,3,4,5,6,-6,-5,-4,-3,-2,-1)
G=((0,0),(1,0),(0,1),(1,1));Z=(0,)*6
W0=(2,3,3,2,1,1);W1=(3,2,3,2,1,1)
W={a:(W0[a-1],W1[a-1],1) if a>0 else (1,1,1) for a in S}
def letter(a,g):
 i=abs(a)
 if g[0] and i in (1,2):i=3-i
 if g[1] and i in (5,6):i=11-i
 return i if a>0 else -i
def sub(q,a):return 2 if q==2 or (q==1 and a==2) else int(a==1)
SW=tuple(q%3*3+q//3 for q in range(9))
ATOM=tuple(2*(q//3==2)+(q%3==2) for q in range(9))
D={a:tuple(3*sub(q//3,a)+sub(q%3,letter(a,(1,0))) for q in range(9)) for a in S}
def act(k,g):
 z,q=k
 if g[0]:z=(z[1],z[0],z[2],z[3],z[4],z[5]);q=SW[q]
 if g[1]:z=z[:4]+(z[5],z[4])
 return z,q
def swap(v,g):return (v[1],v[0],v[2]) if g[0] else v
def step(k,a):
 z,q=k;i=abs(a)-1
 return z[:i]+(z[i]+(1 if a>0 else -1),)+z[i+1:],D[a][q]
def norm(k):return sum(abs(v) for v in k[0])
def add(out,k,v):
 old=out.get(k,(0,0,0));out[k]=(old[0]+v[0],old[1]+v[1],old[2]+v[2])
def full(src,rem):
 out={}
 for k,v in src.items():
  for a in S:
   d=step(k,a)
   if norm(d)>rem:continue
   w=W[a];add(out,d,(w[0]*v[0],w[1]*v[1],v[2]))
 return out
def stream(src,rem):
 out={}
 for r,v in src.items():
  Hr=tuple(g for g in G if act(r,g)==r);seen_letters=set()
  for a in S:
   if a in seen_letters:continue
   seen_letters.update(letter(a,h) for h in Hr)
   y=step(r,a)
   if norm(y)>rem:continue
   candidates=[(act(y,g),g) for g in G]
   d=min(k for k,g in candidates)
   E=tuple(h for h in Hr if letter(a,h)==a)
   seen_g=set();w=W[a]
   weighted=(w[0]*v[0],w[1]*v[1],v[2])
   for k,g in candidates:
    if k!=d or g in seen_g:continue
    seen_g.update((g[0]^e[0],g[1]^e[1]) for e in E)
    add(out,d,swap(weighted,g))
 return out
def lift(src):
 out={}
 for r,v in src.items():
  for g in G:
   k=act(r,g);w=swap(v,g)
   assert k not in out or out[k]==w
   out[k]=w
 return out
def terminal(src):
 t=[[0,0,0] for _ in range(4)]
 for (z,q),v in src.items():
  assert z==Z
  for i in range(3):t[ATOM[q]][i]+=v[i]
 return t

def closed(r):
    # All orbit states are per-state values, not an orbit-summed mass.
    out=[[0,0,0] for _ in range(4)]
    for (z,q),v in lift(r).items():
        if z==Z:
            for i in range(3):out[ATOM[q]][i]+=v[i]
    return out

def check_native(rows,n):
    nw=int(endpoint_weight(n,Z,W0,(1,)*6))
    nc=endpoint_multiplicity(n,Z)
    assert [sum(x[j] for x in rows) for j in (0,1,2)]==[nw,nw,nc]
    return [nw,nc]

def fixed(n):
    t0=time.perf_counter()
    r={(Z,0):(1,1,1)}; peak=1
    for j in range(n):
        r=stream(r,n-j-1)
        peak=max(peak,len(r))
    values=closed(r); total=check_native(values,n)
    return {"n":n,"orbit_peak_states":peak,"terminal":values,"native_total_weight_count":total,
            "elapsed_seconds":round(time.perf_counter()-t0,6)}

def multi(base=14, rounds=2):
    h=2*rounds; target=base+h
    t0=time.perf_counter()
    r={(Z,0):(1,1,1)}; peak=1
    layers=[]
    for j in range(target+1):
        peak=max(peak,len(r))
        if j>=base and (j-base)%2==0:
            # Future-append family: at j=base store radius h; later halo shrinks.
            radius=target-j
            assert all(norm(k)<=radius for k in r)
            values=closed(r)
            total=check_native(values,j)
            layers.append({"n":j,"halo_radius":radius,"state_count":len(r),
                           "terminal":values,"native_total_weight_count":total})
        if j<target:
            r=stream(r,target-j-1)
    return {"base":base,"two_step_rounds":rounds,"target":target,
            "peak_orbit_states":peak,"elapsed_seconds":round(time.perf_counter()-t0,6),"layers":layers}

def endpoints(n):
    # GF for signed-coordinate L1 shell: ((1+x)/(1-x))^6.
    # Fixed-point GFs for one/two axis swaps: f(x^2) f(x)^4 and f(x^2)^2 f(x)^2.
    f=lambda m:(1 if m==0 else 2)
    def convolution(*seqs):
        a=[1]+[0]*n
        for seq in seqs:
            b=[0]*(n+1)
            for j in range(n+1):
                if a[j]:
                    for k in range(n+1-j):
                        if seq[k]:b[j+k]+=a[j]*seq[k]
            a=b
        return a
    single=[f(k) for k in range(n+1)]
    pair=[f(k//2) if k%2==0 else 0 for k in range(n+1)]
    def shell_total(seq):return sum(seq[j] for j in range(n%2,n+1,2))
    N=shell_total(convolution(*([single]*6)))
    A=shell_total(convolution(pair,*([single]*4)))
    B=shell_total(convolution(pair,pair,single,single))
    assert (N+2*A+B)%4==0
    return {"n":n,"reachable_displacements":N,
            "single_swap_fixed":A,"double_swap_fixed":B,
            "orbit_displacements":(N+2*A+B)//4}

def halo_sharpness(base=14,k=2):
    # Every z with |z|_1 <=2k and correct parity is realizable as endpoint
    # of an n-word (when n >= |z|), then a 2k-word suffix returns it.
    # An exactly boundary-reaching word is a useful executable witness.
    assert base>=2*k and base%2==0
    word=[3]*(2*k)+[4,-4]*((base-2*k)//2)
    z,q=Z,0
    for a in word:z,q=step((z,q),a)
    assert sum(map(abs,z))==2*k
    suffix=[-3]*(2*k)
    for a in suffix:z,q=step((z,q),a)
    assert z==Z
    return {"base":base,"future_steps":2*k,"boundary_prefix":word,
            "return_suffix":suffix,"returns_to_zero":True}

def main():
    cases=[]
    for n in (0,2,4,6):
        # Independent full unquotiented parity/halos at tractable sizes.
        r={(Z,0):(1,1,1)}; f=dict(r)
        for j in range(n):
            f=full(f,n-j-1);r=stream(r,n-j-1)
            assert lift(r)==f
        assert closed(r)==terminal(f)
    t0=time.perf_counter()
    m=multi()
    for n in (14,16,18):
        row=fixed(n)
        assert row['terminal']==next(t['terminal'] for t in m['layers'] if t['n']==n)
        cases.append(row)
        print('PASS n=',n,'states=',row['orbit_peak_states'], 'time=',row['elapsed_seconds'],flush=True)
    endpoint_counts=[endpoints(n) for n in (0,2,4,6,14,16,18)]
    # brute independent small lattice-point counts
    from itertools import product
    for entry in endpoint_counts[:3]:
        n=entry['n']
        pts=[z for z in product(range(-n,n+1),repeat=6)
             if sum(map(abs,z))<=n and sum(map(abs,z))%2==n%2]
        assert len(pts)==entry['reachable_displacements']
        orbits=set()
        for z in pts:
            imgs=[act((z,0),g)[0] for g in G]
            orbits.add(min(imgs))
        assert len(orbits)==entry['orbit_displacements']
    report={"schema":"EC49CG_HALO_BRC_EXACT_V1",
            "model":"native signed X6 relative chart; ordered paths; nine-state A/B DFA; weights W0=(2,3,3,2,1,1), W1=(3,2,3,2,1,1), negatives=1; K=C2xC2 covariant channels; count",
            "frozen_base":14,"incremental":m,"independent_fixed_horizon":cases,
            "reachable_displacement_counts":endpoint_counts,
            "boundary_counterexample":halo_sharpness(),
            "small_full_vs_orbit_layer_audit_lengths":[0,2,4,6],
            "scope_limits":["Exact integer recurrences; fixed base=14 and future closure horizons 0,2,4.",
                            "Future horizons beyond 4 require a wider halo/recomputation; no unbounded suffix guarantee.",
                            "One process timings are indicative only; no native-physics time interpretation."]}
    (P/'EXACT_REPORT_EC49CG.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print('ALL_PASS incremental_time=',m['elapsed_seconds'],'fixed_total_time=',sum(x['elapsed_seconds'] for x in cases),'elapsed=',time.perf_counter()-t0)
if __name__=='__main__':main()
