"""Recover the numerical C2 window from archived S15 final outputs. Inputs stay local."""
import argparse
import gzip
import hashlib
import json
from collections import Counter
from functools import lru_cache
from pathlib import Path
from zipfile import ZipFile

Q, DEGREE, WORK = 512, 256, 11
POLICIES = ("s15_65", "s15_195")


def json_file(z, path):
    return json.loads(z.read(path))


def add(left, right, sign, half=False):
    out = {}
    for j in left.keys() | right.keys():
        x = left.get(j, 0) + sign * right.get(j, 0)
        if half:
            assert x % 2 == 0, "final lattice parity check"
            x //= 2
        if x:
            out[j] = x
    return out


def shift(a, amount):
    result = {}
    for j, v in a.items():
        new = (j + amount) % Q
        result[new % DEGREE] = v if new < DEGREE else -v
    return result


def recover(final, output_layer, output_slots):
    visited = set()

    @lru_cache(maxsize=None)
    def previous(level, slot):
        if level == 9:
            visited.add(slot)
            return final[slot]
        half = 1 << level
        left = slot & ~half
        right = left + half
        l, r = previous(level + 1, left), previous(level + 1, right)
        if slot == left:
            return add(l, r, 1, half=True)
        exponent = (left % half) * (Q // (2 * half))
        return shift(add(l, r, -1, half=True), -exponent)

    result = [previous(output_layer, s) for s in output_slots]
    return result, visited


def forward(p, q, exponent):
    twist = shift(q, exponent)
    return [add(p, twist, 1), add(p, twist, -1)]


def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def check(s15_path, c2_path):
    steps = []
    schedules = {}
    with ZipFile(c2_path) as f:
        ctx = json_file(f, "FIXED_WINDOW_CONTEXT.json")
    hist = ctx["historical_outputs"]
    origin = [257, 289]
    children = [257, 321, 289, 353]
    assert [(r["left_slot"], r["right_slot"], r["twiddle"]) for r in ctx["downstream"]] == [(257,321,4),(289,353,132)]
    assert ctx["origin_twiddle"] == 8 and ctx["source_step"] == 6 and ctx["work"] == WORK
    with ZipFile(s15_path) as z:
        mapping = {r["path"]: r for r in json_file(z, "s15/formal/OUTPUT_MAP.json")}
        for rep in (1, 2):
            schedules[rep] = {}
            for policy in POLICIES:
                prefix = f"s15/formal/run{rep}/{policy}/"
                ss = json_file(z, prefix + "DETERMINISTIC.json")["steps"]
                os = json_file(z, prefix + "CALIBRATION_ONLINE.json")
                aa = json_file(z, prefix + "CALIBRATION_PAIRS.json")
                assert len(ss) == len(os) == len(aa) == 48
                schedule = []
                for i, (s, o, a) in enumerate(zip(ss, os, aa)):
                    mapped = mapping[f"run{rep}/{policy}/outputs/{i:03}.json"]
                    assert s["output_sha256"] == mapped["sha256"] and s["output_bytes"] == mapped["bytes"]
                    assert i == s["step"] == o["step"] == a["step"] == mapped["step"]
                    assert o["method"] == a["selected_method"] == s["plan"]["method"] and a["full_joint_equal"]
                    schedule.append(dict(selected_method=o["method"], selected_key=o["reference_key_sha256"],
                                         alternative_method=a["alternative_method"], alternative_key=a["alternative_reference_key_sha256"],
                                         epoch=s["input_epoch"], sha256=mapped["sha256"], nbytes=mapped["bytes"],
                                         active_work_count=s["state_nonzero_work_columns"]))
                schedules[rep][policy] = schedule
        assert schedules[1] == schedules[2]
        for i in range(48):
            record = schedules[1][POLICIES[0]][i]
            other = schedules[1][POLICIES[1]][i]
            assert other["sha256"] == record["sha256"]
            b = gzip.decompress(z.read("s15/formal/output_pool/" + record["sha256"] + ".json.gz"))
            assert hashlib.sha256(b).hexdigest() == record["sha256"] and len(b) == record["nbytes"]
            data = json.loads(b)
            assert data["step"] == i and data["normalization"] == [1, Q] and data["input_epoch"] == record["epoch"]
            assert len(data["rows"]) == 21 * Q
            active = set()
            final = [None] * Q
            for rowno, (x, w, coeffs) in enumerate(data["rows"]):
                assert rowno == 21*x + w and 0 <= w < 21
                if coeffs:
                    active.add(w)
                if w == WORK:
                    final[x] = dict(coeffs)
                    assert len(final[x]) == len(coeffs)
                    assert all(0 <= e < DEGREE and isinstance(v, int) and v for e, v in final[x].items())
            assert len(active) == record["active_work_count"] == other["active_work_count"]
            outs, leaves_needed = recover(final, 7, children)
            layer6, _ = recover(final, 6, children)
            past, _ = recover(final, 5, origin)
            assert len(leaves_needed) == 16
            assert forward(past[0], past[1], 8) == [layer6[0], layer6[2]]
            assert forward(layer6[0], layer6[1], 4) == outs[:2]
            assert forward(layer6[2], layer6[3], 132) == outs[2:]
            if i == 6:
                assert past == [dict(ctx["p"]), dict(ctx["q"])]
                assert layer6 == [dict(hist["layer6_plus"]), dict(ctx["downstream"][0]["q"]),
                                   dict(hist["layer6_minus"]), dict(ctx["downstream"][1]["q"])]
                assert outs == [dict(hist["layer7_" + k]) for k in ("129_plus","129_minus","161_plus","161_minus")]
            local = [past, layer6, outs]
            twist = shift(past[1], 8)
            common = past[0].keys() & twist.keys()
            overlap_cancellations = sum(abs(past[0][j]) == abs(twist[j]) for j in common)
            copy_saving = 2 * len(past[0].keys() | twist.keys()) - overlap_cancellations
            assert copy_saving == len(layer6[0]) + len(layer6[2])
            steps.append(dict(step=i, epoch=record["epoch"], work11_present=WORK in active,
                              copy_saving_from_input=copy_saving,
                              selected_methods=[schedules[1][p][i]["selected_method"] for p in POLICIES],
                              selected_reference_keys=[schedules[1][p][i]["selected_key"] for p in POLICIES],
                              alternative_reference_keys=[schedules[1][p][i]["alternative_key"] for p in POLICIES],
                              four_leaf_support_sizes=[len(x) for x in outs], local_window_sha256=digest(local)))
    by_policy = {}
    for p in POLICIES:
        schedule = schedules[1][p]
        methods = {}
        for how in ("selected", "alternative"):
            for r in schedule:
                key = r[how + "_method"]
                methods.setdefault(how, {}).setdefault(key, Counter())[r[how + "_key"]] += 1
        by_policy[p] = dict(reference_keys_by_arm_and_method=methods,
                            work11_selected_full_steps=[s["step"] for s,r in zip(steps,schedule) if s["work11_present"] and r["selected_method"]=="full_fft"],
                            work11_alternative_full_steps=[s["step"] for s,r in zip(steps,schedule) if s["work11_present"] and r["alternative_method"]=="full_fft"])
    return {"official_output_map_paths": len(mapping), "official_output_pool_unique": len({r['sha256'] for r in mapping.values()}),
            "stable_budgets": list(POLICIES), "independent_runs_with_equal_schedules_and_outputs": 2,
            "work11_present_steps": [s["step"] for s in steps if s["work11_present"]],
            "work11_absent_steps": [s["step"] for s in steps if not s["work11_present"]],
            "all_four_nonempty_steps": [s["step"] for s in steps if all(s["four_leaf_support_sizes"])],
            "source_c2_historical_request7_verified_fields": "layer5 p/q, both layer6 outputs, both sibling right inputs, four layer7 outputs",
            "schedules": by_policy,"steps": steps}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--s15", required=True, type=Path)
    parser.add_argument("--c2", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    txt = json.dumps(check(args.s15, args.c2), indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(txt, encoding="utf-8")
    else:
        print(txt, end="")
