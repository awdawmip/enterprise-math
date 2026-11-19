"""A single-word multiple-contaminant audit, including a pinned C++ replay."""
import argparse
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations, product
import json
from math import comb, prod
from pathlib import Path
import runpy
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory


HERE = Path(__file__).resolve().parent
PREVIOUS = HERE.parent / 'hundredsixth' / 'sampling_check.py'
K = 1 << 64
SIZES = [1 << i for i in (14, 16, 18, 20)]
FACTORS = {511:(7,73), 2047:(23,89), 8191:(8191,), 32767:(7,31,151)}


def field_product(a, b, q=32):
    modulus = {32:0x25, 4:0x7}[q]
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & q:
            a ^= modulus
    return out


def evaluate(coefficients, x, q=32):
    y=0
    for z in reversed(coefficients):
        y=field_product(y,x,q)^z
    return y


def word_columns(seed):
    return [evaluate([(seed>>(5*i))&31 for i in range(13)], j) for j in range(32)]


def field_checks():
    for q in (4,32):
        for a in range(1,q):
            assert sorted(field_product(a,b,q) for b in range(q))==list(range(q))
    # Four positions, 32 equally likely polynomials, strength two; missing top coefficients are 2,3.
    words=[tuple(evaluate((a,b,c),x,4) for x in range(4))
           for a,b,c in product(range(4),range(4),range(2))]
    minhits=[]
    for k in range(1,5):
        worst=32
        for cells in combinations(range(16),k):
            hits=sum(any(row[i//4]==i%4 for i in cells) for row in words)
            worst=min(worst,hits)
        minhits.append(worst)
        lower=sum((-1)**(j+1)*comb(k,j)*32//(4**j) for j in range(1,min(2,k)+1))
        assert worst==lower
    assert minhits[:3]==[int(32*(1-F(3,4)**k)) for k in (1,2,3)]
    rows=[]
    for k in range(1,33):
        bound=sum((-1)**(j+1)*comb(k,j)*(K//32**j) for j in range(1,min(k,12)+1))
        upper=int(K*(1-F(31,32)**k))
        rows.append(dict(k=k,field_worst_hits=bound,equal_32_slot_benchmark_floor=upper,
                         gap_in_seeds=upper-bound))
    assert all(row['gap_in_seeds']==0 for row in rows[:13])
    assert rows[13]['gap_in_seeds']==6
    quot,rem=divmod(K//32,33)
    counts=[quot+(i<rem) for i in range(33)]
    assert 32*sum(counts)==K
    # Every unordered point pair determines one direction, even in characteristic two.
    direction_hist=Counter()
    for h in range(1,1024):
        x,y=divmod(h,32)
        d=32 if x==0 else next(j for j in range(32) if field_product(x,j)==y)
        direction_hist[d]+=1
    assert set(direction_hist.values())=={31}
    h2=2*(K//32)-max(counts)
    assert h2==int(K*(1-F(comb(992,2),comb(1024,2))))
    return dict(small_model_minimum=minhits,blind_by_k=rows,
                affine_plane=dict(worst_two_hits=h2,directions_at_high_count=rem,
                                  same_stratum_policy_two_hits=rows[1]['field_worst_hits']))


def design(v):
    primes=FACTORS[v]
    assert prod(primes)==v
    for p in primes:
        assert all(p%i for i in range(2,int(p**.5)+1))
    rows=[]
    for p in primes:
        if p>=31:
            vectors=[(1,j) if j<p else (0,1) for j in range(32)]
        else:
            vectors=[(1,j%p,j//p) for j in range(32)]
        for a,b in combinations(vectors,2):
            assert any((a[i]*b[j]-a[j]*b[i])%p for i,j in combinations(range(len(a)),2))
        rows.append((p,vectors,(v//p)*pow(v//p,-1,p)))
    return rows


def crt_addresses(n, seed):
    v=n//32-1
    offsets=[0]*32
    for p,vectors,c in design(v):
        coords=[]
        for _ in range(len(vectors[0])):
            seed,z=divmod(seed,p)
            coords.append(z)
        for j,u in enumerate(vectors):
            offsets[j]+=c*(sum(a*b for a,b in zip(u,coords))%p)
    return [j*(v+1)+1+offset%v for j,offset in enumerate(offsets)]


def hash_addresses(addresses):
    h=0
    for x in addresses:
        h=(h*1000003+x)%K
    return h


def field_addresses(n, train, seed):
    out=[]
    for j,t in enumerate(word_columns(seed)):
        pos=train[32*j+t]
        out.append(pos if pos!=j*n//32 else train[32*j+(t+1)%32])
    return out


def native_cases(n, old):
    train=sorted(old['training'](n))
    offsets=word_columns(1<<60)
    pilot={j*n//32 for j in range(32)}
    by_layer=[part for j in range(32)
              if (part:=set(train[32*j:32*j+32])).isdisjoint(pilot)]
    full=[j for j in range(32) if train[32*j] not in pilot]
    assert len(by_layer)==len(full)>=29
    # An omitted degree-twelve word whose targets never use the known pilot or its replacement.
    excluded=[evaluate([0]*12+[16],j) for j in range(32)]
    forbidden={excluded[j]^a for j in range(32) if train[32*j] in pilot for a in (0,1)}
    shift=next(b for b in range(32) if b not in forbidden)
    witness=[train[32*j+(excluded[j]^shift)] for j in range(32)]
    accepted=[train[32*j+offsets[j]] for j in full[:13]]
    all_blind=set(train)-pilot
    v=n//32-1
    D=prod(p**len(vec[0]) for p,vec,_ in design(v))
    a=F(2*v-1,v*v)
    model_hits=D*a
    assert model_hits.denominator==1
    r=K%D
    # Residue-balanced labels: exact deterministic worst lower bound for an arbitrary H-label event.
    H=int(model_hits)
    lower=(K//D)*H+max(0,H-(D-r))
    cases=[
        ('clean',0,[]),('one_seed_hit',1<<60,[accepted[0]]),
        ('thirteen_agree',1<<60,accepted),('fourteen_excluded',0,witness[:14]),
        ('thirtytwo_excluded',0,witness),('all_blind',678901,sorted(all_blind)),
        ('whole_pair_hit',12345,crt_addresses(n,12345)[:2]),
        ('whole_pair_other_seed',678901,crt_addresses(n,12345)[:2])]
    summary=dict(n=n,blind=len(all_blind),full_layers=len(full),omitted_shift=shift,
                 crt_labels=D,crt_uniform_two_hit=str(a),
                 finite_word_guaranteed_hits=lower, finite_word_universal_upper=int(K*a))
    rows=[]
    for label,seed,contaminated in cases:
        assert len(set(contaminated))==len(contaminated) and not pilot.intersection(contaminated)
        chosen=field_addresses(n,train,seed)
        other=crt_addresses(n,seed)
        hits=set(contaminated)
        if label=='thirteen_agree':
            assert len(hits.intersection(chosen))==13
        rows.append(dict(n=n,label=label,seed=seed,contaminated=contaminated,
                         expected_field_pass=not hits.intersection(chosen),
                         expected_crt_pass=not hits.intersection(other),
                         field_hash=hash_addresses(chosen),crt_hash=hash_addresses(other)))
    return summary,rows


def run_native(experiments, evidence, old, cases, timing, sanitize):
    phase=experiments/'brc_residual_sort_preflight_20261111_b118ef26c242'
    for name,digest in old['PINS'].items():
        if name=='sampled_kernels.hpp':
            source=experiments/'brc_residual_sort_sampled_20261108_b0e94005'/name
        elif '/' in name:
            source=phase/name
        else:
            source=evidence/name
        assert sha256(source.read_bytes()).hexdigest()==digest,source
    with TemporaryDirectory() as tmp:
        base=Path(tmp)
        for folder in ('phase5','phase6','unit'):
            (base/folder).mkdir()
        for name in ('phase5/build.py','phase5/probe.hpp','phase6/child.hpp'):
            shutil.copyfile(phase/name,base/name)
        shutil.copyfile(evidence/'bench.cpp',base/'unit/bench.cpp')
        src=(evidence/'holdout.cpp').read_text()
        call='int main(int argc,char** argv)'
        assert src.count(call)==1
        (base/'unit/holdout.cpp').write_text(src.replace(call,'int holdout_cli_unused(int argc,char** argv)'))
        shutil.copyfile(HERE/'sort_native.cpp',base/'unit/driver.cpp')
        compile_cmd=[sys.executable,str(base/'phase5/build.py'),str(experiments),
                     '--unit',str(base/'unit/driver.cpp'),'--output',str(base/'runner')]
        if sanitize:
            compile_cmd.append('--sanitize')
        build=subprocess.run(compile_cmd,capture_output=True,text=True)
        if build.returncode:
            raise RuntimeError(build.stderr)
        lines=[' '.join(map(str,[row['n'],row['label'],row['seed'],len(row['contaminated']),
                                 *row['contaminated']])) for row in cases]
        argv=[str(base/'runner')]
        if timing:
            argv.append(str(timing.resolve()))
        result=subprocess.run(argv,input='\n'.join(lines)+'\n',capture_output=True,text=True,check=True)
    output=[]
    assert len(result.stdout.splitlines())==len(cases)
    for raw,case in zip(result.stdout.splitlines(),cases):
        n,label,seed,*items=raw.split()
        assert (int(n),label,int(seed))==(case['n'],case['label'],case['seed'])
        modes={}
        assert len(items)==15
        for pos,mode in enumerate(('original','field','crt')):
            passed,h,slots,misses,visits=map(int,items[pos*5:pos*5+5])
            if mode!='original':
                assert h==case[mode+'_hash'] and bool(passed)==case['expected_'+mode+'_pass']
            modes[mode]=dict(passed=bool(passed),slots=slots,misses=misses,scan_visits=visits)
        output.append(dict(n=int(n),label=label,seed=int(seed),contaminated=len(case['contaminated']),
                           route=modes))
    return output


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--experiments',type=Path,required=True,help='unpacked frozen experiments directory')
    parser.add_argument('--timings',type=Path,help='write unaggregated machine timing CSV')
    parser.add_argument('--sanitize',action='store_true')
    args=parser.parse_args()
    old=runpy.run_path(str(PREVIOUS))
    report=field_checks()
    summaries,cases=[],[]
    for n in SIZES:
        summary,cur=native_cases(n,old)
        summaries.append(summary)
        cases.extend(cur)
    report.update(word_size=K,pins=old['PINS'],scales=summaries,
                  native=run_native(args.experiments.resolve(),HERE.parent/'sort_evidence',old,
                                    cases,args.timings,args.sanitize))
    print(json.dumps(report,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
