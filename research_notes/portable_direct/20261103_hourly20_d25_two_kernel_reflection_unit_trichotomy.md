# D25: exact p-adic reflection-unit transfer for the original 216/2304 kernels

Date: 2026-11-03 (+08). Research lane logical ID `chatgpt-research-hourly-enterprise-math-20260923`, distinct from maintenance `chatgpt-hourly-enterprise-math-20260921`. Author-side portable mathematics, `UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING`; no native CLAIM/OPEN/Source checkpoint or original H0/B0 experiment is claimed.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Consumes the original 216/2304 comparator at `eeb6f882aae70ec0a2b37d74ea7b7f988ee1a9c4` and the preceding three-moment normal-form proof at `f12541ee71e77f200608fed40ba445faaf642dae`; those remain separate source/author contributions. P000 and ACTIVE Heartbeat World are unchanged; the following ordinary rational arithmetic is an explicitly auxiliary model, **not** a proved native-X6 transfer.

## Original rational kernels and exact ratio

For every prime p>=5 and 0<=k<p, put

    b_k=(2k)!(3k)! / ((k!)^5 216^k)
    c_k=(4k)! / ((k!)^4 2304^k)
    h_k=c_k/b_k=(4k)! k! / ((2k)!(3k)!) (3/32)^k.

These are the original coefficient sources; no change to the weighted p-1 cutoffs is made. Define for 1<=k<p

    f_a(k)=floor(a k/p),  rho_a(k)=a k-p f_a(k), a=2,3,4,
    d_p(k)=f_4(k)-f_2(k)-f_3(k)=v_p(h_k).

Here all rho_a(k) are nonzero mod p, and d_p(k) belongs to {-1,0,+1}.

### Theorem 1 (proved): exact reciprocal signed-valuation bands

For every p>=5 prime and 1<=k<p,

    d_p(p-k)=-d_p(k).

The exact bands are

    d_p(k)=+1 on p/4<k<p/3;
    d_p(k)=-1 on 2p/3<k<3p/4;
    d_p(k)=0 otherwise.

Proof: Since p>3 is prime, ak/p is never an integer for a in {2,3,4} and 1<=k<p. Thus

    floor(a(p-k)/p)=a-1-floor(ak/p).

Substituting the three values a=4,2,3 gives d_p(p-k)=-d_p(k). Evaluating the three floor functions on the breakpoints p/4,p/3,p/2,2p/3,3p/4 gives the displayed bands. These are exact rational index inequalities, not an asymptotic model. QED.

In particular h_k h_(p-k) is a p-adic unit even in the two source-mismatched bands. This motivates the **p-k** involution, which must not be confused with the previously studied **p-1-k** reflection.

### Theorem 2 (proved): exact three-value reflected unit law

For every p>=5 prime and every 1<=k<p, in Z_p / p Z_p,

    h_k h_(p-k) =
      3/16  if 0<k<p/4 or 3p/4<k<p;
     -1/16  if p/4<k<p/3 or 2p/3<k<3p/4;
      1/8   if p/3<k<2p/3.

There are no integer boundary cases at the fractional breakpoints for prime p>=5. The middle interval includes both sides of p/2. All denominators 16,8 are p-units.

**Proof.** Write n=p q+r, 0<=r<p, and define the p-unit factorial block U_p(n)=product_(1<=j<=n, p does not divide j) j. Then the exact factorial identity is

    n! = p^q q! U_p(n),

and Wilson gives

    U_p(pq+r) = (-1)^q r! (mod p).

For n=a k, a in {2,3,4}, write q=f_a(k), r=rho_a(k). The companion n'=a(p-k) has q'=a-1-q and r'=p-r. All p-powers in h_k h_(p-k) cancel by Theorem 1.

A second Wilson identity yields

    r! (p-r)! = (-1)^r r (mod p), 1<=r<p.

The quotient of the small factorial blocks across k and p-k is

    F(k) = f_4!(3-f_4)! /
             [f_2!(1-f_2)! f_3!(2-f_3)!]
         = 3 C(2,f_3)/C(3,f_4).

The remaining p-unit blocks, including the common factor (3/32)^p, reduce to

    (-1)^(rho_4+k-rho_2-rho_3) *
    (rho_4*k)/(rho_2*rho_3) * (3/32)
     = (-1)^(d_p(k))/16   (mod p).

The last equality uses rho_a=ak mod p and
rho_4+k-rho_2-rho_3=-p d_p(k). Thus

    h_k h_(p-k) = (-1)^(d_p(k)) *
                    3 C(2,f_3(k)) / (16 C(3,f_4(k)))
                    (mod p).

Reading the six intervals cut by p/4,p/3,p/2,2p/3,3p/4 gives (3/16,-1/16,1/8,1/8,-1/16,3/16). This proves the stated three-value formula. QED.

**Precision and provenance note.** Omitting the q! factors in n!=p^q q! U_p(n) would falsely predict a single 1/16 unit outside the defect bands. The three-valued law explicitly retains these block multiplicities; this is a substantive arithmetic source distinction.

### Corollary 3 (proved): minimal three-class unit observer

For every prime p>=7 all three bands are nonempty and the three residues 3/16, -1/16, 1/8 are pairwise distinct in F_p (their differences are 1/4,1/16,-3/16). Therefore the single reflected-unit observer k -> h_k h_(p-k) has **exactly three distinct outputs** and cannot be encoded by fewer than three distinct labels while preserving this observer. The valuation d_p(k) alone is insufficient: both the outer and central bands have d=0 but different unit outputs. Three labels are sufficient for this one observer, not automatically for arbitrary future operations. At p=5 the two defect intervals are empty; only two outputs occur.

This is a scoped BRC observer-fidelity certificate: retain the ordered kernel identities, p-k pairing, signed valuation and factorial-block unit class. No geometric/native coordinate identification follows.

### Theorem 4 (proved): fixed-width rational shift-transfer is impossible

For any fixed J>=0 there do not exist rational functions R_j(k) in Q(k), -J<=j<=J, such that

    c_k = sum_(j=-J)^J R_j(k) b_(k+j)

for all sufficiently large positive k. Indeed b_(k+j)/b_k is rational in k for every fixed integer j, by its exact hypergeometric recurrence. Such an identity would force h_k=c_k/b_k to be rational in k. But

    h_(k+1)/h_k = (4k+1)(4k+2)(4k+3) /
                      [16(2k+1)(3k+1)(3k+2)] -> 2/9,

whereas any nonzero rational F(k) satisfies F(k+1)/F(k)->1. Contradiction. This theorem is restricted to *exact characteristic-zero*, p-independent, bounded-shift rational transfers; it does not prohibit p-dependent, genuinely two-index or modulo-p^3 transformations.

Together with the already established independent rank-three polynomial Gosper normal forms, the rational **two-kernel direct-sum** polynomial observation quotient has dimension six: rational linear dependence of b_k and c_k would force h_k rational, hence none exists; any mixed rational antidifference of P_b(k)b_k+P_c(k)c_k splits into two separate Gosper identities. The sum of their individual three-dimensional quotients is therefore direct. This does not claim that the *single fixed signed scalar* W_216-S_2304 needs six moments.

## Finite independent arithmetic check

The companion exact-integer JavaScript checks every prime 5<=p<=2000 (301 primes; 276744 nonzero indices). One path updates h_k using its rational first-order recurrence with p-factors stripped; a second uses factorial unit blocks and the exact q! factors. It checks both valuations, d(k)+d(p-k)=0, the reflected units for each k, and h_(p-1)=1 mod p. All PASS.

Representative residues (outer, defect, middle respectively):

    p=13:  3/16=1,  -1/16=4,  1/8=5  (mod 13).
    p=19:  3/16=18, -1/16=13, 1/8=12 (mod 19).
    p=373: 3/16=210,-1/16=303,1/8=140 (mod 373).

At p=373 the corresponding class counts are (186,62,124); the first defect starts k=94 and its partner lies at p-k=279, while the k=249 example also lies in the negative band (its partner is 124). These are checks of the exact theorem, not independent review or the p373 native H0/B0 benchmark.

## Current frontier and next precise experiment

The frozen scalar target remains OPEN:

    W_216(p-1) == p (mod p^3) for p mod24 in {13,19},
    equivalently Delta_p-R_p == 0 (mod p).

The independent Guo–Zudilin 2304 weighted congruence and the 301-prime *candidate* W_216-S_2304 (mod p^3) comparison remain distinct from a proof of that transfer.

**Next exact action:** seek a terminating, p-dependent two-index relation whose kernel migration explicitly couples k and p-k, and whose three reflected unit bands match Theorem 2. Compute the termwise/triangular signed residual for the original weights (6k+1) and (8k+1), retaining the original p-1 cutoff; test the proposed telescoping at p=13,19,373 and the independently known -2p^3 last-weighted-endpoint discrepancy mod p^4. A valid identity must explain *both* the +1 and -1 valuation bands rather than erasing them by a unit-only termwise map. If successful, prove uniform mod-p^3 W_216-S_2304; otherwise keep the exact failure and revise the two-index ansatz. Avoid reproducing the earlier 301 scalar tests as new research.

Native interface status observed this run: Gateway 0.6.11, `UPSTREAM_CODE_REVIEW_REQUIRED`, `research_authority_granted=false`, `executor_binding_configured=false`, 5/5 active admission jobs. The existing read-only recovery request #6637 is SUCCEEDED; continuation #6638 is FAILED with that exact code gate. No new service session, CLAIM, authorized run, Source checkpoint, Result, review, formal activity or math acceptance was established. Support #1558 remains control's responsibility; #1559 remains the original unexecuted native benchmark. Historical session/staging and scheduler/notification settings are not altered.
