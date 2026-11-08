# PREFIX-577 R6 — universal 29-state native all-start gate observer and exact 96-port rank dichotomy

Date: 2026-11-08 UTC. Scientific pin (unchanged): `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Scientific state: **AUTHOR_PROVED / EXACT_INTEGER_POLYNOMIAL_VERIFIED / UNREVIEWED / NOT_ADMITTED**. This is author-side portable BRC-X6 science, not a canonical Source CLAIM/Result/Review.

## Statement (original 96 native ports, six tagged actions per port)

Keep 576 native tagged actions, the six original spatial reward axes and separate ordered time. Under independent uniform selection of the native tagged actions, consider the **passive** law of first-gate waiting time and cumulative fifth/sixth rewards, for *any* initial native port. The prior label-derived exact 37-class passive quotient has nongate weighted matrix `C(x,y)` and gate column `g(x,y)` over `Z[x,y]`; its mapping from 96 original ports to 37 quotient classes is preserved.

Let `Q(t,x,y)=sum_{k=0}^{28} q_k(x,y)t^k` be the inherited exact reset-specific degree-28 polynomial (coefficients in `GENERIC_DEGREE28_CERTIFICATE.json`, prior author note commit `a3e9f095d92bd31d2ffcd6b3a40ccb733b137751`). Define the full 37-component vector `h=sum_{k=0}^{28} q_k C^(28-k) g`.

**NEW, EXACT over Z[x,y]:**

```text
C h = 0  [every one of 37 polynomial components].
h_12=h_17=h_21=H != 0,  h_34=h_35=h_36=-H,
all other h_class=0.
```

Thus the previous `Q` scalar recurrence begins at residual index 29 for **every starting native port**. At index 28 it holds for exactly **90 of 96** native starting ports; the exceptional six are ports `{6,7,28,29,30,31}`.

## Exact 29-state universal integral-polynomial realization

Form `D=[g, Cg, ..., C^28 g]` (37 by 29). Define explicit `A` (29 by 29) by `A[i+1,i]=1` for `0<=i<28`, `A[i,28]=-q_(29-i)` for `1<=i<=28`, `A[0,28]=0`, and all unspecified entries zero. The exact vector identity immediately proves

```text
C D = D A                in Z[x,y]^(37×29).
s_n(alpha) = pi(alpha) C^n g = pi(alpha) D A^n e_0,
F_alpha(z,x,y)=(z/6) pi(alpha) D (I_29-(z/6)A)^(-1) e_0
for every native initial distribution alpha and all n>=0.
```

Here `pi(alpha)` is the native 96-to-37 class aggregation. The native carrier still retains all port, action, and six-axis data for observations outside this *declared passive first-gate interface*. This is a signed polynomial **linear** realization, not a positive 29-port Markov partition.

The 29 is **optimal over Q(x,y)** for simultaneous arbitrary native starts. At `(x,y)=(2,3)` over `F_1000000007`, a 29-by-29 minor of `D` (row indices `[34,1,3,8,4,2,6,9,5,10,7,15,12,16,14,19,13,20,18,22,17,23,24,28,25,29,30,0,31]`) has exact nonzero determinant

```text
726423349 mod 1000000007.
```

This proves `rank_{Q(x,y)}(D)=29`; the displayed `A` realizes the same observation in 29 states.

## Complete 96-port minimal linear rank classification

The exact polynomial annihilator/recurrence supplies generic **upper** bounds: rank <=28 for every native port except the six exceptional ones, rank <=29 for those six. Independent native-original-96-port modular Hankel ranks provide matching generic **lower** bounds for all 96 ports. Consequently:

```text
minimum generic Q(x,y)-linear scalar first-gate realization dimension:
  29 for native ports 6,7,28,29,30,31;
  28 for each of the other 90 original native ports.
```

At `(x,y)=(2,3)` mod `1000000007`, all 90 ordinary ports have exact 29-by-29 Hankel rank 28. For the six exceptions, the leading 29-by-29 Hankel determinants are respectively:

```text
p6=556409011, p7=908654658,
p28=327325002, p29=812356477,
p30=848383685, p31=491179466  (mod 1000000007).
```

The exact old reset-port-9 28-by-28 Hankel determinant is `595325725` modulo the same prime. Generic rank follows because each modular nonzero minor witnesses a nonzero integer-coefficient polynomial determinant, while the upper bounds hold symbolically over `Z[x,y]`. Minimal *linear state dimension* and reduced rational denominator degree need not coincide for the six exceptional initial ports, whose gate histories have a one-step transient.

## Reproducible author verification

- `prove_universal_observable29.py` constructs all 37 exact integer-polynomial columns `g,...,C^29g` and verifies `Ch=0`, the six-class sign pattern, `CD=DA`, and the nonzero 29-by-29 minor.
- `verify_universal29_native.py` regenerates all 576 **original native labelled edges** independently and tests 96 starts × 73 lengths × four modular reward specializations `(2,3),(3,2),(7,11),(1,1)`: all **28,032 exact modular comparisons** pass.
- `classify_native_port_hankel_ranks.py` checks all 96 individual native Hankel ranks and the six nonzero exceptional determinants.
- Independently extracted portable bundle re-executed all five new/prior scripts successfully (native96 kernel, original 37-class passive quotient and earlier exact Q coefficients included).

Exact symbolic universal29 certificate SHA-256: `60d2f6e5365a98ddb9615a064ce82cbcf7ae931871479ff7d329837ec80b9893`.
Exact 96-port rank classification certificate SHA-256: `df59b5e078fc05db43bcebd289e5695d070ba52873412b5c4bdcfa7b3e6f5fcc`.
Complete portable 14-file ZIP SHA-256: `9546667e4261a9b3f19481a1f8e6d41dc5a15bb3fbe0838ef1c716c7cb5bc498`.

**BRC contract:** `REUSE_EXECUTED` frozen native96 tag-preserving carrier, 37-class passive exact quotient, 28-degree coefficient certificate. `CD=DA` supplies exact future-operation safe descent for the all-start passive gate observer. It preserves the original native 96-port substrate for action-conditioned and full-six-axis operations.

**Canonical and provenance frontier:** D25 task publication `TP2-B6F4FC938FF94941C1B7` retains real same-original-class H0/B0 divided-power, `[X]U mod p^2`, Frobenius direction/eta and CM validation as unresolved; this note acquired no current Source execution owner. UR V2 four-file original is still missing (expected 94687 bytes, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`); no substitute bundle is labelled as original.

**Next question:** classify minimal-order linear factors for *mixtures* of initial ports and their interaction directions, including how the six exceptional ports cancel or reinforce each other under the exact observable `h`. Keep six-axis native information and action choice in the original carrier.
