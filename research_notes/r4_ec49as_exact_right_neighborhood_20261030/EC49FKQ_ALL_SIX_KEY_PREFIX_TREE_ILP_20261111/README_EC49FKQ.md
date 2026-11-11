# EC49FKQ — all nine residual six-key signed-X6 BRC sets solved by exact 0–1 prefix-tree model

Date: 2026-11-11. Author-side finite optimization, reproduced using SciPy 1.17.0 / HiGHS mixed-integer branch-and-bound with zero MIP gap; independent literal-word witness validation. Independent Driver mathematical admission pending.

Frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Input is the frozen 178,850-word, 94-full-raw-key, 24-demand nine-state signed-X6 BRC catalogue used in EC49FKM–FKP; it does not change P000.

## Result and scope

EC49FKP left exactly nine six-full-key subsets whose per-depth necessary lower bounds did not yet exclude 93 native prefixes. For those nine fixed *allowed* key subsets, a complete mixed-integer optimization (no truncated catalogue) returned the following exact integer optima for the full ordered signed native-prefix union:

| Residual set index (FKP order) | Extra keys beyond K4 | Prior per-depth lower bound | HiGHS 0–1 optimum | Independently checked witness |
|---|---|---:|---:|---:|
| 0 | (5,4,1),(5,5,1) | 92 | 98 | 98 |
| 1 | (5,4,1),(6,4,1) | 92 | 98 | 98 |
| 2 | (6,3,1),(6,4,1) | 92 | 98 | 98 |
| 3 | (6,3,1),(7,3,1) | 92 | 98 | 98 |
| 4 | (6,4,1),(6,6,1) | 92 | 112 | 112 |
| 5 | (6,4,1),(7,5,1) | 86 | 112 | 112 |
| 6 | (6,4,1),(7,6,1) | 92 | 112 | 112 |
| 7 | (6,4,1),(8,4,1) | 92 | 112 | 112 |
| 8 | (6,4,1),(8,5,1) | 92 | 112 | 112 |

Here `K4={(2,1,1),(3,0,1),(3,1,1),(4,2,1)}`. "Allowed" means paths may use any subset of these six keys, as long as all 24 labelled demands are realized; using fewer keys is permitted.

**Combined six-key consequence:** EC49FKM ruled out <=4 full keys; EC49FKN proved every five-key solution uses >=99 signed prefixes; EC49FKO/EC49FKP excluded 1995 of the 2004 covering six-key sets at 93 prefixes or less. This computation resolves the nine remaining sets, so no completion with at most six complete raw keys and at most 93 native signed ordered prefixes exists in the pinned model. Seven-key 94-prefix constructions remain available; `C_min(7) ?= 94` is still the mother problem.

## Mathematical reduction: full prefix-tree 0–1 ILP

Fix a six-key set K. Let `W_i(K)` contain all frozen admissible ordered operation words realizing labelled demand i with raw key in K. Construct a rooted trie T(K) whose nonroot nodes are **literal, ordered, signed X6 microstep prefixes** p of the words in `union_i W_i(K)`. Distinct signed sequences have distinct nodes, regardless of terminal signed displacement.

For each nonroot prefix p, use binary `x_p in {0,1}`. For parent q of p, require `x_p <= x_q`, omitting that inequality when q is the empty virtual root. For every demand i require

`sum_{w in W_i(K)} x_{terminal_prefix(w)} >= 1`.

Minimize `sum_{p in T(K) nonroot} x_p`.

**Proof of exact equivalence:** Any choice of one admissible word per demand gives a feasible binary vector by marking exactly the union of its native signed prefixes, with objective equal to that union's size. Conversely, given a feasible binary vector, each demand has at least one selected terminal prefix belonging to an admissible word; select such a word for each label. Parent closure forces all native prefixes of each selected word to have x=1, so their union costs at most the ILP objective. Taking minima in both directions yields equality. This construction is a finite exact 0–1 formulation with no lossy endpoint, key-count, or prefix-label quotient.

The solver processed the complete integer model for all nine K, returned `status=0`, `Optimization terminated successfully (HiGHS Status 7: Optimal)`, integer primal = integer dual bound, `mip_gap=0`. The nine complete 24-word witnesses were checked by a separate literal-state checker, testing the 9-state DFA, final six-axis displacement, observer labels, complete keys and exact prefix-union count. This is reproducible **solver-certified author-side computation**, not a formal proof-assistant or independently reviewed certificate of the solver's internal branch-and-bound trace. The exact ILP formulation itself is proved above.

## Data, reproduction and evidence

- `VERIFY_EC49FKQ_MILP.py`: actually executed nine-set integer-MIP code, using the frozen original catalogue generator in `../EC49FJD_RELEASE_B11_COMPLETE_20261111/EC49FGW_RADIUS5_SCREEN.py`. SciPy 1.17.0 and its HiGHS solver are required for the numeric solve. CLI: `python VERIFY_EC49FKQ_MILP.py <index 0..8> <time_limit_seconds>`.
- `VERIFY_EC49FKQ_WITNESSES.py`: independently executed checker with its own literal signed-step traversal; decode the packed witnesses first.
- `EXACT_WITNESSES_EC49FKQ.json.gz.b64`: nine reproducible 24-word witnesses, encoded as base64(gzip(JSON)); expanded compact JSON SHA256: `45326f659546b3ec1776221eb5e5050362740aad4b4c4e4741610464da220265`.
- `EXACT_SUMMARY_EC49FKQ.json`: all nine integer optima, catalogue/model sizes, evidence and solver status.

Decode: `python -c "import gzip,base64,pathlib,json;p=pathlib.Path('EXACT_WITNESSES_EC49FKQ.json.gz.b64'); w=json.loads(gzip.decompress(base64.b64decode(p.read_text()))); [pathlib.Path(f'MIP_WITNESS_{i}.json').write_text(json.dumps(x,indent=2)+'\\n') for i,x in enumerate(w)]"`.

The complete source of the underlying nine-state generator is the earlier published frozen file; its scientific equations are not repinned. The local author execution used the conversation-delivered EC49FJD evidence package containing that same model and pin, with a different package file Git Blob hash from the present repository copy; this provenance distinction should be considered during independent source review. All nine independently checked witnesses can be audited without the MIP solver.

**Next research unit:** independently prove or formally certify the nine MIP lower bounds (for example via a proof-emitting integer solver or a tighter exact cross-depth combinatorial obstruction) and begin seven-key 93-prefix direct constructions. Retain the seven-key mother question and the immutable science pin.

Project state: author-side GitHub publication, unmerged draft PR #1730; no native current CLAIM/Result and no independent Driver acceptance is asserted.
