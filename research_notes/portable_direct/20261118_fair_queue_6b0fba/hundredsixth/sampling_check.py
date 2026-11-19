#!/usr/bin/env python3
"""Exact mathematics. --experiments also compiles and calls the frozen C++ selector."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
from itertools import combinations
import json
from math import comb
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory

K = 1 << 64
MASK = K - 1
STEP = 0x9e3779b97f4a7c15
M1 = 0xbf58476d1ce4e5b9
M2 = 0x94d049bb133111eb
G = 1 << 32
SIZES = (16384, 65536, 262144, 1048576)
SKEW = (16385, 20003, 65535)
NAMES = ('clean', 'one_blind', 'all_blind', 'reachable_hit', 'reachable_miss',
         'pilot', 'all_blind_plus_reachable')
PINS = {
    'phase5/build.py': '8a282114f9ddc5ed52cb33e1fb19c533778e7287ec2bfe62d8044fbac4ecdad3',
    'phase5/probe.hpp': 'f2e9186856ccc583890c13f140cea1aa61e142805de245133f95902faaa2843c',
    'phase6/child.hpp': '33081d93895a7c774889208ee0aaeea56e657cf7dcfee76bfa3cdbd0dffe562b',
    'sampled_kernels.hpp': '2890d16a360fa9c874dc8de1edec1508f9522602397fc2cb7fbe6e2da55cb192',
    'bench.cpp': '9e2e98e3460b5fc1b4317a5b29bbad0de9c18b39f6dfcb67bf21a518965f7471',
    'holdout.cpp': '13b797dcc29e85af16973bb3566d657c5e9b885c50ce72d19ccaf8d4933a2597',
}


def mixed(x):
    x = ((x ^ (x >> 30)) * M1) & MASK
    x = ((x ^ (x >> 27)) * M2) & MASK
    return x ^ (x >> 31)


def undo_shift(x, shift):
    out = x
    while shift < 64:
        out ^= out >> shift
        shift *= 2
    return out


def unmix(x):
    x = undo_shift(x, 31) * pow(M2, -1, K) & MASK
    x = undo_shift(x, 27) * pow(M1, -1, K) & MASK
    return undo_shift(x, 30)


def ceildiv(a, b):
    return -(-a // b)


def stratum(n, count, j):
    return j*n // count, (j+1)*n // count


def training(n):
    state = 0xb0e9400520261108 ^ n ^ ((1024*0xd1b54a32d192ed03) & MASK)
    out = set()
    for j in range(1024):
        lo, hi = stratum(n, 1024, j)
        state = (state + STEP) & MASK
        out.add(lo + (mixed(state)*(hi-lo) >> 64))
    return out


def address(n, j, seed, avoid):
    lo, hi = stratum(n, 32, j)
    raw = mixed((seed + (j+1)*STEP) & MASK)
    i = lo + (raw*(hi-lo) >> 64)
    while i in avoid:
        i += 1
        if i == hi:
            i = lo
    return i


def seed_for(n, j, i):
    lo, hi = stratum(n, 32, j)
    first_raw = ceildiv((i-lo)*K, hi-lo)
    return (unmix(first_raw) - (j+1)*STEP) & MASK


def six_places(x):
    return x.numerator*10**6 // x.denominator


def analyze(n):
    train = training(n)
    pilot = {j*n//32 for j in range(32)}
    avoid = train | pilot
    hidden = sorted(train - pilot)
    direct_checks = 0
    histogram = Counter()
    d_min, d_max = K, 0
    for j in range(32):
        lo, hi = stratum(n, 32, j)
        available = [i for i in range(lo, hi) if i not in avoid]
        prev = available[-1] - (hi-lo)
        total = 0
        for i in available:
            # Raw offsets prev+1,...,i including the wrapped suffix of a stratum.
            mass = ceildiv((i-lo+1)*K, hi-lo) - ceildiv((prev-lo+1)*K, hi-lo)
            total += mass
            histogram[i-prev] += 1
            d_min, d_max = min(d_min, mass), max(d_max, mass)
            prev = i
        assert total == K
        # Certify a seed for both extremes and a central eligible address in every stratum.
        for i in (available[0], available[len(available)//2], available[-1]):
            seed = seed_for(n, j, i)
            assert address(n, j, seed, avoid) == i
            direct_checks += 1
    assert len(train) == 1024 and len(pilot) == 32
    assert sum(histogram.values()) + len(avoid) == n
    assert sum(a*b for a, b in histogram.items()) == n
    j = 11
    lo, hi = stratum(n, 32, j)
    first, second = [i for i in range(lo, hi) if i not in avoid][:2]
    hit, miss = seed_for(n, j, first), seed_for(n, j, second)
    assert address(n, j, hit, avoid) == first and address(n, j, miss, avoid) == second
    N = n-32
    iid_seed_repair = {}
    for k in (1, 32, len(hidden)):
        miss_prob = Fraction(comb(N-k, 32), comb(N, 32))
        iid_seed_repair[str(k)] = six_places(1-miss_prob)
    row = {
        'n': n, 'budget': min(1 << 22, max(4096, n//2)), 'blind': len(hidden),
        'training_pilot_overlap': 1024-len(hidden), 'raw_preimage_length_histogram': dict(sorted(histogram.items())),
        'min_max_detecting_seed_counts_among_eligible': [d_min, d_max],
        'inverse_seed_witnesses_checked': direct_checks, 'controlled_address': first,
        'hit_seed': hit, 'miss_seed': miss, 'first_blind': hidden[0],
        'ideal_uniform_32_repair_detection_ppm_floor_by_poison_count': iid_seed_repair,
        'optimal_64bit_seed_32_probe_min_singleton_detecting_seeds': K*32//N,
    }
    return row


def small_minimax():
    # Full finite double count for every hidden k-set and every legal s-subset.
    tests = 0
    counts = 0
    for N in range(1, 10):
        masks = [[sum(1 << x for x in v) for v in combinations(range(N), i)]
                 for i in range(N+1)]
        for k in range(N+1):
            for s in range(N+1):
                target = comb(N-k, s)
                transpose = comb(N-s, k)
                assert all(sum(not (a & b) for b in masks[s]) == target for a in masks[k])
                assert target*len(masks[k]) == transpose*len(masks[s])
                tests += 1
        for seed_count in range(1, 18):
            for s in range(N+1):
                c = [0]*N
                for z in range(seed_count):
                    sample = {(s*z+i) % N for i in range(s)}
                    assert len(sample) == s
                    for i in sample:
                        c[i] += 1
                assert min(c) == seed_count*s//N and max(c) == ceildiv(seed_count*s, N)
                counts += 1
    cyclic = 0
    for bits in range(1, 7):
        seed_count = 1 << bits
        for width in range(2, min(seed_count, 8)+1):
            for mask in range(1, 1 << width):
                avail = [i for i in range(width) if (mask >> i) & 1]
                actual = Counter()
                for raw in range(seed_count):
                    i = raw*width//seed_count
                    while not ((mask >> i) & 1):
                        i = (i+1) % width
                    actual[i] += 1
                prev = avail[-1]-width
                for i in avail:
                    assert actual[i] == (ceildiv((i+1)*seed_count, width)
                                         -ceildiv((prev+1)*seed_count, width))
                    prev = i
                cyclic += 1
    return {'matrix_cases': tests, 'rounded_designs': counts, 'N': [1, 9],
            'seed_counts': [1, 17], 'exhaustive_cyclic_skip_masks': cyclic,
            'cyclic_word_bits': [1, 6], 'max_cyclic_stratum_width': 8}


DRIVER = r'''
#include "holdout.cpp"
using V = balance_sort::Values;
int main() {
    const u64 G = u64(1)<<32;
    std::size_t n, first_blind, test_address;
    u64 hit, miss;
    while (std::cin >> n >> first_blind >> test_address >> hit >> miss) {
        V input(n);
        std::vector<bool> P(n), T(n);
        auto learnt = brc_sampled_detail::sample_indices(n, 1024);
        for(auto i : learnt) T[i] = true;
        for(std::size_t i=0;i<n;++i) {
            if (T[i]!=brc_probe::training_position(i,n)) throw std::runtime_error("training");
            input[i]=G*(i%3);
        }
        for(unsigned j=0;j<32;++j) {
            auto i=j*n/32;
            P[i]=true;
            input[i]=G*(j%3);
        }
        std::size_t hidden=0;
        for(std::size_t i=0;i<n;++i) hidden+=T[i]&&!P[i];
        if(!T[first_blind] || P[first_blind] || P[test_address] || T[test_address])
            throw std::runtime_error("placement");
        for(unsigned f=0;f<7;++f) {
            V a=input;
            const u64 seed=(f==4 ? miss : hit);
            if(f==1) a[first_blind]=3*G;
            if(f==2 || f==6)
                for(auto i:learnt) if(!P[i]) a[i]=3*G;
            if(f==3 || f==4 || f==6) a[test_address]=3*G;
            if(f==5) a[0]=3*G;
            std::array<std::size_t,4> observed{};
            for(auto i:learnt) ++observed.at(a[i]/G);
            std::array<u64,64> pilot{};
            for(unsigned j=0;j<32;++j) pilot[j]=a[j*n/32];
            auto B=brc_sampled_detail::cell_budget(n);
            bool p32=holdout::fits(pilot,32,B), p64=holdout::three(a,seed);
            V expected=a;
            std::sort(expected.begin(),expected.end());
            V distinct=expected;
            distinct.erase(std::unique(distinct.begin(),distinct.end()),distinct.end());
            std::array<u64,64> val{};
            std::copy(distinct.begin(),distinct.end(),val.begin());
            bool full=holdout::fits(val,distinct.size(),B);
            // Independent interval partition search on the three or four observed keys.
            u64 cost3=std::numeric_limits<u64>::max();
            for(std::size_t i=1;i+1<distinct.size();++i)
                for(std::size_t j=i+1;j<distinct.size();++j) {
                    u64 sum=(distinct[i-1]-distinct[0])+(distinct[j-1]-distinct[i])
                            +(distinct.back()-distinct[j])+3;
                    cost3=std::min(cost3,sum);
                }
            if(cost3!=(f==0 ? 3 : G+3) || (cost3<=B)!=full)
                throw std::runtime_error("three-interval optimum");
            if(full!=(f==0) || p32!=(f!=5) || p64!=(f==0 || f==1 || f==2 || f==4))
                throw std::runtime_error("route");
            ProbeStats cost;
            if(p64) child_sort<ChildMode::radix>(a,seed,&cost);
            else offset_radix(a,nullptr);
            if(a!=expected) throw std::runtime_error("sorted multiset");
            std::cout<<n<<' '<<f<<' '<<B<<' '<<hidden<<' '<<p32<<' '<<p64<<' '<<full<<' '<<cost3;
            for(auto c:observed) std::cout<<' '<<c;
            if(p64) {
                const auto& c=cost.rows.at(0);
                std::cout<<' '<<c.model_selected<<' '<<c.actual_misses<<' '<<c.counter_slots<<' '<<c.scan_visits;
            } else std::cout<<" -1 -1 -1 -1";
            std::cout<<'\n';
        }
    }
}
'''


def native(experiments, evidence, rows, sanitize):
    phase = experiments/'brc_residual_sort_preflight_20261111_b118ef26c242'
    for name, digest in PINS.items():
        if name == 'sampled_kernels.hpp':
            p = experiments/'brc_residual_sort_sampled_20261108_b0e94005'/name
        elif '/' in name:
            p = phase/name
        else:
            p = evidence/name
        if hashlib.sha256(p.read_bytes()).hexdigest() != digest:
            raise ValueError(f'file changed: {name}')
    root_key = 'int main(int argc,char** argv)'
    with TemporaryDirectory() as t:
        base = Path(t)
        for d in ('phase5','phase6','unit'):
            (base/d).mkdir()
        for name in ('phase5/build.py','phase5/probe.hpp','phase6/child.hpp'):
            shutil.copyfile(phase/name, base/name)
        shutil.copyfile(evidence/'bench.cpp', base/'unit/bench.cpp')
        src = (evidence/'holdout.cpp').read_text()
        if src.count(root_key) != 1:
            raise ValueError('holdout entry point')
        (base/'unit/holdout.cpp').write_text(src.replace(root_key,'int frozen_holdout_main(int argc,char** argv)'))
        (base/'unit/driver.cpp').write_text(DRIVER)
        cmd = [sys.executable, str(base/'phase5/build.py'), str(experiments),
               '--unit',str(base/'unit/driver.cpp'),'--output',str(base/'runner')]
        if sanitize:
            cmd.append('--sanitize')
        p = subprocess.run(cmd, text=True, capture_output=True)
        if p.returncode:
            raise RuntimeError(p.stderr)
        data = ''.join(' '.join(str(row[k]) for k in
                                ('n','first_blind','controlled_address','hit_seed','miss_seed'))+'\n'
                       for row in rows)
        lines = subprocess.check_output([str(base/'runner')], input=data, text=True).splitlines()
    output = {}
    for line in lines:
        n,f,b,h,a,route,full,cost3,*r = map(int,line.split())
        row = next(row for row in rows if row['n']==n)
        assert b==row['budget'] and h==row['blind'] and sum(r[:4])==1024
        output.setdefault(str(n), {})[NAMES[f]] = {
            'pilot': bool(a), 'holdout': bool(route), 'full_fits': bool(full), 'true_c3_slots': cost3,
            'training_key_counts_in_0_G_2G_3G_order': r[:4],
            'root_selected_actual_misses_counter_slots_scan_visits': r[4:] if route else None,
        }
    assert len(lines)==len(rows)*len(NAMES)
    return {'cases': len(lines), 'every_result_matched_std_sort': True, 'by_n': output}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--experiments', type=Path, help='unpacked frozen experiments directory')
    p.add_argument('--evidence', type=Path, default=Path(__file__).resolve().parents[1]/'sort_evidence')
    p.add_argument('--sanitize', action='store_true', help='build C++ with ASan and UBSan')
    args = p.parse_args()
    if args.sanitize and args.experiments is None:
        p.error('--sanitize requires --experiments')
    rows = [analyze(n) for n in SIZES+SKEW]
    result = {'word_modulus': K, 'G': G, 'frozen_sha256': PINS,
              'four_geometric_sizes': SIZES, 'unequal_strata_sizes': SKEW,
              'small_exact_models': small_minimax(), 'rows': rows}
    if args.experiments is not None:
        result['cpp'] = native(args.experiments.resolve(), args.evidence.resolve(), rows, args.sanitize)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
