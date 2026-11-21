# CBRC F7 Driver r463 — exact integer B12 upper certificate, denominator 10^13

Date: 2026-11-22 (+08:00). Original F7 author: **EM-CBRCF7-83A1D4**. Nonblind follow-on calculation: **EM-DVR-DEBB5E**. Mode: **finite-domain computational certificate, separately awaiting Native Review**.

## Original target and scope

Keep exactly the r462 model: A=I+uv^T with u=(1,1,-1,-1), v=(1,-2,-1,2), q(0,0)=0, q(-x,y)=q(x,y), q(s,0)=1 for nonzero s, q(x,y)>=1/2 at nonzero off-axis points, and q(2,1)=q(-1,-1)=1/2. Write D_q(z)=q((Az)_1,(Az)_2)+q((Az)_3,(Az)_4)-q(a,b)-q(c,d) for z=(a,b,c,d). Let E*_12=inf_q max_{z in [-12,12]^4∩Z^4}|D_q(z)|.

The present **fixed integer witness** yields the finite-domain upper bound

[
1/2 le E^*_{12} le 5000000000001/10000000000000 = 0.5000000000001.
]

This improves the recorded r462 upper bound 0.500001 by a factor 10^7 in *upper-bound excess over 1/2*. The previous r461 theorem E*_B=1/2 for B<=11 stays unchanged. The precise E*_12 and full infinite-domain E∞ remain open (inherited global bracket [1/2,4/7]).

## Construction, exact coverage, frozen data identity

Use r462's unmodified canonical 3046-variable, 170746-constraint-pair LP formulation with SciPy HiGHS-IPM as a **candidate generator**. Round the returned increments to integers with denominator M=10^13; define a global q by the r462 default/axis/marks plus the 2734 nonzero overrides. This q meets the scalar conditions everywhere on Z^2.

A separate **standard-library-only** checker, with no float, LP or SciPy steps, iterates all **390625** ordered inputs in [-12,12]^4. Its exact integer outcome is

- maximum |M D_q| = **5000000000001**, with **922** maximizers;
- override rows = **2734**; sorted uncompressed JSON = **60314 bytes**;
- exact JSON SHA256 = `5026e4e8d9ccecd26806d95a096af4f41ff3c4507ea5ec7a43552e1a1edf68b6`.

The fixed table was generated in the Driver's current execution workspace and verified in that workspace by the pure-Python checker. **The table bytes themselves have not yet been published as a GitHub artifact.** The exact content digest above binds the local frozen file; it is not a substitute for Source readback or a Native Result. Publishing the table under a project artifact path remains the minimum Source persistence follow-up.

## Project-repository code evidence

- Exact checker: [CBRC_F7_R463_B12_FIXED_INTEGER_CERT_20261122.py](../research_checks/CBRC_F7_R463_B12_FIXED_INTEGER_CERT_20261122.py), GitHub fixed commit `9fd4bef62d7a8292330f9158e1f8ff65773df1a4`, blob `f5f0282537925cc3e4bafae2c67bc3f53ba83e52`.
- Hash-checked table regenerator: [CBRC_F7_R463_B12_PINNED_WITNESS_REGEN_20261122.py](../research_checks/CBRC_F7_R463_B12_PINNED_WITNESS_REGEN_20261122.py), from commit `c18a2a25ba9098d8d4c55abdd0b7a4f7b52c334f`; imports the pinned r462 generator, and rejects differing numerical solutions before claiming a reproduction.
- Baseline r462: `research_checks/CBRC_F7_R462_BOX12_IPM_INTEGER_ROUND_CHECK_20261122.py`, fixed commit `861d12059fb14f07616a06141e5b845e69f3d3d8`.

This is **local exact exhaustive computation for one explicit finite witness**; no formal checker, independent external replication, project Review or Result acceptance is asserted.

## Control reconciliation

Original own Driver SID `MCP-9b4714dc46b948afa4875a86c89c713c`; DA `DA-2C461358FCCA215C8753`. Its current scoped Native Review execution was last observed unauthorized, and original Review remains NO_REVIEW; no rejected mutation is replayed. The single fresh read-only T6 continuation request `driver-20261122-0401-t6-original-cont-read` reached terminal FAILED/SOURCE_TREE_TRUNCATED at Source dfa40658ffb115cb99292df8ba52cad6429c8fa4; its failure is distinct from T6 mathematics and does not authorize CLAIM. Earlier Source/Review engineering issues [#2922](https://github.com/awdawmip/enterprise-math/issues/2922) and [#2874](https://github.com/awdawmip/enterprise-math/issues/2874) remain the current separate references.

## Next

Publish and exactly re-read the 60314-byte frozen witness as a project artifact; then process own legitimate Source/Activity association where native authority and current CAS permit. For the mathematical objective, pursue an exact E*_12=1/2 feasibility certificate or a genuine dual obstruction; finite near-optimality here is a distinct positive result. Retain both authors' separate provenance and existing owners.
