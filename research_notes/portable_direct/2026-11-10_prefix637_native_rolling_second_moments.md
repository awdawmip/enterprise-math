# PREFIX-637 — Native BRC multi-pattern sliding first/second moment queries

**Status:** Author-side exact theorem and executed Python experiment, 2026-11-10, pending independent review. **Context:** `RS-X6-NATIVE-ROTATION-DYNAMICS`; this is not a formal Result or CLAIM. **Frozen science:** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. P000 V5 and the six native signed axes are unchanged. The calculation uses the restricted typed *positive labelled BRC* carrier: 48 STAR phases, 96 ports and 576 original numbered actions. Four-point probe `d=e4+e11+e14+e32`, intensity `lambda>0`, finite window starting `t>=4`, nonnegative rational gates including zero. Signed amplitude and physical time are separate types.

## Exact theorem: exponential-jet transfer for joint count moments

Fix `p>=1` nonempty original-action-ID patterns and their shared Aho–Corasick automaton, with `S` states. Define

`J2=Q[x_1,...,x_p]/(monomials of total degree >=3)`.

For each **individual original labelled action** `a:s->d` with actual BRC weight `w_a(g)`, the deterministic automaton transition `q->q'` has an output hit vector `h in {0,1}^p` (with all suffix matches). Give that edge the jet

`w_a(g)*(1+sum_i h_i*x_i+(sum_i h_i*x_i)^2/2)` in `J2`.

Classify original parallel edges by their original action ID before accumulating matrix entries. Multiply the chronological `96S x 96S` matrices over `J2`. Lift the actual native 96-port entrance mass `r_t` to AC state zero, apply the transfer product and sum every terminal port/AC state to obtain `H(x)`. For every finite window and every allowed gate sequence,

`H(0)=Z=sum_path w(path)`;

`partial_i H(0)=sum_path w(path)*C_i(path)`;

`partial_i partial_j H(0)=sum_path w(path)*C_i(path)*C_j(path)`,

where `C_i` is the overlapping count of pattern `i`. The diagonal derivative includes the factor `2!`; if `Z>0`, normalized first/second moments and covariance follow. If `Z=0` the mass identities still hold.

**Proof.** Every original labelled path has one deterministic AC state trace. Edge jet multiplication along that path equals its original path mass times the degree-two truncation of `exp(sum_i C_i*x_i)`, because formal commuting exponentials add the per-edge hit vectors. Sum over all labelled paths and differentiate. The proof uses the typed BRC edge masses, preserves original action identity and includes zero-gate paths of zero mass.

For `p=2` represent jet coefficients by `(z,u,v,U,V,W)`: total mass, two first raw mass moments, two diagonal second raw mass moments and the mixed moment. Their associative product is

```
z = a.z*b.z
u = a.u*b.z + a.z*b.u
v = a.v*b.z + a.z*b.v
U = a.U*b.z + 2*a.u*b.u + a.z*b.U
V = a.V*b.z + a.u*b.v + a.v*b.u + a.z*b.V
W = a.W*b.z + 2*a.v*b.v + a.z*b.W
```

## Rolling-window theorem

Store time-ordered native BRC jet matrices in a two-stack aggregate queue: the back stack accumulates bottom-to-top and the front stack top-to-bottom. On removing the oldest step, transfer the entire back stack to an empty front stack in reverse sequence. Each step enters the back stack once and moves to front at most once. Over an initial window of `L` and `W` successive shifts, `O(L+W)` exact matrix–matrix compositions and `O(L)` stored matrices suffice, with two aggregate matrix–vector applications per query. This is true even though chronological matrices do not commute. The current entrance state `r_t` advances by the original native BRC update; zero-gate inversions are unnecessary.

With `D=96S` the dense field-operation bound for fixed pattern count is conservatively `O((L+W)D^3 p^2+W D^2 p^2)`, plus native state/gate updates, initial state reconstruction, the input/output cost and rational bit complexity. A sparse representation may save memory initially but may densify on composition. The theorem concerns amortized matrix **compositions**, not an unconditional wall-clock advantage over direct sparse dynamic programming.

## Executed original-native check

The executable uses the frozen original 576-action enumerator from PREFIX-636 (source weights `(1,1,1,1,0,0)`) and original action patterns `P0=(485,316,52,174)`, `P1=(52,174)` (7 AC states). Python `fractions.Fraction` performs every arithmetic operation exactly. PREFIX-635's separate direct per-layer action DP independently checks `Z`, two first and three second raw moments for **every** window; windows with `L<=4` also enumerate complete labelled paths.

**Observed:** 16 cases crossing `(n,L)=(9,3),(10,4),(12,5),(15,6)` and all-one / positive-rational / periodic-zero / all-zero gate classes; 64 exact window comparisons, 9,864 literal path visits, all assertions passed. The rolling queue performed 144 counted matrix compositions, compared with 244 for naive per-window recomputation; maximum measured output rational bit length was 22 bits; peak stored sparse jet entries 22,050. These counts and sample timings are implementation-specific finite evidence, not an asymptotic performance benchmark.

At `n=15, L=6, lambda=5/4`, all gates one, the first window raw jet is

`(Z,U0,U1,V00,V01,V11)=(26880,400,2560,400,410,2600)`.

The last window is `(860160,12800,81920,12800,13120,83200)`. Both equal the independent native-DP check exactly.

## Reproduction and source integrity

Files next to this note are gzip-compressed, base64-encoded UTF-8 text. Decode each with `base64 -d | gzip -d`, removing the `.gz.b64` suffix:

- `PREFIX637_native_rolling_second_moments.py.gz.b64`: actual executed Python source, uncompressed SHA256 `ebfd27be77cc8b5df78c7e5ce4f3a61512e9850a9ec2d27cbc4d75a105701841`.
- `PREFIX637_native_rolling_moments_results.json.gz.b64`: all 16 cases and 64 windows summary, uncompressed SHA256 `3c11e81ddd5ab48e867fbca04891fe8f955b5fb8e4ad2f059ffc6aaca3e7644d`.

The executable requires the pinned preceding source `PREFIX636_selfcontained_native_rolling_ac.py` and `PREFIX635_COMPLETE/` with PREFIX-635 source plus its four explicitly imported native checkers (included in the locally validated research handoff archive). Run `python3 PREFIX637_native_rolling_second_moments.py` from that directory; it writes its results JSON.

Prior provenance: PREFIX-635 commit `305fff0848138e1d03ba88b4d527eebdf8907602`; PREFIX-636 commit `32ba9fd2e52d6537cfb326a0bc2a4b49443a1488`. All scientific definitions retain frozen pin `f42f2906d77f24085c123f3ccfe9667d41caa96d`.

**Next:** seek sparse/factored jet transfers that avoid fill-in and benchmark exact bit lengths and wall-clock against repeated native sparse DP for longer windows and different gate distributions. For arbitrary pattern count `p`, independently test every quadratic indexing convention and repeated suffix-hit case. This document is an author-side research artifact awaiting independent mathematical review.
