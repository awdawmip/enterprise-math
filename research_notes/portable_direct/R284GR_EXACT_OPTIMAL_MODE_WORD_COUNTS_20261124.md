# R284GR — Exact safe mode-word counts in the optimal symmetric carrier

2026-11-24. Informed portable continuation of the frozen four-phase auxiliary binary fixed-tag model. Author analytic proof and exact integer cross-check; NOT_REVIEWED. No shared CLAIM, no change to P000 or ACTIVE worldview, no native physical attribution. Prior own registration r1-20261124-0256-r284gd-session-v1 was read back as SUCCEEDED, Researcher EM-DIRECT-0C386E, Activity RA-B82240E8488EF5A1DA5186C4. Current owner query r1-20261124-1500-owner-read was RUNNING during derivation; independent work only.

Frozen sources (exact immutable readbacks):
- R284GQ @9f74833b63383390e436542669d7601834a0b2ea:research_notes/portable_direct/R284GQ_ALL_PARAMETER_MINIMIZER_RIGIDITY_20261124.md (symmetric optimal family and mandatory crossing).
- R284GL @5f74ba8a545788cc3fdb080f9953bbe5a0926531:research_notes/portable_direct/R284GL_ASYMMETRIC_THREE_PATTERN_SHARP_CAPACITY_20261124.md (exact attempted-prefix distances).
- R284GE @a112519ea319ef0e0bdf10ee01d817e10fd3dcd5:research_notes/portable_direct/R284GE_EXACT_ADJACENT_ROLLBACK_CAPACITY_20261124.md (full-cycle criterion and order-independent adjacent no-rollback).

## Theorem (all integers u>=1, u<=q<=2u)

Write r=2u+1 and take any integer u+1<=d<=q+1. In the symmetric optimal carrier A=C=2q+d, B=2q+2(r-d), let N(q,u,d) count safe attempted mode words on one edge, with coordinates of one type indistinguishable. A word uses A nonalternating attempts and B alternating attempts. The counts are exact, not probabilities or physical execution times.

If d=r (possible only q=2u), N=binom(4q+r,2q): every word is safe.

Otherwise put s=r-d>0, t=d-s=2d-r>=1, b0=q+s. With binom(n,k)=0 for k<0 or k>n,

    L = sum_{i=0}^t binom(i+q-1,i) *
        [binom(d-1-i+s,s) - binom(d-1-i+s,s-2)],
    R = binom(2q+r-1,b0) - binom(2q+r-1,b0-2),
    N = L*R.

Each edge has the same count by cyclic normalization. GE makes adjacent no-rollback order-independent; the two other phases are excluded by these exact distance tests. Thus the number of full-cycle fixed mode-word tuples is N^4, counting distinct ordered phase edges, with no quotient by phase rotations. If physical coordinate identities are distinguished within each attempted mode, each edge has N*A!*B! possible orders and the full cycle has (N*A!*B!)^4. The repeated Gray minimizer at q>=2u has one mode word per edge (physical permutations not included).

## Proof

GL supplies the exact distances at attempted counts a,b:
    D2 = [d-a]_+ + [b-q]_+ + d,
    D3 = max(0,d,[a-q]_+-q,B-b+[a-q]_+-q+d).
For d=r both are >=r at every prefix. Otherwise a<=A=2q+d implies [a-q]_+-q<=d<r. Consequently safety (D2,D3>=r) is equivalent to
    [d-a]_+ + [b-q]_+ >= s,
    b <= b0 + [a-q]_+.
The lower bound is vacuous when a<=t; for t<a<d it is b>=q+a-t; for a>=d it is b>=b0. The upper bound equals b0 for a<=q. Since d-1<=q, GQ's crossing follows directly: from (d-1,b0) to (q+1,b0) every safe path uses exactly K=q-d+2 successive A steps. Conversely any safe prefix to the former vertex and safe suffix from the latter, joined by this block, are safe. These are exact, unique factorizations of words; no independence of physical omission events is assumed.

Prefix count: for a<=d-1, b<=b0, and the only restriction is the lower bound. Mark the first B step that reaches b=q (q>=1). Its a-coordinate i must be <=t; otherwise an earlier prefix would be unsafe. Conversely any initial path to (i,q-1), followed by this marked B step, is safe; there are binom(i+q-1,i) such paths. The remaining prefix to (d-1,b0) has D=d-1-i A steps and s B steps. The exact restriction is that the integer height b-q+t-a stays nonnegative, initially t-i. Reflection at its first negative step counts forbidden continuations as binom(D+s,D-(t-i)-1)=binom(D+s,s-2); the total is binom(D+s,s). This is the standard unit-step reflection bijection: reflect the initial segment through height -1, turning its starting height h into -h-2 and exchanging the numbers of upward/downward steps on that segment. Sum the disjoint marked prefixes over i to obtain L.

Suffix count: reverse the path from (A,B) to (q+1,b0), with a'=A-a, b'=B-b. The lower bound b>=b0 is automatic throughout the endpoint rectangle. The upper bound b<=b0+a-q becomes b'>=a'-t. The reversed path begins at (0,0), ends at (q+d-1,b0), and stays at height t+b'-a'>=0. Its length is 2q+r-1. Reflection counts forbidden paths as binom(2q+r-1,(q+d-1)-t-1)=binom(2q+r-1,b0-2). This yields R. Multiplication follows from the unique forced block factorization. GE and rotation yield the cycle count above. No SMT or finite extrapolation is used in this counting proof; the inherited global histogram classification remains at its stated evidence grade.

## Consequence: maximizing mode-word flexibility is not the same as maximizing d

At (q,u)=(15,8), the eight minimum-width symmetric configurations correspond to d=9,...,16. Exact one-edge counts:
    9: 33939957924389088
    10: 1190983978074017088
    11: 10681112281230424704
    12: 44972073189281998144
    13: 112545039748905500000
    14: 189363959054919517440
    15: 232270015591550599740
    16: 225890910734335847055
The unique count maximizer is d=15, not the largest d=16. Its compulsory block has length 2 instead of 1. Thus minimizing mandatory block length need not maximize the number of allowable mode words. This comparison counts words, not the fraction of all unrestricted words or physical latency.

At q=2u, d=r and Gray both have all mode words safe, but the symmetric d=r family has binom(10u+1,4u) mode words per edge versus Gray's one. For d<r there exist unsafe words (e.g. all A first violates the lower bound at a=d), so these two endpoint configurations uniquely maximize the fraction of all mode words that is safe, within the classified minimizers. This does not assert the maximizer of absolute count at the transition for arbitrary u.

## Exact executed verification (JavaScript BigInt)

The following program was executed for u=1..22, q=u..2u, d=u+1..q+1. All 2299 comparisons matched an independently accumulated lattice DP using the original asymmetric GL distances (not the derived corridor). The DP evaluates every attempted-count prefix and accumulates safe paths with exact integer arithmetic. The example above was recomputed using the closed count.

```javascript
const C=(n,k)=>{if(k<0||k>n)return 0n;let v=1n;for(let j=1;j<=Math.min(k,n-k);j++)v=v*BigInt(n-j+1)/BigInt(j);return v};
function count(q,u,A,B,Cc){let r=2*u+1,p=x=>Math.max(0,x),m=p(Cc-q),v=Array(B+1).fill(0n);for(let a=0;a<=A;a++)for(let b=0;b<=B;b++){let D2=p(A-a-2*q)+p(p(b-q)+m-q),D3=Math.max(0,Cc-2*q,p(a-q)-q,B-b+p(a-q)-2*q+m);v[b]=D2<r||D3<r?0n:a===0&&b===0?1n:v[b]+(b?v[b-1]:0n)}return v[B]}
function closed(q,u,d){let r=2*u+1,s=r-d,t=d-s,b=q+s;if(s===0)return C(4*q+r,2*q);let L=0n;for(let i=0;i<=t;i++){let D=d-1-i;L+=C(i+q-1,i)*(C(D+s,s)-C(D+s,s-2))}return L*(C(2*q+r-1,b)-C(2*q+r-1,b-2))}
let checks=0;
for(let u=1;u<=22;u++)for(let q=u;q<=2*u;q++)for(let d=u+1;d<=q+1;d++){let A=2*q+d,B=2*q+2*(2*u+1-d),v=count(q,u,A,B,A),w=closed(q,u,d);if(v!==w)throw Error([q,u,d,v,w].join(","));checks++;}
console.log({checks,counts:Array.from({length:8},(_,i)=>String(closed(15,8,9+i)))});
```

## Next

Obtain a sharp optimizer of N over d, including its possible interior maxima and comparison against the all-safe endpoint q=2u. Separately count asymmetric low-omission mode words and distinguish absolute count, normalized safe fraction, and physically labeled order counts. The GP/GQ independent rational certificate replay is still pending; do not redo completed finite capacity scans.
