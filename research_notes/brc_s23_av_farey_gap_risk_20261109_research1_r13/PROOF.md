# Farey–three-gap exact finite-horizon risk evaluator (author-side theorem)

Date: 2026-11-09. Researcher-ID: EM-DIRECT-9ED32E.
Research-Activity-ID: RA-E4E610947AD0C7DA64E7B98C.
Source-locked science: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Continuation: S23/AV 128-history circle-observer results, particularly 200,000-step certificate in `research_notes/brc_s23_av_online_risk_100000_20261109_research1_r12/` at `9dc19e26be782bd67e12c2072a63cda97dd3d110`.
Status: newly proved algorithmic identity and author-side exact integer certificates; independent mathematical review pending.

## 1. Exact question and scope

For irrational 0 < theta < 1 and integers 2 <= m <= n, let t_i={i theta}, 0<=i<n. The first m labelled t_i partition the unit circle into m historical arcs I. The n phase cuts refine each arc. Let M(I;n) be the largest *clockwise length* among the n-point circular gaps contained in that historical arc. Define

    R_theta(m,n-m) = 1 - sum_(historical arcs I) M(I;n).

This is the previously established uniform-phase Bayes risk for predicting the entire future length n-m from m past S23/AV symbolic outputs under the 79-bin observer (after quotienting its 79 symmetric copies). We compute the exact R without constructing/sorting n phase points. Historical arc ownership, endpoints, and future outputs remain distinguished: the relevant BRC carrier is the labelled circle cut set with future gap refinement, not the aggregate cut count.

## 2. Farey neighbors and the three-gap successor theorem

Let a/b < theta < c/d be the *adjacent Farey fractions of order n-1*: b,d <= n-1, bc-ad=1, and b+d >= n. Put

    U=b theta-a >0,    V=c-d theta >0.

Every circular gap among t_0,...,t_(n-1) begins at exactly one index i and has successor index

    s(i)=i+b       if 0<=i<n-b;
         i-d       if d<=i<n;
         i+b-d     if n-b<=i<d.

These three index ranges are disjoint, exhaustive, and have lengths n-b, n-d, and b+d-n. Their respective clockwise gap lengths are U, V, and U+V.

*Elementary proof.* Since b+d>=n the three image ranges are [b,n), [0,n-d), and [n-d,b), hence s is a permutation. The forward angular displacements are U,V,U+V (all in (0,1); the U+V class is empty in the degenerate n=2 case). Their total sum is

    (n-b)U+(n-d)V+(b+d-n)(U+V)
      =dU+bV =bc-ad =1.

A permutation of n distinct circle points with strictly positive forward displacements and total winding exactly one must be their unique clockwise successor cycle. Thus these are *all* gap lengths and their original-index labels. This also supplies a direct proof of the instance of the three-gap theorem needed here.

## 3. Exactly count each gap type inside one historical arc

For a historical arc I=[t_p,t_q) in clockwise order, p,q in {0,...,m-1} adjacent in the sorted initial set, define wrap(p,q)=1 when t_p>t_q, and 0 otherwise. For any consecutive starting-index range [A,B] subset [0,n-1], the number of its phase points belonging to I is

    C(p,q;A,B)= sum_(i=A)^B [
        floor((i-p)theta)-floor((i-q)theta)
        + floor(p theta)-floor(q theta)+wrap(p,q) ].

Proof: for ordinary nonwrapped [u,v), the indicator of {i theta} in [u,v) is floor({i theta}+1-u)-floor({i theta}+1-v). When u>v (wrapped arc), add one. Substitute u={p theta}, v={q theta} and cancel floor(i theta). Lower endpoints are included and upper endpoints excluded. Both are original n-point cuts, so every successor gap belongs to exactly one historical arc.

For a fixed I, evaluate this C on each of the *three disjoint index ranges from §2*. The largest length among {U,V,U+V} with positive count equals M(I;n). Consequently,

    R_theta(m,n-m) = 1 - sum_I max{ type-length : C(I;type-range)>0 }.

This is an exact formula for all irrational theta and all 2<=m<=n. No asymptotic assumption is used.

## 4. Algorithm and complexity

Find the two Farey neighbors via accelerated Stern–Brocot/Euclidean division with denominator cap n-1 (O(log n) arithmetic steps). Sort just the m historical phases (O(m log m) comparisons). The function

    F(N;u,v,w)=sum_(i=0)^(N-1) floor((u*i+v)/w)

is evaluable by the Euclidean floor-sum recursion in O(log(max(N,w))) quotient steps, with signed offsets handled by Euclidean division. Every C uses two such sums and one constant. There are 3m type counts and at most three affine gap comparisons per arc.

Hence one arbitrary-horizon risk value costs O(log n + m log m + m log n) *arithmetic operations* and O(m) working storage. This improves the prior O(n log n)-comparison offline ordered-cut algorithm when n is large and m fixed. Full bit cost additionally depends on the chosen certified real interval, rational denominators, and integer sizes; the verifier keeps that cost explicit rather than treating high precision as free.

For a certified theta interval (lo,hi), choose Farey neighbors that bracket the *entire* interval, so they determine the same index adjacency and circular phase order throughout. Use rational floor sums to count the types. Compare each candidate affine gap size at both rational endpoints to fix a valid winner throughout. The resulting R is an exact affine expression A+B theta on that certified interval. Refine the interval if any required Farey/maximum comparison is unresolved.

## 5. Frozen S23/AV evaluation: n=1,000,000,000,128

For the existing auxiliary observer,

    theta = 79 * (2074774-380295*r)/(79*r-431)-46,
    r = ln(7)/ln(10/7).

160-term rational log-series enclosures certify

    262204504569236716045286/10^24
       < theta <
    262204504569236716045287/10^24.

With m=128 and L=10^12, hence n=1,000,000,000,128, the enclosing Farey neighbors are

    165937423910/632854970141 < theta
      < 197323373351/752555238039.

All 128 historical arcs pass two-endpoint integer range counts and gap-winner comparisons. The resulting *exact* risk is

    R(128,10^12)
      = -4017401528447 + 15321634290944*theta
      ~ 0.9999999998129876622606865.

The probability of correctly predicting the entire trillion-step future sequence is thus ~1.8701233773931345e-10 under the declared uniform-phase model.

The same method independently reproduces all four previous certified endpoints L=1142,10000,100000,200000 and adds exact L=10^6,10^8,10^10 certificates (see RUN_EVIDENCE.txt). This is a finite-horizon *exact* result at arbitrarily chosen n, not a proof of any native X6 dynamic correspondence.

## 6. Independent verification and next mathematical question

VERIFY_FAREY_GAP_RISK.py uses only Python stdlib exact rational/integer arithmetic, includes the 160-term theta certificate, and checks 55 direct-partition instances (49 across seven historical lengths for an independent non-S23 test slope; six S23 short horizons). It checks every claimed equality against the previous exact risk endpoint records and certifies both interval endpoints for four new horizons. Run:

    python VERIFY_FAREY_GAP_RISK.py

Next: derive the complete breakpoint *generator* as n varies using Farey neighbor changes and the three interval type-presence counts; make an output-sensitive algorithm for all intervals rather than one queried horizon. Compare total bit cost and certified theta precision on adversarial near-rational inputs. Preserve plateau 413 as a separate geometric research line.

## Exact provenance

- Frozen science and auxiliary observer: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
- Earlier proof/certificates: awdawmip/enterprise-math@9dc19e26be782bd67e12c2072a63cda97dd3d110, research_notes/brc_s23_av_online_risk_100000_20261109_research1_r12/.
- Current project method: research_priorities/research_method.json at main (read 2026-11-09).
- Classical mathematical ingredient: Farey neighbor/unimodular relations; the needed successor law is proved directly in §2.
