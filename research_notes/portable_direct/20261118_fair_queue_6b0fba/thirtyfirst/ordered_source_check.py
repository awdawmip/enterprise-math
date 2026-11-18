"""Replay the published HBW source hashes with user-supplied archives (Python 3).
The signed arithmetic and routing are imported from the verified source package.
Example: python ordered_source_check.py --archive record.zip --parent-archive parent.zip
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
from zipfile import ZipFile


PRIMARY = "261177ad99b11cb5bdd23dd37669db8426efc2148db170e9af715c1441af0506"
PARENT = "e290a2165763c99bcf714f34659fafd52706995567f72923ab499f261d9c8513"
PINS = {
    "REPORT.zh-CN.md": "08dd1b08a05d6991d3051cabc3f80071d61d97fa9be7b32449ce9fb5fca491e3",
    "THEOREMS.md": "58e24ea97366716c4155f513539306c8695206a49d720e8820b8ac632c01e204",
    "SUMMARY.json": "779bb73f6d69cfe705d69c9c350003d792fd5e9ca2f73773f8c3af9a1be1bea2",
    "MANIFEST.json": "d0a9c959957a1ada95fe09de15e608a9c41a25aab62973b42ad36872381bcd03",
    "SOURCE_BINDINGS.json": "b3df98d16c57d70544205ac7a1f5dbd8d0f23ab88f2a3c7c936e95347b3042e3",
    "run.py": "7765142879b0798998fbe3253da4fc751a0162d9b81206b4a584d0c0e336889b",
    "collision.py": "5ccfde3031cdc0c6c73690d55d6527605769fb1850c7a63900348992bbde1cd2",
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def checked_file(path, expected):
    raw = path.read_bytes()
    if sha(raw) != expected:
        raise ValueError(f"hash check failed for {path.name}")
    return raw


def check_manifest(manifest, read):
    for item in manifest["files"]:
        raw = read(item["path"])
        assert len(raw) == item["bytes"] and sha(raw) == item["sha256"], item["path"]
    return len(manifest["files"])


def bind_source(archive, parent, temp):
    if archive.is_dir():
        root = archive if (archive/"run.py").is_file() else archive/"heartbeat_record_quotient"
    else:
        checked_file(archive, PRIMARY)
        with ZipFile(archive) as z:
            for path in z.namelist():
                assert not Path(path).is_absolute() and ".." not in Path(path).parts
            z.extractall(temp)
        root = temp/"heartbeat_record_quotient"
    for name, pin in PINS.items():
        checked_file(root/name, pin)
    files = check_manifest(json.loads((root/"MANIFEST.json").read_bytes()), lambda p:(root/p).read_bytes())
    binding = json.loads((root/"SOURCE_BINDINGS.json").read_bytes())
    missing = []
    for name, pin in binding["files"].items():
        if (root/name).exists():
            checked_file(root/name, pin)
        else:
            missing.append(name)
    assert missing == ["inherited/MANIFEST.json"]
    parent_entries = None
    if parent:
        checked_file(parent, PARENT)
        with ZipFile(parent) as z:
            prefix = "heartbeat_collision_blocks/"
            raw = z.read(prefix+"MANIFEST.json")
            assert sha(raw) == binding["files"][missing[0]]
            parent_entries = check_manifest(json.loads(raw), lambda p:z.read(prefix+p))
    return root, {
        "primary_zip_sha256_verified": PRIMARY if not archive.is_dir() else None,
        "seven_public_file_hashes_verified": PINS, "primary_manifest_rows_verified": files,
        "bindings_verified_in_primary": len(binding["files"])-len(missing),
        "binding_only_in_parent": missing[0], "parent_zip_sha256_verified": PARENT if parent else None,
        "parent_manifest_rows_verified": parent_entries}


def load_runner(root):
    spec = importlib.util.spec_from_file_location("hbw_audit_frozen_collision", root/"collision.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Trial:
    def __init__(self, source):
        self.A = source.old.Arithmetic(limit=2_500_000)
        self.events, self.result, self.checks = [], {}, 0

    def check(self, label, passed):
        assert passed, label
        self.checks += 1


def archived_replay(root, module):
    trial = Trial(module.m)
    module.run(trial)
    assert trial.result == json.loads((root/"runs/collision/results.json").read_bytes())["result"]
    return {"assertions_passed":trial.checks, "cost":trial.A.stats(),
            "six_fixtures_match_saved_cases_exactly":True}


def work_table(arithmetic, count, modulus):
    values, residue = [], 1
    for _ in range(count):
        values.append(residue)
        residue = arithmetic.mul(2, residue)
        while residue >= modulus:
            residue = arithmetic.sub(residue, modulus)
    return values


def analyze(states, modulus, depth, record_count, denominator, saved, source, arithmetic):
    A = arithmetic
    table = work_table(A, record_count, modulus)
    groups, baseline, weights = {}, {}, {}
    for history, state in states.items():
        exponent = 0
        for bit in reversed(history):
            exponent = A.add(A.mul(2, exponent), bit)
        for visible, amplitude in state.items():
            groups.setdefault((visible, table[exponent]), []).append(amplitude)
            source.accumulate(A, baseline, visible, A.mul(amplitude, amplitude))
    absolute = 0
    for (visible, work), bucket in groups.items():
        joint = source.gather(A, bucket)
        total_abs = source.gather(A, (abs(x) for x in bucket))
        diag = source.gather(A, (A.mul(x,x) for x in bucket))
        source.accumulate(A, weights, visible, A.mul(joint, joint))
        absolute = A.add(absolute, A.sub(A.mul(total_abs,total_abs), diag))
    if depth in (4,6):
        frozen = {(tuple(row["key"][0]),row["key"][1]):row["mass"] for row in saved[str(modulus)]["truth"][str(depth)]["items"] if row["mass"]}
        assert source.snap(weights) == source.snap(frozen)
    delta = {v:A.sub(weights.get(v,0),baseline.get(v,0)) for v in weights.keys()|baseline.keys()}
    l1 = source.gather(A, (abs(x) for x in delta.values()))
    assert not source.gather(A, delta.values())
    face = {v:x for v,x in delta.items() if v[0][2] == 0}
    assert all(x>=0 for x in face.values())
    excess = source.gather(A, face.values())
    assert (l1>0) == (excess>0)
    return {"N":modulus, "T":depth, "numerator_L1":l1, "numerator_absolute_bound":absolute,
            "squared_mass_denominator_Q":denominator, "face_excess_numerator_over_Q":excess}


def replay_from_initial(root, source):
    arithmetic = source.old.Arithmetic(limit=2_500_000)
    frames = json.loads((root/"runs/exhaustive/results.json").read_bytes())["result"]["frames"]
    saved = json.loads((root/"inherited/INPUTS.json").read_bytes())["moduli"]
    states = {():{(source.ORIGIN,0):1}}
    denominator, count = 1, 1
    rows = []
    for depth in range(1,8):
        next_states = {}
        for history, state in states.items():
            children = source.split_step(arithmetic,state)
            norms = [source.norm(arithmetic, child) for child in children]
            assert arithmetic.add(*norms) == arithmetic.mul(9,source.norm(arithmetic,state))
            for bit, child in enumerate(children):
                next_states[history+(bit,)] = child
        states = next_states
        denominator = arithmetic.mul(denominator,9)
        count = arithmetic.mul(count,2)
        if depth<=6:
            assert len(states)==len(frames[str(depth)])
            assert all(source.snap(states[tuple(row["bits"])])==row["state"] for row in frames[str(depth)])
        if depth==3:
            key = ((2,0,1,0,0,0),0)
            assert states[(0,0,0)][key]==-8
            assert arithmetic.mul(-8,-8)==64 and arithmetic.add(arithmetic.mul(-4,-4),arithmetic.mul(-4,-4))==32
        for modulus in (21,35,77):
            rows.append(analyze(states,modulus,depth,count,denominator,saved,source,arithmetic))
    return {"initial_visible_and_work":[[0,0,0,0,0,0],0,1],
            "retained_keys":"ordered record, six coordinates, final port, modular work",
            "source_kernels":["collision.run","run.split_step","run.old.Arithmetic"],
            "saved_record_tree_depths_replayed":[1,2,3,4,5,6],"new_depth":7,
            "T3_coherent_vs_individually_squared":[64,32],"new_source_replay_cost":arithmetic.stats(),
            "rows":rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive",type=Path,required=True,help="verified main ZIP or its unmodified extracted folder")
    parser.add_argument("--parent-archive",type=Path,help="optional predecessor ZIP for cross-archive manifest verification")
    args = parser.parse_args()
    with tempfile.TemporaryDirectory() as temp:
        root, audit = bind_source(args.archive,args.parent_archive,Path(temp))
        coll = load_runner(root)
        out = {"source_bindings":audit,"archived_source_replay":archived_replay(root,coll),
               "independent_regrouping":replay_from_initial(root,coll.m)}
        print(json.dumps(out,indent=2))


if __name__=="__main__":
    main()
