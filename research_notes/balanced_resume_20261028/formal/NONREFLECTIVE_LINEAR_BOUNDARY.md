# Nonreflective linear handles: pre-query gcd simulation and the missing completion bit

Author: EM-DIRECT-099801. Activity: RA-BALANCE-FORMAL-20261028-099801.
Date: 2026-10-28 (Asia/Shanghai).
Status: AUTHOR_PROVED_BOUNDED_INTERFACE_CANDIDATE, pending distinct review.

This is direct supplementary TASK_RESEARCH. It does not execute or take over a
registered Task, issue a Driver verdict, or change Working Truth or Foundation.
The author inherited shared control and source context; this is not blind work.
Registration is fully observed at commit
975a3f434aa219721dbbd36906232401012841b3 on
research/balanced-resume-20261028-18c67b; canonical main intake is pending.

All algebra below is an explicitly external module/computability model. The
project's native substrate remains the signed six-axis Cell torsor of Heartbeat
World, with no native plane. Program stages are separately typed computational
order, not physical time. No native propagation or physical law is inferred.

## 1. Existing result, exact increment, and no-repeat boundary

The inherited result is
`research_returns/N_COUPLED_OPAQUE_LAZY_TYPED_SUPPORT_SCALARIZATION_DELAY_RETURN_20260901.md`,
Git blob 63c02dc9dbafb730cef2db2054f0e5b5c2de7fd8, fully fetched again in this turn.
Its current accepted bounded review is represented by
`driver_reviews/mcp/MCP-cd5eefdde49843898b2a70c1af94d8dd/d532ce9873437bd42300/ROOT_N_COUPLED_CURRENT_NEGATIVE_BOUNDARY_REVIEW_20261014.md`,
blob ab04b44f195c8846854b33a41794aa3d1be2d65d. Immutable month-library locator:
34ac8a0471274dfb2b8b14e9bf79d3aed9542493,
`docs/research_library/202610_month/misc_formal.json`,
entry MISC-FINITE-REFLECTION-SUPPORT-BOUNDARY.

That result proves effective cardinality and presentation recovery for complete
finite reflection, and standard-basis reconstruction for a total linear map.
It expressly leaves genuinely nonreflective compositional interfaces open.
We do not reprove its general cardinality-support identity or its 2500-case run.

The increments here concern three precise interfaces:

1. An adaptive, single-seed linear handle program needs no complete reflection
   for an exact pre-query gcd simulation (Theorem 1).
2. A certified finite generating list for the relevant submodule is sufficient
   for exhaustive local reflection, even without a whole-module iterator
   (Proposition 2, an explicit application of elementary module algebra).
3. A total infinite stream, a known finite cardinality bound, total decidable
   handle validity/equality, and exact composition still need not provide a
   computable completion bit (Theorem 3). This is stronger in its operational
   interface than the older c.e.-relation example, whose completed equality is
   not supplied as a total decision procedure.

These are source-local boundary refinements and classical-method applications.
No literature-wide novelty, efficient factoring algorithm, new global tool
family, or solution of the parent N-coupled objective is claimed.

## 2. Theorem 1: single-seed adaptive equality yields a public gcd first

Let N>=2 be public, R=Z/NZ, and M any R-module. M need not be finite.
Supply exactly one distinguished nonzero opaque handle x and the zero handle.
Allowed handle construction is addition, negation, and scalar multiplication
by public elements of R. Public control may perform arbitrary effective scalar
computation, branch on prior exact equality answers, and use a random tape.
There are no additional opaque seeds, arbitrary handle inspection/serialization,
hidden fresh randomness in operations, nonlinear handle maps, or additional
module observations. Handle equality is extensional equality in M.

For every fixed public input and random tape there is an exact public simulator
with this alternative at every finite stage:

* it reproduces the complete declared public control/equality transcript; or
* before issuing the next handle-equality query, it produces a public integer
  d with 1<gcd(N,d)<N.

In particular, along a prefix in which every compared coefficient difference
is either zero modulo N or a unit modulo N, the full equality transcript is
independent of M and x. A first module-dependent equality answer can occur only
at a query whose already public coefficient difference yields a proper factor
of N. The simulator may produce such a factor even when that query would have
the same answer in two particular modules.

### Proof

Attach a coefficient c(h) in R to every constructed handle, with c(0)=0 and
c(x)=1. Inductively use c(h+k)=c(h)+c(k), c(-h)=-c(h), and c(a h)=a c(h).
Linearity gives the invariant h=c(h)x in M. Coefficient tracking does not erase
the original handles or branches; it is a parallel proof witness.

For a query Eq(h,k), compute d=c(h)-c(k) modulo N and g=gcd(N,d), with
gcd(N,0)=N. If g=N then d=0 in R, so Eq is true. If g=1 then d is a unit;
d x=0 would imply x=0 after multiplying by its inverse, a contradiction.
Thus Eq is false. If 1<g<N, return g before evaluating Eq.

The first two cases supply the exact answer, so the same scalar control branch
and next operation are selected. Induction proves equality of every finite
transcript prefix. Fixing the random tape gives the pathwise randomized claim.
No enumeration of M, basis, presentation, order computation, or bound on |M|
was used. QED.

### Scope and sharp limitations

The nonzero promise matters. If x may be zero, Eq(x,0) differs between zero and
nonzero modules with public coefficient difference 1; there is no proper gcd.

The single-seed restriction matters. For N=15, compare M=F_3 with x1=x2=1
against M'=F_5 with x1=1,x2=2. In both, the seeds are nonzero. The query
Eq(x1-x2,0) is true in the first and false in the second, although both nonzero
coefficient entries 1,-1 are units modulo 15. The supplied seed relation is
information absent from a single coefficient. This is only a type-boundary
countermodel, not a factor-blind construction of these seeds.

For N=pq and a nonzero one-sided seed, its additive order is p or q. Exhaustive
orbit enumeration therefore extracts a factor, but this is an ordinary order
method and is classified as prior-art reuse, not as a new N-coupled primitive.
Theorem 1 is sharper for the stated grammar: the relevant scalar gcd is
available before a discriminating query. Scalar code might independently
factor N; the theorem neither rules that out nor gives a complexity bound.

## 3. Proposition 2: known generators are a local reflection certificate

Let g1,...,gr be handles in an R-module with exact addition, scalar operations,
and extensional equality. Assume this *finite supplied list* is certified to
generate the particular submodule H whose support is being observed. Then H
can be completely reflected without an ambient-module iterator:

    phi : R^r -> H,   a |-> sum_i a_i g_i.

Enumerate the N^r coefficient tuples and deduplicate their image handles using
exact equality. This yields |H|. Enumerate those same tuples for which
phi(a)=0; take them as relation columns C. Then im C=ker phi and
H is isomorphic to coker C. The argument also covers r=0, when H=0 and |H|=1.

For squarefree N=pq the inherited identity

    gcd(N,|H|)=p^[H_p != 0] q^[H_q != 0]

therefore scalarizes the observed submodule. This is an effective, potentially
huge procedure, not a performance claim. If the list merely generates a proper
submodule, it does not certify the support of the ambient module M. A changing
stream of generators does not supply a certificate that the current list is
complete. Those distinctions are exactly what the next theorem preserves.

## 4. Theorem 3: even bounded finite streamed modules can lack a completion bit

Fix any public N>=2. Uniformly from a program index e construct a countable
decidable handle domain D_e, decidable extensional equality, exact total module
operations on valid handles, a computable stream visiting every valid handle,
and the known bound |M_e|<=N, such that

    M_e = 0                 if program e never halts,
    M_e isomorphic to R      if program e eventually halts.

Consequently no algorithm, given these effective interface codes and N,
uniformly halts and outputs |M_e|, or gcd(N,|M_e|), on every e. No uniform
algorithm outputs a certified complete finite generator list on every e.

### Construction and proof

Handles are pairs (s,a) with s a nonnegative integer and 0<=a<N. Declare

    Valid_e(s,a) iff a=0 or program e halts within s computation steps.
    Eq((s,a),(t,b)) iff a=b.

Validity is a bounded computation and equality is total decidable. The
extensional carrier is D_e/Eq. Its zero is [(0,0)]. For valid handles define

    (s,a)+(t,b) = (max(s,t), a+b mod N),
    -(s,a) = (s,-a mod N),
    k(s,a) = (s,ka mod N).

These outputs are valid. If a nonzero residue is produced, at least one input
had a nonzero residue and certified halting by its timestamp; max(s,t) retains
that witness. Negation and scaling have the same property. Equality is a
congruence, and residue arithmetic proves every module axiom. If e never halts
only residue zero has handles; if it halts by h, all residues have handles at
every s>=h. Hence the stated cardinalities 1 or N hold.

At stage s enumerate all N residues, emit each valid (s,a), and proceed forever.
Every stage is finite, each validity test terminates, and each valid handle
eventually occurs. There is no end marker. This supplies a genuine exact
pre-readout addition/scaling semantics; it is not a sealed token with only a
reveal operation.

A uniform exact cardinality or support algorithm would decide whether e halts,
by distinguishing 1 from N. A uniform complete finite generator-list algorithm,
composed with Proposition 2, would do the same. This contradicts undecidability
of halting. QED.

### What the counterexample does and does not establish

It uses empty/full support only. It neither constructs a proper one-sided
support witness nor grants an admissible halting oracle or solves factorization.
It sharpens a missing-interface distinction: eventual finiteness plus a known
bound and total equality does not mean recognizable enumeration completion.
The known bound is an upper bound, not a supplied exact cardinality.

In contrast, under a promise that a streamed finite R_(pq)-module is nonzero
and one-sided, total extensional equality lets one wait for the first nonzero
handle and enumerate its cyclic orbit. The stream eventually exposes such a
handle and its orbit has p or q elements. Thus removing the end marker by
itself does not prevent a promised one-sided witness from scalarizing by the
ordinary order method. This positive-promise statement does not decide empty
support or supply a stopping certificate on inputs without that promise.

At a finite prefix the generated submodule H_s can always be reflected using
Proposition 2. For nested prefixes |H_s| divides |H_(s+1)|. If the whole module
has size at most B, there can be at most floor(log2 B) strict size increases.
That finite change bound supplies no computable bound on the stage of the last
increase: the construction above has only one possible increase, at an
arbitrarily late halting stage. Inferring stabilization from a quiet prefix is
therefore invalid.

## 5. Reuse, validation, and next unresolved interface

Tool coverage was run before the new construction. Existing T0_BRC typed
branch/provenance discipline is REUSE_APPLIED: coefficients are retained with
their full handles and actual public branch trace. Existing operation-safe
quotient discipline is REUSE_APPLIED: the single-seed simulator is scoped to
its exact future language; no multi-seed or physical quotient is asserted.
The elementary gcd, finite generator enumeration and halting diagonalization
are classical methods; this report does not register any new T family.

`verify_nonreflective_boundary.py` supplies exact finite diagnostics for the
single-seed equality lemma over several semiprimes, adaptive simulations,
the two-seed boundary, and the streamed activation module. The universal
arguments and halting obstruction are the paper proofs above; a finite test
cannot certify general undecidability or all programs.

The new search boundary is narrower: withholding complete finite iteration
does not rescue a one-seed linear/equality interface, or a certified finite
generated observed submodule. A genuine remaining constructor would have to
supply a different admitted interface (for example genuinely independent seed
relations or a non-linear effect) and its complete source-bound semantics.
No existence, admissibility, usefulness, or success of such a constructor is
asserted. The parent objective and formal Task states remain unchanged/open.
