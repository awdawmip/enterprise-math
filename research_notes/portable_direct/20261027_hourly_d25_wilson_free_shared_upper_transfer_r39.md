# D25/LIFT R39 — Wilson-free upper W2/S2 regularized rank transport

Date: 2026-10-27 (Asia/Hong_Kong). Portable TASK_RESEARCH author work; logical lane \`chatgpt-research-hourly-enterprise-math-20260923\` (user-declared continuation label, not an assertion of fresh native session authority). Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`, parent D25/LIFT/JT2 OPEN. Frozen scientific Source \`c47e13e4aba0e006366f989d6334d443f6333ae3\`; control HEAD is separate. Classification: **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**.

## Question and sources

R34/R35 prove a relative W/S transfer only at the unique \`p≡19 mod24\` lower-half S-weight-zero rank; R38 independently produces the W2 and S2 *upper-half* p-adic source jets. The new question is whether the actual unchanged upper-overlap W/S sources admit one **all-order, Wilson-free p-unit transfer** across the \`p≡13 mod24\` exceptional S-weight zero and whether it has a regular rank recurrence.

Fix every prime \`p=6m+1>=7\`, and the genuine unchanged rational summands

\`\`\`text
w_k=(6k+1)(2k)!(3k)! / ((k!)^5 216^k),
s_k=(8k+1)(4k)! / ((k!)^4 2304^k).
3m+1<=k<=4m;  j=p-1-k in [2m,3m-1].
a=2k-p, b=3k-p, r=4k-2p, all in [0,p-1].
\`\`\`

Define a **weight-regularized** relative source and short factorial port

\`\`\`text
tau_k := (k! (4k)!/((2k)!(3k)!)) * (3/32)^k,
C_(p,k) := 2*k!*r!/(a!*b!) * (3/32)^k,
P_(p,k) := prod(i=1..p-1)(1+p/i) * prod(i=1..r)(1+2p/i)
            /[prod(i=1..a)(1+p/i) * prod(i=1..b)(1+p/i)].
\`\`\`

All products are exact rational products in \`Z_(p)\`.

## Theorem A — all-order original-source transfer

For every stated p,k, **exactly in the rationals**

\`\`\`text
tau_k = C_(p,k)*P_(p,k) in Z_(p)^x,
s_k/w_k = (8k+1)/(6k+1)*tau_k.                         (A1)
\`\`\`

No Wilson quotient is present; tau is a p-unit even if the *original S linear weight* is divisible by p. Indeed \`v_p(w_k)=2\`, and \`v_p(s_k)=2+v_p(8k+1)\` on this overlap, with precisely one possible weight-zero index:

\`\`\`text
p≡13 (mod24), j_*=(3p-7)/8, k_*=(5p-1)/8,
8k_*+1=5p,  v_p(s_(k_*))=3, v_p(w_(k_*))=2.   (A2)
\`\`\`

**Proof.** Here \`p<=2k,3k<2p\` and \`2p<=4k<3p\`. Exact factorial splitting yields

\`\`\`text
(2k)!/p  = (p-1)! * a! * prod(i=1..a)(1+p/i),
(3k)!/p  = (p-1)! * b! * prod(i=1..b)(1+p/i),
(4k)!/p² = 2*((p-1)!)² * r! *
             prod(i=1..p-1)(1+p/i) * prod(i=1..r)(1+2p/i).
\`\`\`

Both factorial blocks cancel exactly in the ratio, giving tau=C P. Direct unchanged-term cancellation gives s/w. \`6k+1\` is a p-unit throughout this band; \`8k+1=5p\` precisely when \`p≡5 mod8\`, i.e. \`p≡13 mod24\` within \`p≡1 mod6\`. Legendre's formula yields the exact valuations. QED.

## Theorem B — regular rank evolution and first source jet

For \`3m+1<=k<4m\`, the exact recurrence is

\`\`\`text
tau_(k+1)/tau_k =
 [(4k+1)(4k+2)(4k+3)]/[16(2k+1)(3k+1)(3k+2)].       (B1)
\`\`\`

All denominators are p-units over these transitions. This rank transport remains regular through the index where S's external weight vanishes; the weight is not divided away.

Writing \`H_n=sum(i=1..n)1/i\`, expansion of the exact product gives

\`\`\`text
tau_k ≡ C_(p,k)*[1+p(H_(p-1)+2H_r-H_a-H_b)] (mod p²)
      ≡ C_(p,k)*[1+p(2H_r-H_a-H_b)]         (mod p²). (B2)
\`\`\`

The second line uses \`H_(p-1)=0 (modp)\`. The recurrence follows by dividing consecutive factorial tau values and cancelling \`4k+4,2k+2,3k+3\`. The jet follows from the first-order product expansion, using p-unit denominators; no Wilson or Fermat quotient appears. QED.

## Actual original-source singular and paired certificates

At p≡13 mod24, with \`k=k_*\`, the regular tau unit reconstructs the **true** exceptional S source:

\`\`\`text
[s_k/p³]_(modp)
   = [5/(6k+1)*tau_k*(w_k/p²)]_(modp),
[(s_k/w_k)/p]_(modp)
   = [10*k!*r!/( (6k+1)*a!*b! )*(3/32)^k]_(modp).
\`\`\`

The sum \`Σ_(k=3m+1..4m)(w_k-s_k)=Σ w_k[1-(8k+1)/(6k+1)*tau_k]\` is therefore an exact **unchanged-input paired upper-port representation**. It retains both W/S labels and excludes R38's unpaired lower-j S2 family, W3/S3 high-high, original low half, fixed Hasse and Green infinity/boundary source identities. It is not a proof of the still-open all-prime W=S modulo p³.

Representative directly checked residues \`(p,j_*,k_*,w/p² modp,(s/w)/p modp,s/p³ modp)\`:

\`\`\`
(13,4,8,9,11,8); (181,67,113,83,107,12);
(373,139,233,234,325,331); (733,274,458,9,45,405).
\`\`\`

**Executed author checks:** independent modular p-free original factorial calculations against exact short product at p³, Wilson-free jet at p², tau rank recurrence, singular residues and paired contributions for all **80 primes** \`7<=p<=997, p≡1 mod6\`: **6,098** upper shared-rank positions, **22** special indices. Twelve original rational \`Fraction\` equalities at p=7,13,19,37 also passed. Executed checker is retained as \`20261027_hourly_d25_wilson_free_shared_upper_transfer_r39_check.py\` (author evidence). The general theorem is established by factorial identities, not finite enumeration. This is not a native H0/B0 experiment or independent Driver audit.

**BRC COMPOSE_APPLIED:** carrier \`(unchanged W/S source, arithmetic rank, exact p-valuation, p-unit tau, original linear weight, modulus, future observer)\`; source labels remain separate. P000 and ACTIVE X6 worldview are unmodified. R40 separately classifies the unique S-weight-zero rank across all p mod24 residue classes. Native CLAIM/open/Source checkpoint depends on authenticated owner recovery under existing control support #1558; no role-bound write is inferred from this portable file.
