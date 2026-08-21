                "raw_component_roots": [list(x) for x in sorted(c3["raw_branches"].keys())],
                "deduplicated_canonical_component_roots": [list(x) for x in sorted(c3["canonical_branches"].keys())],
            },
            "C4_gaussian_factor_allocations": {
                "factorization": c4["norm_factorization"],
                "deduplicated_component_roots": [list(x) for x in sorted(c4["branches"].keys())],
            },
            "native_component_trace_branches_and_compressed_path_fibers": [
                {
                    "components": row["components"],
                    "alpha": row["alpha"],
                    "norm_certificate": row["norm_certificate"],
                    "trace_id": row["trace_id"],
                    "candidate_membership": row["candidate_membership"],
                    "derivation_channel_ids": {
                        key: [ch.get("channel_id") for ch in channels if ch.get("channel_id")]
                        for key, channels in row["derivation_channels"].items()
                    },
                    "path_fiber": {
                        "compressed": row["path_fiber"]["compressed"],
                        "first_ranked_path_id": row["path_fiber"]["first_ranked_path_id"],
                        "last_ranked_path_id": row["path_fiber"]["last_ranked_path_id"],
                        "certificate_sha256": row["path_fiber"]["certificate_sha256"],
                    },
                }
                for row in rows
            ],
        },
        "post_discovery_brute_verification": verification,
        "one_sector_total_path_cardinality": total_cert["one_sector_total_path_cardinality"],
        "final_generated_root_set_sha256": sha256_obj(discovered["generated_component_roots"]),
    }


def build_provenance_graph(discovered: Mapping[str, object], rows: Sequence[Mapping[str, object]]) -> Dict[str, object]:
    N = discovered["input"]["N"]
    r = discovered["scalar_root"]["r"]
    nodes: List[Dict[str, object]] = [
        {"id": f"N:{N}", "type": "SCALAR_SQUARED_NORM", "value": N},
        {"id": f"r:{r}", "type": "SCALAR_ROOT", "value": r},
    ]
    edges: List[Dict[str, str]] = [{"from": f"N:{N}", "to": f"r:{r}", "relation": "EXACT_INTEGER_SQRT"}]
    channel_nodes: Dict[str, Dict[str, object]] = {}
    channel_memberships: Dict[str, set] = defaultdict(set)
    channel_root_edges = set()
    for row in rows:
        a, b = row["components"]
        root_id = f"alpha:{a},{b}"
        trace_id = f"trace:{a},{b}"
        fiber_id = f"fiber:{a},{b}"
        nodes.extend([
            {"id": root_id, "type": "COMPONENT_ROOT", "components": [a, b]},
            {"id": trace_id, "type": "NATIVE_COMPONENT_TRACE", "trace": row["trace_id"]},
            {"id": fiber_id, "type": "NATIVE_PATH_FIBER", "cardinality": row["path_fiber"]["compressed"]["fiber_cardinality"]},
        ])
        edges.append({"from": root_id, "to": trace_id, "relation": "ROOT_TO_TRACE"})
        edges.append({"from": trace_id, "to": fiber_id, "relation": "TRACE_TO_NONCOMMUTATIVE_PATH_POLYNOMIAL"})
        for candidate_key, channels in row["derivation_channels"].items():
            for channel in channels:
                cid = channel.get("channel_id")
                if cid is None:
                    continue
                compact_channel = {
                    k: channel[k]
                    for k in (
                        "channel_id", "identity", "classification", "canonical", "k", "h", "m", "n",
                        "orientation", "beta", "beta_norm", "alpha_before_orientation", "unit",
                        "split_prime_allocations", "pre_unit_value", "value"
                    )
                    if k in channel
                }
                channel_nodes.setdefault(cid, compact_channel)
                if channel_nodes[cid] != compact_channel:
                    raise AssertionError(f"channel id collision with unequal data: {cid}")
                channel_memberships[cid].add(candidate_key)
                channel_root_edges.add((cid, root_id))
    for cid in sorted(channel_nodes):
        nodes.append({
            "id": cid,
            "type": "ALGEBRAIC_DERIVATION_CHANNEL",
            "candidate_memberships": sorted(channel_memberships[cid]),
            "data": channel_nodes[cid],
        })
        edges.append({"from": f"r:{r}", "to": cid, "relation": "FACTORIZATION_DRIVES_CHANNEL"})
    for cid, root_id in sorted(channel_root_edges):
        edges.append({"from": cid, "to": root_id, "relation": "DERIVES_COMPONENT_ROOT"})
    node_ids = [node["id"] for node in nodes]
    if len(node_ids) != len(set(node_ids)):
        raise AssertionError("provenance graph node ids are not unique")
    return {
        "schema": "R063_STAGE0_DERIVATION_PROVENANCE_GRAPH_V1",
        "nodes": nodes,
        "edges": edges,
        "node_id_uniqueness": True,
        "quotient_policy": "return one native trace branch per component root; retain algebraic derivation channels as higher provenance enrichment",
        "multiplicity_classification": "ALGEBRAIC_ROOT_DERIVATION_MULTIPLICITY_IS_NOT_NATIVE_PATH_MULTIPLICITY",
    }


def markdown_candidate_matrix(verification: Mapping[str, object], regression: Mapping[str, object]) -> str:
    cmp = verification["comparisons"]
    c2_missing = cmp["C2"]["missing"]
    c2_extra = cmp["C2"]["extra"]
    first_c2 = regression["C2_first_failure"]
    return f"""# R063 Stage 0 — Path-root operator candidate matrix

Task: `{TASK_ID}`  
Researcher: `{RESEARCHER_ID}`

| Candidate | Construction | N=2500 complete? | Extras? | Classification |
|---|---|---:|---:|---|
| C0 | ordinary scalar `N -> sqrt(N)` | No | No | Retains only scalar radius/norm magnitude; loses component, trace, provenance, path multiplicity. |
| C1 | brute `a^2+b^2=N` inverse fiber | Yes by definition | No | Verification oracle only; set-valued restatement, not accepted as discovery. |
| C2 | `N(beta)=r`, then `alpha=beta^2` | {str(cmp['C2']['exact_set_equality']).lower()} | {len(c2_extra)} | Exact norm-preserving lift but incomplete here; missing branches are preserved below. |
| C3 | factor `r`, enumerate divisor-scaled canonical Euclid/Gaussian channels `r=k(m^2+n^2)`, then `k(m+nJ)^2` | {str(cmp['C3']['exact_set_equality']).lower()} | {len(cmp['C3']['extra'])} | Complete for square native norms by the scaled primitive Pythagorean theorem; regression passes through `r<=512`. |
| C4 | direct Gaussian prime allocation for norm `N=r^2` | {str(cmp['C4']['exact_set_equality']).lower()} | {len(cmp['C4']['extra'])} | Complete constructive factorization route; same canonical root fiber as C3, with Gaussian exponent-allocation provenance. |

## Classified C2 negative result

N=2500 C2 missing branches (derived only after discovery freeze by the verifier): `{json.dumps(c2_missing)}`.  
N=2500 C2 extras: `{json.dumps(c2_extra)}`.

Across the non-customized square regression the first C2 failure is at `r={first_c2['r'] if first_c2 else 'none'}`. This C2 failure is a **classified candidate limitation**, not a checker error.

## Inverse fiber versus discovery

`INVERSE_NORM_FIBER` names a set by the target equation. `SCALAR_ROOT_FACTORIZATION_GENERATOR` constructs the members from integer/Gaussian factorization and exact exponent or Euclid-channel choices. C3/C4 are therefore constructive discovery operators; C1 is only the post-freeze completeness oracle.
"""


def markdown_c3_theorem(verification: Mapping[str, object], regression: Mapping[str, object]) -> str:
    return f"""# R063 Stage 0 — Scaled-square lift theorem

## Statement

Let `N=r^2` with `r>=1`. Define C3 from the integer factorization of `r` by enumerating divisors `k|r`, putting `h=r/k`, constructing Gaussian roots `m+nJ` of norm `h`, and retaining the canonical channels:

- axis channel: `h=1, (m,n)=(1,0)`;
- nondegenerate channel: `m>n>0`, `gcd(m,n)=1`, and `m,n` have opposite parity.

For each canonical channel form

`alpha = k(m+nJ)^2 = k(m^2-n^2) + 2kmn J`,

and retain both ordered nonnegative component orientations when distinct.

Then the deduplicated C3 output is exactly

`{{(a,b) in N_0^2 : a^2+b^2=r^2}}`.

## No-extra proof

Every generated channel satisfies

`[k(m^2-n^2)]^2 + (2kmn)^2 = k^2(m^2+n^2)^2 = r^2`.

Hence C3 produces no extra branch.

## Completeness proof

Take any nonnegative ordered solution `a^2+b^2=r^2`.

If one component is zero, the axis channel with `k=r,m=1,n=0`, followed by the ordered orientation rule, generates it.

Otherwise set `d=gcd(a,b)`. Prime valuations in `d^2 | r^2` imply `d|r`. Dividing by `d` gives a primitive integer Pythagorean triple. The classical primitive Pythagorean classification supplies unique `m>n>0`, `gcd(m,n)=1`, opposite parity, with

`r/d=m^2+n^2`

and the two primitive legs equal to `m^2-n^2` and `2mn` up to order. Therefore C3 visits `k=d`, reconstructs the branch, and its orientation rule restores the original ordered pair.

Thus C3 is complete for every square native norm, not only the central finite case.

## Evidence

- N=2500 exact equality against the post-freeze brute oracle: `{verification['comparisons']['C3']['exact_set_equality']}`.
- N=2500 extras: `{len(verification['comparisons']['C3']['extra'])}`.
- Regression `1<=r<={regression['r_range'][1]}` combined C3/C4 checker mismatch count: `{regression['combined_checker_mismatch_count']}`.

Raw noncanonical scaled-square channels are retained as derivation provenance, but are quotiented before the component-root/trace branch is returned. This is why algebraic derivation multiplicity can exceed one without multiplying the native trace branch itself.
"""


def markdown_c4_audit(discovered: Mapping[str, object], verification: Mapping[str, object]) -> str:
    meta = discovered["C4"]["norm_factorization"]
    roots = sorted(discovered["C4"]["branches"].keys())
    allocations: List[str] = []
    for pair in roots:
        channels = discovered["C4"]["branches"][pair]
        allocations.append(f"- `{pair}` <- `{json.dumps(channels, sort_keys=True)}`")
    allocation_text = "\n".join(allocations)
    return f"""# R063 Stage 0 — Gaussian factor route audit

C4 does not scan the target Diophantine equation. It factors the norm integer and uses the UFD structure of `Z[J]`.

For a norm integer `M`, the construction is:

1. `2` ramifies through the Gaussian prime `1+J`; its Gaussian exponent is fixed by `v_2(M)`.
2. Every prime `q == 3 (mod 4)` remains inert; `v_q(M)` must be even and contributes the fixed integer Gaussian factor `q^(v_q(M)/2)`.
3. Every prime `p == 1 (mod 4)` splits as `pi_p * conjugate(pi_p)`. If `v_p(M)=e`, choose `t=0..e` and allocate exponents `(t,e-t)` between the conjugate pair.
4. Multiply by the four units and keep the ordered nonnegative sector representatives.

This enumerates every Gaussian integer of norm `M` and nothing else by unique factorization.

## Central factorization metadata

```json
{json.dumps(meta, indent=2, sort_keys=True)}
```

## Discovered first-quadrant factor-allocation channels

{allocation_text}

C4 root equality with the post-freeze N=2500 brute fiber: `{verification['comparisons']['C4']['exact_set_equality']}`. C4 and canonical C3 agree **before** brute verification.

C4 is stronger as a factorization provenance description: it exposes Gaussian prime-exponent allocation directly. C3 instead exposes the scalar-root-to-Euclid scaled-square channel. They quotient to the same component-root set for square native norms.
"""


def markdown_path_formula(rows: Sequence[Mapping[str, object]], total_cert: Mapping[str, object]) -> str:
    branch_lines = "\n".join(
        f"- `{row['components']}`: `Lambda={row['path_fiber']['compressed']['coefficient_extraction']}`, cardinality `{row['path_fiber']['compressed']['fiber_cardinality']}`"
        for row in rows
    )
    return f"""# R063 Stage 0 — Exact path-valued square-root formula

For square input `N=r^2`, let `GRoot_E(N)` be the deduplicated ordered nonnegative component-root set generated by C3 (equivalently C4) **before** any brute target-fiber verification.

For `(a,b) in GRoot_E(N)`, define

`Lambda(a,b) = [u^a v^b](uX_i+vX_j)^(a+b)`,

where `u,v` commute and `X_i,X_j` are noncommuting native path generators. Coefficient extraction returns exactly all words with `a` copies of `X_i` and `b` copies of `X_j`.

Then

`PathSqrt_E(N) = disjoint_union_{{(a,b) in GRoot_E(N)}} Lambda(a,b)`.

After the frozen R061 origin incidence is attached, `Lambda(a,b)` realizes the trace

`T_{{a,b}}^(ij)=[X_i^a X_j^b]`

with exact path cardinality `binom(a+b,a)`.

For C3 the same construction can be written

`r=k(m^2+n^2)` -> `(a,b)=orientation(k(m^2-n^2),2kmn)` -> `Lambda(a,b)`.

The quantity `a+b` is only the path-letter count. Native line length is `sqrt(a^2+b^2)=r`; jump count is never substituted for native length, and no carrier vector relation is used as a native identity.

## Central branch fibers

{branch_lines}

Exact one-sector total path cardinality: `{total_cert['one_sector_total_path_cardinality']}`.

## Algebraic versus path multiplicity

Algebraic derivation channels are provenance above a **single deduplicated component root / trace branch**. Native path multiplicity is the binomial number of noncommutative linearizations inside that trace. These multiplicities are different layers and are not identified.

## Downstream-only BRC readout

Only after the path fibers are constructed may R062 project each branch as

`path witnesses -> identical natural-number multiplicity -> Boolean support 1`.

No BRC object participates in root or path discovery.
"""


def markdown_repro(discovery_sha: str, regression: Mapping[str, object], total_cert: Mapping[str, object], hardcode_scan: Mapping[str, object], summary_sha: str) -> str:
    return f"""# R063 Stage 0 — Reproducibility proof

Task: `{TASK_ID}`  
Taskbook source: `{TASKBOOK_SOURCE}`  
Owner branch: `{OWNER_BRANCH}`  
Researcher: `{RESEARCHER_ID}`

## Deterministic command

```text
python3 scripts/r063_stage0_validate_path_valued_sqrt_2500.py --out research_results/R063_STAGE0
```

The checker uses only Python exact integers, `isqrt`, integer factorization, Gaussian integer multiplication/norm, deterministic modular square-root/Cornacchia split-prime construction, exact binomial arithmetic, and deterministic combination rank/unrank.

## Phase barrier

`discover_from_scalar_root(N)` is called first. Its JSON-safe payload is materialized as `R063_STAGE0_DISCOVERY_PHASE_FROZEN.json` and hashed **before** `verify_against_norm_fiber` is called.

Frozen discovery SHA256: `{discovery_sha}`.

The brute function `brute_norm_fiber` is reachable only from the verification/regression code path and is not called by discovery.

## Anti-hardcode audit

Source scan pass: `{hardcode_scan['pass']}`.  
Nontrivial discovered-pair literal hits in checker source: `{json.dumps(hardcode_scan['nontrivial_discovered_pair_literal_hits'])}`.

## Exact replay checkpoints

- General square regression range: `1 <= r <= {regression['r_range'][1]}`.
- Combined C3/C4 regression mismatch count: `{regression['combined_checker_mismatch_count']}`.
- Regression row SHA256: `{regression['rows_sha256']}`.
- One-sector total path-cardinality certificate SHA256: `{total_cert['total_certificate_sha256']}`.
- Replay summary core SHA256: `{summary_sha}`.

