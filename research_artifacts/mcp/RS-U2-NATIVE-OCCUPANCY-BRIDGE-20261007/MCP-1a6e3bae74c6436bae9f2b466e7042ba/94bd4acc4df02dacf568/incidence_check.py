"""Bounded U2 incidence audit: real pinned BRC, two primitive-edge depths only.

This is a task-specific check, not a field-solver library or native admission.
No ordinary rational propagation, matrix arithmetic, pi or trig is substituted.
"""
from __future__ import annotations
import hashlib
import json
import argparse
import base64
import gzip
from pathlib import Path
import sys
import time

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'source'))
import packet_router as R

START = time.perf_counter()
CHECKS = 0
SEEN = []


def check(value, message):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(message)


def observe(state):
    SEEN.append(state)
    return state


def combine(states):
    return observe(R.total(states))


def chain(a, b):
    return observe(R.serial(a, b))


def atom(weight):
    return observe(R.edge(weight))


def blob(path):
    raw = path.read_bytes()
    return {'bytes': len(raw), 'git_blob_sha1': hashlib.sha1(
        b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest(),
        'sha256': hashlib.sha256(raw).hexdigest()}


# Globally consistent incidence: H_p consists of all listed triples containing p.
# Port 2*j is +E_(j+1), port 2*j+1 is -E_(j+1), in the full native X6.
H = ((0, 2, 4), (1, 3, 5), (6, 8, 10), (7, 9, 11), (0, 6, 8))
HP = {p: tuple(h for h in H if p in h) for p in R.PORTS}
rho = R.Q(1, 4)
lam = R.Q(1, 48)
attenuation = atom(rho)
bulk_edge = atom(lam)
seed = atom(R.Q(1, 12))
one = atom(1)
third = atom(R.Q(1, 3))
two_thirds = atom(R.Q(2, 3))
columns = {}
packet_basis = []
for p in R.PORTS:
    ps = R.packets(p, one, tag=('basis', p), incidence=HP[p])
    check(bool(ps), 'nonempty incidence for every signed input')
    packet_basis.extend(ps)
    columns[p] = R.marginals(ps)
    SEEN.extend(columns[p].values())
    check(combine(columns[p].values()).total == one.total, 'column mass conservation')
    check(columns[p][p].total == third.total, 'anchored diagonal mass 1/3')
    check(not columns[p][p ^ 1].live, 'opposite port excluded by distinct axes')
    turning = combine(v for q, v in columns[p].items() if R.axis(q) != R.axis(p))
    check(turning.total == two_thirds.total, 'pure-input exact 2/3 turning')
row = {q: combine(columns[p][q] for p in R.PORTS) for q in R.PORTS}
check(row[0].total == R.Q(4, 3), 'global-H row +E1 = 4/3')
check(row[1].total == R.Q(1), 'global-H row -E1 = 1')
check(combine(row.values()).total == R.Q(12), 'all row masses sum to 12')

# Enumerate the actual two-edge path/packet grammar, keeping every leaf separate.
# This preserves source, initial signed input, joint packet IDs, ordered ports,
# current signed input and raw chart-relative X6 endpoint. There is no state-key
# quotient before propagation and no deletion of a self-source contribution.
cells = (R.ZERO, R.advance(R.ZERO, 0))
occupied = set(cells)
layer = [{'source': b, 'initial_input': p, 'cell': z, 'incoming': p,
          'history': (), 'state': seed}
         for b, z in enumerate(cells) for p in R.PORTS]
layers = [layer]
emitted_packets = [0, 0]
for depth in (1, 2):
    nxt = []
    for parent_index, parent in enumerate(layer):
        z, p, state = parent['cell'], parent['incoming'], parent['state']
        if z in occupied:
            ps = R.packets(p, state,
                tag=('source', parent['source'], 'initial', parent['initial_input'],
                     'depth', depth, 'parent', parent_index),
                born_at=z, incidence=HP[p])
            emitted_packets[depth - 1] += len(ps)
            emissions = [(q, chain(packet.leg, attenuation), packet.tag)
                         for packet in ps for q in packet.ports]
        else:
            emissions = [(q, chain(state, bulk_edge), None) for q in R.PORTS]
        for q, contribution, packet_tag in emissions:
            target = R.advance(z, q)
            event = {'depth': depth, 'from': z, 'incoming': p,
                     'packet_tag': packet_tag, 'outgoing': q, 'to': target}
            nxt.append({'source': parent['source'], 'initial_input': parent['initial_input'],
                        'cell': target, 'incoming': q ^ 1,
                        'history': parent['history'] + (event,), 'state': contribution})
    layer = nxt
    layers.append(layer)

layer_cwm = [combine(item['state'] for item in layer) for layer in layers]
expected_total = atom(2)
for depth, actual in enumerate(layer_cwm):
    check(actual.total == expected_total.total, 'exact layer l1 mass')
    if depth != 2:
        expected_total = chain(expected_total, attenuation)

first = {}
returns = {}
predicted = {}
lam2 = chain(bulk_edge, bulk_edge)
for b in range(2):
    first[b] = {q: combine(item['state'] for item in layers[1]
                          if item['source'] == b and item['history'][0]['outgoing'] == q)
                for q in R.PORTS}
    for q in R.PORTS:
        check(first[b][q].total == chain(bulk_edge, row[q]).total,
              'first outgoing budget equals lambda times its row mass')
    returns[b] = combine(item['state'] for item in layers[2]
                         if item['source'] == b and item['cell'] == cells[b])
    neighboring_ports = [q for q in R.PORTS if R.advance(cells[b], q) in occupied]
    correction = chain(atom(3), combine(row[q] for q in neighboring_ports))
    coefficient = combine((atom(12), correction))
    predicted[b] = chain(lam2, coefficient)
    check(returns[b].total == predicted[b].total, 'corrected two-edge return formula')
check(returns[0].total == R.Q(1, 144), 'A own return is 16 lambda squared')
check(returns[1].total == R.Q(5, 768), 'B own return is 15 lambda squared')
check(returns[0].total != returns[1].total, 'equal occupied degree need not imply equal return')

R.CALLS['one_state_recurrent_cwm'] += 1
comparison = R.brc.one_state_recurrent_cwm([rho])
tail = chain(chain(atom(2), observe(comparison.depth(3))),
             atom(comparison.total_mass_closure))
check(tail.total == R.Q(1, 24), 'global omitted response after depth 2')
check(all(R.brc.is_positive_path_realizable(state) for state in SEEN),
      'all recorded finite CWM carriers positively realizable')

report = {
    'schema': 'U2_ANCHORED_INCIDENCE_TWO_EDGE_CHECK_V1',
    'status': 'CONDITIONAL_CIRCUIT_CERTIFICATE_NOT_NATIVE_ADMISSION',
    'task_id': 'RS-U2-NATIVE-OCCUPANCY-BRIDGE-20261007',
    'researcher_id': 'EM-DIRECT-FA0C27',
    'authorship': 'Temporary collaborator of the same authorized research execution; not independent review.',
    'source_commit': 'fe9ce58293ac77b72092512620e8670ca9be2d78',
    'source_pins': {'packet_router.py': blob(ROOT / 'source/packet_router.py'),
                    'brc_weighted.py': blob(R.SOURCE)},
    'reuse': {'family': 'T0_BRC', 'resolution': 'REUSE_EXECUTED_AND_COMPOSE_APPLIED',
             'entrypoints': ['packet_router.packets', 'packet_router.marginals',
                 'brc.cwm_edge', 'brc.cwm_propagate', 'brc.cwm_recoalesce',
                 'brc.one_state_recurrent_cwm'],
             'kernel_change': 'None: existing packet_router removes only two unused relative imports and checks all function/class ASTs unchanged.'},
    'typing': {'space': 'Full native X6; signed coordinates below are chart-relative displacements, not final Cell addresses.',
               'depth': 'Ordered primitive-edge relation depth, not physical time or heartbeat count.',
               'carrier': 'Positive CWM response, joint packet membership and complete depth-two path/source/port labels.',
               'observer': 'Source-separated first-port response and exact depth-two own return; global l1 mass and tail comparison.',
               'future_scope': 'Exactly the declared two-step history-blind branch law; full packet records retained. No signed amplitude or force cancellation.',
               'native_triad_admission': 'UNKNOWN; distinct-axis anchored circuit syntax alone does not establish TRIADIC_CLOSURE_E.',
               'native_occupancy_successor': 'UNKNOWN'},
    'input': {'global_H': H, 'anchored_H': HP, 'lambda': lam, 'rho': rho,
              'cells': cells, 'seed_per_source_input': seed,
              'kernel_scope': 'Same H at both materials; proof permits different anchored H at each material.'},
    'kernel_columns': columns, 'row_sums': row, 'first_step_by_source_and_port': first,
    'two_edge_self_returns': returns, 'two_edge_formula_check': predicted,
    'layer_cwm': layer_cwm, 'global_depth_gt_2_tail_bound': tail.total,
    'proof_boundary': 'Old degree-only formula needs sum of occupied-neighbor row masses = occupied degree. Row balance is equivalent only if required for every one-neighbor configuration with fixed kernel.',
    'resources': {'depth': 2, 'global_triple_classes': len(H),
                  'anchored_packet_basis_classes': len(packet_basis),
                  'labelled_layer_records': [len(x) for x in layers],
                  'emitted_joint_packets_by_depth': emitted_packets,
                  'actual_brc_calls': dict(R.CALLS), 'assertions': CHECKS,
                  'max_numerator_bits': max(v.total.numerator.bit_length() for v in SEEN),
                  'max_denominator_bits': max(v.total.denominator.bit_length() for v in SEEN),
                  'max_count_bits': max(v.count.bit_length() for v in SEEN),
                  'elapsed_seconds': time.perf_counter() - START,
                  'all_depth_path_count_finite_claimed': False},
    'labelled_layers': layers,
}
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--full-evidence', type=Path,
                    help='Optionally also retain the exact uncompressed full JSON at this path.')
args = parser.parse_args()
full = json.dumps(R.to_json(report), separators=(',', ':')).encode() + b'\n'
if args.full_evidence:
    args.full_evidence.write_bytes(full)
compressed = gzip.compress(full, compresslevel=9, mtime=0)
encoded = base64.b64encode(compressed) + b'\n'
archive = ROOT / 'incidence_trace.json.gz.b64'
archive.write_bytes(encoded)
summary = R.to_json(report)
del summary['labelled_layers']
summary['full_evidence_storage'] = {
    'encoding': 'gzip level 9, mtime=0; standard base64 plus final LF',
    'path': archive.name, 'uncompressed_bytes': len(full),
    'uncompressed_sha256': hashlib.sha256(full).hexdigest(),
    'gzip_bytes': len(compressed), 'gzip_sha256': hashlib.sha256(compressed).hexdigest(),
    'base64_bytes': len(encoded), 'base64_sha256': hashlib.sha256(encoded).hexdigest(),
    'lossless_roundtrip_verified': gzip.decompress(base64.b64decode(encoded)) == full,
    'retained_labelled_layer_records': [len(x) for x in layers],
    'compression_scope': 'Storage encoding only; no mathematical observer quotient or path deletion.'}
output = ROOT / 'incidence_check.json'
output.write_text(json.dumps(summary, separators=(',', ':')) + '\n')
print(json.dumps({'output': str(output), 'bytes': output.stat().st_size,
                  'archive_bytes': len(encoded), 'full_sha256': hashlib.sha256(full).hexdigest(),
                  'returns': R.to_json(returns), 'row_plus1': str(row[0].total),
                  'row_minus1': str(row[1].total), 'resources': report['resources']}))
