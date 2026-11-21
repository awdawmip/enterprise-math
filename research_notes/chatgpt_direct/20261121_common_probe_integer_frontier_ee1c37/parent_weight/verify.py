"""Exact weighted obstruction after the complete parent-family classification.

No LP/MILP solver or floating arithmetic is used. The only inherited census
facts are completeness of the 250 mothers and the native orbit representatives
for the two proper minimum-cost types. Every expanded proper class is priced
and checked against the original forbidden triples.
"""
from pathlib import Path
from itertools import combinations, permutations, product
from collections import Counter
from hashlib import sha256
import argparse
import json
import struct
import time

COORD = [(i//25, i//5%5, i%5) for i in range(125)]
DOMAIN = (1 << 125)-1
TYPES = {(9,557):24000, (10,744):12000}


def points(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length()-1
        mask ^= bit


def move(mask, shift=(0,0,0), scale=1, signs=(1,1,1)):
    out = 0
    for p in points(mask):
        x = COORD[p]
        y = [(scale*signs[j]*x[j]+shift[j]) % 5 for j in range(3)]
        out |= 1 << (25*y[0]+5*y[1]+y[2])
    return out


def center(mask):
    values = []
    for axis in range(3):
        counts = [sum(COORD[p][axis] == value for p in points(mask)) for value in range(5)]
        assert sorted(counts) == [2,2,2,2,5]
        values.append(counts.index(5))
    return 25*values[0]+5*values[1]+values[2]


def main():
    here = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--parent-result', type=Path, default=here.parent/'parent_integer/result.json')
    ap.add_argument('--native-inputs', type=Path, default=here.parent/'integer_cuts/mother12/native_sublevels/inputs')
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--bank', type=Path, help='Optional comparison with the inherited complete discovery bank')
    args = ap.parse_args(); args.output.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    parent_data = args.parent_result.read_bytes(); parent_doc = json.loads(parent_data)
    assert parent_doc['status'] == 'COMPLETE_NATIVE_PARENT_FAMILY_CLASSIFICATION'
    assert parent_doc['cost_profile'] == [[9,557,2],[10,744,5],[11,936,2],[11,944,1],[12,1104,2]]
    parent_raw = (args.native_inputs/'parent').read_bytes()
    assert sha256(parent_raw).hexdigest() == parent_doc['parent_sha256']
    mothers = {int(a)+(int(b)<<64) for a,b in map(str.split,parent_raw.decode().splitlines()[:250])}
    assert len(mothers) == 250 and all(m.bit_count() == 13 for m in mothers)
    centers = {m:center(m) for m in mothers}
    assert max((a&b).bit_count() for a,b in combinations(mothers,2)) == 3
    normalized = {tuple(sorted(map(int,row['parents']))) for row in parent_doc['normalized_embedded_feasible_parent_families']}
    assert len(normalized) == 4
    base = next(family for family in normalized if all(len(set(COORD[centers[m]])) == 1 for m in family))
    reflected = {tuple(sorted(move(m,signs=(1,s,t)) for m in base)) for s,t in product((1,-1), repeat=2)}
    assert reflected == normalized
    families = {tuple(sorted(move(m, shift, scale) for m in family))
                for family in normalized for shift in COORD for scale in (1,2)}
    assert len(families) == parent_doc['all_parent_family_count'] == 200
    weights = set()
    for family in families:
        union = 0; marked = 0
        for m in family:
            assert m in mothers and not(m & union)
            union |= m; marked |= 1 << centers[m]
        assert union.bit_count() == 65 and marked.bit_count() == 5
        weights.add((union,marked))
    assert len(weights) == 100
    base_union = sum(base); base_marked = sum(1 << centers[m] for m in base)
    distinct = sum(1 << p for p,x in enumerate(COORD) if len(set(x)) == 3)
    equal = sum(1 << p for p,x in enumerate(COORD) if len(set(x)) == 1)
    assert base_union == distinct|equal and base_marked == equal

    native_raw = (args.native_inputs/'obs').read_bytes()
    assert sha256(native_raw).hexdigest() == parent_doc['obs_sha256']
    header = 125*125*32
    observations = [int.from_bytes(native_raw[i:i+32],'little') for i in range(0,header,32)]
    forbidden = {sum(1<<p for p in native_raw[i:i+3]) for i in range(header,len(native_raw),3)}
    assert len(forbidden) == 47000
    def price(ids):
        total = 0
        for x in ids:
            combined = 0
            for y in ids: combined |= observations[125*x+y]
            total += combined.bit_count()
        return total

    seed_data = (here/'proper_seeds.json').read_bytes(); seeds = json.loads(seed_data)
    linears = set()
    for order in permutations(range(3)):
        for signs in product((1,-1),repeat=3):
            for scale in (1,2):
                linears.add(tuple(25*((scale*signs[0]*x[order[0]])%5)
                                  +5*((scale*signs[1]*x[order[1]])%5)
                                  +(scale*signs[2]*x[order[2]])%5 for x in COORD))
    assert len(linears) == 96
    shifts = [tuple(1 << (25*((x[0]+s[0])%5)+5*((x[1]+s[1])%5)+(x[2]+s[2])%5) for x in COORD) for s in COORD]
    banks = {kind:set() for kind in TYPES}; orbit_counts = []
    for seed in seeds['representatives']:
        kind = (seed['size'], seed['cost']); ids = seed['points']
        assert kind in banks and len(ids) == kind[0]
        assert sum(1<<p for p in ids) == int(seed['mask'])
        orbit = set()
        for linear in linears:
            image = [linear[p] for p in ids]
            for shift in shifts: orbit.add(sum(shift[p] for p in image))
        orbit_counts.append({'size':kind[0],'cost':kind[1],'seed_mask':seed['mask'],'orbit_size':len(orbit)})
        banks[kind].update(orbit)
    assert {kind:len(rows) for kind,rows in banks.items()} == TYPES
    direct_native_classes = 0
    for kind, rows in banks.items():
        for mask in rows:
            ids = list(points(mask))
            assert len(ids) == kind[0] and price(ids) == kind[1]
            assert not any(sum(1<<p for p in triple) in forbidden for triple in combinations(ids,3))
            assert not any(mask & mother == mask for mother in mothers)
            direct_native_classes += 1
    bank_binding = None; original_columns = []
    if args.bank:
        raw = args.bank.read_bytes(); selected = {kind:set() for kind in TYPES}
        for lo,hi,cost,tag in struct.iter_unpack('<QQII',raw):
            if (tag%256,cost) in selected: selected[tag%256,cost].add(lo+(hi<<64))
            if (tag%256,cost) in ((9,557),(10,744),(11,936),(11,944)):
                original_columns.append((lo+(hi<<64),tag%256,cost))
        assert selected == banks
        bank_binding = sha256(raw).hexdigest()

    # Check every weight function represented by the 200 possible parent
    # families, not only one symmetry representative.
    weight_checks = []; class_checks = 0
    for union, marked in sorted(weights):
        histograms = {}
        for kind,rows in banks.items():
            hist = Counter((mask&union).bit_count()-3*(mask&marked).bit_count() for mask in rows)
            assert min(hist) == kind[0]-8
            histograms[f'{kind[0]},{kind[1]}'] = dict(sorted(hist.items()))
            class_checks += len(rows)
        mother_intersections = Counter(((m&union).bit_count(),(m&marked).bit_count()) for m in mothers)
        assert mother_intersections == {(6,0):120,(7,1):120,(13,1):10}
        weight_checks.append({'union_mask':str(union),'center_mask':str(marked),
                              'proper_weight_histograms':histograms,
                              'mother_intersection_histogram':[[*key,value] for key,value in sorted(mother_intersections.items())]})

    frame_checks = []
    for frame in parent_doc['frames']:
        cores = list(map(int,frame['core_masks'])); assert len(cores) == 2 and not cores[0]&cores[1]
        core_parents = [next(m for m in mothers if c&m == c) for c in cores]
        for c,m in zip(cores,core_parents):
            assert c == m ^ (1<<centers[m]) and price(list(points(c))) == 1104
        compatible = sorted(f for f in families if all(m in f for m in core_parents))
        assert compatible == sorted(tuple(sorted(map(int,f))) for f in frame['compatible_parent_families'])
        if frame['frame'] == 2:
            assert not compatible
            frame_checks.append({'frame':2,'compatible_family_count':0,'exclusion':'No admissible parent family.'})
            continue
        assert frame['frame'] == 1 and len(compatible) == 1
        family = compatible[0]; union = sum(family); marked = sum(1<<centers[m] for m in family)
        free = DOMAIN ^ (cores[0]|cores[1])
        assert (free&union).bit_count()-3*(free&marked).bit_count() == 26
        assert all((c&union).bit_count()-3*(c&marked).bit_count() == 12 for c in cores)
        # All allowed embedded size-11 columns have w>=8. Every forbidden
        # embedded size-11 column has w>=2 (delete two points of weight <=1
        # from a mother of weight at least4), hence multiplier6 repairs it.
        cert = {'schema':'SHORT_PARENT_FARKAS_V1','frame':1,'free_mask':str(free),
                'allowed_parent_masks':list(map(str,family)), 'union_mask':str(union),'center_mask':str(marked),
                'point_rule':'1_U - 3*1_Z, values -2,0,1',
                'prescribed_types':[[9,557,2],[10,744,5],[11,936,2],[11,944,1]],
                'type_multipliers':[-1,-2,-8,-8], 'parent_forbidden_weight_multiplier':6,
                'parent_cut':'-sum(x_C for forbidden size-11 parent columns) >= 0',
                'negative_constant':26-(2*1+5*2+3*8),
                'all_column_inequalities':'Proper columns checked in complete native orbits; all embedded 11-subsets follow from the 250-mother intersection histogram.',
                'review_status':'NOT_REVIEWED'}
        assert cert['negative_constant'] == -10
        if original_columns:
            slacks = []; forbidden_count = 0
            for mask,size,cost in original_columns:
                if mask & ~free: continue
                forbidden_column = size == 11 and not any(mask&m == mask for m in family)
                forbidden_count += forbidden_column
                beta = 1 if size == 9 else 2 if size == 10 else 8
                slacks.append((mask&union).bit_count()-3*(mask&marked).bit_count()-beta+6*forbidden_column)
            assert len(slacks) == 7953 and forbidden_count == 2286 and min(slacks) == 0
            cert['optional_complete_bank_column_check'] = {'candidates':len(slacks),
                'forbidden_columns':forbidden_count,'minimum_integer_column_slack':min(slacks)}
        (args.output/'short_farkas.json').write_text(json.dumps(cert,indent=2)+'\n')
        frame_checks.append({'frame':1,'compatible_family_count':1,'free_point_weight':26,
                             'required_class_weight_lower_bound':36,'integer_farkas_constant':-10,
                             'parent_forbidden_weight_multiplier':6})

    result = {'status':'COMPLETE_EXACT_WEIGHTED_PARENT_OBSTRUCTION',
              'cost_profile':parent_doc['cost_profile'],'parent_family_dependency_sha256':sha256(parent_data).hexdigest(),
              'parent_input_sha256':sha256(parent_raw).hexdigest(),'obs_sha256':sha256(native_raw).hexdigest(),
              'seed_file_sha256':sha256(seed_data).hexdigest(),'optional_bank_sha256':bank_binding,
              'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
              'orbit_counts':orbit_counts,'proper_classes_priced_and_legality_checked':direct_native_classes,
              'parent_families':len(families),'different_weight_functions':len(weights),
              'exact_proper_class_weight_checks':class_checks,
              'whole_domain_weight':50,'profile_weight_lower_bound':60,'contradiction_gap':10,
              'frame_checks':frame_checks,'weight_checks':weight_checks,
              'arithmetic':'Python integers only; no optimizer, no floating comparison',
              'scope':'The stated cost-9858 profile and its complete parent-family classification only.',
              'review_status':'NOT_REVIEWED','elapsed_seconds':time.monotonic()-started}
    (args.output/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('weight_checks','orbit_counts')},indent=2))


if __name__ == '__main__': main()
