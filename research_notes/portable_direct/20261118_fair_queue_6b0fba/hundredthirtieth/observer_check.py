"""Replay the public recorder and B01 consumer, print the exact C04 candidate manifest."""
import argparse
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import product
import json
from pathlib import Path

import numpy as np
from observer_api import (ALPHABET, B01Observer, B01_SHA256, Phase, Registers,
                          calibration_correlation, inverse_record, record)


def raw(model, preparation, word, *, histories=False, sheet=0):
    """Separate replay using actual positive CWM and B01 microinstructions."""
    source, brc = model.source, model.brc
    out = {}
    for z, mass in preparation:
        trace = [source.read(z)]
        weight = brc.cwm_edge(mass)
        for a in word:
            for instruction in source.instructions(z, a, sheet):
                z = source.primitive(z, instruction, sheet)
                weight = brc.cwm_propagate(weight, brc.CWM_ONE)
            trace.append(source.read(z))
        key = tuple(trace) if histories else trace[-1]
        out[key] = brc.cwm_recoalesce(out.get(key, brc.CWM_ZERO), weight)
    return out


def read_bins(model, preparation, word):
    entries = raw(model, preparation, word)
    return tuple(entries.get(key, model.brc.CWM_ZERO).total
                 for key in product(range(3), repeat=2))


def rank_mod101(matrix):
    matrix = matrix.copy() % 101
    rank = 0
    for col in range(matrix.shape[1]):
        indices = np.flatnonzero(matrix[rank:, col])
        if not len(indices):
            continue
        other = rank + indices[0]
        matrix[[rank, other]] = matrix[[other, rank]]
        row = matrix[rank] * pow(int(matrix[rank,col]), -1, 101) % 101
        matrix[rank+1:] = (matrix[rank+1:] - matrix[rank+1:,[col]] * row) % 101
        rank += 1
    return rank


def phase_checks(model):
    result = {}
    for copies in (9,27):
        pair = []
        for ready in (True,False):
            rows = []
            for j in range(3):
                for a in range(3 if copies == 27 else 1):
                    for t in range(3):
                        rows.append((Registers(j,a,a if ready else t), Fraction(1,copies)))
            bins = [Fraction(0)] * 3
            raw_mass = model.brc.CWM_ZERO
            for reg,w in rows:
                done = record(reg)
                bins[(done.receiver-done.source)%3] += w
                raw_mass = model.brc.cwm_recoalesce(raw_mass,model.brc.cwm_edge(w))
            phase = Phase(bins[0]-bins[2],bins[1]-bins[2])
            assert phase == calibration_correlation(rows) == Phase(int(ready),0)
            assert (raw_mass.count,raw_mass.total,raw_mass.dominant) == (copies,1,Fraction(1,copies))
            pair.append([str(x) for x in phase])
        result[str(copies)] = pair
    return result


def prepare(model, indices):
    return [(model.reps[int(i)],Fraction(1,len(indices))) for i in indices]


def finite_depth(model):
    pos = [12,13,14,21,22,23,156,157,158,165,166,167,300,301,302,309,310,311]
    neg = [9,10,11,18,19,20,153,154,155,162,163,164,297,298,299,306,307,308]
    starts = np.array(pos+neg)
    reached = [starts]
    counts = []
    for depth in range(7):
        counts.append(len(reached))
        for points in reached:
            a,b = np.split(model.labels[points],2)
            assert np.array_equal(np.bincount(a,minlength=9),np.bincount(b,minlength=9))
        if depth != 6:
            reached = [op[state] for state in reached for op in model.ops.values()]
    word = 'TTTFETE'
    rows = [prepare(model,indices) for indices in (pos,neg)]
    laws = [read_bins(model,row,word) for row in rows]
    assert laws[0][0]-laws[1][0] == Fraction(1,9)
    for row,law in zip(rows,laws):
        assert model.future_observer(row).read(word) == law
    return dict(positive_classes=pos,negative_classes=neg,equal_words_per_depth=counts,
                distinguishing_word=word,label=[0,0],raw_masses=[str(v[0]) for v in laws])


def main(repo,b01):
    model = B01Observer(repo,b01)
    source = model.source
    old_output = b01.with_name('feedback_checked.json')
    prior_digest = sha256(old_output.read_bytes()).hexdigest()
    assert prior_digest == '1cb0724840ed293fa4c69bdededf321017e11086dbbdf9cd698d4ebbdac2cfd0'
    prior = json.loads(old_output.read_text())
    path = 'research_tasks/RS-EULER-RR-20261012-12_C04_GEN2.md'
    data = (repo/path).read_bytes()
    spec_hash = sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    assert spec_hash == 'f8cba3d92f54faa6f1fe4bfa9aa4847822649a68'
    registers = [Registers(*e) for e in product(range(3),repeat=3)]
    assert all(record(inverse_record(r)) == inverse_record(record(r)) == r for r in registers)
    equiv = 0
    for slope,shift,z in product((1,2),range(3),registers):
        convert = lambda v: Registers(*((slope*i+shift)%3 for i in v))
        assert record(convert(z)) == convert(record(z))
        equiv += 1
    micro = 0
    for z,i in model.table.items():
        assert 3*source.read(z)[0]+source.read(z)[1] == model.labels[i]
        for letter,sheet in product(ALPHABET,range(2)):
            y = z
            for instruction in source.instructions(z,letter,sheet):
                y = source.primitive(y,instruction,sheet)
            assert y == source.fused(z,letter) and model.table[y] == model.ops[letter][i]
            if letter == 'E':
                assert y[:5] == z[:5] and Registers(y[0],y[5],y[6]) == record(Registers(z[0],z[5],z[6]))
            micro += 1
    assert len({source.transcript(z,'TTTTE') for z in model.reps}) == len(model.reps) == 432
    # Rebuild actual indicator rows from the recorded words, without elimination coefficients.
    rows = []
    for word,(j,d) in model.words:
        labs = model.labels
        for a in reversed(word):
            labs = labs[model.ops[a]]
        rows.append((labs == 3*j+d).astype(np.int64))
    matrix = np.stack(rows)
    assert rank_mod101(matrix) == 409
    ready = [i for i,z in enumerate(model.reps) if z[5] == z[6]]
    assert len(ready) == rank_mod101(matrix[:,ready]) == 144
    kernel = model.kernel
    assert np.array_equal(kernel[:,list(model.free)],np.eye(23,dtype=np.int64))
    assert (kernel.min(),kernel.max()) == (-1,1)
    assert np.all(np.count_nonzero(kernel == 1,axis=1)==18)
    assert np.all(np.count_nonzero(kernel == -1,axis=1)==18)
    assert not np.any(matrix@kernel.T)
    assert all(not np.any(matrix[:,perm]@kernel.T) for perm in model.ops.values())
    # Old B01 consumer asks for source projection after the actual feedback branch.
    efts = []
    for flip in (0,1):
        prep = [((0,s,0,1,0,s^flip,s^flip),Fraction(1,2)) for s in (0,1)]
        expected = read_bins(model,prep,'EFT')
        assert model.future_observer(prep).read('EFT') == expected
        efts.append([str(sum(expected[3*j:3*j+3])) for j in range(3)])
    assert efts == prior['ready_two_world_EFT_laws']
    # Distinct positive laws, same complete set of terminal responses, different histories.
    parts = [prepare(model,np.flatnonzero(kernel[0]==sgn)) for sgn in (1,-1)]
    encs = [model.future_observer(prep) for prep in parts]
    assert encs[0].coordinates == encs[1].coordinates
    example_words = ('','F','EFT','TTTTE','TEFFFFETTTTEEET')
    for prep,enc in zip(parts,encs):
        for word in example_words:
            assert read_bins(model,prep,word) == enc.read(word)
    history = [raw(model,part,'TTTTE',histories=True) for part in parts]
    assert not (history[0].keys() & history[1].keys())
    assert all(len(h)==18 and sum(x.total for x in h.values())==1 for h in history)
    # The terminal law preserves masses. CWM counts retain a different branch identity.
    z = model.reps[0]
    split = [[(z,Fraction(1))],[(z,Fraction(1,2)),(z,Fraction(1,2))]]
    assert model.future_observer(split[0]).coordinates == model.future_observer(split[1]).coordinates
    counts = [next(iter(raw(model,p,'T').values())).count for p in split]
    assert counts == [1,2]
    assert model.increments == (9,12,22,35,61,104,137,29)
    failures = 0
    for bad in (lambda: record(Registers(3,0,0)),
                lambda: model.future_observer([(z,0)]),lambda: model.future_observer([(z,0.5)]),
                lambda: model.future_observer([(z,Fraction(1,2))]),
                lambda: encs[0].read('G')):
        try:
            bad()
        except (ValueError,TypeError):
            failures += 1
    assert failures == 5
    return dict(registration='RS-EULER-RR-20261012-12',generation='TP2-01D3657A122132165C4B',
                inputs={'gen2_git_blob':spec_hash,'b01_sha256': B01_SHA256,
                        'b01_result_sha256':prior_digest,'pinned_git_blobs':source.PINS},
                source_regressions={'register_inputs':len(registers),'affine_relabelling_checks':equiv,
                                    'nine_and_27_phase_coefficients_ready_unprepared':phase_checks(model),
                                    'ready_EFT_source_laws':efts},
                independent_checks={'primitive_fused_class_comparisons':micro,'invalid_input_rejections':failures},
                effective_states=len(model.reps),worlds=len(model.table),
                basis_additions_by_depth=list(model.increments),independent_terminal_rows=409,rank_ready=144,
                certified_rows_sha256=sha256(matrix.astype('uint8').tobytes()).hexdigest(),
                kernel_shape=list(kernel.shape),kernel_positive_negative_per_row=[18,18],
                kernel_row_major_int8_sha256=sha256(kernel.astype('int8').tobytes()).hexdigest(),
                arbitrary_word_witness={'equal_signatures':True,'positive_worlds':[list(z) for z,w in parts[0]],
                       'negative_worlds':[list(z) for z,w in parts[1]],'mass_per_world':'1/18',
                       'direct_replay_words':list(example_words),'complete_TTTTE_transcript_TV':'1'},
                shortest_complete_radius=finite_depth(model),branch_refinement_counts=counts)


if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--b01',type=Path,default=Path(__file__).resolve().parent.parent/'hundredninth'/'feedback_check.py')
    args = parser.parse_args()
    print(json.dumps(main(args.repo.resolve(),args.b01.resolve()),ensure_ascii=False,indent=2,sort_keys=True))
