"""Static, signed coordinate observers on named FCC STAR slots. Python 3.10+."""
import argparse
import hashlib
import importlib.util
import json
import sys
from collections import Counter
from itertools import combinations, permutations, product
from pathlib import Path

KERNEL_PATH = 'src/enterprise_math/brc_weighted_recurrent.py'
KERNEL_SHA = '7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26'
AXES = ('AB', 'AC', 'AD', 'BC', 'BD', 'CD')
STARS = tuple(tuple(i for i, e in enumerate(AXES) if v in e) for v in 'ABCD')
MATCH = ((0, 5), (1, 4), (2, 3))
ALL24 = list(permutations('ABCD'))


def encode_bytes(o):
    return json.dumps(o, sort_keys=True, separators=(',', ':')).encode()


def load_core(repo):
    path = repo / KERNEL_PATH
    assert hashlib.sha256(path.read_bytes()).hexdigest() == KERNEL_SHA
    spec = importlib.util.spec_from_file_location('fcc_brc_frozen', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module.recurrent_mass_power


class SignedCoordinates:
    """Each term has its own two-edge positive path and a named +/- endpoint."""
    def __init__(self, core):
        self.core = core
        self.cache = {}
        self.requests = 0
        self.graphs = []

    def linear(self, slots, x):
        self.requests += 1
        key = tuple((s, sign, x[s]) for s, sign in slots)
        if key in self.cache:
            return self.cache[key]
        n = len(key) + 3
        adjacency = [[0] * n for _ in range(n)]
        for j, (_, sign, value) in enumerate(key):
            # The first edge carries absolute mass, the second retains its signed port.
            adjacency[0][3+j] = abs(value)
            adjacency[3+j][1 if sign*value >= 0 else 2] = 1
        row = self.core(adjacency, 2)[0]
        value = row[1] - row[2]
        assert value.denominator == 1
        self.cache[key] = value.numerator
        self.graphs.append((key, row[1].numerator, row[2].numerator))
        return value.numerator

    def get(self, x):
        original = tuple(tuple(self.linear(((e,1),(t[-1],-1)),x) for e in t[:2]) for t in STARS)
        repair = tuple(self.linear(tuple((j,1) for j in u)+tuple((j,-1) for j in MATCH[-1]),x)
                       for u in MATCH[:2])
        return original + (repair,)


def project_residue(word, q):
    return tuple(tuple(k % q for k in y) for y in word)


def relabel(x, permutation):
    labels = dict(zip('ABCD', permutation))
    out = [0]*len(x)
    for i, edge in enumerate(AXES):
        dest = ''.join(sorted(labels[v] for v in edge))
        out[AXES.index(dest)] = x[i]
    return tuple(out)



def zero_triangle_count(observer, word, q):
    # Disjoint slot namespaces retain original row and overlap identities.
    lifts = (None,)*6 + tuple(v for local in word for v in (*local,0))
    transitions = []
    for e,edge in enumerate(AXES):
        i,j = ('ABCD'.index(v) for v in edge)
        a=6+3*i+STARS[i].index(e)
        b=6+3*j+STARS[j].index(e)
        transitions.append(observer.linear(((a,1),(b,-1)),lifts)%q)
    edge_values=(None,)*18+tuple(transitions)
    triangles=[]
    for i,j,k in combinations('ABCD',3):
        slots=((18+AXES.index(i+j),1),(18+AXES.index(j+k),1),(18+AXES.index(i+k),-1))
        triangles.append(observer.linear(slots,edge_values)%q)
    derived=observer.linear(((24,1),(25,-1),(26,1)),(None,)*24+tuple(triangles[:3]))%q
    assert derived==triangles[3]
    return triangles.count(0)

def check_finite(observer, q):
    alphabet = tuple(product(range(q), repeat=2))
    words = {}
    profiles = Counter()
    min_vectors = []
    for tail in product(range(q),repeat=5):
        x = (0,*tail)
        word = project_residue(observer.get(x), q)
        assert word[:4] not in words
        words[word[:4]] = word
        stars_active = sum(u!=(0,0) for u in word[:4])
        extended_active = stars_active + (word[-1]!=(0,0))
        profiles[stars_active,extended_active] += 1
        if stars_active == 2:
            counts = Counter(x)
            assert sorted(counts.values())==[1,5]
            exceptional = next(i for i,k in enumerate(x) if counts[k]==1)
            assert [v for v,c in enumerate(word[:4]) if c!=(0,0)] == ['ABCD'.index(v) for v in AXES[exceptional]]
            min_vectors.append((exceptional, x))
    assert len(min_vectors)==6*(q-1) and len(words)==q**5
    results={}
    for width in (4,5):
        counts = Counter()
        for full in words.values():
            word = full[:width]
            counts[word] += 1
            for i, letter in enumerate(word):
                for alt in alphabet:
                    if alt != letter:
                        counts[word[:i]+(alt,)+word[i+1:]] += 1
        hist=Counter(counts.values())
        hist[0]=len(alphabet)**width-len(counts)
        if width==4:
            for recv in product(alphabet,repeat=4):
                good=zero_triangle_count(observer,recv,q)
                assert good in (0,1,2,4) and counts.get(recv,0)==(1 if good==4 else good)
            assert hist[2]==6*(q-1)*q**5 and hist[1]==(1+4*(q-1)*(q-2))*q**5 and max(hist)==2
        else:
            assert hist[1]==q**5*(1+5*(q*q-1)) and max(hist)==1
        results[str(width)]={'list_histogram':dict(sorted(hist.items())),
                             'ambient_words':len(alphabet)**width}
    return {'q':q,'messages':len(words),'minimum_four_block_messages':len(min_vectors),
            'joint_weight_distribution':{f'{a}/{b}':c for (a,b),c in sorted(profiles.items())},
            'triangle_decodings_compared_to_direct_lists':len(alphabet)**4,'radius_one':results}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--repo',type=Path,required=True)
    args=parser.parse_args()
    obs=SignedCoordinates(load_core(args.repo))
    finite=[check_finite(obs,q) for q in (2,3)]
    # Verify equivariance of the extra block on a signed integral witness and all 24 charts.
    x=(0,3,-1,4,6,-2)
    diag=(1,)*6
    chart=obs.get(x)
    assert obs.get(tuple(a+1 for a in x))==chart
    for permutation in ALL24:
        y=relabel(x,permutation)
        labels=dict(zip('ABCD',permutation))
        match_labels=tuple(tuple(sorted(''.join(sorted(labels[v] for v in AXES[e])) for e in pair)) for pair in MATCH)
        canonical=tuple(tuple(sorted(AXES[e] for e in pair)) for pair in MATCH)
        magnitudes=chart[-1]+(0,)
        transported=[0]*3
        for i,pair in enumerate(match_labels):
            transported[canonical.index(pair)]=magnitudes[i]
        assert obs.get(y)[-1]==tuple(transported[i]-transported[-1] for i in range(2))
    angles={}
    for i,edge in enumerate(AXES):
        v=tuple(int(k==i) for k in range(6))
        word=obs.get(v)
        assert sum(x!=(0,0) for x in word)==3
        received=tuple(word[j] if j=='ABCD'.index(edge[0]) else (0,0) for j in range(4))
        assert sum(x!=(0,0) for x in received)==1
        assert sum(x!=y for x,y in zip(received,word[:4]))==1
        angles[edge]={'valid_word':word,'ambiguous_received':received}
    scalar={}
    for q in range(2,21):
        all_plus=tuple((j,1) for j in range(6))
        # An S4-invariant scalar must have equal coefficients. Reduction is a static observer.
        change=obs.linear(all_plus,diag)
        allowed=[k for k in range(q) if (k*change)%q==0 and
                 all((k*t)%q!=0 for t in range(1,q))]
        if allowed:
            scalar[str(q)]=allowed
    assert set(scalar)=={'2','3','6'}
    print(json.dumps({'entrypoint':KERNEL_PATH+':recurrent_mass_power','kernel_sha256':KERNEL_SHA,
        'carrier':'anchored raw six signed coordinates; fixed static signed endpoint readout',
        'allowed_futures':'static chart restrictions, named S4 relabeling, one block error/list decoding',
        'axes':AXES,'STAR_indices_zero_based':STARS,'opposite_pair_indices_zero_based':MATCH,
        'integral_minimal_witnesses':angles,'finite':finite,'sum_scalar_q_le_20':scalar,
        'integral_S4_relabelings_verified':len(ALL24),
        'receipt':{'positive_path_depth':2,'max_graph_vertices':max(len(k)+3 for k in obs.cache),
            'max_positive_branches':max(map(len,obs.cache)),'requests':obs.requests,
            'typed_unique_kernel_calls':len(obs.cache),
            'complete_branch_ledger_sha256':hashlib.sha256(encode_bytes(obs.graphs)).hexdigest(),
            'signed_endpoints_example':obs.graphs[:3]}},sort_keys=True,indent=1))


if __name__=='__main__':
    main()
