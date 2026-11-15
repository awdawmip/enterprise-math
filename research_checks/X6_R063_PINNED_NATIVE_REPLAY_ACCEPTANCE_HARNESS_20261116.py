#!/usr/bin/env python3
"""R063 Stage0 *original-object* replay harness. Does not change the source or inputs.

Pass the authorized checkout of the frozen R063 branch as --repo-root.
This script does not itself implement C2/C3/C4 and is not evidence of a native
replay until the original process exits 0 and all exact artifacts are validated.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ORIGINAL = {
    'scripts/r063_stage0_validate_path_valued_sqrt_2500.py': 'b4e000a6377f2858ae434eb0eecd0c25c33e8592',
    'scripts/r063_stage0_checker_parts/part00.inc': '4a69c4d698887bce56323f393cb979609ce4ab0a',
    'scripts/r063_stage0_checker_parts/part01.inc': '913078c642b8995bfc135ef0350912387a17cdb8',
    'scripts/r063_stage0_checker_parts/part02.inc': 'b543e185ec415b512c0ca0421616404cc12a19a7',
    'scripts/r063_stage0_checker_parts/part03.inc': '4f1bbf72abed19dc7dc605371872ee31c501cebe',
    'scripts/r063_stage0_checker_parts/part04.inc': 'a1834a4b39a9d528760e67220b5fe5f368c9e655',
}
EXPECTED_ROW_DIGEST = '51891fbf9c3a66b1e00dfaa92fa6ae46984e4a6c99325624ec5b88371b66dcae'
EXPECTED_DISCOVERY_DIGEST = '6dd26e75436fb6740134590fc243b59ab9eb287cadbc46d417d5bbbb74022f0d'
EXPECTED_SECTOR_BRC = 110695538274255714208
EXPECTED_GATES = {
    'INPUT_ONLY_DISCOVERY_NO_BRANCH_HARDCODE',
    'SCALAR_SQRT_2500_EXACT',
    'SECTOR_NORM_ALGEBRA_TYPED',
    'C2_UNSCALED_SQUARE_LIFT_CLASSIFIED',
    'C3_SCALED_SQUARE_LIFT_CLASSIFIED',
    'C4_GAUSSIAN_FACTOR_ROUTE_CLASSIFIED',
    'DISCOVERED_COMPONENT_ROOTS_MATCH_D2500_EXACTLY',
    'NO_EXTRA_COMPONENT_ROOTS',
    'ALGEBRAIC_DERIVATION_VS_NATIVE_PATH_MULTIPLICITY_CLASSIFIED',
    'PATHIFICATION_FORMULA_EXACT',
    'HUGE_PATH_FIBER_COMPRESSED_REPRESENTATION_EXACT',
    'ONE_SECTOR_TOTAL_PATH_CARDINALITY_EXACT',
    'R061_TRACE_IDENTITY_COMPATIBILITY_PASS',
    'GENERAL_R_SQUARED_REGRESSION_R_LE_512_PASS_OR_MINIMAL_COUNTEREXAMPLE_PRESERVED',
    'NO_JUMP_COUNT_AS_NATIVE_LENGTH_LEAKAGE',
    'NO_CARRIER_VECTOR_RELATION_PROMOTED_TO_NATIVE_IDENTITY',
    'COMMITTED_DETERMINISTIC_CHECKER_PASS',
}
ARTIFACTS = (
    'R063_STAGE0_DISCOVERY_PHASE_FROZEN.json',
    'R063_STAGE0_SQRT2500_DISCOVERY_TREE.json',
    'R063_STAGE0_COMPONENT_ROOT_FIBER.json',
    'R063_STAGE0_PATH_CARDINALITY_CERTIFICATE.json',
    'R063_STAGE0_DERIVATION_PROVENANCE_GRAPH.json',
    'R063_STAGE0_GENERAL_SQUARE_REGRESSION.json',
    'R063_STAGE0_MISMATCHES.json',
    'R063_STAGE0_REPLAY_SUMMARY.json',
    'R063_STAGE0_PATH_ROOT_OPERATOR_CANDIDATE_MATRIX.md',
    'R063_STAGE0_SCALED_SQUARE_LIFT_THEOREM.md',
    'R063_STAGE0_GAUSSIAN_FACTOR_ROUTE_AUDIT.md',
    'R063_STAGE0_PATH_VALUED_SQRT_FORMULA.md',
    'R063_STAGE0_REPRODUCIBILITY_PROOF.md',
)

def require(test: bool, label: str) -> None:
    if not test:
        raise AssertionError(label)

def canon(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8')

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def original_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()

def verify_pins(repo: Path) -> dict[str, str]:
    pins = {}
    for rel, want in ORIGINAL.items():
        p = repo / rel
        require(p.is_file() and not p.is_symlink(), 'missing/unsafe original file: '+rel)
        actual = original_blob_sha1(p.read_bytes())
        require(actual == want, 'frozen Git blob mismatch: '+rel+' '+actual)
        pins[rel] = actual
    loader = repo / next(iter(ORIGINAL))
    require('exec(compile(_SOURCE' in loader.read_text(encoding='utf-8'), 'original loader no longer recognized')
    return pins

def read_json(directory: Path, basename: str) -> dict:
    data = json.loads((directory / basename).read_text(encoding='utf-8'))
    require(isinstance(data, dict), 'artifact not a JSON object '+basename)
    return data

def validate_outputs(output: Path, *, terminal: dict | None = None) -> dict:
    for name in ARTIFACTS:
        require((output / name).is_file(), 'missing original output '+name)
    discovery = read_json(output, 'R063_STAGE0_DISCOVERY_PHASE_FROZEN.json')
    discovery_core = {k:v for k,v in discovery.items() if k!='discovery_snapshot_sha256'}
    discovery_actual = sha256(canon(discovery_core))
    require(discovery.get('discovery_snapshot_sha256') == discovery_actual,
            'frozen discovery internal hash mismatch')
    require(discovery_actual == EXPECTED_DISCOVERY_DIGEST,
            'frozen discovery changed from historical original')
    regression = read_json(output, 'R063_STAGE0_GENERAL_SQUARE_REGRESSION.json')
    require(regression.get('r_range') == [1,512], 'regression did not cover exact 1..512')
    require(type(regression.get('tested_r_count')) is int and regression['tested_r_count']==512,
            'regression case count is not exactly 512')
    require(regression.get('combined_checker_mismatch_count') == 0,
            'C3/C4 original regression mismatch')
    require(regression.get('C3_mismatch_count') == 0 and regression.get('C4_mismatch_count') == 0,
            'original C3/C4 individual regression mismatch')
    require(regression.get('rows_sha256') == EXPECTED_ROW_DIGEST,
            'row digest differs from original 512-case frozen certificate')
    summary = read_json(output, 'R063_STAGE0_REPLAY_SUMMARY.json')
    core = {k:v for k,v in summary.items() if k!='summary_core_sha256'}
    require(sha256(canon(core)) == summary.get('summary_core_sha256'), 'summary core hash mismatch')
    require(summary.get('N') == 2500 and summary.get('r') == 50,
            'wrong original N/r')
    require(summary.get('discovery_snapshot_sha256') == discovery_actual,
            'summary/discovery snapshots disagree')
    require(summary.get('ordered_nonnegative_component_root_count') == 6,
            'wrong number of original sector roots')
    require(summary.get('one_sector_total_path_cardinality') == EXPECTED_SECTOR_BRC,
            'wrong exact original sector BRC')
    gr = summary.get('general_regression', {})
    require(gr.get('r_range') == [1,512] and gr.get('rows_sha256') == EXPECTED_ROW_DIGEST,
            'summary/regression disagree')
    gates = summary.get('acceptance_gates', {})
    require(set(gates) == EXPECTED_GATES and len(gates)==17,
            'not the exact 17 original acceptance gates')
    require(all(v is True for v in gates.values()), 'one or more acceptance gates failed')
    mismatches = read_json(output, 'R063_STAGE0_MISMATCHES.json')
    require(mismatches.get('mismatch_count') == 0, 'original mismatch artifact nonzero')
    if terminal is not None:
        require(terminal.get('status') == 'PASS', 'original terminal did not report PASS')
        require(terminal.get('discovery_snapshot_sha256') == discovery_actual,
                'terminal does not bind frozen discovery')
        require(terminal.get('general_regression_mismatch_count') == 0,
                'terminal regression mismatch')
        require(terminal.get('one_sector_total_path_cardinality') == EXPECTED_SECTOR_BRC,
                'terminal BRC mismatch')
    hashes = {name:sha256((output / name).read_bytes()) for name in ARTIFACTS}
    return dict(
        schema='R063_PINNED_NATIVE_REPLAY_ACCEPTANCE_HARNESS_V1',
        original_object='six pinned source files, N=2500, regression r=1..512',
        acceptance_gates=17,
        regression_rows_sha256=EXPECTED_ROW_DIGEST,
        discovery_sha256=discovery_actual,
        full_regression_cases=512,
        author_acceptance_only=True,
        independent_driver_review='NOT_PERFORMED',
        output_sha256=hashes,
    )

def original_replay(repo: Path, output_parent: Path, timeout_seconds: int) -> dict:
    pinned = verify_pins(repo)
    output_parent.mkdir(parents=True, exist_ok=True)
    out = Path(tempfile.mkdtemp(prefix='R063_NATIVE_FROZEN_', dir=output_parent))
    cmd = [sys.executable,
           str(repo / 'scripts/r063_stage0_validate_path_valued_sqrt_2500.py'),
           '--N','2500','--regression-max-r','512','--out',str(out)]
    p = subprocess.run(cmd, cwd=repo, capture_output=True, text=True,
                       timeout=timeout_seconds, check=False)
    (out/'native_original_stdout.txt').write_text(p.stdout,encoding='utf-8')
    (out/'native_original_stderr.txt').write_text(p.stderr,encoding='utf-8')
    require(p.returncode==0, 'original pinned program exit '+str(p.returncode))
    lines=[t.strip() for t in p.stdout.splitlines() if t.strip()]
    require(lines, 'missing original terminal JSON')
    terminal=json.loads(lines[-1])
    result=validate_outputs(out, terminal=terminal)
    result.update(output_directory=str(out),original_process_exit=p.returncode,
                  source_git_blobs=pinned,
                  stdout_sha256=sha256(p.stdout.encode('utf-8')),
                  stderr_sha256=sha256(p.stderr.encode('utf-8')))
    (out/'REPLAY_HARNESS_INDEPENDENT_ACCEPTANCE.json').write_bytes(canon(result)+b'\n')
    return result

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo-root',type=Path,required=True)
    ap.add_argument('--output-parent',type=Path,required=True)
    ap.add_argument('--timeout-seconds',type=int,default=1800)
    args=ap.parse_args()
    require(args.timeout_seconds>0, 'positive timeout required')
    report=original_replay(args.repo_root.resolve(),args.output_parent.resolve(),args.timeout_seconds)
    print(json.dumps(report,ensure_ascii=False,sort_keys=True))

if __name__=='__main__':
    main()
