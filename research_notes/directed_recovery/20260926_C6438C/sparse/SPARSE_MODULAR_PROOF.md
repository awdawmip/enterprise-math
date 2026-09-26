# Complete sparse modular columns from actual BRC addition

Status: AUTHOR_EXECUTED / UNREVIEWED / NOT_ADMITTED. Researcher EM-DIRECT-C6438C;
activity RA-CAAAC604CB513AEA8BBC1DFC; registration Source
f0e5fb6f478a5a380ab5a7533d2585f7f43ee3bf. Same-context contribution, not independent
review. Frozen Shor source HEAD 0852cad130c1d877174d235687cf60c19f318c58.

## What is closed

For every integer N >= 2 and 0 <= b < N with gcd(N,b)=1, this compiler produces
every basis column of exactly the Stage78 modular permutation, including the
identity tail above N. It never takes an order or a factor as input. Its
construction is a composition of the existing, actually executed 12-state
positive BRC full-adder transducer. No dense W-by-W matrix or classical phase
reference is executed by production compilation. Here W=2^ceil(log2 N).

The result is a typed exact replacement for the *representation and execution
of this positive deterministic permutation*. It neither changes the positive
BRC kernel into a signed kernel nor supplies a physical reversible realization
of a discarded arithmetic register. Arithmetic input/carry records are retained
in the certificate. The full residual vector and signed companions are retained
when the permutation is used inside the Shor simulator.

This removes the prior dense modular-table bottleneck. It does not bound the
Shor work support by a polynomial in log N; W itself remains exponential in the
binary input length. The phase approximation and probability observer are
unchanged.

## Existing coverage and source boundary

Read enterprise_toolbox_registry.json at Source
5ab9c3befa50b24b26a87c63affcbf45ea4d8084, Git blob
3889506451091ebcfbf7a58cda6517c4af8c3597. T0_BRC covers support/result/provenance
composition; T7 covers finite relabeling. T0's hard boundary forbids inferring
erased provenance from Boolean support. Targeted connector searches for
`recurrent_mass_power sparse permutation` and `BRC permutation sparse support
provenance` returned no matches. Thus the work reuses T0/T7 and the frozen
full_adder_columns constructor; it proposes a narrow sparse representation
extension, not a new global tool family or evidence of global registry absence.

The actual vendor is byte-verified by Stage45 verify_vendor: source commit
bc7babbb9e890f6d5a7094430a5fbdccf66c77ad, path
src/enterprise_math/brc_weighted_recurrent.py, blob
4e6b3132580e3cd70a20a0d8bd4d28792b961afb. Its recurrent_mass_power accepts only
nonnegative exact rational matrices. The source explicitly excludes signed
amplitudes and infinite-state recurrence. We preserve this boundary.

## Lemma 1: the actual arithmetic primitive

Stage78 full_adder_columns builds a positive BRC graph on 12 states. For each
input code 4x+2y+c in {0,...,7}, one positive unit edge goes to the output label
8+2s+d, where s is the low bit and d the carry of x+y+c. An actual
recurrent_mass_power(graph,1) call certifies every one of these eight source
rows. The returned columns satisfy x+y+c=s+2d.

add_unsigned(L,R,w) uses only these returned column values to obtain s_i,c_i.
It records every bit index, input code, sum bit and output carry, plus L,R,w.
Multiply x_i+y_i+c_i=s_i+2c_(i+1) by 2^i and sum. All internal carries telescope,
giving L+R=low+2^w carry, with c_0=0. This proves the routine for every width w
and all declared inputs 0 <= L,R < 2^w. No extrapolation from tested widths is
used. All bit-local provenance is retained and replayable.

## Lemma 2: one complete modular multiplication table

Put n=ceil(log2 N), W=2^n, w=n+1, M=2^w. Begin with r_0=0. At source y, emit
target r_y, then apply the actual adder to r_y+b, obtaining s. Since r_y,b<N,
0 <= s <= 2N-2 < M, so its overflow is zero. Apply the same adder to s+(M-N).
The resulting carry is one exactly when s>=N. Its low output is s-N in that
case; otherwise keep s. The unused subtraction low output and the carry remain
in the certificate; they are not claimed physically erased. Hence

    r_(y+1) = r_y+b                 if s<N,
              r_y+b-N             if s>=N.

Induction gives 0<=r_y<N and r_y congruent to b*y modulo N for all 0<=y<=N.
Therefore r_N=0 and every emitted target is exactly the former Stage78 target.
For y=N,...,W-1 emit y. This proves equality of *all* W columns, including zero
input and every unused computational-basis label.

For coprime b, b*y=b*z modulo N implies y=z modulo N; on [0,N) this means y=z.
Together with the disjoint identity tail this is a permutation. Conversely a
non-coprime b has colliding residues, so the complete permutation validator
rejects it. The implementation checks the whole target range and injectivity;
it does not assume coprimality or invoke an order oracle. Its N-step loop has a
finite explicit bound, and certificate replay repeats the actual typed digit
operations rather than calling an arithmetic reference implementation.

## Lemma 3: sparse embedding, composition, inverse and control

For a permutation p on X={0,...,W-1}, define its positive row-source matrix

    E(p)[x,z] = 1 if z=p(x), and 0 otherwise.

There is exactly one positive unit branch per source. The sparse object stores
all these branches through targets[x] and their content-addressed source
certificate. The certificate itself must accompany the object; its digest is
an identity check, not a replacement for available provenance.

For two such maps p,q,

    (E(p) E(q))[x,z] = sum_y [y=p(x)] [z=q(y)] = [z=q(p(x))].

Thus SparsePermutation.then is exactly the positive BRC serial product.
Repeated products, including zero length, follow by induction. Each composite
provenance object retains its ordered left and right expressions; equal target
tables are not asserted to have equal path provenance.

For the inverse map, E(p^-1)=E(p)^T and both endpoint composites are identity.
The inverse provenance retains the original edge identity in reversed direction.
Endpoint identity does not delete the forward/inverse history.

For a classical/coherent control label c in {0,1}, use the disjoint carrier
{0,1} x X and C(p)(0,x)=(0,x), C(p)(1,x)=(1,p(x)). Its positive matrix is the
direct sum I and E(p). No control label is identified or traced out. The
controlled method uses labels c*W+x and proves this exact direct-sum equality.

These equations hold for arbitrary finite X and any number of serial/control
operations. The finite tests below check that the implementation realizes the
equations, while the equations provide the general scope.

## Lemma 4: signed, complex and retained-mode fibre transport

Keep the positive and negative companion lanes separate: (x,+) and (x,-).
Lift each branch as (x,s)->(p(x),s). This is still an ordinary positive unit
permutation, on 2W labels. Its character readout is A(x)=m_+(x)-m_-(x).
Because p is bijective, at z only the source p^-1(z) contributes. Therefore
character after positive transport equals signed transport after character.
This is a commuting-square identity, not a claim that negative amplitudes are
positive BRC mass. The same equation applies componentwise to real/imaginary
parts and all 61 retained modes; no fibre coordinate is inspected, deleted,
normalized or replaced by its norm during transport.

The permutation preserves all fibre inner products and the sum of squared
coordinates. Combining this with Lemma 3 proves equality inside any declared
linear signed-fibre program, including controlled modular steps interleaved
with the original BRC phase/H4 steps and terminal instruments. It does not
permit a later observer to forget the modular input/carry source certificate
or to treat a measured classical control as still coherently available.

## Costs and failure boundary

The optional sparse_modular_power_chain constructs b_0=a and
b_(i+1)=table_(b_i)[b_i]. Lemma 2 gives b_(i+1)=b_i^2 modulo N without ordinary
modular multiplication in this compiler. It returns the complete table and
certificate identity at every position. sparse_modular_power_trace similarly
uses table_b[y] for set exponent bits and table_b[b] for each next square. The
usual binary-exponent invariant proves its output is a^e modulo N; the original
input exponent and all selected/identity steps remain in the trace. Neither
routine uses a minimal order. These APIs allow explicit replacement of both
stream initialization and postprocessing modular powers; they do not silently
monkeypatch frozen code.

sparse_classical_postprocess retains the exact existing continued-fraction
denominator iterator, candidate order, returning-exponent tests, odd-exponent
rejection, actual gcd_brc calls, factor sorting and retry reasons. Only its two
modular-power call sites use sparse_modular_power_brc. The just-proved equality
of modular powers gives identical control flow and output for every supported
N,a,t,k; no probability approximation or minimal-order assertion is introduced.

The former Stage78 implementation materializes W^2 rational entries and calls
recurrent_mass_power(P,1). The frozen vendor performs both I*P and P*P in that
iteration, using two dense cubic multiplication loops even for depth one.
Thus it uses Theta(W^3) rational loop operations and Theta(W^2) matrix storage.

The new compiler calls the fixed 12-state adder constructor once per fresh
cache and reuses its certified columns. It performs exactly 2N(n+1) digit
applications, stores W targets, and retains O(N log N) digit records. It uses
O(W+N log N) scalar/record operations under the word-operation model. Certificate
bit size is O(W log N + N (log N)^2), because retained input values and bit/edge
indices have nonconstant sizes. Python integer bit costs are additional. A
single application transports each occupied input endpoint once and all its
fibre coordinates remain unchanged; full-array application has O(W) references.

This is a reduction in redundant dense BRC work, not a polynomial-time integer
factoring theorem. A large residue support, exact amplitude bit lengths, phase
approximation budget, sampling randomness and bad-base retry probabilities
remain separate resource or semantic obligations.

Inputs outside integer N>=2, 0<=b<N are rejected; nonpermutation tables are
rejected; missing/mutated columns, digit records, edge identities, identity tails
and resource counts are rejected by certificate replay. This interface does
not accept arbitrary weighted branching, partial permutations or discarded
fibres under the same proof.

## Actual validation

Run `python -B -S verify_sparse_modular.py` with BRC_STAGE87_SOURCE pointing to
the immutable Stage87 checkout if moved. Only the standard library is required.

- Six inputs (3,2),(5,2),(7,3),(15,2),(21,2),(21,20): all 100 complete basis
  columns equal the original actual BRC modular_columns outputs.
- Serial composition: all eight start columns of a 24-state layered positive
  BRC graph at depth two agree with sparse composition.
- Controlled direct sum: all 16 basis columns agree with actual BRC execution.
- Inverse: all eight inverse columns agree; both compositions have all identity
  columns while their history expressions remain present.
- Signed transport: the actual 16-state positive sign-cover kernel agrees on
  488 exact rational retained coordinates (8 source labels times 61 modes), and
  the quadratic norm is unchanged.
- Eight negative controls are rejected, including digit/target/provenance/
  coverage/tail/resource tampering, non-coprime base and duplicate targets.
- Larger N=33,257,1009 retain 64,512,1024 complete columns and replay every
  arithmetic record. They require zero new dense kernel calls after the adder
  is certified. These tests do not replace the general proof.
- Thirty-two modular exponents for N=21,a=2 and a 12-step repeated-square chain
  equal the existing actual BRC modular-power outputs. Every selection and
  square column retains its source certificate; no ordinary pow reference runs.
- All 96 readout values across (N,a,t)=(15,2,4),(21,2,6),(15,14,4) produce exactly
  the original BRC postprocessing dictionaries, including every rejection tuple,
  factor list, status and minimal_order_claimed flag. This also preserves the
  bad-base retry path and k=0 behavior.

The final run records 26 actual recurrent_mass_power calls. RESULTS.json lists
each call with state count, depth and elapsed time. CERTIFICATES.json.gz contains
all small and larger arithmetic certificates, with deterministic gzip mtime and
an uncompressed SHA256. MANIFEST.json binds the source and evidence bytes.

No frozen source file was modified. No fresh classical Shor/QFT reference,
trigonometric phase, new precision, factor, minimal order or ideal-success
number was used to construct or validate this result.
