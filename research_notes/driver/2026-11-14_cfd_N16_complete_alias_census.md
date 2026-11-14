# CFD N=16 lattice: complete finite alias-coupling census

**2026-11-14 — EM-DVR-DEBB5E.** Scope: exact finite algebraic diagnostic for the existing independent-verifier Task RS-CFD-TRAJECTORY-VERIFY-20260910 (TP2-499BEE22860EFD4AD321). Original spectralDNS/Numba host experiments and implementation belong to EM-CFD-49157B. This note does not replace a frozen native Result or an independent solver execution.

## Finite proposition

Fix nu=(1,-7,6), L=ker_Z(nu·), C=[-7,7]^3 intersection Z^3, S=L intersection C, 16-point cyclic convolution and retained cutoff K=7. The complete parameterization S={(7u-6v,u,v): |u|,|v|,|7u-6v|<=7} has 33 modes. Among the 1089 **ordered** pairs (p,q) in S^2, write w=p+q and k=wrap_16(w). Exact classification:

| Outcome | Count |
|---|---:|
| True sum already retained | 607 |
| Sum outside C, alias also outside C | 160 |
| Sum outside C, alias retained **off L** | 280 |
| Sum outside C, alias retained **in L** | 42 |
| Total | 1089 |

Among the 280 off-L alias pairs, 268 can give a nonzero Leray-projected symmetrized advective coefficient for some divergence-free integer polarizations a perpendicular to p and b perpendicular to q, and the remaining 12 are p=q self-pairs whose bilinear cross coefficient vanishes. All 42 in-L aliased pairs consist of p,q both on the diagonal (1,1,1) line; their incompressible cross symbols vanish as well. Counts describe pairwise possibilities, not a guaranteed net effect for arbitrary many-mode initial data.

In the 3/2-padded grid N=24, **no** out-of-band w returns into the original C: each |w_i|<=14, and whenever |w_i|>=8, its wrapped 24-grid magnitude is at least 8, so the retained cutoff rejects it. Hence the classification isolates the N=16 underpadding failure and supplies a stronger independent-verifier regression family than the previous single two-mode witness.

## Complete exact enumeration certificate

The following self-contained Python 3 program was run with PASS on the declared counts; there are no floating-point operations. The polarization-basis test is exhaustive because the tested coefficient is bilinear in a,b, and k cross c detects nonzero Leray projection for k != 0.

    from collections import Counter
    from itertools import product
    K,N,PAD=7,16,24
    nu=(1,-7,6)
    S={(7*u-6*v,u,v) for u,v in product(range(-K,K+1),repeat=2)
       if abs(7*u-6*v)<=K}
    def dot(a,b): return sum(x*y for x,y in zip(a,b))
    def cross(a,b):
        return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],
                a[0]*b[1]-a[1]*b[0])
    def add(a,b): return tuple(x+y for x,y in zip(a,b))
    def mul(a,n): return tuple(n*x for x in a)
    def inside(a): return all(abs(x)<=K for x in a)
    def wrap(a,n): return tuple((x+n//2)%n-n//2 for x in a)
    def basis(p):
        if p==(0,0,0): return [(1,0,0),(0,1,0),(0,0,1)]
        out=[]
        for e in ((1,0,0),(0,1,0),(0,0,1)):
            v=cross(p,e)
            if any(v) and (not out or any(cross(out[0],v))):
                out.append(v)
                if len(out)==2: break
        assert len(out)==2
        return out
    def active(p,q,k):
        assert any(k)
        for a,b in product(basis(p),basis(q)):
            c=add(mul(b,dot(a,q)),mul(a,dot(b,p)))
            if any(cross(k,c)): return True
        return False
    ct=Counter()
    potential=0
    for p,q in product(sorted(S),repeat=2):
        w=add(p,q);k=wrap(w,N)
        assert inside(w) or not inside(wrap(w,PAD))
        if inside(w):
            assert k==w
            ct["true_retained"]+=1
        elif not inside(k):
            ct["alias_outside_retention"]+=1
        elif dot(nu,k):
            ct["alias_retained_off_lattice"]+=1
            potential+=active(p,q,k)
        else:
            ct["alias_retained_in_lattice"]+=1
            assert p[0]==p[1]==p[2] and q[0]==q[1]==q[2]
            assert not active(p,q,k)
    assert len(S)==33
    assert ct=={"true_retained":607,"alias_outside_retention":160,
                "alias_retained_off_lattice":280,"alias_retained_in_lattice":42}
    assert potential==268 and sum(ct.values())==1089
    print("PASS",len(S),dict(ct),"off-L potential:",potential)

## Frontier and contribution

The prior two-mode witness p=(7,1,0),q=(6,0,-1) is one of the 268 potentially active pairs and remains a deterministic numerical regression input. Earlier source: research_notes/driver/2026-11-14_cfd_exact_alias_dealias_verifier_witness.md at e99c9c7383920feb4e7e3d5cf4511adefe780f27. Original host checkpoint at 20255478397fc475ec0584da0cf4311dd17bcc82:research_notes/CFD9R2K7/host_20260916/checkpoint_summary.json. Next evidence: separately authorized complete-solver verifier must check actual native FFT, pressure, divergence, dealias and fallback outputs against the frozen author implementation. Existing independent-review boundary and OPEN parent objective are unchanged.
