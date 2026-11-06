# D25 — Pfaff two-port transversality and unique p² root lifts

Date: 2026-11-07, TASK_RESEARCH author-side result, PROVED / FINITE_VERIFIED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_BENCHMARK.
Task publication TP2-B6F4FC938FF94941C1B7. Original scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged. Research lane chatgpt-research-onhour-enterprise-math-20260923; no maintenance-lane authority used.
Consumes the previous exact Pfaff identities at Enterprise Math commit 29bffe3be88039bf21739b44ded15c75e1e99d2f; does not reclaim another owner's mathematics.

## Theorem: two ports cannot vanish together, and each zero is simple

For prime p=6m+1>3, set D(z)=sum_{k=0}^m binom(m,k)binom(2m,k)z^k, E(z)=D(z)+6D'(z), z0=1/2, and define integer ports
S=sum_{k=0}^m binom(m,k)binom(2m+k,k),
T=sum_{k=0}^m k binom(m,k)binom(2m+k,k).
The already-proved terminating Pfaff formulas imply
2^m D(z0)=S; 2^m D'(z0)=V=-2m S+4T;
2^m E(z0)=B=(1-12m)S+24T.
Thus modulo p, B=3(S+8T).

**Unconditional all-prime theorem.** For every such p, S and S+8T are not simultaneously zero modulo p. Every zero at z0 of either D or E modulo p is simple.

Proof: the terminating hypergeometric polynomial D={}_2F_1(-m,-2m;1;z) solves the exact differential equation
z(1-z)D''+[1+(3m-1)z]D'-2m²D=0.
At z0 in F_p, a multiple zero of D of multiplicity 2<=r<=m would require z0(1-z0)r(r-1)=0. Since m<p and z0 is not 0 or 1, this is impossible. Hence D(z0)=0 implies D'(z0) nonzero, so S=T=0 is impossible. If S=0 and S+8T=0 then T=0, proving mutual exclusion.

The same equation gives D''(z0)=8m²D(z0)-2(3m+1)D'(z0). Therefore
E'(z0)=48m²D(z0)-(36m+11)D'(z0).
Because 6m=-1 in F_p, E'(z0)=(4/3)D(z0)-5D'(z0) modulo p.
When E(z0)=0, D'(z0)=-D(z0)/6; thus E'(z0)=(13/6)D(z0).
D(z0) is then nonzero by mutual exclusion. For p!=13, E' is nonzero. For p=13, m=2 and the exact ports are S=26,T=40,B=362=11 mod13; therefore E(z0) is not zero. QED.

This proves the **non-overlap/simple-root property**, not the all-prime conjectured residue-class selection of which port vanishes.

## Explicit mod-p² Hensel displacement

Use integer V=-2mS+4T, B=(1-12m)S+24T, U=(-36m-11)V+48m²S.
By Pfaff and the ODE, 2^mD'(z0)=V and 2^mE'(z0)=U exactly.
For z=z0+p u in Z/p²Z,
2^mD(z)=S+p u V mod p²; 2^mE(z)=B+p u U mod p².
Each zero port has a *unique* root lift:
- When S=0 mod p, V=4T nonzero mod p and u_D=-(S/p)(4T)^{-1} mod p.
- When B=0 mod p, p!=13 and U nonzero mod p; u_E=-(B/p)U^{-1} mod p.
The quotients S/p and B/p are integers only on their respective zero branch. This yields a labelled first-order p-adic observer instead of a collapsed scalar product.

## Independent exact computation

Checker: d25_pfaff_port_hensel_check_20261107.py. It evaluates S,T as integer binomial sums, independently evaluates D,D',D'' as polynomial jets, compares all identities mod p², checks the lifted zero and a distinct neighbouring nonroot. Executed on all 148 primes 7<=p<=1999 and p=6m+1 (77 D-zero, 71 E-zero); plus p=5113. All PASS.
Witnesses (p,branch,u,z lifted mod p²,scaled derivative mod p):
(7,E,6,18,4); (13,D,6,163,4); (19,D,16,124,16);
(31,E,12,853,30); (37,D,25,241,1); (67,D,40,436,25);
(373,D,276,33384,103); (5113,E,3707,5882507,3205).

BRC COMPOSE_APPLIED: exact carrier (p,m,S,T); observer ports D(z0),E(z0), first-order deformation z0+p u; retain valuation and source/branch labels. This is external arithmetic rather than native H0/B0 execution.

## Continuation and state

Frozen mother target W_p=p mod p³ for primes p mod24=13,19, equivalently Delta_p-R_p=0 mod p. Next: compare the explicit D-port displacement u_D at p=19,373 with previously certified signed Clausen J_19=6,J_373=98 and nonzero original216 second-shell/parameter jet; attempt an exact p²-correction identity. Prove or disprove all-prime class selection S=0 mod p on p mod24=13,19 independently. Native p373 original-class H0/B0 divided-power [X]U, Frobenius/eta and signed Hesse Green/kappa with independent reproduction remain NOT_EXECUTED/PENDING_OWNER under issue #1559.

On 2026-11-07, Site gateway reads of Source status/checkpoint/original receipt returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false; a separate configuration status showed research_authority_granted=false. Original target_request_id onhour11-20261106-1400-exact-research-lane-continuation and Source checkpoint revision22 are **historical** pointers, not fresh Source results; no current session, CLAIM, run, formal Result or review was verified. Do not adopt the maintenance lane identity. This source-separated artifact is author-side and unreviewed.
