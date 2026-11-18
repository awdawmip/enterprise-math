"""Read-only replay of two fixed public codecs; exact conditional shard study.

This uses the public repository's Git objects and writes only to a temporary tree.
Python 3.12+, standard library.  The check, forward and rollback modes share
the frame registry and both unmodified source implementations.
"""
import argparse
from collections import Counter, defaultdict
from contextlib import redirect_stdout
import hashlib
from fractions import Fraction
from io import BytesIO, StringIO
from itertools import product
import json
from math import gcd, lcm
from pathlib import Path
import runpy
import subprocess
import sys
import tarfile
from tempfile import TemporaryDirectory


PIN = "d2984d1a0c5c8221ee103084dd3da68dd039dfaa"
PROTO = "research_notes/cell_address_adapter_v2_20260913_a8d47f21"
SPACE = "X6-fixed-native-chart"
ENVELOPE = "FIXED_X6_SLICE_ROLLBACK_V1"
EXPORTS = ("FinalCellAddress|encode_raw_slice|decode_raw_slice|step_cell|"
           "cell_step_distance|cell_squared_distance|validate_cell_address")


def dump(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))


def load_json(raw):
    def unique(pairs):
        obj = {}
        for k, v in pairs:
            if k in obj:
                raise ValueError("DUPLICATE_KEY")
            obj[k] = v
        return obj
    return json.loads(raw, object_pairs_hook=unique)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args])


def workspace(repo, root):
    paths = ["src/enterprise_math", "tests/test_cell_address_contract.py", "tools/validate_cell_address.py", PROTO]
    archive = git(repo, "archive", PIN, *paths)
    with tarfile.open(fileobj=BytesIO(archive)) as members:
        members.extractall(root, filter="data")
    source = root / PROTO
    frozen = json.loads((source / "results.json").read_bytes())
    sys.path[:0] = [str(source), str(root / "src")]
    argv = sys.argv
    try:
        sys.argv = ["test_adapter.py", "--geometry", str(root/"src/enterprise_math/geometry.py")]
        with redirect_stdout(StringIO()):
            old = runpy.run_path(str(source / "test_adapter.py"))
    finally:
        sys.argv = argv
    for key in ("status","scope","tests","negative_controls"):
        assert old["out"][key] == frozen[key]
    from enterprise_math import cell_address
    return old, cell_address


class Migration:
    def __init__(self, old, codec):
        self.ad = old["ad"]
        self.codec = codec

    def forward(self, legacy_json):
        # The codec alone erases the spelling; the receipt preserves its exact text.
        address = self.ad.load(legacy_json)
        key = self.ad.decode(address)
        if key.space != SPACE or any(key.native[2:]):
            raise ValueError("OUTSIDE_REGISTERED_SLICE")
        target = self.codec.encode_raw_slice(key.native[:2])
        return {"schema": ENVELOPE, "snapshot": PIN, "space": key.space, "v1": target.to_wire(),
                "legacy_json": legacy_json, "legacy_sha256": sha(legacy_json.encode("utf-8"))}

    def rollback(self, packet):
        needed = {"schema","snapshot","space","v1","legacy_json","legacy_sha256"}
        if type(packet) is not dict or set(packet) != needed or type(packet["legacy_json"]) is not str:
            raise ValueError("MALFORMED_MIGRATION_RECEIPT")
        # Parse the target with the same strict public loader, avoiding bool/int
        # and float/int comparisons accepting an unsupported version or coordinate.
        target = self.codec.FinalCellAddress.from_json(dump(packet["v1"]))
        replay = self.forward(packet["legacy_json"])
        if replay != packet or target.to_json() != dump(replay["v1"]):
            raise ValueError("ROLLBACK_RECEIPT_MISMATCH")
        return packet["legacy_json"]


def expect_reject(fn, exceptions=(TypeError,ValueError)):
    try:
        fn()
    except exceptions:
        return
    raise AssertionError("a negative control was accepted")


def snapshot_migration(old, migration):
    ad = migration.ad
    frames, keys = old["frames"], old["keys"]
    counts = Counter()
    cache = {}
    audited = hashlib.sha256()
    for key in keys:
        for frame in frames:
            raw = ad.dump(ad.encode(key,frame.tag))
            if any(key.native[2:]):
                expect_reject(lambda: migration.forward(raw))
                counts["outside"] += 1
                continue
            receipt = migration.forward(raw)
            assert migration.rollback(receipt) == raw
            idkey = receipt["space"], dump(receipt["v1"])
            assert cache.setdefault(idkey,key.native) == key.native
            audited.update(raw.encode()+b"\x00"+dump(receipt["v1"]).encode()+b"\n")
            counts["supported"] += 1
    assert len(cache)==9 and counts == {"supported":27,"outside":2160}
    return {"source_keys":len(keys),"distinct_supported_spatial_keys":len(cache),"spellings":dict(counts),
            "supported_legacy_to_target_sha256":audited.hexdigest()}


def timeline(old,migration):
    ad = migration.ad
    v1 = migration.codec
    counts = Counter()
    by_t = []
    audit = hashlib.sha256()
    for t in range(12):
        by_t.append(Counter())
    for ordinal,key in enumerate(old["keys"]):
        current = ad.encode(key,"A")
        for t in range(12):
            tag = old["frames"][(t+1)%3].tag
            nxt = ad.move(current,t%6,1,tag) if t%2 else ad.reframe(current,tag)
            source = ad.decode(current)
            target = ad.decode(nxt)
            inside = not any(source.native[2:]), not any(target.native[2:])
            status = {(True,True):"inside", (False,False):"outside",
                      (False,True):"enters", (True,False):"exits"}[inside]
            counts[status] += 1
            by_t[t][status] += 1
            # Clock and source ordinal discriminate repeated visits at the same cell.
            row = [ordinal,t,t+1,"move" if t%2 else "reframe",ad.dump(current),ad.dump(nxt)]
            if all(inside):
                converted = [migration.forward(x) for x in row[4:]]
                a,b = (v1.FinalCellAddress.from_wire(r["v1"]) for r in converted)
                if t%2:
                    assert t%6 in (0,1)
                    label = ("E1_FORWARD","E2_FORWARD")[t%6]
                    assert v1.step_cell(a,label)==b
                else:
                    assert a==b
                assert row == [*row[:4],*(migration.rollback(x) for x in converted)]
            else:
                # Preserve full source row as quarantined; never project a crossing.
                for ok, value in zip(inside,row[4:]):
                    if not ok:
                        expect_reject(lambda: migration.forward(value))
            audit.update((dump([row,status])+"\n").encode())
            current=nxt
    assert counts == {"inside":63,"outside":8640,"enters":18,"exits":27}
    return {"events":sum(counts.values()),"counts":dict(counts),"per_source_clock":[dict(c) for c in by_t],
            "time_and_full_legacy_event_sha256":audit.hexdigest()}


def edge_and_boundary(old,migration):
    ad, codec = migration.ad, migration.codec
    def canonical(records):
        old["canonical_edges"](ad,records)
        result = {}
        for row in records:
            a,b = (codec.FinalCellAddress.from_wire(migration.forward(ad.dump(x))["v1"])
                   for x in (row.source,row.target))
            axis,sign = row.axis,row.sign
            if axis not in (0,1) or sign not in (-1,1):
                raise ValueError("OUT_OF_SLICE_MOVE")
            label = ("E1","E2")[axis] + ("_FORWARD" if sign==1 else "_REVERSE")
            if codec.step_cell(a,label)!=b:
                raise ValueError("EDGE_DIRECTION_MISMATCH")
            value=(a.to_json(),b.to_json(),axis,sign,row.weight)
            if result.setdefault(row.edge_id,value)!=value:
                raise ValueError("CONFLICTING_EDGE_ID")
        return result
    records = old["records"]
    edges = canonical([*records,old["parallel"]])
    for k,v in old["with_parallel"].items():
        assert edges[k][2:] == v[2:] and edges[k][:2] == tuple(
            codec.encode_raw_slice(p.native[:2]).to_json() for p in v[:2])
    replace = old["replace"]
    expect_reject(lambda: canonical([*records,replace(records[0],weight=old["Fraction"](2,3))]))
    right = sorted(codec.decode_raw_slice(codec.FinalCellAddress.from_wire(
        migration.forward(ad.dump(a))["v1"]))[0] for a in old["correct"])
    wrong = sorted(codec.decode_raw_slice(codec.FinalCellAddress.from_wire(
        migration.forward(ad.dump(a))["v1"]))[0] for a in old["wrong_range"])
    assert right==[0,1,2] and wrong==[-1,0,1]
    init=codec.FinalCellAddress.from_wire(migration.forward(ad.dump(ad.encode(old["k0"],"A")))["v1"])
    assert init.coordinates==(0,1,1,0,0,0)
    assert old["S"].seeds != old["R"].seeds
    return {"source_declarations":len(records),"canonical_ids_with_parallel":sorted(edges),
            "two_step_path_weight_histogram":{str(w):n for w,n in old["hist"](old["with_parallel"].values()).items()},
            "naive_alias_paths":old["N"]["alias_branch_inflation"]["naive_two_step_paths"],
            "decoded_boundary":right,"numeric_range_counterexample":wrong,"initial_zero":init.to_wire()}


def negative_controls(root,old,migration):
    ad,v1=migration.ad,migration.codec
    A=ad.encode(old["k0"],"A")
    raw=ad.dump(A)
    pad="  "+raw+"\r\n"
    assert migration.rollback(migration.forward(pad)) == pad
    packet=migration.forward(raw)
    bad=load_json(raw)
    bad["frame"]["tag"]="unknown"
    expect_reject(lambda:migration.forward(dump(bad)))
    bad["frame"]["tag"]="A"
    bad["frame"]["offset"][0]+=1
    expect_reject(lambda:migration.forward(dump(bad)))
    expect_reject(lambda:migration.rollback(dict(packet,space="other")))
    expect_reject(lambda:migration.rollback(dict(packet,legacy_sha256="unrelated")))
    expect_reject(lambda:migration.rollback(dict(packet,v1=dict(packet["v1"],version=True))))
    expect_reject(lambda:migration.rollback(dict(packet,v1=dict(packet["v1"],coordinates=[1,0,1,0,0,0]))))
    expect_reject(lambda:migration.forward('{"version":2,"version":2}'))
    expect_reject(lambda:load_json('{"schema":1,"schema":1}'))
    expect_reject(lambda:migration.forward(dump(dict(load_json(raw),version=1))))
    a=v1.FinalCellAddress.from_wire(packet["v1"])
    expect_reject(lambda:old["g"].l1_distance(a,a))
    expect_reject(lambda:v1.step_cell(a,"E3_FORWARD"))
    cli=[sys.executable,str(root/"tools/validate_cell_address.py")]
    replies=[]
    for testspec in (packet["v1"],dict(packet["v1"],version=2)):
        run=subprocess.run(cli,input=dump(testspec),text=True,capture_output=True)
        replies.append(run.returncode)
        assert load_json(run.stdout)["valid"] == (run.returncode==0)
    assert replies==[0,2]
    return {"public_v1_cli_return_codes":replies,"noncanonical_wire_whitespace_rollback":True,
            "rejected":["unknown frame","altered registered offset","receipt namespace","receipt digest",
                        "bool V1 version","spliced target","duplicate V2 field","duplicate receipt field",
                        "V1 version on V2 wire","V1 in old L1 sequence","unsupported E3 step"]}


def shard_checks(codec):
    checked = 0
    examples = []
    for M,q in product(range(1,7),repeat=2):
        period=lcm(M,q)
        cells=defaultdict(list)
        for face in range(3):
            for a,b in product(range(1,period+1),repeat=2):
                digits=[a,b]
                digits.insert(face,0)
                obj=codec.FinalCellAddress(tuple(digits)+(0,0,0))
                native=codec.decode_raw_slice(obj)
                assert codec.encode_raw_slice(native)==obj
                cells[tuple(z%M for z in digits)].append(native)
        for u,v in product(range(q),repeat=2):
            h=gcd(q,M*u,M*v)
            offsets=(u,u+v,0)
            histogram=Counter()
            ambiguity=[]
            optimal_hits=0
            for z,raw in cells.items():
                base=u*z[0]+v*z[1]-(u+v)*z[2]
                expected={(base+off+j*h)%q for zi,off in zip(z,offsets) if zi==0 for j in range(q//h)}
                weights=Counter((u*m+v*n)%q for m,n in raw)
                actual=set(weights)
                optimal_hits+=max(weights.values())
                assert expected==actual
                histogram[len(actual)]+=1
                if not any(z):
                    ambiguity=sorted(actual)
            theory=Counter()
            for mask in range(1,8):
                indices=[i for i in range(3) if mask & (1<<i)]
                count=(M-1)**(3-len(indices))
                if count:
                    theory[(q//h)*len({offsets[i]%h for i in indices})]+=count
            assert histogram==theory and max(histogram)==len(ambiguity)
            error=1-Fraction(optimal_hits,3*period**2)
            distinct=len({o%h for o in offsets})
            correction=(0,0,2*M-1,3*M-1)[distinct]
            assert error==1-Fraction(h,q)*(1-Fraction(correction,3*M*M))
            if (M,q,u,v) in ((5,5,1,2),(6,6,0,2),(2,6,1,1),(5,6,3,0)):
                examples.append({"M":M,"q":q,"u":u,"v":v,"h":h,"zero_input_outputs":ambiguity,
                                 "fiber_size_histogram":dict(sorted(histogram.items())),"balanced_period_optimal_error":str(error)})
            checked+=1
    return {"parameter_sets":checked,"examples":examples,"M_and_q_ranges":[1,6]}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True,help="public enterprise-math Git clone containing the frozen commit")
    parser.add_argument("mode",choices=["check","forward","rollback"],nargs="?",default="check")
    args=parser.parse_args()
    with TemporaryDirectory() as folder:
        root=Path(folder)
        old,codec=workspace(args.repo,root)
        migration=Migration(old,codec)
        if args.mode=="forward":
            print(dump(migration.forward(sys.stdin.buffer.read().decode("utf-8"))))
        elif args.mode=="rollback":
            sys.stdout.buffer.write(migration.rollback(load_json(sys.stdin.buffer.read().decode("utf-8"))).encode("utf-8"))
        else:
            surfaces=git(args.repo,"grep","-l","-E",EXPORTS,PIN,"--","*.py").decode().splitlines()
            print(json.dumps({"upstream_git_commit":PIN,"pinned_V2_fixture_summary_replayed":True,
                              "typed_public_api_symbol_files":[s.split(":",1)[1] for s in surfaces],
                              "snapshot":snapshot_migration(old,migration),"timeline":timeline(old,migration),
                              "edges_and_boundary":edge_and_boundary(old,migration),
                              "controls":negative_controls(root,old,migration),"conditional_shards":shard_checks(codec),
                              "coverage_manifest":{"changed_in_local_study":["supported V2 research fixture to V1 envelope"],
                              "unaffected":["signed scalar geometry","native full key","layer and clock semantics"],
                              "gated":["off-slice endpoints","frame drift","conflicting edge declarations"],
                              "unavailable":["production cache configuration","production persisted backlog","full-X6 final codec"]}},
                             indent=2,sort_keys=True))


if __name__=="__main__":
    main()
