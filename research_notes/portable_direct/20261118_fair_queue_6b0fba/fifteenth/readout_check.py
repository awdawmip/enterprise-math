"""Audit of the frozen t=4 scalar readout and an exact native transport.

Archive-only mode rereads signed BRC receipts. --stage RP14_Run also runs
the actual frozen instrument on another modulus and checks every legal query.
No classical phase reference or ideal state propagation.
"""
import argparse
import base64
import gzip
import hashlib
import json
import os
import sys
from fractions import Fraction as F
from pathlib import Path

EVIDENCE_SHA = 'f72432fc27ca89136bb8cb2511344e9729d133f55d1ebe69f32b5f57dd5d6e13'
BANK_SHA = '79491e65feec104f2cdc9de510263efef749d8a1174f9cab4c20146a0171615c'
# These are reference labels, authenticated against a typed modular table below.
REF = (1, 2, 4, 8, 16, 11)
STEPS = (2, 4, 2, 1)


def digest(value):
    return hashlib.sha256(value).hexdigest()


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'))


def bits_for_coin(prob):
    den = prob.denominator
    return 2*(1-F(1, den)) if not den & (den-1) else F(2)


def coin(prob, bit):
    """0 denotes the plus outcome. Fresh unbiased bit() on each invocation."""
    num, den = prob.as_integer_ratio()
    if num in (0, den):
        return int(num == 0)
    while num:
        digit, num = divmod(2*num, den)
        u = bit()
        if type(u) is not int or u not in (0, 1):
            raise ValueError('fresh bit unavailable')
        if u != digit:
            return int(u > digit)
    return 1


def read_table(rec):
    folder = rec/'20260927_C6438C/qft_row_queries/readable_evidence'
    manifest = json.loads((folder/'INDEX.json').read_text())
    entry = next(x for x in manifest['artifacts'] if x['restore_path'].startswith('gram_research/'))
    chunks = []
    for part in entry['chunks']:
        raw = (folder.parent/part['path']).read_bytes()
        assert digest(raw) == part['text_sha256']
        chunks.append(base64.b64decode(raw))
    packed = b''.join(chunks)
    assert digest(packed) == entry['sha256'] == EVIDENCE_SHA
    data = json.loads(gzip.decompress(packed))
    assert data['source_bank']['payload_sha256'] == BANK_SHA
    case = next(c for c in data['cases'] if c['dimension'] == 61)
    assert case['retained_residual_nonzero'] and case['all_joint_branch_and_work_masses_equal']
    binding = case['prefix_evidence'][0]['oracle']
    # Verify the relabeling convention from the frozen forward/inverse receipts.
    columns = set()
    for item in case['prefix_evidence']:
        for cert in item['oracle']['typed_modular_certificates']:
            for c in cert['queried_columns']:
                columns.add((c['b'], c['source'], c['target']))
    for j, z in enumerate(REF):
        target = REF[(j+1) % 6]
        assert (2,z,target) in columns or (11,target,z) in columns

    table, weights, live = {}, {}, {}
    for item in case['prefix_evidence']:
        h = ''.join(map(str,item['history']))
        live[h] = set()
        for plan in item['transitions']:
            e, w = REF.index(plan['candidate']), REF.index(plan['latent_before'])
            assert e == (w + plan['auxiliary_bit']*STEPS[len(h)]) % 6
            key = h, e
            p = F(plan['bit_probability_given_proposed_label'])
            s = F(plan['proposal_norm_sum'])
            assert s > 0 and F(plan['plus_norm']) == 2*s*p
            assert F(plan['minus_norm']) == 2*s*(1-p)
            assert table.setdefault(key, p) == p and weights.setdefault(key,s/2) == s/2
            live[h].add(w)
    assert all(sum(v for (h,_),v in weights.items() if len(h)==i)==1 for i in range(4))
    children = {(tuple(c['history']),REF.index(z)):F(m)
                for c in case['checks'] for z,m in c['joint_label_masses']}
    for (h,e), p in table.items():
        for b,f in ((0,p),(1,1-p)):
            assert children.get((tuple(map(int,h+str(b))),e),0) == weights[h,e]*f
    return table, weights, live, binding, data['actual_BRC_core_calls']


class Readout:
    """Source-bound template. A new walker begins at work 1."""
    def __init__(self, program, table, live, binding):
        from lazy_streaming import LazyStreamingProgram
        if type(program) is not LazyStreamingProgram or program.t != 4 or program.dim != 61:
            raise ValueError('this template requires the frozen full t=4 program')
        if (program.codec is not None or canonical(program.phase_bindings) != canonical(binding['phase_bindings'])
                or canonical(program.h4_binding) != canonical(binding['native_two_H4_binding'])):
            raise ValueError('template word or instrument mismatch')
        # Prove order exactly six through a^2, a^3 and a^6; no orbit is input.
        square = program.tables[2][1]
        cube = program.tables[3][square]
        sixth = program.tables[1][square]  # a^4 times a^2
        if square == 1 or cube == 1 or sixth != 1:
            raise ValueError('six-cycle certificate unavailable')
        self.program = program
        self.exception = {key:p for key,p in table.items() if p != F(1,2)}
        self.live = {h:sum(1<<e for e in es) for h,es in live.items()}
        self.allowed = {h:sum(1<<e for g,e in table if h==g) for h in live}
        self.h, self.w, self.e = '', 1, 0

    def step(self, bit):
        i = len(self.h)
        if i >= 4 or not (self.live.get(self.h,0) >> self.e) & 1:
            raise ValueError('finished or invalid prefix')
        c = bit()
        if type(c) is not int or c not in (0,1):
            raise ValueError('fresh proposal bit unavailable')
        z = self.program.tables[i][self.w] if c else self.w
        e = (self.e+c*STEPS[i]) % 6
        if not (self.allowed[self.h] >> e) & 1:
            raise ValueError('zero proposal mass')
        p = self.exception.get((self.h,e),F(1,2))
        b = coin(p,bit)
        self.h, self.w, self.e = self.h+str(b), z, e
        return b, z


def live_test(rec, stage, table, live, binding):
    pkg, earlier = rec/'20260926_C6438C', rec/'20260926_0C08F0'
    os.environ.update(BRC_STAGE87_SOURCE=str(stage), BRC_STREAMING_PREVIOUS=str(earlier),
                      BRC_ZERO_ENDPOINT_SOURCE=str(earlier/'adversarial/zero_endpoint_extension.py'))
    for p in (stage,pkg/'new_word_compiler',pkg/'optimization/streaming',
              rec/'20260927_C6438C/qft_row_queries/gram_research'):
        sys.path.insert(0,str(p))
    from compiled_streaming import bank_from_compilation
    from single_walker import PointRowOracle, transition_plan
    from lazy_streaming import LazyStreamingProgram
    from stage45.brc_loop_recheck import CALLS, verify_vendor
    vendor = verify_vendor()
    raw = gzip.decompress((pkg/'direct_word_integration/DIRECT_WORD_INTEGRATION_RESULTS.json.gz').read_bytes())
    assert digest(raw)==BANK_SHA
    start = len(CALLS)
    bank = bank_from_compilation(json.loads(raw)['phase_compilation'],t=4,epsilon=F(1))['bank']
    program = LazyStreamingProgram(57,8,4,bank,61)
    walker = Readout(program,table,live,binding)
    # The checker obtains labels by native columns; the online walker does not enumerate them.
    zs = [1]
    for _ in range(5):
        zs.append(program.tables[3][zs[-1]])
    assert program.tables[3][zs[-1]] == 1 and len(set(zs))==6
    compared = 0
    for h, exponents in live.items():
        oracle = PointRowOracle(program,tuple(map(int,h)))
        for w in exponents:
            for c in (0,1):
                plan = transition_plan(oracle,zs[w],c)
                e = (w+c*STEPS[len(h)]) % 6
                assert plan['candidate']==zs[e]
                assert plan['bit_probability_given_proposed_label']==table[h,e]
                compared += 1
    # A deterministic execution tests wiring only. Distribution is checked by receipts/identities.
    tape = iter([0,1,0,0,0,1,0,0,0,0,1,1,1,1,1,1]*4)
    example = [walker.step(lambda:next(tape)) for _ in range(4)]
    bad = LazyStreamingProgram(15,2,4,bank,61)
    try:
        Readout(bad,table,live,binding)
    except ValueError as err:
        assert 'six-cycle' in str(err)
    else:
        raise AssertionError('wrong cycle accepted')
    return dict(input=[57,8,4], label_cycle=zs, comparisons=compared, sample=example,
                wrong_period_rejected=True, actual_BRC_core_calls=len(CALLS)-start,
                vendor_git_blob=vendor['git_blob'])


def check_coin(p,depth):
    # Compare the actual stopping program to exact counts on equiprobable cylinders.
    # Only unresolved cylinders need splitting; deterministic children are tallied.
    class NeedMore(Exception):
        pass

    def replay(prefix):
        cursor = iter(prefix)
        def bit():
            try:
                return next(cursor)
            except StopIteration:
                raise NeedMore
        try:
            return coin(p,bit)
        except NeedMore:
            return None

    plus_count = 0
    active = [()]
    for k in range(depth+1):
        pending = []
        for prefix in active:
            b = replay(prefix)
            if b is None:
                pending.append(prefix)
            elif b == 0:
                plus_count += 1
        target = p*(1<<k)
        assert plus_count == target.numerator//target.denominator
        assert len(pending) == int(target.denominator != 1)
        plus_count *= 2
        active = [prefix+(digit,) for prefix in pending for digit in (0,1)]


def distance(p,k):
    residue = (p*(1<<k)) % 1
    return min(residue,1-residue)/(1<<k)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,default=Path('/workspace/enterprise-math'))
    ap.add_argument('--stage',type=Path,help='frozen native RP14_Run source directory')
    ap.add_argument('--verify',type=Path,help='compare generated sections to a saved JSON')
    args=ap.parse_args()
    rec=args.repo.resolve()/'research_notes/directed_recovery'
    table,w,live,binding,old_calls=read_table(rec)
    for p in set(table.values())|{F(0)}:
        check_coin(p,32)
    expected=sum(w[k]*bits_for_coin(p) for k,p in table.items())
    long_mass=sum(w[k] for k,p in table.items() if p.denominator & (p.denominator-1))
    assert expected==F(9663675351,2147483648) and long_mass==F(13,32)
    for k in range(27,101):
        tv=sum(w[q]*distance(p,k) for q,p in table.items())
        assert tv==F(3 if k%2 else 5,32*(1<<k))
    out=dict(archive_sha256=EVIDENCE_SHA,phase_payload_sha256=BANK_SHA,
             archive_BRC_calls=old_calls,legal_history_label_cells=len(table),
             exceptional_cells=[[h,e,str(p)] for (h,e),p in sorted(table.items()) if p!=F(1,2)],
             live_masks={h:sum(1<<j for j in es) for h,es in live.items()},
             fair_default_mask={h:sum(1<<j for (g,j) in table if g==h) for h in live},
             nondyadic_mass=str(long_mass),expected_fresh_readout_bits=str(expected),
             expected_fresh_total_bits=str(4+expected),fixed_budget_identity_checked=[27,100],coin_prefix_counts_checked=[0,32])
    if args.stage:
        out['new_native_run']=live_test(rec,args.stage.resolve(),table,live,binding)
    if args.verify:
        saved=json.loads(args.verify.read_text())
        for key,value in json.loads(json.dumps(out)).items():
            assert value==saved[key], key
        print('PASS (including new native run)' if args.stage else 'PASS (frozen receipt audit)')
    else:
        print(json.dumps(out,sort_keys=True,indent=2))


if __name__=='__main__':
    main()
