"""Replay frozen U27 transitions. Run with --bundle-dir /path/to/em_u27_followup."""
import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys

Q = Fraction
MANIFEST_SHA = "e6a86c8ab44f674b126844358e893d893d0c58b6e16353c89660ff35adfafdb5"
ARCHIVE_SHA = "a450cc3e235ca3d37211d31b2d4eb41dd2d4ac28b77c73d18d1b6e3ce45cc9a7"


def load(root):
    data = (root / "PACKAGE_MANIFEST.json").read_bytes()
    assert sha256(data).hexdigest() == MANIFEST_SHA
    entries = json.loads(data)["files"]
    for name, fields in entries.items():
        raw = (root / name).read_bytes()
        assert len(raw) == fields["bytes"] and sha256(raw).hexdigest() == fields["sha256"], name
    path = root / "baseline/cell_u27/work_exposure.py"
    spec = importlib.util.spec_from_file_location("f07_pinned_u27", path)
    u = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = u
    spec.loader.exec_module(u)
    return u, len(entries)


def tv(p, q):
    return sum(abs(p.get(x, 0) - q.get(x, 0)) for x in p.keys() | q.keys()) / 2


class SourceChain:
    """The source labels are not conditioned or renormalized. Store committed macro state."""

    def __init__(self, u, cap, episode):
        self.u = u
        self.episode = episode
        self.k = u.v.Episode(cap) if episode else u.v.Capped(cap, Q(1, 16))
        self.initial = (u.f.root_state(), None, False)
        self.rows = {}
        self.evaluations = 0

    def row(self, x):
        if x in self.rows:
            return self.rows[x]
        s, missing_side, done = x
        u = self.u
        if done:
            return {x: u.ONE}
        out = {}
        for label, q in self.k.proposals:
            self.evaluations += 1
            for y, w, _ in self.k.transition(s, label, q):
                if not w.live:
                    continue
                # Episode returns absolute states. OneContact canonicalizes internally.
                if self.episode and y != s:
                    y = u.f.canonical(y)
                edge, complete = missing_side, False
                if self.episode and len(y.paths.links) != len(s.paths.links):
                    if edge is None:
                        edge, = set(s.paths.table()) - set(y.paths.table())
                    else:
                        assert edge in y.paths.table()
                        complete = True
                u.add(out, (y, edge, complete), w)
        assert u.r.total(out.values()).total == 1
        self.rows[x] = out
        return out

    def advance(self, law, safe_cap=None):
        u = self.u
        nxt = {}
        for x, weight in law.items():
            for y, edge in self.row(x).items():
                if safe_cap is None or y[0].paths.length() <= safe_cap:
                    u.add(nxt, y, u.r.serial(weight, edge))
        return nxt


def totals(law):
    return {x: w.total for x, w in law.items()}


def survival_summary(u, chains):
    report = {}
    for kind, caps in chains.items():
        hazards = {}
        for cap, chain in caps.items():
            surv = {chain.initial: u.ONE}
            rows = []
            for t in range(1, 4):
                surv = chain.advance(surv, 4)
                rows.append({"steps": t, "safe_reachable_states": len(surv),
                             "first_exit_by_t": str(1 - u.r.total(surv.values()).total)})
            hazards[str(cap)] = rows
        assert hazards["5"][1]["first_exit_by_t"] == "0"
        assert Q(hazards["5"][2]["first_exit_by_t"]) > 0
        assert Q(hazards["6"][0]["first_exit_by_t"]) == Q(11, 221280)
        report[kind] = hazards
    return report


def observation(u, small, large):
    init = small.initial
    a, b = small.row(init), large.row(init)
    root_modes = lambda x: x[0].modes
    def modes(law):
        out = {}
        for x, w in law.items():
            u.add(out, root_modes(x), w)
        return totals(out)
    mode_tv = tv(modes(a), modes(b))
    full_at_one = tv(totals(a), totals(b))
    assert mode_tv == 0 and full_at_one == Q(11, 221280)
    safe = {x: w for x, w in b.items() if x[0].paths.length() <= 4}
    survival = u.r.total(large.advance(safe, 4).values())
    path_tv = 1 - survival.total
    a2, b2 = small.advance(a), large.advance(b)
    endpoint_tv = tv(totals(a2), totals(b2))
    assert 0 < endpoint_tv < path_tv
    return {"mode_TV_1": str(mode_tv), "state_TV_1": str(full_at_one),
            "state_TV_2": str(endpoint_tv), "path_TV_2": str(path_tv),
            "difference_at_2": str(path_tv - endpoint_tv),
            "endpoint_support_2": [len(a2), len(b2)]}


def work_example(u, b, delta_list):
    v, f, r = u.v, u.f, u.r
    kernel = v.Episode(b)
    s = f.root_state()
    ledger = v.Ledger(s, b)
    prep_mass = u.ONE
    labels = [('mode', (2, 3)), ('mode', f.EDGE), ('contact', f.EDGE, 0)]
    prep_stages = []
    for label in labels:
        y, w = v.accepted(kernel, s, label)
        prep_mass = r.serial(prep_mass, w)
        prep_stages.append(ledger.commit(label, y))
        s = y
    assert prep_mass.total == Q(1, 802816) and len(s.paths.links) == 3
    label = ('body', 0, 4, True)
    branches = kernel.transition(s, label, dict(kernel.proposals)[label])
    target, w, tag = branches[0]
    assert w.total == Q(1, 885120)
    start = len(ledger.log)
    work = ledger.commit(label, target)
    frames = list(u.references(s, target, ledger.log[start:]))
    # Compare the actual carried IDs with the published deterministic compiler.
    # A fresh Ledger may relabel records; matching here is on stages and eligibility only.
    rebuilt = u.compile_branch(s, label, f.canonical(target), b)
    assert [(x['frame']['kind'], set(x['eligible'])) for x in rebuilt] == [
        (x['frame']['kind'], set(x['eligible'])) for x in frames]
    assert work == v.work_cost(s, label, f.canonical(target), b)
    before_position = s.paths.cells[0]
    after_position = target.paths.cells[0]
    for item in frames:
        assert set(item['eligible']) == {(2, 3)}
    assert all(pos == after_position for pos in ledger.free.values())
    out = []
    for delta in delta_list:
        alive, loss, sw, fw, trace = u.exposure_transfer(frames, delta)
        h = delta / 49
        assert alive.total == (1-h)**work
        assert sw.total + fw.total == sum((1-h)**j for j in range(work))
        out.append({"delta": str(delta), "loss": str(loss.total),
                    "expected_executed_work": str(sw.total + fw.total),
                    "survival": str(alive.total)})
    return {"B": b, "prep_full_positive_mass": str(prep_mass.total),
            "prep_delivery_stages": prep_stages, "branch_mass": str(w.total), "tag":tag,
            "old_length":s.paths.length(), "new_length":target.paths.length(), "work": work,
            "peak_bound_count":max(len(i['frame']['bound']) for i in frames),
            "peak_held_count":max(len(i['frame']['held']) for i in frames),
            "old_depot":before_position,"new_depot":after_position,
            "final_free_ids_at_new_depot":sorted(ledger.free),
            "stages":[i['frame']['kind'] for i in frames], "resource_trace":[
                {key:sorted(item['frame'][key]) for key in ('bound','free','held')}
                for item in frames], "exposure":out}


def completed_repair(u, cap, deltas):
    v, r = u.v, u.r
    k = v.Episode(cap)
    s = u.f.root_state()
    ledger = v.Ledger(s, cap)
    prepare = [('mode', (2,3)), ('mode', u.f.EDGE), ('contact', u.f.EDGE, 0)]
    word = [('body',0,4,True), ('body',0,5,False), ('contact',u.f.EDGE,0)]
    frames, costs, lengths = [], [], []
    mass = u.ONE
    for label in prepare:
        y, _ = v.accepted(k, s, label)
        ledger.commit(label,y)
        s = y
    for label in word:
        y, branch = v.accepted(k,s,label)
        start = len(ledger.log)
        costs.append(ledger.commit(label,y))
        frames.extend(u.references(s,y,ledger.log[start:]))
        lengths.append(y.paths.length())
        mass = r.serial(mass,branch)
        s = y
    assert u.f.EDGE in s.paths.table() and ledger.validate(stable=True) is not None
    assert mass.total == Q(1,799759027200)
    counts = [len(item['eligible']) for item in frames]
    assert counts == [1]*(len(frames)-2)+[2,2]
    risks = []
    for d in deltas:
        alive, loss, sw, fw, trace = u.exposure_transfer(frames,d)
        h = d/49
        assert alive.total == (1-h)**(len(frames)-2)*(1-2*h)**2
        # Nonnegative second moment from stopped probabilities in the published trace.
        second = r.serial(alive,u.E(len(frames)**2))
        for item in trace:
            second = r.merge(second,u.scale(u.E(item['first_new_loss_mass']),item['stage']**2))
        survival_before = [Q(1)] + [item['survival'] for item in trace[:-1]]
        assert second.total == sum((2*j+1)*q for j,q in enumerate(survival_before))
        risks.append(dict(delta=str(d),survival=str(alive.total),first_loss=str(loss.total),
                          work_mean=str(sw.total+fw.total),work_second_moment=str(second.total)))
    return dict(B=cap,word=word,word_mass_from_damaged=str(mass.total),work_by_step=costs,
                lengths_after=lengths,eligible_counts=counts,results=risks,
                peak_in_use=max(len(item['frame']['bound'])+len(item['frame']['held']) for item in frames),
                free_ids_at_final_depot=sorted(ledger.free))


def detection_witnesses(u):
    out = []
    grow = ('pair',(0,1),0,4,True)
    for b in range(4,17):
        for gap in (1,2):
            t = (b-4)//2+1
            require_release = gap == 1 and b%2 == 0
            k = u.v.Episode(b+gap)
            if require_release:
                word = [('mode',u.f.EDGE),('contact',u.f.EDGE,0)]+[grow]*t
                t += 2
            else:
                word = [grow]*t
            s = u.f.root_state()
            mass = u.ONE
            for ix,label in enumerate(word):
                s, branch = u.v.accepted(k,s,label)
                mass = u.r.serial(mass,branch)
                assert (s.paths.length()>b) == (ix==len(word)-1)
            assert mass.live and len(word)==t
            out.append(dict(B=b,gap=gap,first_distinguishing_step=t,final_length=s.paths.length()))
    return out


def pair_bound(u, s):
    k = u.v.Capped(7, Q(1,16))
    out = []
    for current in (u.f.root_state(), s):
        weights = []
        for label,q in k.proposals:
            if label[0] != 'pair' or not label[-1] or label[1] not in current.paths.table():
                continue
            y,w = u.v.accepted(k,current,label)
            assert y.paths.length() == current.paths.length()+2 and w.total == Q(1,9216*2305)
            weights.append(w)
        out.append({"links":len(current.paths.links), "growing_label_count":len(weights),
                    "total_mass":str(u.r.total(weights).total)})
    assert out[1]['total_mass'] == str(Q(1,295040))
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bundle-dir', type=Path, required=True)
    root = parser.parse_args().bundle_dir
    u, count = load(root)
    fixture = json.loads((root/'fixtures/base_case.json').read_text())
    assert fixture['inventory_B'] == 4 and Q(fixture['pre_release_epsilon']) == Q(1,16)
    assert tuple(map(tuple,fixture['body_cells'])) == u.f.root_state().paths.cells
    deltas = list(map(Q,fixture['work_loss_delta_reference']))
    caps = {name:{b:SourceChain(u,b,episode) for b in (4,5,6)}
            for name,episode in [('persistent_BC',False),('episode_first_side',True)]}
    report = survival_summary(u,caps)
    contraction = observation(u,caps['persistent_BC'][4],caps['persistent_BC'][6])
    # Full common row at the damaged state, including original labels & result tags.
    k = caps['episode_first_side'][6].k
    s = u.f.root_state()
    for label in [('mode',(2,3)),('mode',u.f.EDGE),('contact',u.f.EDGE,0)]:
        s, _ = u.v.accepted(k,s,label)
    def tagged_row(b):
        out = {}
        kern = u.v.Episode(b)
        for label,q in kern.proposals:
            for y,w,tag in kern.transition(s,label,q):
                u.add(out,(label,y,tag),w)
        return out
    first, second = tagged_row(5), tagged_row(6)
    assert first == second and u.r.total(first.values()).total == 1
    result = {
        "source":{"full_archive_sha256":ARCHIVE_SHA,"manifest_sha256":MANIFEST_SHA,
                  "manifest_entries_verified":count,"lambda":"1/48","epsilon":"1/16",
                  "labels_per_row":len(k.proposals)},
        "clock":"committed macro proposals; episode stops on recapture; work costs count ledger frames",
        "baseline_four_time_hitting":report,"data_processing":contraction,
        "damaged_common_row":{"B":[5,6],"distinct_label_state_tag_atoms":len(first),"TV":"0"},
        "reachable_damaged_branch":[work_example(u,b,deltas) for b in (4,5,6)],
        "complete_repair_word":[completed_repair(u,b,deltas) for b in (5,6)],
        "resource_observer_scope":{"macro":"canonical named words, modes, episode first lost side and completion; full successive states",
            "stages":"ordered free/bound/held IDs, positions, working label and completed/pending incidence",
            "first_loss":"first eligible release at a stage; other T05 events retain their own rules"},
        "earliest_hit_positive_witnesses":detection_witnesses(u),
        "pair_growth_check":pair_bound(u,s),
        "evaluated_macro_rows":{name:{str(b):len(ch.rows) for b,ch in data.items()}
                                for name,data in caps.items()},
        "executed_macro_transition_label_calls":{name:{str(b):ch.evaluations for b,ch in data.items()}
                                for name,data in caps.items()}}
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))


if __name__ == '__main__':
    main()
