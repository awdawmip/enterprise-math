# PREFIX-1118 — integer determinant rigidity and simultaneous rational approximation

2026-11-27, EM-DIRECT-780BBE / TASK_RESEARCH, own RA-0ABD84561C86E53067DB0322 (original registration receipt r6-20261123-2358-session-start-own-v1 verified). Author proof, NOT_REVIEWED. Independent research, no new CLAIM, no Task or review mutation. Parent PREFIX-1117, 2b9517e722e86d194c3f864753a0e1689ed888d9:research_notes/portable_direct/2026-11-27_r6_prefix1117_arithmetic_separation.md; exact 8800 output 897771dcc60212121f1e222bf139da189cce0078:research_notes/portable_direct/2026-11-27_r6_prefix1117_root_8800_result.json. Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d and joint observer/time companions; same Stage46 X6 signed BRC model, chart O, incoming -e1, signed reversal -5 (phase cover 5q), other weights 1, next incoming -d, both orientations Link{O,e1} blocked without renormalization, exactly two negatives. Preserve native cell, port, sign/phase, ordered branch multiplicity. The arithmetic here is an auxiliary observer on the inherited signed BRC certificate, not a new native propagation, classical comparison or native spatial plane. The symbol d below denotes the inverse-scale coefficient, not a native direction.

## 1. All true near hits in a dyadic window lie on ONE line

Let f(m)=rho*m+c+d/m with d>0, E>0. A true near hit is an integer pair (m,j) with |f(m)-j|<=E/m^2. Fix a real L>0 and window L<=m<=2L. Suppose d/10+2E/L<1. Then all true near hits in this window are collinear in the auxiliary integer (m,j) relation chart (at most one j per m if 2E/L^2<1; impose that condition as well).

Proof. For three distinct scales a<b<z, let e_m=f(m)-j_m. The integer determinant
D=(z-b)j_a-(z-a)j_b+(b-a)j_z
annihilates the affine terms. The identity
(z-b)/a-(z-a)/b+(b-a)/z = (b-a)(z-b)(z-a)/(abz)
gives
|D|<=d*(b-a)*(z-b)*(z-a)/(abz)+2E*(z-a)/L^2.
Put t=b/a, s=z/a; 1<t<s<=2. The positive factor is (t-1)(s-t)(s-1)/(ts). For fixed t it increases in s: (s-t)(s-1)/s=s-(t+1)+t/s, derivative 1-t/s^2>0. At s=2 it is (t-1)(2-t)/(2t)<1/10, since t^2-(14/5)t+2=(t-7/5)^2+1/25>0. Thus |D|<d/10+2E/L<1, so D=0. If at least two hits exist, every other hit lies on their unique line. For >=2 hits, reduce its slope to coprime p,q, q>0; then h=q*j-p*m is an integer constant and all scales are in the same residue class -p^{-1}h mod q (q=1 gives residue 0). This is a theorem about TRUE near hits, not all finite-box uncertainty candidates. No chosen CF direction is required.

For Stage46, the 8800 box gives d_u<10 and the exact determinant margin 1-d_u/10-2E/10^8 = approx 0.022913734035845117>0. E=400000 and 2E/(10^8)^2<1. Consequently the theorem applies to EVERY dyadic window L>=10^8, conditional only on that d bound and inherited model correspondence. The upper bound on d also holds in the earlier much wider PREFIX-1112 box, so this structural conclusion does not rely on the last digits of the 8800 anchor.

## 2. Simultaneous rational approximation is necessary for triple clusters

On the primitive line of two true hits a<b, put delta=rho-p/q, gamma=c-h/q. The exact two signed equations e_a=delta*a+gamma+d/a and e_b=delta*b+gamma+d/b give
delta=d/(ab)+(e_b-e_a)/(b-a),
gamma=-d*(1/a+1/b)+(b*e_a-a*e_b)/(b-a).
Since b-a>=q and L<=a<b<=2L:
|delta-d/(ab)|<=2E/(q*L^2),
|gamma+d*(1/a+1/b)|<=4E/(q*L).
In particular if q>8E/d then delta>0 and gamma<0; the approximation is one-sided for both coefficients. These identities retain the signed residuals, and their exact input/output is the full pair of hits; no inference of exact cancellation is made from a small scalar.

If there are >=3 true hits, Section 1 puts them all on this line and PREFIX-1117 curvature spacing gives q^2<=16EL/d (use H=2L). Thus L>=d*q^2/(16E). Combining yields
|rho-p/q| <= (d+2E/q)*(16E/d)^2/q^4,
|c-h/q| <= (2d+4E/q)*(16E/d)/q^2.
If rho is irrational and there are infinitely many unbounded windows with triples, their q tend to infinity: bounded denominators and slopes converging to rho would force rho rational. Hence infinitely many reduced fractions approximate rho from below at O(q^-4), with a simultaneous approximation of c from above at O(q^-2) using the SAME q. As a conditional consequence, if the irrationality exponent of rho is <4, all sufficiently large dyadic windows contain at most two true hits. The definition of exponent here is the supremum of nu with infinitely many reduced p/q satisfying 0<|rho-p/q|<q^-nu; any fixed constant times q^-4 suffices for every nu<4 at large q. Also if c is rational, then eventually no triples for any irrational rho: write c=A/B in reduced form, and nonzero |c-h/q|>=1/(Bq), contradicting the O(q^-2) bound and gamma<0 for large q. If rho is rational, PREFIX-1117 already gives eventual absence of true hits for any fixed real c and d>0. No irrationality exponent or rationality result for actual Stage46 coefficients is asserted. Even an at-most-two theorem would not by itself establish eventual separation.

## 3. Exact finite threshold computation: all 122 candidates, at most one genuine ambiguity

Loaded the attached PREFIX-1117 archive; all 20 manifest entries passed sha256sum -c. Reused exact PREFIX-1116 lattice sweep (2ec540692bf1ba695b60416903db654f797f3e67:research_notes/portable_direct/2026-11-27_r6_prefix1116_convergent_lattice.py), raw 8800 coefficients and previous ordered candidate list; no new anchor/native CT run. Recomputed the ten doubling windows [15845632502852867518708790067200000000,16225927682921336339157801028812800000000), counts [0,0,0,0,0,0,0,0,26,96], all 122 pairs exactly agree with the parent list.

For each candidate define closed slope threshold interval [l,u] using PREFIX-1115:
l=(j-c_u-d_u/m-E/m^2)/m,
u=(j-c_l-d_l/m+E/m^2)/m.
If rho<l then f(m)-j<-E/m^2; if rho>u then f(m)-j>E/m^2. Conditional signs follow from the inherited PREFIX-1107 strict sign and PREFIX-1097 last-negative monotonicity (all candidate offsets are within the applicable local radius; parent max band width <1). Exactly all 122 threshold intervals lie strictly inside the current rho box and are strictly pairwise separated. Min adjacent gap approx 3.945557973688398e-83 (strictly >3945/10^86), maximum threshold width approx 1.0333859155427213e-113 (strictly <1034/10^116). Consequently for ANY fixed parameter triple in the box at most ONE of these 122 positions can actually satisfy |f(m)-j|<=E/m^2. All others have strict sign, although their signs are not individually certified from the box alone. Under the inherited signs, there are at most 123 binary last-negative sign patterns (treat zero as not negative); unknown exact-zero oracle termination is not assumed. A terminating binary sign/negative-membership oracle would need at most 7 queries. First balanced query can be the 61st threshold: m=15277668224026231384019257485398459832779, j=327553767725281603641909970817076312509991.

The verifier also constructs ALL 123 strict sign patterns using the SAME midpoint c,d and one rational rho in each consecutive threshold gap (including the two end gaps). These witnesses verify directly against the strict analytic band by exact Fraction arithmetic. Thus the present rectangular box alone permits every cut and cannot certify any individual sign among the 122. They are witnesses in the auxiliary parameter model only, not alternative actual BRC spectra. To reduce all uncertainty to at most one candidate, it is sufficient to get a nested rho interval of width strictly below the minimum gap, keeping current c,d intervals. The required shrink factor is approx 24207.808030434782; a factor 24209 suffices. This is a concrete precision target for one-dimensional joint root refinement, not a guaranteed new anchor output. A narrower box need not exclude its last candidate.

For the two occupied windows the SAME convergent denominator q=3380890274893182433251695995418378677023 was used. Union of all 122 uncertainty points gives 43 distinct lines in this direction with histogram {1:10,2:4,3:12,4:17} (multiplicity:number of lines); this is a finite-box observation, distinct from the single-line theorem for true near hits.

## 4. Actual execution and evidence

Exact Fraction verifier ran normally. Output log:
n 122 window_counts [0, 0, 0, 0, 0, 0, 0, 0, 26, 96] gap 3.945557973688398e-83 maxwidth 1.0333859155427213e-113 shrink_factor 24207.808030434782 determinant_margin 0.022913734035845117
all_patterns_admitted 123 cf_q 3380890274893182433251695995418378677023 line_count 43 line_size_histogram {'1': 10, '2': 4, '3': 12, '4': 17}
first binary query (15277668224026231384019257485398459832779, 327553767725281603641909970817076312509991)
prefix1118_result.json SHA256 7ab33b99d7bf1c97503b947e3aa93481cfb9ce24e8596e2c3838233be3.

Actual verifier below. Obtain prefix1116_lattice.py and root_8800_result.json from the immutable paths above; prefix1117_result.json from parent execution archive (SHA256 5204d06289bba9d8155044be15f673e07d63d66b32bb7fc997b088d2ae1821a8). Its pair list comparison is an additional check; the complete sweep is the coverage basis. Exact raw root hash 367ed5c982ef92405623cfe6633aa29ce1449bfa2e1cb2e355fd8692d84355a9. New ZIP contains actual code, original inputs, full ordered rational thresholds, output log and hashes. The inherited 8400/8800 root commands' normal exits remain unconfirmed; this turn verifies auxiliary arithmetic, not the validity of the root construction. No new individual sign closures or window extension claimed. Continuous certified endpoint remains 4265326180744162387203315935318273935179 exclusive, conditional on inherited premises.

```python
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
from prefix1116_lattice import load,sweep,expand,E,G

R,C,T=load('root_8800_result.json')
prev=json.loads(Path('prefix1117_result.json').read_text())
# Re-run exact inherited arithmetic sweep, not native propagation.
w=sweep((R,C,T),prev['windows'][0]['L'],prev['end'])
pairs=sorted(p for x in w for p in expand(x))
assert pairs==[tuple(p) for p in prev['remaining']] and len(pairs)==122
z=sorted(((F(j)-C[1]-T[1]/m-F(E,m*m))/m,(F(j)-C[0]-T[0]/m+F(E,m*m))/m,m,j) for m,j in pairs)
assert all(R[0]<l<=u<R[1] for l,u,m,j in z)
gap=min(y[0]-x[1] for x,y in zip(z,z[1:])); assert gap>0
maxwidth=max(u-l for l,u,m,j in z)
assert R[1]-R[0]<24209*gap
# A strict width less than gap ensures at most one threshold interval is intersected.
assert F(3945,10**86)<gap and maxwidth<F(1034,10**116)
# Exact collinearity certificate for all dyadic windows at m>=10^8.
margin=1-T[1]/10-F(2*E,10**8)
assert margin>0
# Fixed c,d at their midpoints, all 123 strict sign patterns admitted by the input box.
cm,dm=sum(C)/2,sum(T)/2
for i in range(len(z)+1):
    lo=R[0] if i==0 else z[i-1][1]
    hi=R[1] if i==len(z) else z[i][0]
    rho=(lo+hi)/2
    for k,(_,_,m,j) in enumerate(z):
        v=rho*m+cm+dm/m-j
        assert v>F(E,m*m) if k<i else v<-F(E,m*m)
# Same CF direction for the last two windows; classify distinct occupied lines exactly.
p,q=w[-1]['p'],w[-1]['q'];assert (p,q)==(w[-2]['p'],w[-2]['q'])
counts={}
for m,j in pairs:
    h=q*j-p*m;counts[h]=counts.get(h,0)+1
out=dict(n=len(z),window_counts=[x['count'] for x in w],gap=str(gap),maxwidth=str(maxwidth),shrink_factor=str((R[1]-R[0])/gap),margin=str(margin),ordered=[dict(m=m,j=j,lower=str(l),upper=str(u)) for l,u,m,j in z],all_patterns_admitted=123,cf_p=p,cf_q=q,line_count=len(counts),line_size_histogram={str(n):list(counts.values()).count(n) for n in sorted(set(counts.values()))},input_sha256={name:hashlib.sha256(Path(name).read_bytes()).hexdigest() for name in ['root_8800_result.json','prefix1117_result.json','prefix1116_lattice.py']})
Path('prefix1118_result.json').write_text(json.dumps(out,indent=2)+'\n')
print('n',len(z),'window_counts',out['window_counts'],'gap',float(gap),'maxwidth',float(maxwidth),'shrink_factor',float((R[1]-R[0])/gap),'determinant_margin',float(margin))
print('all_patterns_admitted',123,'cf_q',q,'line_count',len(counts),'line_size_histogram',out['line_size_histogram'])
print('first binary query',z[60][2:]);print('sha256',hashlib.sha256(Path('prefix1118_result.json').read_bytes()).hexdigest())
```

## 5. Next

Study the intrinsic coupled approximation condition for (rho,c) from signed BRC spectral construction, especially exclusion of triple clusters without assuming the actual irrationality exponent. For immediate finite closure, use a nested root-only refinement of rho by >=24209 in width (or exact sign oracle with termination proof); retain c,d and original signed carrier. Verify anchor completion when useful; no claim of all-scale strict separation or exact zero decision. Mother B_fix,odd(32), other spectral roots, independent review and observation audit remain open. The current LEASED owner query r6-20261127-0451-leased-read-v1 was RUNNING at latest observation before saving; do not infer empty or claim a task from it. Only independent science and own Activity bookkeeping here.
