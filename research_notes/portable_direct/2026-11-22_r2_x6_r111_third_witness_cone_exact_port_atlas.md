# X6 R111 — A third-witness residue certificate and an exact seven-direction Port atlas

2026-11-22 | AUTHOR_PROOF / EXACT_RATIONAL_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED

Frozen ontology: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json (P000 V5).
Scientific predecessor: R104 (13 nonzero mod-3 sign orbits), R109 (12 on a cone), R110 (two-witness residue exclusion) @21fad2aa0cd969f60f17e2a8131e74df4a7a2ede. All conclusions here concern the **conditional auxiliary positive-weight six-pair BRC observer**, not native X6 Cell/Link/heartbeat evolution. All six original pair observations and integer Port provenance remain intact.

## Model

For nonzero a=(x,y,z) in Z^3, identify a with -a and put

    q(a)=max(sum(max(a_i,0)),sum(max(-a_i,0))).
    u=x+3y+6z; v=3x+12y+30z; h=7x+39y+126z.

For w=(A,B,C,D)>0, retain all six pair observers:

    F_w(a)=max(|u|/(A+B), |v|/(A+C), |h|/(A+D),
               |v-u|/(B+C), |h-u|/(B+D), |h-v|/(C+D)).

For integer p>=10, eta_p(w)=min_{a !=0,q(a)<=p} F_w(a), and
N_p(w)={±a : q(a)<=p and F_w(a)<3 eta_p(w)/2}.

## Theorem 1 — single new feasible witness, Port >=10

Let m=min(A,B), n=min(A,B,C), and b=(9,-5,1) with q(b)=10 and moment triple (u,v,h)=(0,-3,-6). Its exact score is

    V_b(w)=F_w(b)=max(3/(C+m), 6/(D+m), 3/(C+D)).

If

    V_b(w) <= min(2/(A+B), 6/(C+m), 8/(D+n)),               (R111-B)

then for every integer p>=10,

    |N_p(w)| <= 12.

The hypothesis is checkable using only positive weights and the stated **feasible** b direction. It is equivalent to these four homogeneous weak inequalities:

    3(A+B) <= 2(C+m),
    3(A+B) <= D+m,
    D >= C,
    3(D+m) <= 8(C+m).                                     (R111-CONE)

Indeed, the first inequality forces C>=2m. Hence n=m and D>=C>=m, so 3/(C+D)<=3/(C+m), and the three upper comparisons for V_b reduce exactly to the four listed inequalities.

### Infinite-lattice proof

The b witness is feasible for p>=10, so eta_p<=V_b. R104's mod-3 lemma: two distinct unoriented vectors in the strict 3/2-near set cannot share any nonzero sign-orbit in (Z/3Z)^3. If they did, orient them with a congruent to b modulo 3, then c=(a-b)/3 is a nonzero integer difference with q(c)<=2p/3<=p and F(c)<eta_p, a contradiction. A vector in the zero orbit similarly contracts by division by 3. Thus 13 nonzero sign-orbits are the only possibilities.

Consider the single orbit L={±(0,1,2)} in the **original x,y,z coordinates**. Orient a so x=0,y=1,z=2 mod 3. Then u=x+3y+6z is divisible by 3. The first inequality R111-B gives

    |u| < 3 eta_p (A+B)/2 <= 3 V_b (A+B)/2 <= 3,

hence u=0. Solving x=-3y-6z yields v=3(y+4z). Since y+4z=1+8=0 mod 3, v belongs to 9Z. With u=0, the retained (A+C) and (B+C) observations imply

    |v|/(C+m) <= F_w(a) < 3 eta_p/2 <= 3 V_b/2 <= 9/(C+m),

so v=0. Now u=v=0 gives a=(6z,-4z,z), h=12z. All three retained h-pairs yield

    |h|/(D+n) <= F_w(a) < 3 eta_p/2 <= 3 V_b/2 <= 12/(D+n),

forcing z=0 and contradicting a !=0. Thus L is empty and the other twelve orbits each contain at most one near direction. QED.

The non-strict certificate boundary is valid because near-optimal membership is strict. This theorem holds for all positive real w satisfying its displayed inequalities, not only sampled rational weights.

## Theorem 2 — strict extension beyond R110 and a complete all-Port example

Take the positive quadruple

    w0=(1,1,6,16).

It lies in the **strict interior** of R111-CONE:

    6<14,  6<17,  16>6,  51<56.

At this point R110's older two-witness upper bound, from s=(10,-5,1) and t=(24,-14,3), equals U_st=min(1/2,6/7)=1/2. R110-CERT requires U_st<=min(1,6/7,8/17)=8/17, which fails (1/2>8/17). The new b witness instead gives V_b=3/7<8/17. Therefore the new certificate covers a nonempty open four-dimensional region outside the former certificate. The result also lowers the sufficient Port requirement from 27 to 10 on this region.

At w0, for **every integer p>=10**,

    eta_p(w0)=3/7.                                           (1)

Proof: b has F=3/7 and q=10. Conversely, for any nonzero integer a, if u!=0 then F>=|u|/2>=1/2>3/7. If u=0 but v!=0, then v is a nonzero multiple of 3 and F>=|v|/7>=3/7. If u=v=0, the inverse moment map gives a=(6z,-4z,z), h=12z, so F>=12/17>3/7 for z!=0. The determinant of the moment map is 36 and its zero kernel is {0}. This proves (1) across the infinite lattice.

Moreover, the **entire** strict near set N_p(w0) consists of precisely the following rows whose q value is <=p:

| Unoriented a=(x,y,z) | q(a) | F_w0(a) |
|---|---:|---:|
| (1,0,0) | 1 | 1/2 |
| (5,-4,1) | 6 | 1/2 |
| (9,-5,1) | 10 | 3/7 |
| (10,-5,1) | 11 | 1/2 |
| (15,-9,2) | 17 | 3/7 |
| (19,-10,2) | 21 | 4/7 |
| (25,-14,3) | 28 | 4/7 |

Thus |N_10|=3, |N_11|=4, |N_17|=5, |N_21|=6, and |N_p|=7 for all p>=28, with the indicated intermediate Port thresholds.

### Whole-lattice completeness certificate

Since eta=3/7, strict-near means F<9/14. For w0 the six denominators are (2,7,17,7,17,22), so every such vector lies in the **complete integer moment box**

    |u|<=1, |v|<=4, |h|<=10,
    |v-u|<=4, |h-u|<=10, |h-v|<=14.                    (2)

The integer inverse is

    x=(h+19u-8v)/2,
    y=(-h-14u+7v)/3,
    z=(h+11u-6v)/12.

Necessary and sufficient congruences for this inverse to be integral are

    v=0 (mod 3),  h-u=0 (mod 6),  h-u-6v=0 (mod 12).

Exact enumeration of u=-1..1, v=-4..4, h=-10..10 with all six inequalities (2) and these congruences gives exactly 14 nonzero oriented solutions, namely ± the seven displayed rows. Every integer vector outside the moment box violates at least one of the original six inequalities; hence the atlas is proved for the infinite lattice and all Port budgets, not inferred from a finite Port scan.

Companion script x6_r111_dual_witness_verify.py uses Python Fraction and separately scans the full 38,598 unoriented nonzero directions with q<=28 to cross-check six Port values (10,11,17,21,27,28). Exact result: PASS. The finite scan is auxiliary to the symbolic infinite-lattice reduction. No independent mathematical review or Lean formalization is asserted.

## Relation, control and next question

R111 strengthens the R110 **sufficient** twelve-direction certificate by a different concrete feasible BRC direction b; the general 12-versus-13 question outside the union of certified cones is still open. Next try other short witnesses and residue-orbit exclusions, or construct an exact 13-orbit witness. Keep the original pairwise observation map, P000 V5 pins and any separate native R063 six-file benchmark. Neither Research Activity nor formal native CLAIM/PROGRESS/Result/Review authority is conferred by this proof.
