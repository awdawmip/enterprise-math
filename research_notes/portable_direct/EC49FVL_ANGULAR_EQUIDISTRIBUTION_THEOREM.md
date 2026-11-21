# EC49FVL — Angular equidistribution and mesoscopic locality of certified rational-phase exclusions

Date: 2026-11-21 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED / NOT_ADMITTED.

## Source, preservation and mother question

This is an independent portable-research continuation of EC49FVK, frozen science BRC16943. Its source is:
- EC49FVJ/FVK Draft PR #2886, exact head 34284e2c73c711c3ae80e53e762051b76c01b6cd.
- EC49FVJ_FOUR_PRIME_PROJECTIVE_PHASE_THEOREM.md; EC49FVK_REDUCED_RATIONAL_PHASE_DENSITY_THEOREM.md at that commit.
- EC49FVJ_FOUR_PRIME_PROJECTIVE_PHASE_VERIFY.py and EC49FVK_PRIMITIVE_PHASE_DENSITY_VERIFY.py at that commit.
- The derived Bernoulli observation is the same rational-width likelihood ratio t(x)=log R(x)/log S(x). No change to input constants, finite-field predicates, Source firewall, P000 or ACTIVE Heartbeat World native X6 ontology. This is a scalar *observer* readout from the fixed substrate, not a claim that a one-dimensional continuum is a new native spatial primitive.

EC49FVK proved that four projective prime certificates p in {11,17,19,31} exclude the exact fraction δ=36018427/39813120 of distinct reduced rational phase values, asymptotically under denominator height. It left open whether that certified density holds near a prescribed phase or in a shrinking phase interval. We settle both questions at a quantified asymptotic scale.

## Definitions

Write q=h/(h+n) with h,n positive integers and gcd(h,n)=1, and let H be a positive integer. This is a one-to-one correspondence with 0<h/k<1 reduced and k=h+n≤H.

Let P_H(I) count such primitive (h,n) with q∈I, and let N_H(I) count those whose ordered exponent pair satisfies at least one of the four EC49FVJ projective certificates. Every member of N_H(I) is certified not to equal t(x) for **any** rational x∈(0,1).

The four predicates are periodic in (h,n) modulo

    Q=lcm(10,16,18,30)=720,
    M=720·11·17·19·31=79,302,960.

For a residue vector r∈(Z/MZ)^2 let it be *primitive-admissible* when no prime dividing M divides both its components. Denote all such residues by A_M, and the subset satisfying at least one four-prime certificate by S_M. The exact finite CRT and primitive mask calculation from EC49FVK gives

    δ=|S_M|/|A_M|=36018427/39813120=0.9046873744132587...

This is a *certified exclusion* probability, not the density of all mathematically impossible phase values.

## Theorem — uniform angular distribution in all intervals

For every real interval I=[a,b)⊆[0,1], write w=b-a. Uniformly for all choices of a,b (even if they depend on H),

    N_H(I) = δ · (3/π²) · w H² + O_M(H log(2H)),                 (1)
    P_H(I) =     (3/π²) · w H² + O_M(H log(2H)).                 (2)

In particular, if F(H)=sum_{k=2}^H φ(k)=P_H([0,1)) is the number of reduced rational phases and E(H)=N_H([0,1)), then

    sup_{0≤a<b≤1} | N_H([a,b))/F(H) - δ(b-a) |
       = O_M(log(2H)/H),                                      (3)

and, for sufficiently large H,

    sup_{0≤a<b≤1} | N_H([a,b))/E(H) - (b-a) |
       = O_M(log(2H)/H).                                      (4)

Thus the empirical distribution of *certified* excluded rational phases converges to the uniform Lebesgue measure on (0,1), not merely to a global density. It is uniform in interval placement.

**Shrinking-window corollary.** For any sequence I_H⊆(0,1) of intervals of length w_H with H w_H/log(2H)→∞, uniformly in the position of I_H,

    N_H(I_H)/P_H(I_H) = δ + O_M(log(2H)/(H w_H)) → δ.         (5)

A surviving value is not thereby proven attainable by any rational width; the assertion concerns this specific set of finite-field certificates.

## Proof

**Geometric lattice count, uniform in sector.** Let K_T(I) be the real triangle
    { (u,v)∈R² : u≥0, v≥0, u+v≤T, a≤u/(u+v)<b }
(with origin and endpoint conventions immaterial to the error). It has area wT²/2. It is a convex polygon with vertices 0, T(a,1-a), T(b,1-b), and perimeter bounded by an absolute constant times T, independently of a,b.

For any fixed residue r modulo M, the number of positive integer pairs in K_T(I) congruent to r is
    w T²/(2M²) + O(T/M+1).                                    (6)
The estimate follows by scaling the translate of the lattice M Z² and bounding its boundary-intersecting fundamental squares; boundary length is O(T), uniformly in the angular endpoints. It remains valid for degenerate narrow sectors, because the same boundary estimate covers them.

**Primitive condition within a fixed admissible class.** Fix r∈A_M. Any common divisor d of an integer pair in class r is necessarily coprime to M. Apply Möbius inversion over d and the invertibility of d modulo M:
    C_H(r,I) =
      Σ_{1≤d≤H,(d,M)=1} μ(d)
      # { (u,v)∈K_{H/d}(I)∩N² : (u,v)≡d^{-1}r mod M }.
The ratio u/(u+v) is unchanged under scaling by d. Substitute (6) and sum the errors:
    C_H(r,I)
     = wH²/(2M²) Σ_{(d,M)=1} μ(d)/d²
         + O_M(H log(2H))
     = wH²/(2M²) ∏_{p∤M}(1-p^{-2})
         + O_M(H log(2H)).                                  (7)
Replacing the finite d sum by its infinite product causes O_M(H) additional error. All bounds are uniform in I. Classes outside A_M contain no primitive pair.

**Exact certified density.** Sum (7) over S_M, then over A_M. Because
    |A_M|=M² ∏_{p|M}(1-p^{-2})
and
    ∏_p(1-p^{-2})=1/ζ(2)=6/π²,
we obtain
    N_H(I) = (|S_M|/|A_M|) wH²/(2ζ(2)) + O_M(H log(2H))
           = δ·(3/π²)wH²+O_M(H log(2H)),
and the same formula with δ=1 for P_H(I). This proves (1)–(2).

For I=[0,1) the primitive total is F(H)=3H²/π²+O(H log(2H)) and E(H)=δ·3H²/π²+O_M(H log(2H)). Divide (1) by F(H), or by E(H), to obtain (3)–(4). Both suprema inherit the interval-uniform errors.

Finally, divide (1) by (2) for any w_H satisfying H w_H/log(2H)→∞; the main term w_H H² dominates the uniform error. This proves (5). QED.

## Exact crosscheck (not the asymptotic proof)

EC49FVL_SECTOR_EQUIDISTRIBUTION_VERIFY.py uses only Python stdlib integers and Fraction and independently reconstructs the EC49FVJ four-prime finite-field patterns from the *frozen* rational inputs. It verifies all sixteen primitive mask counts over 331,776 base pairs modulo 720 and exactly recomputes δ. It enumerates every reduced h/k for k≤100,300,600,1000, testing all four certificates, and partitions [0,1) into thirds via j=min(2,3h//k). It does **not** use floating point to decide certification or sector membership.

Selected exact counts, expressed as certified/primitive within the successive sectors [0,1/3), [1/3,2/3), [2/3,1):
- H=100: 921/1015, 921/1012, 927/1016; total 2769/3043.
- H=300: 8249/9130, 8257/9136, 8262/9131; total 24768/27397.
- H=600: 32987/36501, 32907/36496, 33030/36502; total 98924/109499.
- H=1000: 91687/101399, 91582/101392, 91715/101400; total 274984/304191.
- Exact CRT density δ=36018427/39813120; verifier terminal result: ALL PASS.

These finite-H proportions are visibly not identical and do not themselves prove (1)–(5). The proof is the elementary uniform primitive-lattice-point argument above together with the previously established projective predicate periodicity and exact mask density.

## What is genuinely new, scope and next

New relative to EC49FVK: (i) an angular-uniform discrepancy theorem, (ii) convergence of the *conditional* empirical distribution of certified phases to uniform Lebesgue measure, and (iii) a moving/shrinking angular-window theorem with the sufficient scale w_H≫log H/H. These are facts about the exact four-prime certificate subset, not about all impossible rational phases and not a new native X6 geometry. They invoke the frozen EC49FVJ/FVK finite-field exact computation as an explicit load-bearing dependency.

Open questions:
1. Derive useful **explicit** discrepancy constants, not merely a fixed-modulus O_M, for practical H. M is large, so the theorem alone promises no short-range effectiveness at H≈1000.
2. Determine whether a stronger arithmetic cancellation gives an interval scale below log H/H for this specific certificate set.
3. Expand prime-local certificates, or find an actual rational-width realization among the uncertified ~9.531% of reduced phase values.
4. Independently audit the FUQ/FUR compound minimax transfer; until then this is only a theorem about the frozen derived Bernoulli observer.

GitHub publication alone does not establish a formal CLAIM, Result, independent Review, or mathematical admission.
