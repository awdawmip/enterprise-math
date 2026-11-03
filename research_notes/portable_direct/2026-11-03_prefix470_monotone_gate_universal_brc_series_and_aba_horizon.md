# PREFIX-470 — Universal base-state series for sign-consistent gates and full aba future quotient

Date: 2026-11-03, Asia/Shanghai. Scientific input frozen at EM commit f42f2906d77f24085c123f3ccfe9667d41caa96d. Continuation of PREFIX-469 at f924b265d6509925e91fcf7364ffdebce4a14295. STATUS: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED. Applicable behavioral rules read separately at current main. No P000 or worldview change.

## Defined object and observer

In a chosen native affine X6 chart, take 11 signed native directions: x=+E1 and five ordinary pairs ±E2,...,±E6. Every ordinary letter may follow any history. Gated x is allowed initially, and afterwards exactly when the immediately preceding word equals the fixed ordinary-letter gate w (length k≥1). This is a typed *model of ordered native paths*, not an accepted physical heartbeat clock.

For a path, s=#x; y_i=#(+E_{i+1})−#(−E_{i+1}); p_i=min(#+E_{i+1},#−E_{i+1}); A=p2+2p4+p5; C=p3+p5. At fixed n, the base positive-weight BRC observer is f=(s,y1,...,y5,A,C), integer multiplicity stored separately. Distinct f-values count as B_n(w). History state q is retained when future legal operations require it. This signed relative chart is not the final Cell address, and f is not complete branch provenance.

## Theorem A: all full-Parikh support counts

Write the full 11-letter count vector as (s,c1,...,c10) and let h_j be the number of letter j in w. For s≥1 the vector is feasible **iff** c_j≥(s−1)h_j for all j; with s=0 every ordinary vector is feasible. Necessity: each of the s−1 x occurrences after the first x requires a distinct immediate preceding w block, separated by x. Sufficiency: the explicit word x(wx)^(s−1)r, with r an arbitrary ordering of all unused ordinary letters, is legal. This remains true when w has overlapping prefixes/suffixes.

Summing the disjoint cases s=0 and s=1+t gives the generating function for the number P_n(w) of different *full unordered count vectors*:

    Σ_{n≥0}P_n(w)z^n = (1+z−z^(k+1))/((1−z)^10(1−z^(k+1))).    (A)

Thus full Parikh support depends on the gate's length k, not its letter order or overlap.

## Theorem B: universal BRC base-observer generating function

Assume **sign consistency:** w contains at most one sign from each of the five paired axes; it may repeat a signed direction, and the pattern can overlap itself. Then for every n≥0 and every such w of length k,

    G_w(z):=Σ_{n≥0} B_n(w)z^n
          = (1+2z²)(1+z)²(1+z−z^(k+1)) / ((1−z)^8(1−z^(k+1))).  (B)

**Proof.** Fix s and signed displacements y. Write t=(n−s−Σ|y_i|)/2=Σp_i. If the gate has h_i occurrences of sign σ_i on axis i, the Parikh support inequalities read

    p_i≥L_i=max(0,h_i(s−1)−max(σ_i y_i,0)), s≥1,

with L_i=0 for axes absent from the gate and for s=0. Set v_i=p_i−L_i≥0 and t'=Σv_i. The retained (A,C) is a translate of the valuation image of (v1,...,v5) with Σv_i=t'. The image has EXACTLY the points

    0≤C'≤t', 0≤A'≤2t'−C',

so its cardinality is R(t')=(t'+1)(3t'+2)/2. Proof of the complete interval: for fixed C'=v3+v5, v5 ranges 0,...,C'; the remaining t'−C' units placed among v1,v2,v4 give every A-value 0,...,2(t'−C'); adding v5 fills the entire 0,...,2t'−C'. Therefore

    Σ_{t'≥0} R(t')z^(2t') = (1+2z²)/(1−z²)^3.                (C)

For any h≥0 and σ∈{+1,−1}, direct geometric summation over y≤0, 1≤σy≤h, σy>h gives

    Σ_{y∈Z} z^(|y|+2max(0,h−max(σy,0))) = z^h(1+z)/(1−z). (D)

Multiply (D) over five axes; Σh_i=k. For s≥1 this yields z^(k(s−1))[(1+z)/(1−z)]^5, while s=0 gives [(1+z)/(1−z)]^5. Finally sum s:

    1+Σ_{s≥1}z^(s+k(s−1))=(1+z−z^(k+1))/(1−z^(k+1)).

Multiplication by (C), with (1−z²)^3=(1−z)^3(1+z)^3, proves (B) as an identity of formal integer power series. Its n-th coefficient has asymptotic

    B_n(w)=n^8/[3360(k+1)]+O_k(n^7).

This derives from the order-nine pole at z=1; all other singularities have smaller pole order. For k=2, formula (B) reproduces PREFIX-468. The k=3 formula for aba, aaa, aab, baa and abb is therefore identical at the base observer level, although their suffix automata differ.

Sign consistency is an actual theorem hypothesis: simultaneous positive/negative requirements on a single axis produce a different two-sided displacement sum. Positive-weight supports do not represent signed amplitude cancellation.

## Theorem C: exact aba suffix-state occupancy

Set w=aba, a=+E2, b=+E3. Use KMP longest-suffix-prefix states q=0 (none), q=1 (a but not aba), q=2 (ab), q=3 (aba). Initial q=0 additionally permits the first x. Define Q_j(n)=#{base f reachable at n with suffix q=j}. Put B_m=0 for m<0, and abbreviate B_n=B_n(aba). Then

    Q1(n)=B_(n−1) (n≥1);
    Q2(n)=B_(n−2) (n≥2);
    Q3(n)=B_(n−3) (n≥3);

with zeros at earlier indices. Also

    Q0(0)=1; Q0(1)=B1−1; Q0(3)=B3−4;
    Q0(n)=B_n−3 for n≥2 other than n=3.                 (E)

**Proof.** The q2 and q3 languages are exactly legal prefixes followed by ab and aba, respectively. Appending a fixed known signed sequence has an injective action on f: each reverse signed coordinate is known, and the change in a paired cancellation number under adding a signed direction is determined by the post-step signed coordinate and the known direction. For q1, every feasible unordered count vector admits a word not ending ab: if s≥1 take x(aba x)^(s−1) followed by remaining ordinary letters arranged b before a, with other letters arranged to avoid a terminal ab; for s=0 use the same ordinary ordering. Appending a yields q1 and is injective on base f; deleting a gives the reverse.

For q0, a word with any ordinary letter other than a,b can be realized ending in that letter. If s≥2, arrange residual letters before the final aba x block so that it ends x. For s=0 with only a,b, q0 exists iff a=0 or b≥2, excluding a^n and a^(n−1)b (n≥2). For s=1, ending x is possible when a≥2,b≥1; starting with x and ending b or bb works when a=0 or b≥2. The excluded configurations are x a^(n−1) (n≥2) and, exceptionally, xab at n=3. These excluded vectors contain no negative paired steps; n=s+Σ|y_i| forces all p_i=0 and rules out a different Parikh realization of the same f. Hence there are three excluded base f-keys for n≥2 except four at n=3; n=1 excludes only a. This proves (E).

Let F_n=Σ_{j=0}^3 Q_j(n). For n≥4,

    F_n=B_n+B_(n−1)+B_(n−2)+B_(n−3)−3.

Exactly F0=1,F1=11,F2=74,F3=348. The **all-n closed full-history series** is

    ΣF_n z^n = (1+z+z²+z³)G_aba(z) − z − 3z² − 4z³ − 3z⁴/(1−z). (F)

It follows that F_n=n^8/3360+O(n^7).

## Theorem D: minimal finite-future observation

Starting from q=3,2,1,0, the shortest *additional* legal suffix that produces another x has respective lengths 1,2,3,4, witnessed by x, ax, bax, abax. Thus for future-observation horizon H=1 the suffix partition is {0,1,2}|{3}; for H=2 it is {0,1}|{2}|{3}; and for H≥3 it separates all four states (q0 versus q1 is witnessed by bax). H=0 merges all. Since every reachable f has a q0 or q1 representative by the above classification, the exact minimal numbers of f-aware states are

    N_0(n)=B_n;
    N_1(n)=B_n+B_(n−3);
    N_2(n)=B_n+B_(n−2)+B_(n−3);
    N_H(n)=F_n for all H≥3.                                (G)

At known n and given a codebook, an optimal dense fixed-width code uses ceil(log2 N_H(n)) bits. The codebook construction and updating algorithm remain separate engineering questions. Ordered path provenance is preserved only as far as the declared observers and future operations require.

## Exact executed test, scope and literature

The accompanying standard-library Python certificate independently: enumerates reachable (11-letter count, suffix q) by integer dynamic programming; enumerates **all** 11-part vectors with length n≤8 and checks the feasibility iff; calculates f and Qj,NH; calculates closed-series coefficients by integer binomial convolution; and, for n≤5, independently enumerates all legal ordered words and compares state multiplicities. It further tests monotone-sign gates aaa,aab,abb,baa,ababa for n≤6. Every actual assertion passed.

For aba:
    n=3: ordered=1100, Parikh=275, B=275, (Q0,Q1,Q2,Q3)=(271,65,11,1), F=348, N=(275,276,287,348)
    n=4: ordered=11001, Parikh=935, B=932, Q=(929,275,65,11), F=1280, N=(932,943,1008,1280)
    n=6: ordered=1100320, Parikh=7017, B=6824, Q=(6821,2685,932,275), F=10713, N=(6824,7099,8031,10713)
    n=8: ordered=110054001, Parikh=35970, B=33295, Q=(33292,15697,6824,2685), F=58498, N=(33295,35980,42804,58498).

Exact formula-only values (not independently enumerated): B10=123829,F10=238860; B20=10549216,F20=26802872.

Related established methods: A.W. To, *Parikh Images of Regular Languages: Complexity and Applications* (2010), https://arxiv.org/abs/1002.1464; K. Woods, *Presburger Arithmetic, Rational Generating Functions, and Quasi-Polynomials*, Journal of Symbolic Logic 80(2), 433–449 (2015), https://doi.org/10.1017/jsl.2015.4 . These are literature context; the explicit X6 (B)/(F)/(G) identities are derived above, not attributed to the cited papers.

BRC reuse: PREFIX-465 exact positive weight valuation map; PREFIX-466 fixed-gate model; PREFIX-467 future-observer quotient; PREFIX-468 closed ab base series; PREFIX-469 finite historical state counting. Discrete length is not physical time. No phase, π, trigonometric, or Shor arithmetic was used.

**Next PREFIX-471:** derive the modified single-axis displacement series when a gate requires both signs of one native axis, and find the smallest pair of gates of the same length that yield different B_n. Separately improve exact ranking/unranking of reachable f/q keys without a complete codebook; retain the arbitrary-degree X6 moment rank problem as an independent route.

**Actual control:** GitHub account awdawmip has admin/push; native task-list read returned CONTROL_QUOTA. Native session registration returned STATIC_READONLY_SCOPE_DENIED and operation_sent=false. Active owner, Researcher-ID and formal CLAIM remain unverified; this is author-side Source evidence, not independent Review or Admission.
