# EC49DB + EC49DC-1 executed exact arithmetic evidence

Executed in a Python 3 standard-library local process on 2026-11-01 before GitHub publication. These are actual checker outputs, not forecasted/assumed validations. The source verifier and literal compressed seed certificate are stored unchanged at the adjacent paths, with their immutable Git blobs read back after publication.

1. **python3 VERIFY_EC49DB_GITHUB.py**, original rational positive BRC channels W0=(2,3,3,2,1,1), W1=(3,2,3,2,1,1):

~~~json
{"finite_lift_minors_h2_through_h12":1298,"literal_seed_paths":150,"nonzero_seed_minors":9,"prime":1000003,"seed_det_mod":{"('eq', 2, (-2, 0))":828162,"('eq', 2, (0, 0))":338530,"('eq', 2, (0, 2))":61410,"('eq', 2, (2, 0))":405253,"('eq', 3, (0, 0))":98859,"('le', 2, (-2, 0))":285218,"('le', 2, (0, 0))":949109,"('le', 2, (0, 2))":46019,"('le', 2, (2, 0))":165905},"status":"PASS"}
~~~

2. **python3 VERIFY_EC49DC_WEIGHT_OPEN.py** re-executed the same 9 seed and 1298 lift checks for two declared positive-weight inputs:

~~~text
Reference: W0=(2,3,3,2,1,1), W1=(3,2,3,2,1,1).
Q=1, boundary Γ=(-216,216,216,216).
All 9 seed minors and 1298 lifted interior minors: PASS.

Distinct point: W0=(2,3,5,2,1,1), W1=(5,4,5,2,1,1).
Q=3, boundary Γ=(-3000,3600,3600,3600).
Seed determinant residues mod 1000003 in order
eq2 (-2,0),(0,0),(0,2),(2,0); eq3 (0,0);
le2 (-2,0),(0,0),(0,2),(2,0):
543369, 927850, 720861, 812834, 336039, 743574, 540033, 754979, 247788.
All 9 seed minors and 1298 lifted interior minors: PASS.
~~~

3. Original local stdout SHA256: EC49DB_ACTUAL_RUN.log = df73ab835130942bf9ba000b995d6108916b4e5eb4ee040080388ba49b9212af; EC49DC_ACTUAL_RUN.log = 1c9a45577ded0a43dd553c7281a88efa9e97fe421383e24f57e2c5bf512d631e.

**Inference boundary:** Nonzero modular determinants certify integer/rational nonzero minors for the finitely reconstructed words. The all-h theorem is established by the explicit symbolic lift (which has parameter-mononomial row factors); genericity follows from the nonzero polynomial P. The finite tests alone are not all-h or generic proofs. All native Source claim/Driver admission remains pending.
