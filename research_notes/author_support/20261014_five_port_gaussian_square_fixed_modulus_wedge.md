# Author-only five-port BRC: exact Gaussian-square transfer and a 160-layer infinite wedge

Date: 2026-10-14 Asia/Shanghai.
Status: AUTHOR_SYMBOLIC_DERIVATION / AUTHOR_EXACT_CERTIFICATE / UNREVIEWED / NOT_ADMITTED.
This is **not** a canonical Task Result, CLAIM, Driver acceptance, P000 amendment or native X6 theorem. Native service em_status returned BACKEND_IDENTITY_CHECK_UNAVAILABLE (operation_sent=false); no active owner was authenticated by this author.

Source controls: GLOBAL_KNOWLEDGE_V1 main@91edc5638207c8851a9774206034890d54444492; Enterprise Math main@cc07006d61f879395dd247a37ed88d17d4ae8fd0.
Earlier formal five-port residual work is historically author-only, NOT assumed independently admitted.

## Exact typed model

Five labeled ports w=0,...,4 independently carry finite ordered words in X (weight q^w) and Y (weight q^(2w)), preserving positive integer multiplicities.

G_(x,y)(q)=[X^x Y^y] product_(w=0)^4 (1-X q^w-Y q^(2w))^(-1).

For x>=0 even, y>=0 and odd m=x+2y+5>=23, H_r is the exact coefficient mass in exponent class r mod m, and Delta_(x,y)=H_(m-10)-H_(m-19). The cyclic histogram is the declared observer; no identification of distinct future-sensitive provenance is asserted.

Let h_j(q)=[j+4 choose 4]_q and b_(j,s)=[q^s] h_j(q)^2 (outside degree range set to zero).
Let K_(m,j)=sum_(k in Z)(b_(j,4j+km)-b_(j,4j-9+km)).
Let W(N,0)=1 and W(N,k)= (N/k) binom(N-k-1,k-1) for N>=2k, k>=1.

For ALL odd m>=23 and 0<=y<=(m-5)/2, an exact folded/unfolded identity holds:

Delta_(m-5-2y,y)= sum_(j=0)^y (-1)^j W(m-5-2j,y-j) K_(m,j).            (T)

Proof: With n=m-5, the charge n generating product factors via formal alpha,beta solving alpha+beta=1, alpha beta=-z. Put alpha=(1+sqrt(1+4z))/2, beta=-z/alpha. Lagrange inversion gives [z^k]alpha^N=W(N,k), so coefficient extraction yields
G_(n-2y,y)=sum_(j=0)^y (-1)^j W(n-2j,y-j) h_(n-j) h_j.
For any m-th root zeta of order>=5,
h_(m-5-j)(zeta)=zeta^(-4j-10) h_j(zeta).
At roots of order 1 or 3 this equality need not hold, but the contrast filter zeta^10-zeta^19 vanishes. Since m is odd no order 2 or 4 is relevant. Apply the discrete Fourier cyclic contrast exactly, yielding (T). The K sum explicitly retains every cyclic alias. All calculations are integer/rational exact; no physical phase or classical propagation is inferred.

For m>4y+9, all K_(m,j) (j<=y) are alias-free constants kappa_j; hence Delta_(m-5-2y,y)=P_y(m) is a degree-y rational polynomial with leading coefficient 1/y!. First kappa values j=0,..,5 are (1,5,29,109,312,728).
First fixed-m edge values for ALL odd m>=23:
y=0: 1;
y=1: m-10;
y=2: (m^2-23m+168)/2;
y=3: (m^3-39m^2+614m-3720)/6.

## Infinite in m, finite in y: exact Newton certificate

**Theorem (author computer-assisted):** for every integer 1<=y<=160 and every odd m>=4y+11,
Delta_(m-5-2y,y) > Delta_(m-3-2y,y-1).
For each y set B=4y+11, t=(m-B)/2>=0, Q_y(t)=P_y(B+2t)-P_(y-1)(B+2t). This polynomial has degree y and exact Newton expansion
Q_y(t)=sum_(k=0)^y C_(y,k) binom(t,k), C_(y,k)=Delta_t^k Q_y(0).
The exact verifier computes all 13,040 C_(y,k) from the finite y+1 original polynomial values for each y, and checks strictly positive every coefficient, including the independently expected top coefficient C_(y,y)=2^y. Therefore Q_y(t)>0 for all integer t>=0, **without bounding m**. No theorem asserted for y>160 or the folded region m<4y+11.
Certificate: fixed_modulus_wedge_positive_newton_certificate.json, 1,177,341 bytes, SHA256=78432b1c4fc73d9b79735063aec0b1c2e184399197c9022fd2ea0fbfdd43d802; reproducer verify_fixed_modulus_wedge.py (kept in separately delivered author research package, **not yet Source-published**).

Corollary for all odd m>=23: the first six fixed-m residuals indexed y=0,...,5 are strictly increasing; use theorem for m>=31 and exact original positive-mass cyclic recurrence for four exceptional m=23,25,27,29.

## Independent finite evidence and falsifier

The Gaussian-square transfer was evaluated for 190 full odd modulus sequences m=23..401, all strictly positive/unimodal/log-concave; ALL 20 inherited 23..61 sequences matched entry by entry; 85 independent original ordered-port cyclic-path examples passed positive-mass checks. These finite observations are **not** universal theorems.

For each odd m=23,25,...,39, the fixed-m residual generating polynomial D_m(z)=sum_y Delta_(m-5-2y,y) z^y is NOT real-rooted: its true degree d=(m-5)/2 is certified independently by positive top-degree counts 16,20,27,35,43,53,65,77,92, while necessary Newton normalized coefficient inequality fails because
(m-10)^2(m-7)-(m-5)(m^2-23m+168)=m^2-43m+140<0.
This eliminates universal real-rootedness as the mechanism for strict unimodality.

## Provenance, exact limits, continuation

Local reproducible original proofs, script, and decimal certificates (including a full 190-sequence certificate) are bundled with this turn's research package. This GitHub note preserves a human-comprehensible author-only frontier, **not** the 1.18 MB full Newton certificate. Files and Source are not conflated. No activity record, native session, CLAIM, frozen Result or independent Driver review is implied.

Next: derive a UNIFORM in y positive Newton transfer or exact coefficient injection, especially across the folded region m<4y+11; otherwise find a first counterexample to universal strict unimodality/positive contrast. Do not repeat the already falsified real-rootedness route. Preserve BRC labeled-port mass/provenance; no native six-axis/time transport is known.
