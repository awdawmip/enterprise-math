# Three exact shortcuts for the aligned two-bit scalar observer

Status: symbolic design after the first aligned execution; no implementation or
new scientific execution in this unit. All arithmetic stated below is an exact
identity. A future implementation must retain its typed routing and replay costs.

The executed predecessor uses fixed scalar signs
w(x)=(-1)^(bit_ell(x)+bit_k(x)), with 0<=ell<k<g, L=2^g, V=2^ell and supplied
R,r. Its aligned domain has V|R. The exact stretching identity is

    A_two(V*z+t)=(-1)^z*((V-t)*A_one(z)-t*A_one(z+1)),

for 0<=t<V, on compressed length M=L/V and bit k-ell, with the extension
A_one(M)=0 for an empty overlap. The frozen proof is
TWO_BIT_PERIOD_NESTING.md, SHA-256
9189f01243aa308f516534337b40e6e2c03a7fcf3f79a7dde179a5689bca1d26,
published under hybrid source 55e8e66b76d062c6c72432f0f5b364c3e9b1bba8,
research_notes/directed_recovery/20260927_C6438C/qft_gap_hybrid/next_design/.
The following changes do not alter the original raw factor 4^-g.

## 1. Cancellation using the highest signed bit

More generally, let S be any nonempty subset of {0,...,g-1}, k=max(S),
U=2^k and w_S(x)=(-1)^(sum_(j in S) bit_j(x)). If R divides U, then for every
residue a modulo R,

    H(a)=sum_(0<=x<L; x congruent a mod R) w_S(x)=0.     (1)

Proof: partition [0,L) into complete blocks of length 2U. Within each block,
pair x in its first half with x+U in its second half. Their lower bits agree,
their bit k differs, and no signed bit above k exists. Hence their weights
are opposites. Their residues agree because R|U. This fixed-point-free pairing
cancels each residue class individually, proving (1).

It follows that the signed pair count at any r is zero:

    K(r)=sum_a H(a)*H(a+r)=0.                           (2)

This proof does not enumerate the R residues or claim that doing so is cheap.
It certifies the zero directly. It applies to two-bit signs and to arbitrary
nonempty scalar Walsh masks, independent of any lower-bit alignment condition.
It does not apply to arbitrary chronological matrix weights.

A successor confined to the predecessor's aligned input domain can validate
V|R first and then test U modulo R. A separately declared broader domain can
use (2) at some previously nonaligned inputs, but must change its admission
contract and validate those new cases. The smallest successor should preserve
the old domain and comparison grid. All divisions, scales and the returned
zero must have paid typed receipts. Public bit indices may select k; numerical
divisibility must not be guessed from the fixtures.

## 2. Eliminate a zero-coefficient shifted sum

On an aligned displacement progression d=b+jR, the remainder t=d mod V is
constant. When its observed value is zero, the identity becomes

    A_two(V*z)=(-1)^z*V*A_one(z).                       (3)

The shifted A_one(z+1) need not be computed. Its coefficient is exactly zero,
including when z=M-1 and the shifted overlap is empty. This saves the entire
shifted progression's moment requests and reconstruction work, not merely a
final multiplication. The certificate must explicitly record the observed t=0
and the zero-coefficient identity; it must not imply that an omitted sum was
actually evaluated. The original z parity sign still applies. Nonzero t keeps
both terms and the exact empty-tail checks from the predecessor.

Because ell=0 gives V=1, every remainder is zero in that subfamily, so all
shifted calls can be omitted there. For ell>0, the condition is per orientation,
not a blanket property of the tuple or an invitation to omit nonzero weights.

## 3. Highest compressed bit gives two affine pieces

Suppose the selected single bit in the compressed problem is its highest bit.
Equivalently the original two-bit input has k=g-1. Put U_c=M/2. On its overlap
domain 0<=d<M, the single-bit correlation is

    A_one(d)=M-3d     for 0<=d<=U_c,
             d-M     for U_c<=d<M.                    (4)

Both branches give -U_c at the junction. To derive (4) directly, the sign word
is positive for the first U_c entries and negative for the last U_c entries.
For d<=U_c there are d sign-mismatched pairs and M-2d matched pairs, giving
M-3d. For d>=U_c all M-d pairs are sign-mismatched, giving d-M. This proof uses
an overlap count, without a floor-moment table.

Consider one canonical positive-step progression d=b+aj with a>0 and b>=0.
If b>=M its sum is empty and zero. Otherwise let

    n=1+floor((M-1-b)/a),
    q=0                                      if b>U_c,
      min(n,1+floor((U_c-b)/a))              if b<=U_c,
    T(s)=s*b+a*s*(s-1)/2.

Exactly the first q points are in the lower affine piece. Thus the complete
single-progression answer is

    S(b,a;M)=M*(2q-n)+T(n)-4*T(q).                     (5)

Proof: the low part is q*M-3*T(q); the high part is
[T(n)-T(q)]-(n-q)*M. Adding yields (5). All floor divisions have nonnegative
numerators on their reached branch. Each division by two is exact because
s*(s-1) is even. The q=min(...) bound is explicit even though the canonical
geometry can imply it; a certificate should show the chosen typed count.

The formula includes n=1, q=0, q=n and a term exactly at M/2. It excludes
nonempty evaluation at d=M. A shifted progression with head b+1 obtains its
own canonical n and q; it must not blindly reuse the original counts. All
coefficients and results may be signed. The structural test k=g-1 is public
index routing, while counts, divisions and affine sums remain actual typed work.

## 4. Combination and evidence plan

A new version may preserve the current V|R admission, then use highest-bit
residue cancellation (1)-(2), otherwise apply the existing orientation and
parity decomposition. Each surviving branch omits its shifted sum only if
t=0. For each needed single progression it uses (5) when k=g-1 and the frozen
direct floor-moment progression otherwise. At r=0 the negative orientation
starts at R; coincident half-modulus heads retain both multiplicities.

This is a structural algorithm, not per-fixture selection of the cheaper saved
answer. New routing work, repeated scale construction, all exact divisions,
certificate generation and paid failed replays must be retained. The current
aligned implementation and its saved experiment are frozen and must not be
rewritten to make the historical counts appear smaller.

The completed predecessor's six tuples and 36 values are a reusable exact
comparison source. Its independent typed comparator enumerated 720 ordered
pairs once per tuple; do not repeat that experiment merely for a new dispatcher
if its complete saved evidence and sources remain verified. A new actual run
must declare its own strict positive replay and negative controls before
execution, record any failure once, and preserve all actual native traces.
Costs of such a successor are currently unknown. Small-input speedup and a
complexity breakthrough cannot be inferred from these identities alone.

The scope remains supplied-modulus scalar coefficients. This does not supply
order finding, general unaligned mixed-floor evaluation, growing-mask
compression, chronological matrix products, or full Shor sampling.

Global-Knowledge-Sync: main@9f0e65b / GLOBAL_KNOWLEDGE_V1
