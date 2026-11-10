# R44 — Adaptive dyadic phase certificates and sparse extinction-rank updates

Date: 2026-11-10. Frozen scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Continuation of R43 Draft PR #1987 at 25876fa923a88c6d64e9be703b3d3bd42c204bf6. Author mathematical proof and exact finite validation, independent review pending. Scope: a label-preserving auxiliary irrational-circle observer; no claim of native X6 physical rotation, and P000 is unchanged.

## Model and explicit dyadic input construction

Take alpha=sqrt(2)-1, m>=2 historical half-open circular arcs induced by indices z=0,...,m-1, and integer source windows W_J=[J-N,J), N>=1. Preserve labelled maximal source tau_k(J)=max{t in W_J: owner(t)=k}, or None for an empty arc.

For precision b>=1 put D=2^b, s_b=isqrt(2D^2), L_b=(s_b-D)/D, H_b=(s_b+1-D)/D. The enclosure [L_b,H_b] contains alpha strictly; its width is 1/D. As b increases these enclosures are nested. Construct the R42 midpoint residue model with Q=2D, U=2s_b+1-2D and delta=1. The representation of each source is r_t=tU mod Q. Importantly, U comes from unreduced dyadic numerators, not from adding separately reduced Fraction numerators.

## Theorem R44.1 (preserve proven source labels when refining precision)

Suppose an R42 order/owner strict-integer certificate has established historical order, an initial exact last-source vector and incoming-source owners for true alpha in [L_b,H_b]. A subsequent enclosure [L_c,H_c] subset [L_b,H_b] retains every already certified owner and every previous exact window vector. Recompute the midpoint residues at c for the first uncertified source t and continue; no previous source label needs replay solely on account of the precision refinement.

Proof: the certificate states a fixed phase order/owner across the entire old parameter interval; true alpha belongs to every nested interval. Restricting its domain preserves the relation. R43's one-source window-update rule produces the cached vectors from these certified labels. Their exactness is inductively invariant. Reinitializing a modular representation for the pending source does not change the underlying labelled relation. QED.

## Theorem R44.2 (uniform explicit termination for a finite sqrt(2)-1 workload)

For every nonzero integer k, dist(k alpha,Z)>1/(4|k|).

Proof: choose nearest integer l to k alpha. Its conjugate alpha'=-1-sqrt(2). The norm (k alpha-l)(k alpha'-l)=l^2+2kl-k^2 is a nonzero integer. Moreover |k alpha'-l|<=2sqrt(2)|k|+1/2<4|k|. Thus |k alpha-l|>1/(4|k|). QED.

For a declared finite set of historical/source phase comparisons, let M>=1 bound all nonzero absolute index differences |t-z| and |z-z'|. If width w=2^-b<1/(4M^2), every noncoincident pair has true distance from an integer greater than its entire variation |k|w over the enclosure. The midpoint strict comparisons used by R42 therefore certify the historical and incoming-source order. Exact historical coincidences t=z have a separate equality branch. A sufficient choice is any b with 2^b>4M^2, hence O(log M) bits. The sufficient bound can be much larger than the actual first successful precision. For exact endpoint/Floor Sum repair also certify the finite set of endpoint floors it uses, applying the same separation logic to the relevant nonzero integer arguments; the implementation checks those assertions directly.

## Theorem R44.3 (two-label update of any fixed-threshold extinction rank)

Define F_J(x)=sum_k 1{tau_k(J)=None or tau_k(J)<x}, for fixed integer threshold x. Let D_J={k:tau_k(J+1)!=tau_k(J)}. R43 proves |D_J|<=2, because only the incoming label and a possibly expired maximum's label can change. Therefore

F_(J+1)(x)-F_J(x) =
  sum_(k in D_J) [1{tau_k(J+1)=None or tau_k(J+1)<x}
                   -1{tau_k(J)=None or tau_k(J)<x}].

Proof: cancel all unchanged terms. QED. Using an ordered multiset and a separate empty-label count, updates and queries each take O(log m) comparisons. This gives a sparse exact interface for the compatible fixed-Farey-stage R35/R36 extinction-rank functional; stage changes require their own coordinate mapping.

## Complexity with the actual input representation

Let b be the current dyadic precision and j the bit width of incoming source indices. Constructing each enclosure involves integer isqrt on O(b)-bit operands. On a precision change, recompute m historical residues and sort O(m log m) b-bit comparisons, then reseed the current source residue by one multiplication/remainder on b- and j-bit inputs. Without a precision change, each incoming source uses a b-bit modular addition, O(log m) b-bit comparisons and two integer boundary tests on O(max(b,j)) bits. Here delta=1, so the bound tests need no multiplier for width. Exact one-label expiry repairs carry their separately measured Floor Sum/endpoint cost. Sparse output is O(K(j+log m)) bits plus repairs and initial state; printing each full m-vector costs Omega(K m j) bits. Precision construction, history preprocessing, initial last-source selection, repair and output costs are distinct terms.

## Executed validation

The extended local validator VERIFY_R44.py and its frozen R42/R43 dependencies executed six cases: J=100, 1000, 10^6, 10^9; short window N=5; and negative J. 1,414 exact full window vectors match a separately built high-precision Euclidean Floor Sum reference. Short-window cases also match direct brute-force. 1,408 window shifts checked 5,632 sparse rank identities and exercised 171 one-label repairs, 20 precision refinements; no precision change replayed prior labels. One local implementation improvement removed redundant phase reseeds during ordinary repairs: only 26 initial or changed-precision seeds were needed, versus 1,402 modular-addition steps. The full Python source, JSON certificate and literal run log are in the corresponding R44 research bundle. The companion VERIFY_R44_COMPACT.py in this commit is a standalone independently executable exact smoke test for three smaller families.

Independent mathematical review and project admission pending. This run does not rerun the entire R32/S23 298-affine-segment compiler.
