# Conditional high-density resonance of the aggregate sections

Status: **PURE_SYMBOLIC_DERIVATION / NOT_EXECUTED / NOT_ADMITTED**. Shared author context `EM-DIRECT-C6438C`, activity `RA-CAAAC604CB513AEA8BBC1DFC`. No scientific program, numerical grid, provider query or remote operation was used. This is a conditional positive mechanism, not a completed selector or a general native Shor algorithm.

The frozen inputs are `AGGREGATE_WITNESS_PROBE_AUDIT.md`, SHA-256 `c76465057ce793825916c3d22c85acc83703becfeb5154c05b362468dd5933fd`, and `LOCAL_SECTION_HIT_ANALYSIS.md`, SHA-256 `a7994a9d998f9d07a2662059638f753fd99b0c49cf2334e11d3e35884bbfc8ec`. Both remain unchanged. The moment determinant here is the unstopped modular branch aggregate, not a signed-mode frame/Gram norm correction.

## 1. Exact local zero set when the public clock is +1 or -1

Let p be an odd prime, a in `F_p^*`, `Q=2^t` with `t>=1`, `q=Q mod p`, and `A=a^Q`. Set

`G=G_Q(a)`, `H=G_Q(a^2)`,

`C=a^(-2(Q-1)) (QH-G^2)(QH+G^2)`,

`F_minus=Q(a-1)(A+1)-(a+1)(A-1)`,

`F_plus =Q(a-1)(A+1)+(a+1)(A-1)`.

The prime and the local orders used below are proof variables, not available factor/order inputs. Direct algebra gives

| Clock | F_minus | F_plus |
|---|---|---|
| q=1 | `2(a-A)` | `2(aA-1)` |
| q=-1 | `2(1-aA)` | `2(A-a)` |

For `a!=1,-1`, the already proved division-free identity

`(a-1)^4(a+1)^2 C = a^(-2(Q-1))(A-1)^2 F_minus F_plus`

therefore implies

`C=0 <=> a^Q=1 or a^(Q-1)=1 or a^(Q+1)=1`.       (1)

The exceptional points must be evaluated directly: C(1)=0, while `C(-1)=Q^4=1 mod p` under this clock assumption. In particular -1 is not a zero, although it belongs to the Q-th roots of unity.

For an integer n>0 write `H_n={a in F_p^*: a^n=1}` and `d_n=gcd(n,p-1)`. The exact zero set, including its exceptional points, is

`Z(C) = (H_Q union H_(Q-1) union H_(Q+1)) minus {-1}`.       (2)

Q is even. Consequently the gcd of any two of Q,Q-1,Q+1 is 1: for the outer two it divides 2 but both are odd. Hence the three subgroups intersect pairwise only at 1. Inclusion-exclusion, followed by deleting -1, proves

`|Z(C)| = gcd(Q,p-1)+gcd(Q-1,p-1)+gcd(Q+1,p-1)-3`.        (3)

The usual root count `|H_n|=gcd(n,p-1)` can equivalently be obtained from the polynomial gcd of `X^n-1` and `X^(p-1)-1`; it does not assume an algorithm was given a generator of the field's unit group. Formula (3) is exact for either clock sign and every odd p, including p=3. It is not an approximation from polynomial degree.

Thus in this resonance the extra sections are precisely neighboring exponent conditions. The geometry has specialized to a known algebraic mechanism; it is not an independent new root solver.

## 2. An exact half-density family

Suppose `p=3 mod 4`, and write `p-1=2m` with m odd. Assume

`Q=1 mod p*m`.                                            (4)

Since Q is even and relatively prime to m,

`gcd(Q,p-1)=2`, `gcd(Q-1,p-1)=m`, `gcd(Q+1,p-1)=1`.

The middle equality follows because m divides Q-1 and Q-1 is odd. The last follows because Q+1 is odd and its gcd with m divides 2. Equation (3) gives

`|Z(C)|=m=(p-1)/2`.                                      (5)

More strongly, `H_Q={1,-1}`, `H_(Q-1)=H_m`, and `H_(Q+1)={1}`. Therefore

`Z(C)=H_m = the nonzero quadratic residues modulo p`.      (6)

For completeness, every square satisfies x^m=1 by Fermat's identity. The squaring map on `F_p^*` has kernel `{1,-1}`, hence has exactly m images. This identifies H_m with that image without choosing a discrete logarithm.

There is also a direct coordinate formula. Since Q is even and Q=1 mod m, `Q=m+1 mod 2m`. Let `chi_p(a)=a^m` in `{1,-1}`. Then

`A=chi_p(a) a`,

`F_minus=2a(1-chi_p(a))`.                                (7)

Because q=1, C and F_minus have exactly the same prime support at this component: both vanish precisely when chi_p(a)=1. The other section F_plus has only the root a=1. This is a genuine dense section rather than a low-degree rare-root example.

Condition (4) is sufficient, not asserted necessary. In particular the half-density conclusion does not extend to every horizon, every odd prime, or every integer base without its unit precondition.

## 3. CRT separation, saturation and a useful conditional selection law

First consider a squarefree semiprime `N=p_1 p_2` with distinct odd primes. Fix a horizon for which both local clocks are in `{1,-1}`. For a uniformly sampled unit modulo N, its two reductions are independent uniform units. If `rho_j` is (3) divided by `p_j-1`, then

`Pr(1<gcd(C,N)<N) = rho_1(1-rho_2)+rho_2(1-rho_1)`,

`Pr(gcd(C,N)=N) = rho_1 rho_2`.

If both primes are 3 mod 4 and the same Q satisfies (4) at each, both rho values equal 1/2. The exact probabilities are then

`proper divisor: 1/2`, `saturation: 1/4`, `unit: 1/4`.       (8)

There is a conditional way to avoid that last random separation step. In this semiprime family the Jacobi symbol is

`Jacobi(a,N)=chi_(p_1)(a) chi_(p_2)(a)`.

If it is -1, precisely one component is a square, so (6) guarantees that gcd(C,N) is proper. The same proper divisor is obtained by the much smaller section probe `gcd(a^Q-a,N)`, because (7) has the same local support and N is squarefree. This is a **conditional certificate-selection law**: a factor-blind Jacobi test can select opposite characters, once the required horizon resonance is in force.

This observation reuses quadratic characters and CRT. It does not claim a newly implemented native Jacobi interface, a free random-unit sampler, proof that an unknown input is a semiprime of this form, or a cheap construction of Q. A uniform-unit Jacobi=-1 event has probability 1/2 for this family, but its actual typed computation and retries would still be charged. The final proper-divisor certificate is sound without knowing the promise; the claimed success rate depends on the promise.

For more squarefree components all satisfying the same half-density condition, independent local characters give proper-C probability `1-2^(1-k)` for k distinct primes. A Jacobi=-1 restriction still excludes all-square saturation, but no longer guarantees a proper divisor for every k: when k is odd it permits all k characters to be -1, which gives a unit C. The two-component guarantee must therefore not be generalized silently.

Prime powers need a separate valuation statement. Local zero/nonzero support is still controlled by the reduction modulo p, but the exact gcd can be a partial prime power, and the Jacobi symbol weights prime powers by exponent parity. Equations (8) and the exact semiprime gcd equality above are stated only for squarefree inputs. If two prime-power components have opposite local characters, C is nonunit at one and a unit at the other, which is sufficient for a proper factor, but it need not return that entire first component.

### Why separate section probes can improve on a saturated product

Away from a=1,-1, the three sets in (1) are disjoint. Each component's C-zero therefore has one type: baseline Q, neighboring exponent Q-1, or neighboring exponent Q+1. The clock sign decides which neighboring type is carried by F_minus and which by F_plus.

Under paid unit conditions for a-1 and a+1, the three probes `A-1,F_minus,F_plus` expose those types. If two components both make C vanish but do so in different **probe channels**, one of these separate gcds is proper even though the product gcd is N. If they vanish in the same channel, that channel may itself saturate. This is a concrete benefit of keeping the probes separate; it is not a universal cure for saturation. In the half-density family both dense root sets are in F_minus, so two square components saturate that probe together. Character selection, rather than merely factoring the formula, is what separates them in (8).

## 4. The clock must be tested and its acquisition charged

The hypothesis q=1 at a prime means `p divides 2^t-1`; q=-1 means `p divides 2^t+1`. Before attributing a factor to C, the same already computed public clock q permits the two direct tests

`gcd(q-1,N)`, `gcd(q+1,N)`.

If only one component has the tested sign, its proper factor has already been exposed. If the two components have opposite signs, these tests already separate them. The independent benefit of the aggregate section can therefore lie in **synchronized same-sign resonance where the clock gcd saturates**, or outside the present clock-resonance theorem. Omitting the clock tests would hide information already paid for.

For odd N, a fully saturated positive clock `2^t=1 mod N` is equivalent to `ord_N(2)` dividing t. A fully saturated negative clock requires that this order r be even and that `t=r/2 mod r`; in particular r divides 2t but not t. For composite N these negative-clock conditions are not sufficient alone: one also needs `2^(r/2)=-1 mod N`. The order-two element of the cyclic subgroup generated by 2 may instead have mixed CRT signs. These are schedule constraints, not available order inputs.

In the half-density construction, `p*m` is odd. Thus a positive t satisfying (4) exists: any multiple of `ord_(p*m)(2)` works. For several such primes a common multiple of their corresponding orders works. Those moduli/orders contain unknown factor information. The theorem gives no cheap method for obtaining such t and does not even promise that finding it is easier than the target problem.

Moreover the fixed dyadic recurrence forms `a^(2^t)` through t modular squarings. An integer t with a short written description is not automatically a short execution of those t updates. Computing the separate clock `2^t mod N` may use an exponent-t binary method, but that does not compute `a^(2^t)` in the same number of steps without further justified structure. Every search horizon, squaring, gcd, failed clock and saturated event belongs in the cost.

This explains the relationship with the previous low-degree bound. Here Q is necessarily large enough that the useful half-density is compatible with that bound. Compact high-degree sections can indeed be dense. The open issue is selecting a useful compact section at a useful cost, not whether such sections can exist.

## 5. Arbitrary interval lengths are a separate, honest extension

The T1 interval family `[0,Q)` can be considered at even Q other than powers of two; a separate arbitrary-horizon bridge is being derived by the other author. No implementation or execution of that bridge is claimed here. Pure substitution already identifies a useful limit of that route.

For odd N, choosing Q=N+1 forces q=1 modulo every component, and Q=N-1 forces q=-1. This removes the need to discover a dyadic clock resonance. The factor channels then reduce, up to certified unit factors and signs, to the neighboring ordinary exponent probes:

| Chosen Q | Baseline | Two extra channels |
|---|---|---|
| N+1 | `a^(N+1)-1` | `a^N-1`, `a^(N+2)-1` |
| N-1 | `a^(N-1)-1` | `a^N-1`, `a^(N-2)-1` |

The baseline/section union statement retains the a-1,a+1 unit qualifications or must handle those exceptional points separately. For example at Q=N+1, `F_minus=-2a(a^N-1)` and `F_plus=2(a^(N+2)-1)`; at Q=N-1, `F_minus=-2(a^N-1)` and `F_plus=2a(a^(N-2)-1)`.

Thus forcing the public clock is a valid construction, but it does not force component separation. It produces familiar power-gcd tests whose local root counts need their own analysis. In particular a globally forced identity can give gcd N rather than a divisor. No half-density claim follows merely from Q=N+1 or N-1.

## 6. Native-tool consequence and remaining gap

The new positive statement is exact: a lawful aggregate section can have half of all local units as roots, and synchronized components can still be separated by a proper-divisor observation. Once the stated resonance is available, the full determinant can even be replaced by a smaller neighboring-exponent section for the declared squarefree family. This is an algebraic simplification of the witness interface, not full-law preservation or orbit compression.

The outstanding tool requirement is correspondingly concrete: construct or recognize a useful factor-blind horizon/section, with all schedule acquisition costs, and prove a component-separation rule under an explicitly stated input class. A native implementation must retain clock-gcd outcomes, candidate selection, all typed section/gcd costs, failures and saturation. Existing geometry supplies the correct section identities; it does not supply the missing selector. Quadratic-character/CRT reasoning and exponent gcds are **REUSE**, and their proposed integration with the native aggregate interface is an **EXTENSION CANDIDATE**, not a new classical theorem or an admitted BRC Shor completion.

The exact zero-count formula, half-density subgroup identification and two-prime Jacobi selection were additionally checked symbolically by the shared-context peer. No independent formal admission or scientific execution is asserted.

Global-Knowledge-Sync: main@7a63984 / GLOBAL_KNOWLEDGE_V1.
