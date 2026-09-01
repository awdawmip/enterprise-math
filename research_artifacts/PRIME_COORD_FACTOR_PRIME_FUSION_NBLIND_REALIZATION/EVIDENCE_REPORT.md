# PCF6 Evidence Report — Prime Fusion N-Blind Composite-Ring Realization

Task: `RS-PRIME-COORD-FACTOR-PRIME-FUSION-NBLIND-REALIZATION`  
Publication: `TP2-064103C123D4486521E7`  
Researcher: `EM-PCF6-79EC8F`  
Claim: `chatgpt-pcf6-20260828-1420-79ec8f`

## 1. Exact ambient N-blind descent

Write the unfactored input modulus as `H` to avoid collision with the source channel `N(a,b)`. Put

- `R_H=(Z/HZ)`,
- `f=X^2+1`,
- `g=X^2+X+1`,
- `F=f g=X^4+X^3+2X^2+X+1`,
- `A_H=R_H[X]/(F)`,
- `T_H=multiplication by [X]` on `A_H`.

This construction consumes only `H`. The integral identity

`(X+1)f-Xg=1`

base-changes to every `R_H`, hence

`A_H ~= R_H[X]/(f) x R_H[X]/(g)`.

For proof-side `H=pq`, ordinary coefficient CRT further gives

`A_H ~= A_p x A_q`.

Thus the **ambient quartic fusion algebra and its multiplication operator are genuinely N-blind and functorial**.

This does not yet recover corrected T10. The corrected object is channel-oriented across the two hidden prime components, while the ambient quartic object retains both polynomial channels at both components.

## 2. Selector/idempotent theorem for the corrected rank-2 mixed carrier

Assume `H=pq` with distinct primes `p,q>3`, with the oriented local Prime Fusion conditions using `f` on `p` and `g` on `q`.

Let `c in R_H` be the CRT selector

`c=0 mod p`, `c=1 mod q`.

Then

- `c^2=c mod H`;
- `gcd(c,H)=p`;
- `gcd(c-1,H)=q`.

Define

`h_c=(1-c)f+c g=X^2+cX+1`

and

`D_c=R_H[X]/(h_c)`.

Proof-side CRT gives exactly

`D_c ~= F_p[X]/(f) x F_q[X]/(g)`.

Moreover its `R_H`-valued root locus is exactly

`{x mod H : f(x)=0 mod p and g(x)=0 mod q}=M_{p,q}`,

the corrected T10 channel-oriented mixed locus.

So a nontrivial selector constructs the desired rank-2 mixed carrier, but the selector itself already splits `H` by one gcd.

## 3. Basis-independent trace extraction theorem

The obstruction does not depend on choosing the displayed companion matrix.

Let `M` be any free rank-2 `R_H` module and `T in End_R_H(M)`. Suppose its proof-side reductions satisfy

- `charpoly(T mod p)=X^2+1`;
- `charpoly(T mod q)=X^2+X+1`.

For a rank-2 operator the characteristic polynomial is

`X^2-tr(T)X+det(T)`.

Therefore

- `tr(T)=0 mod p`;
- `tr(T)=-1 mod q`;
- `det(T)=1 mod p,q`, hence `det(T)=1 mod H`.

Set

`c=-tr(T) mod H`.

Then `c=0 mod p`, `c=1 mod q`, so `c` is the nontrivial CRT idempotent and

`gcd(c,H)=p`.

Conversely, from such a `c`, multiplication by `X` on `D_c=R_H[X]/(X^2+cX+1)` has trace `-c`, determinant `1`, and the required two local characteristic polynomials.

Hence, at exact free-rank-2 operator strength,

`CORRECTED_ORIENTED_MIXED_REALIZATION <=> NONTRIVIAL_CRT_IDEMPOTENT`

with an explicit one-gcd extraction map from the realization to a factor split.

This is the task's load-bearing no-go: the corrected mixed carrier cannot be supplied as a factor-blind constructor input unless the missing `N_ONLY_ASYMMETRY_GENERATOR` has already produced exactly the information needed to split the modulus.

The reverse orientation exchanges `p,q` and the complementary idempotent.

## 4. Ambient synchronization theorem

Because `f=Phi_4` and `g=Phi_3`, the ambient generator satisfies

`T_H^12=I`

for every `H`. If `gcd(H,6)=1`, both channel components have exact operator orders `4` and `3`, so the ambient regular operator has exact order `12`, independent of the hidden factors.

For `1<=k<=12`, let `Delta_k=det(T_H^k-I)`. Exact integral computation gives

- `|Res(f,X^k-1)|=0` if `4|k`, `4` if `k=2 mod 4`, and `2` if `k` is odd;
- `|Res(g,X^k-1)|=0` if `3|k`, otherwise `3`.

Therefore

`|Delta_k|=0` if `3|k` or `4|k`, otherwise `6` for odd `k` and `12` for even `k`.

For any `H` coprime to `6`,

`gcd(H,Delta_k)` is therefore exactly `H` in the zero cases and `1` otherwise. The corresponding field rank defect is

`2*[3|k]+2*[4|k]`,

again independent of the hidden prime.

So the first natural ambient orbit/rank/determinant family is exactly synchronized and yields no nontrivial split.

## 5. Fixed-polynomial determinant no-go

For every fixed `P in Z[X]`, multiplication by `P(T_H)` on the free rank-4 ambient algebra has

`det(P(T_H)) = Res(F,P) mod H`.

The right-hand side is the reduction of one fixed integer `delta_P`.

- If `delta_P=0`, its gcd with `H` is the trivial value `H`.
- If `delta_P != 0`, the only primes it can expose belong to the finite prime support of `delta_P`.

Thus no finite family of fixed, H-independent polynomial-determinant probes on the universal ambient operator can be a universal semiprime separator. This statement does **not** rule out a genuinely H-dependent constructor; it isolates why an additional N-only asymmetry generator is necessary.

## 6. Full-root carrier degeneracy classification

For primes `p,q>3` satisfying the oriented algebraic conditions `p=1 mod 4` and `q=1 mod 3`, the corrected mixed locus always has four roots.

The complete fused root set of `F` modulo `pq` has cardinality

`4(1+[p=1 mod 3])(1+[q=1 mod 4])`,

so only `4`, `8`, or `16` roots can occur.

The full fused root set equals the corrected four-root oriented locus exactly when

`p != 1 mod 3` and `q != 1 mod 4`,

i.e. `p=5 mod 12` and `q=7 mod 12` under the oriented split conditions. Under the source T9 branch coupling, this coincidence subfamily is `p=5 mod 24`, `q=7 mod 12`.

This is only a **root-predicate coincidence degeneracy**. It does not give a general factor-blind channel-labelled rank-2 algebra; outside this subfamily the universal fused root set strictly contains extra roots, and globally the rank-2 carrier still requires the selector/idempotent described above.

## 7. H=91 pressure guard

For the frozen pressure witness `p=13`, `q=7`, `H=91`, the selector is

`c=78`,

with `c=0 mod 13`, `c=1 mod 7`, `c^2=c mod 91`, and `gcd(c,91)=13`.

The selector polynomial is

`h_c=X^2+78X+1 mod 91`.

Its roots are exactly

`{18,44,60,86}=M_{13,7}`,

whereas the full roots of `F` are

`{9,16,18,44,60,74,81,86}`.

This simultaneously checks the corrected T10 universe and the selector theorem.

## 8. Exact checker evidence

Primary checker:

`python scripts/check_prime_coord_factor_prime_fusion_nblind_realization.py`

Authoring-time output:

`PCF6_CHECK_PASS source_pairs=412 public_profiles=412 selectors=412 root_classes=4:144,8:224,16:44 pressure=PASS trace_split=PASS ambient_sync=PASS`

The `public_worker(H)` function accepts only `H`; factors occur only in the external theorem-verifier compartment.

Independent checker:

`python scripts/check_prime_coord_factor_prime_fusion_nblind_realization_independent.py`

Authoring-time output:

`PCF6_INDEPENDENT_PASS algebraic_pairs=432 root_classes=4:144,8:216,16:72 selector_equivalence=PASS fixed_cyclotomic_sync=PASS pressure=PASS`

The second implementation does not reuse the primary 4x4 matrix route; it reconstructs the classification from local cyclotomic roots and CRT.

All finite counts are regression/falsification evidence only. The selector/trace obstruction, ambient CRT decomposition, 12-period synchronization, resultant formula, and root-count trichotomy are exact arguments.

## 9. Exact comparison with the corrected Prime Fusion package

- **T3 fusion algebra:** descends fully and canonically to `A_H`; retained.
- **T4/T5 pointed residue:** not an N-only constructor when the useful pointed root is supplied; once a useful root is present, gcd channel recovery remains exact.
- **T6 reciprocal-trace idempotent:** exact and now exposes the constructor boundary sharply: a useful oriented root produces the split rather than generating itself N-blindly.
- **T8 abstract product shape:** survives proof-side CRT, but channel labels are not recovered by the abstract product alone.
- **T10 corrected oriented mixed locus:** does not descend as a general factor-blind rank-2 carrier; its coefficient/trace is exactly the hidden CRT selector.
- **T11 sixth-power readout:** remains exact for an oriented mixed root; it is a decoder after the asymmetry/root exists, not an N-only source of that root.
- **Ambient rank/orbit/determinant probes:** the universal generator is synchronized; fixed-polynomial determinants reduce to fixed integer resultants.

## 10. Verdict boundary

Primary verdict:

`FUNCTORIAL_REALIZATION_OBSTRUCTED`

Meaning: the universal quartic ambient algebra is N-blind and functorial, but the **corrected channel-oriented rank-2 mixed realization** cannot be functorially selected from unfactored `H` without producing a nontrivial CRT idempotent. Any exact such rank-2 operator exposes that idempotent as minus its trace and therefore yields a nontrivial gcd immediately.

This is not a factoring lower bound, not a proof that no H-dependent factoring algorithm exists, and not a speedup claim. The smallest remaining program object is the same one isolated by PCF1:

`N_ONLY_ASYMMETRY_GENERATOR`, now sharpened to `N_ONLY_NONTRIVIAL_IDEMPOTENT_OR_EQUIVALENT_SELECTOR_GENERATOR` for the corrected mixed-carrier route.
