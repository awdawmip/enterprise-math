# PREFIX-1094b -- Seven base densities plus two mixed-shift states; exact moment anchor theorem

2026-11-26. AUTHOR_EXACT_ALGEBRAIC_REDUCTION / FINITE_EXACT_SYMBOLIC_COMPUTATION / NOT_REVIEWED. Follow-up in the same independent R6 continuation as PREFIX-1094. Frozen P000 V5 and Stage46 two-negative signed paired BRC input unchanged; full branch, port, phase, Cell equality and ordered multiplicities inherited through the exact CT observer. No native-state collapse or new classical numerical comparison. Same own activity RA-0ABD84561C86E53067DB0322, research identity metadata EM-DIRECT-780BBE / TASK_RESEARCH. No claim or shared task mutation. Original owner query r6-20261126-0458-owner-read has now returned SUCCEEDED / error=null, snapshot as_of 2026-11-25T21:00:03.774312Z at Source 6ef4949f9a48d3349766b474b5cef8105a6aafd4, LEASED filter empty; Source changed at completion, no fresh write authority asserted.

Parent: 73e04d060c31c64a3c9fcd3986ce03617a74f0b1:research_notes/portable_direct/2026-11-26_r6_prefix1094_radial_density_pencil.md. This addendum supersedes the parent's *open 35-state reduction* statement, not its proved pencil.

## 1. Repeated weighted states give algebraic constraints

Use the parent's six absolute-shift blocks indexed by a. Each has exact grouped ODE y_a'=L_a(R)y_a, L_a=P_a^-1 B_a, regular on R in (0,4), (4,16), (16,36). For every state h in a block, its actual weighted radial measure is mu_b, where the nonnegative shifted profile b is obtained by incrementing the selected a_i by one. The sorted profile b determines the measure exactly by permutation invariance of the character carrier. This equality is an observer equality for all radial tests, not a native spatial quotient.

Across all six blocks the 78 entries are exactly 35 distinct sorted b profiles. For each b, select the first encountered derivative row as a rational linear form in the 35 functions; for each other occurrence subtract its derivative row from the selected one. All 43 duplicate derivative rows differ as formal rational linear forms. On the actual density vector Y, every difference vanishes identically in each regular interval because the corresponding function mu_b is the same function in both blocks. Write these 43 equations as C(R)Y(R)=0.

An actual exact symbolic calculation over QQ(R), using the fixed six blocks and ordered grouped states below, found rank(C)=28. Order the columns with the 28 profiles with max(b)>1 first, followed by the seven profiles with max(b)<=1. The reduced row echelon form is [I_28 | -T(R)] with zero rows below. The 28x7 matrix T has 163 nonzero coefficients and all are polynomials in R of degree at most 3 (rational constants allowed). Thus on every regular interval

 Y_rest(R)=T(R) y(R),

where y_j=mu_(0^(6-j),1^j), j=0,...,6. The computation uses exact rational function row reduction; no finite sampling assumption. If intermediate row operations have isolated poles, the polynomial identity for the reconstructed functions extends there by analytic continuity. No extra finite singularity is introduced by reconstruction.

The seven base densities are exactly the zero-shift grouped block of PREFIX-1094, with a=0, r=6. They already satisfy its own closed rational ODE, so the actual original weighted observer needs only this seven-component differential state. The two mixed signed shifts still use the scalar dilation auxiliaries nu_1 and nu_2 of PREFIX-1094. Their ODEs R nu_Q'=Q nu_Q-mu_abs(d) have known polynomial readouts mu_abs(d) from the seven base densities. This is a closed nine-component ODE for the actual weighted observer on each regular interval. The 66-term signed residual density is a rational readout, via the moment operator E=-d/dR(R*), exactly as in the parent. It preserves every original D_m(k) on the declared polynomial observation family (distributional endpoint information is kept in the original moment representation, not reconstructed from this open-interval ODE alone).

The rank and polynomial readout are sufficient for this exact forward reduction on the actual density. An attempted separate full differential compatibility test for arbitrary formal solutions of the reduced system did not finish within the local command time limit. No claim that arbitrary unconstrained initial values describe the original BRC measure. Actual initialization is fixed by the original moments; the next section provides a rigorous anchor route.

## 2. Exact interior point anchors from the original moments

Let Y(R) denote the nine real densities of the reduced system, with finite signed measures on [0,36]. The seven base measures have total variations at most 6^j, because |S|<=6 on the full six-character carrier. The mixed dilation measure has total variation at most 6^A/(Q+1). Thus a rational bound V for the sum of the nine total variations is available directly from the fixed input.

Fix any rational R0 in a regular open interval, and a closed centered interval J=[R0-rho,R0+rho] in that same band. Let L be a rational upper bound for the induced infinity norm of the nine-state rational ODE matrix on J. Shrink rho if necessary so L*rho<=1/2. Such rational choices exist because the matrix is continuous near R0; denominators can be bounded by rational interval estimates on a small enough interval.

For every t in J, standard integral iteration for this *analytic observer ODE* gives ||Y(R0)||_inf <= exp(L*rho)||Y(t)||_inf <= 2||Y(t)||_inf (use exp(s)<=1/(1-s) for 0<=s<1). Integrate in t and use sum total variation <=V, obtaining ||Y(R0)||_inf <= V/rho. In turn the ODE gives sup_J ||Y'||_inf <= 2 L V/rho. These bounds require no numerical classical propagator and no unknown density values.

Choose N a multiple of the denominator of rational x0=R0/36, set a=N x0, b=N(1-x0), and let

 K_N(R)=(N+1)/36 * binom(N,a)*(R/36)^a*(1-R/36)^b.

This is a nonnegative polynomial with integral 1 on [0,36], maximized at R0. For each component of the measure vector, I_N=integral K_N dmu is exactly computable from the inherited BRC paired moments (mixed auxiliary moments divide by j+Q+1). Its second moment about R0 under Lebesgue integration is explicitly

 sigma_N^2=36^2*((a+1)*(b+1)/((N+2)^2*(N+3))
                    +((a+1)/(N+2)-x0)^2).

This follows by integrating the polynomial beta weight, or by exact factorial integration; it tends to zero. Set tau_N=max(K_N(R0-rho),K_N(R0+rho)), an exact rational upper bound for K_N outside J by unimodality. Since each endpoint has a strictly smaller base x^x0(1-x)^(1-x0) than at x0 and binom(N,a)*x0^a*(1-x0)^b<=1, tau_N tends to zero exponentially times N+1. The ratio can also be checked entirely rationally by taking N in multiples of the fixed denominator.

Split the difference I_N-Y(R0) into the local and complementary parts. The derivative bound and Cauchy-Schwarz give the local contribution <=(2 L V/rho)*sqrt(sigma_N^2). The absolute complement from the signed measures is at most V*tau_N; the missing constant contribution from Y(R0) is at most (V/rho)*36*tau_N. Consequently

 ||I_N-Y(R0)||_inf <= (2 L V/rho)*sqrt(sigma_N^2)
                       + V*(1+36/rho)*tau_N.                (2)

All RHS terms are rational or a square root of a rational and can be bounded by exact rational inequalities. Therefore the actual nine-component interior density vector has arbitrarily accurate rational enclosures using only original exact moments. In particular this removes the need for an unverified numerical value or a classical reference calculation to initialize a local analytic observer. The existence theorem applies at any rational interior point; its practical degree/cost and the sharpness of L,V,rho remain to be optimized. A proof of positivity at the singular endpoint R=0 is still required to certify the complete interval.

## 3. Actual symbolic computation and reproducible certificate

The following code reproduces the block construction, all 43 relations, rank 28 and polynomial readout. It uses the exact BRC CT-derived differential pencil of PREFIX-1094, not a new numerical evolution. The executed computation additionally found 548 nonzero entries in the 35 selected derivative rows and their common denominator R^4(R-36)(R-16)(R-4). The coefficient matrix T digest below was obtained from a separate completed exact run after dropping the slow differential-consistency check.

```python
from collections import Counter
from itertools import product
import sympy as sy
from sympy.polys.matrices import DomainMatrix
import hashlib,json
R=sy.symbols('R')
shifts=[(3,0,0,0,0,0),(2,1,0,0,0,0),(2,0,0,0,0,0),
        (1,1,0,0,0,0),(1,0,0,0,0,0),(0,0,0,0,0,0)]
rows={}; relations=[]; repeats=0; differences=0
for a in shifts:
    g=sorted(Counter(a).items()); av=[v for v,_ in g]
    r=[n for _,n in g]; A=sum(a)
    states=list(product(*(range(n+1) for n in r)))
    ix={h:i for i,h in enumerate(states)}; n=len(states)
    U=sy.zeros(n); D=sy.zeros(n); H=sy.diag(*map(sum,states))
    J=sy.diag(*(sum(v*k for v,k in zip(av,h)) for h in states))
    I=sy.eye(n)
    bs=[tuple(sorted(v for aa,h,rr in zip(av,hs,r)
                    for v in [aa+1]*h+[aa]*(rr-h))) for hs in states]
    for h in states:
        i=ix[h]
        for k in range(len(r)):
            if h[k]<r[k]:
                U[i,ix[h[:k]+(h[k]+1,)+h[k+1:]]]=r[k]-h[k]
            if h[k]:
                D[i,ix[h[:k]+(h[k]-1,)+h[k+1:]]]=h[k]
    P=R*(I-D)-U; B=H+J-I+(I-A*I-H)*D
    dm=DomainMatrix.from_Matrix(P)
    num,den=dm.inv_den(); nm=num.to_Matrix()*B
    dv=dm.domain.to_sympy(den)
    for i,b in enumerate(bs):
        row={bb:sy.cancel(nm[i,j]/dv) for j,bb in enumerate(bs) if nm[i,j]!=0}
        if b in rows:
            repeats+=1
            rel={k:sy.cancel(rows[b].get(k,0)-row.get(k,0))
                 for k in set(rows[b])|set(row)}
            relations.append(rel)
            if any(v!=0 for v in rel.values()):differences+=1
        else:rows[b]=row
assert (len(rows),repeats,differences)==(35,43,43)
assert sum(map(len,rows.values()))==548
bs=sorted(rows)
base=[b for b in bs if max(b)<=1]; rest=[b for b in bs if max(b)>1]
order=rest+base
C=sy.Matrix([[rel.get(b,0) for b in order] for rel in relations])
dm=DomainMatrix.from_Matrix(C).to_field()
rr,piv=dm.rref()
assert piv==tuple(range(28))
T=-rr.to_Matrix()[:28,28:]
assert sum(v!=0 for v in T)==163
assert all(sy.denom(sy.cancel(v))==1 for v in T) # rational coefficients as expanded polynomial
assert max(sy.Poly(v,R).degree() for v in T if v!=0)==3
assert hashlib.sha256(json.dumps([[str(v) for v in row] for row in T.tolist()],
    separators=(',',':')).encode()).hexdigest()=='333adb48c52ac3c5530e8d0509a7b45b77db62a99e65557cafbd70ce38bba312'
```

The exact run reported the denominator LCM via monic polynomial denominators, equal to 1 (constant rational denominators are allowed). If a SymPy version exposes a constant denominator directly in the final assert, equivalently check sy.Poly(v,R) over QQ for every coefficient; this is the mathematical condition. The hash is tied to the executed SymPy string serialization. No density anchor value, interval propagation or new sign certificate was actually evaluated in this addendum. No independent review.

## 4. Next

Construct explicit interval matrix and signed readout for the nine-state system, evaluate (2) at a rational lower-band anchor, then use certified analytic enclosure away from the singular origin. Separately obtain a computable origin asymptotic remainder or regular-singular certificate. The complete positivity hypothesis 0<x<1/24 (0<R<3/2) and the conditional full negative mass of PREFIX-1093 remain unresolved. Mother B_fix,odd(32), p and d remain open.
