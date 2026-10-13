# Proposed tool contract: resonant boundary and endpoint observers

Status: PROPOSED / LOCAL NONCANONICAL TOOL-PROPOSAL. This extracts three
already proved finite-field interfaces; it is not an implementation, new
execution, novelty claim, canonical toolbox registration or Native acceptance.
The fixed CM24 C/tau/F_CM target and all mathematical parents remain OPEN.

Provenance: UNKNOWN local Root-delegated nonauthor helper
/root/cm24_extension_paper_check; directed NONBLIND. Root retains direction
and publication; original CM/Hart owners are unchanged. No new owner, Task,
Claim, Run, branch, Source write, script, prime check, sample or Green run.
All input proofs and earlier review originals are preserved unchanged.

## 1. Fixed mathematical objects and evidence requirements

The descriptor identifies the exact declared F_p, p=6m+1 prime in the
classes13/19mod24, m>=2, N=3m=(p-1)/2, and the operators

    J=2x(x-1)(x-4)d^2+(5x^2-15x+4)d+(x-1),
    Pi=Pi_(0..N), q=x(x-3)^2/4,
    D*=z(1-z)d^2+(3/2-5z/2)d-5/9.

Canonical basis data are fixed, linked to the same parameter descriptor:

    h_0=h_N=g != 0, phi_n=4^(-n)h_n/g, J phi=0,
    psi_0=0, psi_1=1, J psi=4 epsilon_0-4 epsilon_N.

The prime-family, g unit, canonical basis and proof provenance are input
premises. This proposal does not create a new primality test, basis builder,
mathematical acceptance or identity-based independence. Formal integer
exponents are retained; they are not identified modulo p-1 or via z^p-z.
All signed values are actual F_p elements, with their object/coordinate
bindings retained. Source byte custody and mathematical validity are distinct.

## 2. Interface A: finite Laurent projection certificate

Input:

* The fixed operator/parameter descriptor.
* A finite formal Laurent P=sum_k P_k x^k, with actual integer exponents;
  alternatively a verified binding to its complete finite coefficient data.
* If materialized output is requested, a central coefficient view P_0,...,P_N
  explicitly linked to that same Laurent object.

Output:

* Exact domain statement: Pi J P=J Pi P for every such finite Laurent P.
* The four crossing witnesses below, with actual integer indices.
* Optionally the complete retained coefficient vector of J Pi P. This is
  identical to Pi J P under the verified domain, without scanning outer
  blocks for mathematical contamination.

The monomial law is

    J x^k=a_k x^(k+1)+b_k x^k+d_k x^(k-1),
    a_k=(2k+1)(k+1), b_k=-(10k^2+5k+1), d_k=4k(2k-1).

Crossing certificate:

    outside -> inside: a_(-1)=0; d_(N+1)=4(N+1)(2N+1)=0,
    inside -> outside: d_0=0; a_N=(2N+1)(N+1)=0.

These are all possible crossings because exponent shifts are only -1,0,+1.
The identity concerns this exact cut/operator; it does not authorize other
cuts, rational/infinite-series truncation, deleting outer endpoint blocks,
or silently applying an unproved gauge identity to a different carrier.

## 3. Interface B: strict source and prescribed terminal compatibility

Input:

* The fixed canonical h/g descriptor, including g unit.
* The complete strict source y=(y_1,...,y_(N-1)).
* Optionally a terminal b prescribed independently of the output value.
* When reporting a carrier-derived source, the actual raw-top-zero premise:
  e.g. degree F'<=p-2 and S_n=-[x^(N+n)]q'F'(q), whose legal primitive
  proves S_N=0. The zero-seed terminal rule itself applies to the canonical
  zero-seed response of any strict y.

Output:

    c(y)=-sum_(n=1)^(N-1) h_n y_n/g,
    complete normalized forcing=(0,y_1,...,y_(N-1),c(y)),
    residual kappa(y,b)=g b+sum_(n=1)^(N-1)h_n y_n,
    compatible(y,b) iff kappa(y,b)=0 iff b=c(y).

Proof certificate: rank J=N on its (N+1)-coefficient window, h is its
nonzero left kernel with h_0=h_N=g, and the full raw source (c,y,0)
has left pairing zero. Alternatively the normalized source (0,y,b)
requires the same pairing. No internal h coefficient is inverted.

c is a derived weighted observation, not an independent parameter or a
freely adjustable seed. A source-preserving carrier change cannot change it.
The optional b stays separate from c; assigning b=c after seeing the answer
does not demonstrate an independently prescribed terminal requirement.

For an actual central carrier the raw P_0,P_1 must stay retained:

    A=P_0, c=4P_1-P_0,
    Z=P-A phi-(c/4)psi.

This is a consistency interface, not a new Green solver. No old t_0/4
seed or class-19 terminal is transferred to a new B. If y=v=-beta^h-t,
the inherited ledger gives c_v=c_h-t_0; demanding c_v=0 requires the
additional exact weighted identity c_h=t_0. The old class-19 t_0=-1/3
is retained in its own original source object.

## 4. Interface C: full signed carrier endpoint from central plus outer data

Input:

* The exact q/central-cut descriptor and an actual carrier B of degree<=p-2
  with B_N=0, or a verified binding to its complete preserved coefficients.
* The complete central P=Pi W_B for W_B=x^(-N)(x-3)B(q)/24, including its
  actual raw seed. Normalized Z alone is not this input.
* The actual signed outer evaluation

      Omega_B=W_-(1)+W_+(1),
      W_-=sum_(k<0)[x^k]W_B x^k,
      W_+=sum_(k>N)[x^k]W_B x^k.

  Omega must be linked to the same B/W_B and obtained from those actual
  finite blocks. A desired target endpoint is not provenance for Omega.

Output:

    central_sum=P(1)=sum_(n=0)^N P_n,
    full_signed_readout=-12(central_sum+Omega_B)=B(1).

Proof certificate: q(1)=1 and W_B(1)=-B(1)/12. Both negative and positive
outer blocks enter with their actual signs. No tail is set to zero.

Ambient necessity certificate: delta B=1 preserves B_N=0 and all central
coefficients because delta W=x^(-N)(x-3)/24 has only negative exponents.
It nevertheless changes B(1) by1. Therefore the central observer alone is
insufficient on this enlarged family. This is not a variation of the
singleton fixed original forcing: D*(delta B)=-5/9.

For the future language consisting only of B(1) and fixed scalar multiples,
one actual scalar Omega_B in addition to complete central P is sufficient.
The necessity is for retaining information distinguishing this endpoint
fiber; it does not assert that this particular scalar representation is
the only possible one. No source-to-Omega transport or fixed C/tau/F_CM
equality is supplied by this readout.

## 5. State, joint retention and paid costs

Retained mathematical state binds the parameter/operator/basis descriptor
to complete signed source y, actual raw central P, derived c, any independent
b and its residual, and the actual Omega/outer-object binding. Canonical
phi/psi/h data stay linked to the same p and finite indices. c and Omega
are different objects: c is fixed by y, while Omega retains carrier-endpoint
information absent from central P. Original Source proofs, B coefficients,
outer blocks, full half-prefix tail, class branch and all target components
remain preserved; this proposal does not authorize deleting evidence.

Operational endpoint compression to Omega is permitted only within the
explicit B(1)/fixed-multiple future language. It must not be reused for
different endpoints, derivative jets, full coefficient recovery, expanded
source operations or a changed cut. Those require the original full state
or additional proved observers. Normalizing Z does not authorize dropping
the raw A needed to recover central P.

Let ell be the number of supplied Laurent coefficients and b_p=ceil(log2 p).
The following are paid field-operation bounds, not measurements:

* A's four scalar crossing checks cost O(1). Materializing J Pi P from an
  already linked central view costs O(N) field operations and O(N) retained
  output elements. Extracting that view from unindexed input additionally
  pays O(ell) input scans/reads and exponent comparisons; that work is not
  hidden in O(N).
* B computes its weighted sum, c and optional kappa/predicate in O(N)
  field operations. Computing or loading h, phi, psi and cached h/g weights
  is separately paid preprocessing. The inverse of g must be paid once
  or already present in an explicitly paid scoped cache. A compatibility
  comparison and output serialization have positive costs.
* C sums the N+1 central coefficients and combines them with the actual
  Omega in O(N) field operations. Computing B(q), W_B, central coefficients
  or Omega from unprocessed B is additional paid construction; this contract
  grants none of it for free. Summing already materialized outer blocks
  pays for every supplied outer coefficient.

Keeping full joint central/source/basis views takes O(N) field elements,
or O(N b_p) bits, plus immutable evidence/bindings and actual supplied
outer state. Each readout can use O(1) accumulator workspace after inputs
are available; that does not erase the retained input evidence. A stored
output vector costs O(N) elements. Multiplication, additions, reads, modular
representation, inversion, comparisons and serialization are positive.
With multiplication cost M(b_p), O(N) field arithmetic contributes
O(N M(b_p)) plus paid additions/reads/output and any separately charged
inversion, basis/preprocessing or carrier construction. No field operation
is equated to one bit instruction, API block or Native physical step.

## 6. Failure modes, reporting and unsupported claims

* WRONG_DOMAIN: mismatched p/N/operator/cut, nonfinite Laurent data, wrong
  source lengths, or formal exponents silently reduced as function indices.
* PRECONDITION_UNVERIFIED: prime-family/g-unit/basis provenance missing,
  unmatched central/outer carrier bindings, or asserted raw-top-zero without
  its actual degree/primitive premise. A numerical value can be reported
  conditionally, but no verified carrier equality is then claimed.
* INCOMPATIBLE_TERMINAL: kappa(y,b) is nonzero for a legal independently
  prescribed b. Preserve its exact value and full source; do not alter y,
  overwrite b, fit a seed or mark a mathematical parent completed.
* INSUFFICIENT_ENDPOINT_STATE: central P is supplied without an actual
  Omega or equivalent complete endpoint observer. Do not infer B(1) from
  the projection, from c, from a target value or from dropped outer tails.
* UNSUPPORTED_FUTURE_LANGUAGE: another cut, infinite/rational expansion,
  other endpoints/jets, full B recovery, total target equality or direct
  native/physical propagation is requested beyond this scoped readout.

The proposal provides no implementation, new acceptance, novelty, dimension,
Working Truth/Foundation or native promotion claim. It does not identify
source surjectivity with fixed-target completion or treat a custody success
as a mathematical check. Static field algebra has no mandatory native time
axis; review/custody metadata are separately typed.

## 7. Exact proof basis and next action

The immediate proof basis is the unchanged
CM24_GENERIC_ZERO_SEED_TERMINAL_AND_FULL_ENDPOINT_LEDGER_PAPER.md
(10165B, SHA256ceeb0416b5ec3df646e2e43387ba0c9139030c686a2eb9d344a4e40802dc2e48)
and its complete pin chain, including the frozen original 12020B half-source
specification. The current generic ledger is under separate peer review;
this PROPOSED extraction neither replaces that review nor upgrades its status.

Root may preserve this proposal together with the actual proof/review records
and decide any subsequent canonical intake. No such intake or Source write
is performed here. Independent weighted terminal requirements and the full
fixed-target carrier endpoint mechanism remain their precise open interfaces.
