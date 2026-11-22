# X6 R110 — An all-weight residue-exclusion certificate and an extended sharp twelve-near cone

2026-11-22 | AUTHOR_PROOF / EXACT_INTEGER_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED

Frozen scientific ontology: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json (P000 V5). This is the conditional auxiliary four-positive-weight six-pair BRC observer developed in X6 R104–R109, not a theorem about native X6 Cell/Link/heartbeat evolution. Original joint pair observations and the exact integer lattice are retained.

## Definitions

For an unoriented nonzero integer triple a=(x,y,z), let q(a)=max(sum of positive components, sum of absolute negative components). Define exact integer moments

    u=x+3y+6z,   v=3x+12y+30z,   h=7x+39y+126z.

For arbitrary positive real weights w=(A,B,C,D), the complete six-pair score is

    F_w(a)=max(|u|/(A+B), |v|/(A+C), |h|/(A+D),
               |v-u|/(B+C), |h-u|/(B+D), |h-v|/(C+D)).

For an integer p>=11 set eta_p=min F_w(a) over nonzero q(a)<=p, and N_p(w)={unoriented a: q(a)<=p and F_w(a)<3 eta_p/2}.

Define an *explicit* upper bound using the feasible directions s=(10,-5,1), q=11, and t=(24,-14,3), q=27:

    U(w) = min( 1/[min(A,C)+min(B,D)],
                6/[C+min(A,B,D)] ).

The two equalities F_w(s)=1/[min(A,C)+min(B,D)] and F_w(t)=6/[C+min(A,B,D)] follow by substituting their exact moment triples (1,0,1) and (0,-6,0).

## Theorem 1 — general sufficient certificate

Let A,B,C,D be arbitrary positive real numbers and let p be any integer >=27. If

    U(w) <= min( 2/(A+B),
                 6/[C+min(A,B)],
                 8/[D+min(A,B,C)] ),                         (R110-CERT)

then the strict 3/2-near set satisfies

    |N_p(w)| <= 12.

The inequalities are non-strict, including equality cases, because the defining near-optimal cutoff is strict. This is an all-integer-lattice theorem, not a finite Port search. The criterion uses only four weights and two explicitly feasible BRC directions; no unknown optimum or numerical optimization is required.

### Proof

For p>=27, both s and t are feasible, whence eta_p<=U. Suppose a∈N_p lies in the mod-3 sign orbit L={±(0,1,2)}. Orient it so x≡0, y≡1, z≡2 (mod 3).

First u≡x≡0 (mod 3). The retained (A+B) observation and R110-CERT give

    |u| < (3/2) eta_p (A+B) <= (3/2) U(A+B) <= 3,

so integrality forces u=0.

Now x=-3y-6z, and v=3(y+4z). The chosen residue has y+4z≡1+8≡0 (mod 3), so v∈9Z. Since u=0, *both* original v-pair observations imply

    F_w(a) >= |v|/[C+min(A,B)].

The second certificate inequality gives |v|<9, hence v=0.

Solving u=v=0 yields a=(6z,-4z,z) and h=12z. With u=v=0, all three original h-pair observations give

    F_w(a) >= |h|/[D+min(A,B,C)].

The last certificate inequality gives |h|<12, hence z=0, a contradiction. Thus L contains no strict-near representative.

To make the orbit count self-contained, the other twelve orbits follow from the standard norm/Port argument: if two distinct unoriented near vectors a,b have the same nonzero mod-3 sign orbit, choose their orientations so a≡b (mod 3). Then c=(a-b)/3 is a nonzero integer vector with q(c)<=2p/3<=p and F_w(c)<(3 eta_p/2+3 eta_p/2)/3=eta_p, impossible. A near vector congruent to zero mod 3 would itself yield c=a/3 with strictly smaller score and Port. Thus all near vectors occupy distinct nonzero sign orbits; (3^3-1)/2=13 such orbits exist. Excluding L gives at most twelve. QED.

## Theorem 2 — a strict extension of the R109 cone

Assume the *three* order conditions

    B<=A,   B<=D,   A<=C.

Under these conditions the two candidate scores simplify to F(s)=1/(A+B) and F(t)=6/(B+C). Consequently R110-CERT holds whenever

    B+D <= max( 8(A+B), 4(B+C)/3 ).                        (R110-CONE)

For every integer p>=27 this proves |N_p(w)|<=12. R109 required B+D<=8(A+B); R110-CONE is strictly weaker and admits an additional unbounded family with 3(B+D)<=4(B+C).

Example outside the old cone: w=(5,1,100,100), for which B+D=101>48=8(A+B) but 3(B+D)=303<=404=4(B+C). Here U=6/101 and the certificate holds.

More generally the certificate can apply outside all three order conditions: at w=(2,5,100,100), B>A, yet U=1/17 and all three certificate thresholds are >=1/17. This weight is outside R109's original cone.

Sharpness is inherited without relaxing its proof: w=(9,1,58,41) satisfies R110-CERT and has exactly twelve strict near directions for every p>=38 by the complete R109 exact witness. Therefore twelve is the best possible upper bound on the certified weight region.

## Reproducibility and proof status

The companion standalone checker x6_r110_residue_certificate_verify.py uses exact integer-scaled rational scores and enumerates all 95,133 unoriented nonzero integer vectors q<=38. It checks (i) the two candidate score identities, (ii) the complete certificate at four explicit weight vectors, (iii) the exact q<=27 and q<=38 minima, (iv) the strict near counts and excluded residue orbit, and (v) the sharp twelve witness. Its result is x6_r110_residue_certificate_results.json; all checks passed in the author run. Finite computations verify these particular rational weights; Theorem 1 and the derived cone rely on the symbolic proof above.

Source relation: R104's universal thirteen-orbit estimate; R109's twelve-near theorem and exact twelve witness, fixed at enterprise-math@7dbbc8d8268096b33a1d503c44f780d1ef91f87c. Current P000 and normative method records govern scope; no frozen input, native time dynamics, official CLAIM/PROGRESS, Result or Review was changed.

Next: determine whether the failure of R110-CERT is genuinely compatible with all thirteen nonzero mod-3 sign orbits, or whether another residue orbit can be excluded by a different pair of short witness directions. The explicit complement is a smaller, sharply stated search region; do not infer that thirteen is attainable merely because this sufficient certificate fails.
