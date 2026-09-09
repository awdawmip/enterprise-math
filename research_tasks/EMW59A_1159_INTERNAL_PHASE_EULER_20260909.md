<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "parent_objective_id": "EM-FREE-W59A-ISSUE1159-WALLIS-SINE-ROTATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "task_id": "RS-EMW59A-1159-IPQ-EULER",
  "title": "Issue 1159 internal phase quantization and log-free Euler completion",
  "frontier": "The finite Dirichlet/Wallis core is already verified, while the later free-research branch proposes an internal S,C,tau phase-quantization identity and a direct product-defect route to the Euler product that no longer needs classical Chebyshev/pi as a proof input. The proof route is durable but not yet independently closed as a single theorem package.",
  "next_action": "Read the state-machine handoff first, independently rederive the internal recurrence identity D_n(2-2C(theta)) S(theta)=S((n+1)theta), and use it to prove complete finite root quantization, the exact mode-radius formula, and a locally uniform Euler product with an explicit direct tail certificate.",
  "dependencies": [],
  "source_refs": [
    "research_notes/EM_FREE_W59A_ISSUE1159_STATE_MACHINE_HANDOFF_20260909.md",
    "research-branch:free/1159-internal-phase-euler-w59a@9e6e9abe813aa17a7eff1ee8278e2f0e9f73312c",
    "lean-branch:free/1159-spectral-precision-lean-w59a@269b1cafac209e42d6770b0aae4a4d8d0a981f8a",
    "research_notes/WALLIS_SINE_INTERNAL_PHASE_QUANTIZATION_EULER_PRODUCT_20260904.md"
  ],
  "evidence_status": "FREE_RESEARCH_1159_DURABLE_HANDOFF_20260909",
  "last_progress_ref": "research_notes/EM_FREE_W59A_ISSUE1159_STATE_MACHINE_HANDOFF_20260909.md",
  "last_progress_at": "2026-09-09T10:55:00+08:00",
  "hard_block": "INTERNAL_PHASE_QUANTIZATION_TO_EULER_PRODUCT",
  "tags": ["EM-FREE-W59A", "issue-1159", "Wallis", "Dirichlet", "phase-quantization", "Euler-product", "tau"],
  "registry_key": "RS-EMW59A-1159-IPQ-EULER",
  "identity_lane": "RW59IPQ",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null
}
-->

# Issue 1159 internal phase quantization and log-free Euler completion

Status: `READY / FREE-RESEARCH INTEGRATION`

## Mother question

Can the Euler product for the internally completed sine law be derived entirely from the native finite Dirichlet recurrence and the project-internal power-series rotation law, with classical `pi`, circle spectra, and Chebyshev roots used only as later compatibility checks?

## Frozen inputs and scope

Read `research_notes/EM_FREE_W59A_ISSUE1159_STATE_MACHINE_HANDOFF_20260909.md` first and consume the verified finite determinant, compact-error, Hermitian-spectrum, parity, Hamming/Wallis, and decimation results rather than replaying them.

Use the immutable research source `free/1159-internal-phase-euler-w59a@9e6e9abe813aa17a7eff1ee8278e2f0e9f73312c`. The candidate internal objects are the power-series functions `S,C` and their first positive zero `tau`. Classical trigonometric naming is admissible only after the internal theorem is proved, as a compatibility readout.

Preserve the correction recorded in the handoff: the newer direct product-defect method is a strengthening of the older logarithmic-tail route, not evidence that the older theorem had the briefly alleged zero-denominator defect.

## Hard target and required outputs

Hard target: `INTERNAL_PHASE_QUANTIZATION_TO_EULER_PRODUCT`.

Deliver all of the following, or a precise obstruction replacing any failed item:

1. Rebuild the minimum internal analytic package for `S,C,tau`: addition/doubling laws, first-zero positivity, and the sign information actually required by the proof.
2. Prove the recurrence identity `D_n(2-2C(theta)) S(theta)=S((n+1)theta)` without importing a classical root list.
3. Prove that for `M>=2` and `1<=k<M`, `u_(k,M)=2-2C(k tau/M)` gives all `M-1` finite Dirichlet roots, with exact ordering or an equivalent completeness argument.
4. Prove `rho_(k,M)=2M S(k tau/(2M))`, fixed-mode convergence `rho_(k,M)->k tau`, and the intrinsic lower bound needed for product tails.
5. Derive the exact finite spectral product for `F_M` and prove a direct finite product-tail estimate strong enough to pass uniformly to the infinite Euler product on every fixed compact interval.
6. Close `S(x)/x = product_(k>=1)(1-x^2/(k^2 tau^2))` internally and recover the Wallis readout `tau=2 W_infinity` at `x=tau/2`.
7. State exactly which steps are native finite algebra, internal analytic completion, and classical compatibility. Produce a durable proof note and a formalization-ready lemma graph; formalize the stable core when efficient.

## Research value to preserve

This route would make the infinite product a genuine completion theorem of the finite rotation spectrum rather than a classical sine-product theorem retrofitted onto the model. It also supplies the common internal phase needed by the later spectral-arithmetic and precision tasks.

The direct product-defect route appears both simpler and quantitatively sharper than the earlier logarithmic tail argument, so retaining exact constants and domain hypotheses has independent precision value.

## Success, kill, and return criteria

Success is a noncircular internal proof of complete finite phase quantization and the locally uniform Euler product, together with explicit finite tail bounds and a clean semantic layer split.

Kill any route that requires the classical zero set of sine, a continuous circle/Fourier spectrum, or `tau=pi` as an input to the native quantization. A classical comparison after the internal theorem is acceptable.

If the internal addition/first-zero package is insufficient, return the smallest missing analytic lemma and an exact statement showing why it is necessary rather than silently importing a classical theorem.