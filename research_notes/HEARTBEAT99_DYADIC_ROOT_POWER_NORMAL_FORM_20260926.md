# Heartbeat99 — 同一实际根的整次幂、二进约分正规形与精确位长下界

Progress-Event-ID: HEARTBEAT99-DYADIC-ROOT-POWER-NORMAL-FORM-20260926-61d81400
Status: AUTHOR_SYMBOLIC_DERIVATION / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED
Global read: 61d81400bf3aa69ae147afbfef5cb47ccabff7dd
Source read and publication preflight: 51b7e237c1b7aaeebcbe7b7781fa31e62c327625
Symbolic parent: 6cc27a05bc0e4ab50b9ee9f7f8995f62563eb2dc:research_notes/HEARTBEAT98_ORDERED_LOW_RANK_WORD_20260926.md (blob ab90e40498ce3d953e5e201aa888e8090d67abef)
Last executable parent, as recorded: Stage97 cumulative 2b1821fa01a89eb4f0f45d99ba8bfab2a003fd42.
Inherited contribution provenance: HB90-0de6b47ad07848a1b6e8347fd5156ca6; only historical/local contribution provenance, not an authenticated platform or service identity.
Research-Activity-ID: not obtained; REGISTER_PENDING. No session/CLAIM or independent-review identity is borrowed. This note is neutral research preservation, not a formal Result or mathematical admission.

## 0. Actual progress and execution boundary

The present container.exec, python.exec and python_user_visible.exec administrative/file-check attempts all returned ClientError. No successful local file verification, new scientific BRC call, complete-basis run, Shor regression, package construction, numerical benchmark or bundle readback occurred. Files.search on the supplied Stage97 ZIP returned no indexed matches and Files.read returned no readable archive content. These failures do not establish that the original package is corrupt or missing. Its root coefficients have NOT been re-extracted or revalidated in this turn.

This is a new symbolic specialization of the exact actual-gate identity preserved in Stage98, not execution of that adapter. Stage98's two-pass-to-one-pairing formula is inherited, not rediscovered. The new results are: an exact two-integer norm algebra for every same-root power; a normalized recurrence that removes known common powers of two before forming a direction; the exact least dyadic denominator of the full power matrix under explicit primitive hypotheses; a finite-order classification of this reflection-pair family; and a scoped H4 word-length lower bound.

P000 six native spatial axes and separate time remain unchanged. An internal linear plane, matrix dimension, exponent h or algorithmic step is not a spatial axis or calibrated heartbeat. The complete 61-mode carrier, source labels, fixed gate order, CF-only rules, random-source and failure semantics remain unchanged. Born-type readout and ideal Shor targets remain BORROWED_REFERENCE. No trigonometry, pi expansion, numerical matrix exponential, ordinary numerical propagator or new ideal QFT run is used. All computations below are symbolic identities of the inherited BRC gate; their executable integer/pairing realization remains pending.

## 1. Exact model and separation of data from operations

Let e=e0, z in Z^d, S=2^B, z^T z=S^2, with d>=2. The mother line has d=61. Write

    a = z0,   n = z-a e,   n0=0,   H=n^T n=S^2-a^2.
    F(v)=2 v v^T-I  for a unit vector v.
    W=F(e) F(z/S).

This is the actual reflection-pair identity, including all components of n, not a replacement by a named ideal angle. Both factors are kept. The complete operator is identity on span(e,n)^perp; a state in that complement must not be deleted.

All statements about an original fixed bank are conditional on actually verifying this carrier identity and exact input z,S. Numerical values of B, nu_2(a), or their primitive reduction for the frozen W4 are not asserted from a stage name or remembered approximation. Common-factor normalization of z,S is a representation operation, not normalization of a physical/probability state.

## 2. Two-integer exact norm algebra for an arbitrary power

Define integer pairs (A_h,B_h) for h>=0 by

    (A_0,B_0)=(1,0),
    (A_1,B_1)=(a,1),
    A_(h+1)=a A_h-H B_h,
    B_(h+1)=A_h+a B_h.                            (1)

For pairs define

    (A,B) star (C,D) = (AC-H BD, AD+BC).           (2)

A direct expansion shows that the norm A^2+H B^2 is multiplicative under (2). Consequently

    A_h^2+H B_h^2=S^(2h),
    (A_(h+k),B_(h+k))=(A_h,B_h) star (A_k,B_k).   (3)

No square root or angle is required. The unit direction

    w_h=(A_h e+B_h n)/S^h                         (4)

satisfies

    W^h = F(e) F(w_h).                           (5)

Proof of (5): on coordinates (x0,c) in span(e,n), the metric is diag(1,H). Put

    M(A,B)=[[A,H B],[-B,A]].

These matrices multiply by the pair law (2). The restriction of F(e)F(w_h) is M(A_h,B_h)^2/S^(2h), whereas W restricts to M(a,1)^2/S^2. Equation (3) proves (5) on the plane. On its orthogonal complement both sides are identity. Degenerate H=0 is directly handled by W=I.

For h=2, (A_2,B_2)=(2a^2-S^2,2a), and the new direction is exactly

    w_2=(2a z-S^2 e)/S^2.

Thus the Stage98 W^2 formula is recovered without altering the actual gate. This is an algebraic consistency proof, not a newly executed comparison.

A binary addition chain can form the pair using O(log h) pair compositions. Its coefficients need not have O(log h) bits. No exact periodic reduction of h is authorized by the ideal phase label.

## 3. One full tail pairing for the entire same-root block

For a complete input row x, compute once

    q=n^T x,     L_h=A_h x0+B_h q.

Then (5) gives

    (W^h x)0 = -x0+2 A_h L_h/S^(2h),
    (W^h x)i = xi-2 B_h n_i L_h/S^(2h), i>0.     (6)

Only the one complete pairing q is needed after the power coefficients have been constructed. Original x is retained in every coordinate. The complete signed n, not merely its norm or its first few entries, is used.

The actual inverse is obtained by B_h -> -B_h with A_h and S^h unchanged, equivalently transposing the actual matrix. Therefore W^h W^(-h)=I exactly. This does not imply W^h=I at any nominal ideal period.

This is an operator representation. It does not reduce the full state to x0,q. For x0=q=0, the correct output is the original nonzero x. Whole-block contraction is allowed only with the same control condition and no intervening operation that changes the block semantics. A measurement, change of controlling register, different noncommuting root, or unaccounted source encoding breaks this shortcut unless separately proved safe.

## 4. Primitive dyadic normal form before constructing long coefficients

For the nontrivial denominator theorem, first remove the common power of two of all entries of z and of S. Assume henceforth z is 2-primitive: at least one entry is odd, S=2^B, and 0<|a|<S. Let

    nu=nu_2(a),      c=a/2^nu (odd),
    kappa=B-nu-1.

The main case is kappa>=1. Define

    lambda=2^(2 kappa),
    Delta=H/2^(2 nu)=4 lambda-c^2>0.

Use two NORMALIZED integer sequences, distinguished from the raw pair:

    p_0=2, p_1=c;     q_0=0, q_1=1;
    f_(h+2)=c f_(h+1)-lambda f_h,
    for f=p and f=q.                             (7)

They satisfy

    p_h^2+Delta q_h^2=4 lambda^h.                 (8)

For every h>=1, p_h and q_h are odd. Indeed p_1=c, p_2=c^2-2lambda, q_1=1 and q_2=c are odd; lambda is even, so (7) preserves oddness.

The connection to the raw pair is exact:

    A_h=2^(h(nu+1)-1) p_h,
    B_h=2^((h-1)(nu+1)) q_h,       h>=1.         (9)

One proof is to eliminate the other coordinate in (1), obtaining f_(h+2)=2a f_(h+1)-S^2 f_h for both raw sequences. Dividing by the factors in (9) gives (7) with the stated initial values. Equation (8) then follows from (3).

Thus no need exists to construct those common powers only to divide them out afterwards. Set

    z_h=2^nu p_h e+q_h n,
    S_h=2^(nu+1+h kappa).                         (10)

Then z_h^T z_h=S_h^2, and

    w_h=z_h/S_h,
    W^h=F(e)F(z_h/S_h).                           (11)

The vector z_h is 2-primitive. There is an odd tail entry of n: if a is even, primitive z forces one; if a is odd and B>=2, n^T n=S^2-a^2 is odd, also forcing one. Since q_h is odd, that tail entry remains odd in z_h.

The raw vector A_h e+B_h n has EXACT common 2-adic valuation (h-1)(nu+1), not merely at least that value. This proves both the allowable early cancellation and its endpoint. For h=0 use W^0=I separately; (10) still represents e but is not primitive then.

Normalized pairs also have an exact composition formula:

    p_(h+k)=(p_h p_k-Delta q_h q_k)/2,
    q_(h+k)=(p_h q_k+q_h p_k)/2.                  (12)

The halves are exact integers for these certified sequences. This is a candidate BRC pair-composition/valuation adapter, not permission to replace it with an unrecorded numerical matrix routine.

## 5. Exact least matrix denominator: a lower bound, not a storage guess

For a dyadic rational matrix M define

    lde_2(M)=min{j>=0 : 2^j M has only integer entries}.

For the primitive hypotheses in section 4 and every h>=1,

    lde_2(W^h)=2(nu+1+h kappa)-1
             =2B-1+2(h-1)kappa.                  (13)

Proof: let b_h=nu+1+h kappa, so S_h=2^b_h. Every entry of F(e)F(z_h/S_h) has denominator dividing 2^(2b_h-1). Choose j>0 with n_j odd. As q_h is odd, (z_h)_j is odd, and

    (W^h)_(j,j)=1-2(z_h)_j^2/2^(2b_h).

Its numerator over 2^(2b_h) is 2 times an odd integer, hence has EXACT 2-adic valuation one. That one entry needs denominator 2^(2b_h-1). This matches the upper bound and proves (13).

Consequences:

- The denominator exponent grows linearly with h for kappa>=1 even though the active plane remains fixed.
- This concerns the actual reduced matrix in the original coordinate basis, not an unnecessarily multiplied denominator in a particular program.
- The legal basis input e_j above attains this denominator in an output coordinate. Therefore an explicit exact raw-vector evaluator has this worst-case output bit requirement.
- It does not say every input or every actual Shor trajectory attains the bound. Complement states remain unchanged; cancellations in particular inputs can lower their denominators.
- It is not a lower bound on all symbolic or encoded descriptions: the original word W^h can be stored by W and h. Asking for exact numerical coordinates later must still produce their actual precision. Exact symbolic description is not the same cost contract as expanded output.

In the common conditional case a odd, nu=0 and (13) becomes

    lde_2(W^h)=2h(B-1)+1.                          (14)

For illustration, B=2 gives exponents 3,5,7,... for h=1,2,3,... . This is an algebraic specialization of the theorem, not a new bank instance, BRC execution or Shor benchmark. The actual frozen root's primitive B and nu have not been extracted in this turn, so no frozen 5409-bit output denominator is revised.

## 6. Finite-order classification within this dyadic reflection-pair family

For a/S dyadic and the same exact reflection-pair W, its finite order is completely classified:

    |a|=S:           W=I;
    a=0:             W has order 2;
    |a|=S/2:         W has order 3;
    all other cases: W has infinite order.           (15)

Proof: |a|=S forces n=0. If a=0, e and w are orthogonal, and W is -I on their plane and I on its complement. If |a|=S/2, the plane restriction has determinant one and trace -1; its quadratic identity is R^2+R+I=0, so W^3=I, with W not identity. In all remaining cases, primitive reduction has kappa>=1: a reduced dyadic number strictly between -1 and 1 whose denominator is two is only +/-1/2. Formula (13) then gives lde_2(W^h)>0 for every h>=1, excluding W^h=I and all finite periods.

This classification does NOT apply to every separately synthesized dyadic orthogonal gate. In particular, a separately implemented integral quarter-turn is not required to be a single pair of this special form with a dyadic unit direction. It does not change P000 or make a statement about primitive physical angles. A gate's ideal phase index is not its actual finite order.

## 7. Scoped fixed-alphabet word-length consequence

Take the logical alphabet consisting of coordinate H4=H tensor H operations, integral sign operations and permutations, with the same original input/output coordinates. A product using g H4 operations has every matrix entry in 2^(-g) Z. Hence any exact such realization of W^h must satisfy

    g >= lde_2(W^h)
      = 2B-1+2(h-1)kappa.                         (16)

The same entry argument applies to extra zero-initialized clean ancilla coordinates: the effective input/output matrix is a submatrix of the full circuit. Any additional nonintegral encoding/decoding or nonzero prepared rational resource must be separately included; (16) does not grant free encoders or bound a different primitive alphabet.

Thus replacing h serial applications in a classical evaluator by one pairing does not make their exact clean H4 realization a one-gate physical operation. The explicit matrix requires linearly growing denominator exponent and correspondingly many denominator-bearing H4 factors in this alphabet. This is not an optimal synthesis count, not a bound on approximate synthesis, not a factorization lower bound, and not a quantum-speedup claim.

## 8. Precise executable follow-up, still pending

The unfinished Stage98 execution unit is preserved, not declared complete. When the actual local runtime is available:

1. Revalidate supplied Stage97 bundle bytes and the canonical BRC source pin before interpreting the frozen W carrier. Extract actual z,S; record primitive reduction, nu and kappa. Do not assume a is odd.
2. Use the inherited signed BRC pair/linear-column extension to certify z^T z=S^2, n, H and the raw/normalized recurrences. Add special-case branches from (15) instead of applying (13) outside its hypotheses.
3. Start with h=2. Compare the Stage98 formula, (1)-(6), and the normalized (7)-(11), against two calls to the original actual root on all 61 basis columns and declared complete signed rows. Compare exact rational outputs and original canonical denominators, not merely norms.
4. Extend to a bounded declared exponent set, inverse, controlled blocks and source-bound order. Check (13) using an actual odd tail diagonal, including nu>0 synthetic valid carriers. A symbolic identity test is not a fresh Shor experiment.
5. Only after the adapter is verified, inject it without changing the original sampler/CF/field rules. Re-run all frozen low-bit inputs, every compared prefix and child, final complete 61-mode states, canonical denominators, tails, probabilities, failures and interrupted-random-source recovery.
6. Measure coefficient construction, pair count, row materializations, raw and reduced bit lengths, cache cost and total time separately. Physical root-word multiplicity remains h. The expected denominator lower bound may prevent some proposed bit savings even where pairing count improves.

Mandatory negative controls: dropping the original x; dropping tail coordinates; applying the nu=0 formula when a is even; applying the nonperiodic formula in the order-3 case; reducing powers modulo an ideal phase index; crossing a measurement or changed control boundary; using equality of norm/readout as equality of full state; and writing numerical pending items as PASS.

No executable adapter is claimed here. No actual large root coefficients, new output fractions, timing advantage or changed Shor precision certificate have been computed. The parent model-to-ideal certificate remains only an inherited record, not a new regression result.

## 9. Prior work and precise claim scope

Second-order polynomial recurrences and norm algebras are established mathematics, not a general novelty claim. NIST DLMF 18.9 supplies classical recurrence background. Amy, Glaudell, Li and Ross, Improved Synthesis of Toffoli-Hadamard Circuits (arXiv:2305.11305), explicitly discuss dyadic orthogonal matrices and H tensor H synthesis. Only official HTML/abstracts were read for background; no PDF full-text or exhaustive novelty audit was performed. No Chebyshev/trigonometric function was numerically evaluated, and no external synthesis program replaced BRC.

Background: https://dlmf.nist.gov/18.9 ; https://arxiv.org/abs/2305.11305 .

The concrete new derivation is the exact same-root recurrence specialized to the inherited complete reflection pair, its primitive dyadic cancellation law, least-denominator equality (13), finite-order boundary (15), and clean fixed-alphabet consequence (16). Those results separate compression of operations from state erasure and from intrinsic exact-output precision. All are same-author symbolic claims awaiting independent review. Scientific BRC calls this turn: 0. New Shor regressions: 0. Local validation: unavailable/pending. Project-text publication does not establish execution or admission.
