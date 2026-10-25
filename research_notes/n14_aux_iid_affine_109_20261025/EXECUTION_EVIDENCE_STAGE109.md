# Stage109 exact computation: executed author-side evidence

Scientific scope: external iid ternary full ordered-history N=14, not P000/X6/Heartbeat transfer. Source input GLOBAL_KNOWLEDGE_V1 main@babff194f059aaaa452e7827f815845aefcb647a; Enterprise Math starting main@f651ea40d12cee192ecab1bc741f98f1a9e01892.

## Observed local execution

A full expanded bottom-up exact rational checker (`derive109.py`) returned:

```text
DUAL K109=491857029/506348 L109=116416632/126587 Gamma109=957523557/506348
TIES [((10, 3, 0), ('P', 'C')), ((10, 3, 3), ('Q', 'C'))]
GAPS: 680 states; 1240 nonchosen comparisons; 1238 strictly positive; 0 negative; min positive 20261/759522
FIRST_HITS A: count=120 P=390625/5971968 Q=390625/20155392
FIRST_HITS D: count=2051 P=1281875/9172942848 Q=1281875/3869835264
MIX du/dw=22757603/10565760000 eta/dw=23181244375/130840802044674048 wmax=1
alpha109=13084102500820187507/37682150988866125824
V109=1934432626777903782385/150728603955464503296
PASS_STAGE109_EXACT_AUTHOR
```

A second author-coded top-down Fraction Bellman plus literal ordered-history DFS independently returned:

```text
FIRST_HITS_LITERAL_PASS {'(10, 3, 0)': ['120', '390625/5971968', '390625/20155392'], '(10, 3, 3)': ['2051', '1281875/9172942848', '1281875/3869835264']}
DFS_PASS w=0: nodes=995728 leaves=663819
DFS_PASS w=1: nodes=952657 leaves=633054
DFS_PASS w=1/2: nodes=995728 leaves=663819
PASS_INDEPENDENT_LITERAL_STAGE109
```

Local compact rational checker `CHECKER_STAGE109.py` also executed and printed:

```text
PASS_STAGE109_EXACT_680_STATES_1240_COMPARISONS_REAL_INTERVAL
```

The `next_dual110.py` fixed-action gap scan executed and returned K110=6497577/6734, L110=3069240/3367 at (13,6,4) competing Q, dual-only candidate.

## Integrity and evidence limits

Local complete research ZIP (with expanded proof, two independent author programs, exact certificate, observed stdout, next-root helper and SHA256 manifest) was assembled, hash-verified, reopened, and the compact checker rerun after extraction. Final ZIP SHA256: `355817df2d1e23950b889a635dc1b5554a0a71816fcebc98df985e4c9195b59f`. Individual local SHA256 examples: `derive109.py=92b1d6ff0da4fe1857e5d8be4deeab3dedeb65cc0a2aa7b6a4b8303030ff202a`, `independent_ordered109.py=825222a0ff3e60ab72dc8f99a046e64945b46600af45ae10a2d55fc965ad981f`, `CHECKER_STAGE109.py=c351366f6b1e8c262f5be432e517a7b932504cb0ccae0300d431088b6fe57bdd`.

The GitHub CHECKER_STAGE109.py and INDEPENDENT_ORDERED_STAGE109.py are compact reformattings of the same exact algorithm; their Git Blob identities were read back from immutable commit 2bdf3d77041ce6a0ccd998f4f618ca7a21cd996d, but **they are not asserted to be byte-identical to the locally executed expanded programs**. The full executed copies and raw stdout live in the local ZIP. Further independent review should execute the GitHub versions directly and check the full written proof. No independent Research Driver was activated and no native mathematical acceptance was granted.

Native controls: tasks read failed CONTROL_QUOTA; session_start denied STATIC_READONLY_SCOPE_DENIED, operation_sent=false. No bypass via Google Drive attempted.
