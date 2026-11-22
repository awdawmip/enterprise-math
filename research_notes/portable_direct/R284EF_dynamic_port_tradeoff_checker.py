#!/usr/bin/env python3
"""R284EF exact cache/measurement frontier and recovery on frozen R284CO Port f.
Run in research_notes/portable_direct alongside R284CO and R284EE.
"""
import hashlib, json, random, sys, time
from itertools import product
from collections import Counter
from R284EE_diagonal_two_read_checker import readouts
PIN='acba2d8667903434aaa2a10720f43637fcc2421b'
PIN_BLOB='b46e0f682b58e47c27094b4bea6fa4e55119a3ee'
DIAGONALS=(0b1001,0b0110)

def formula(m,k):
    if m==0: return 2
    return {2:2+2*m,3:3+m,4:4}[k]

def exact_dp(word,k):
    # A 4-bit mask denotes measured labels in the fixed orbit;
    # every step permits optional prefetch and arbitrary eviction.
    cur={mask:mask.bit_count() for mask in range(16)
         if mask&DIAGONALS[0]==DIAGONALS[0] and mask.bit_count()<=k}
    parity=0
    for switch in word:
        parity ^=switch
        required=DIAGONALS[parity]
        nxt={}
        for cache,cost in cur.items():
            for target in range(16):
                if target&required!=required or target.bit_count()>k: continue
                c=cost+(target&~cache).bit_count()
                if c<nxt.get(target,10**9): nxt[target]=c
        cur=nxt
    return min(cur.values())

def cache_oracle_count(path,k):
    parity=0; cache={0,3}; count=2
    for q in path:
        if q!=65: parity ^=1
        required={0,3} if parity==0 else {1,2}
        if k==4:
            count+=len(required-cache);cache |=required
        elif k==2:
            count+=len(required-cache);cache=set(required)
        else:
            missing=required-cache
            count+=len(missing)
            spare=cache-required
            cache=set(required)
            if spare:cache.add(min(spare))
    return count

def main():
    start=time.perf_counter()
    f=readouts()  # exact frozen SHA256 verified inside R284EE.readouts
    build_ms=(time.perf_counter()-start)*1000
    assert len(f)==65536
    assert max(f)==8436072374 and min(f)==7988637418
    start=time.perf_counter()
    B=[(f[i],f[i^65]) for i in range(65536)]
    inverse={p:i for i,p in enumerate(B)}
    assert len(inverse)==65536
    for i,p in enumerate(B):
        assert inverse[p]==i
        for q in (1,64,65):
            j=inverse[p]^q
            assert B[j]==(f[j],f[j^65])
    inverse_ms=(time.perf_counter()-start)*1000
    # Complete coverage of all binary switch words of lengths 0..12.
    checked=0
    for n in range(13):
        for word in product((0,1),repeat=n):
            for k in (2,3,4):
                assert exact_dp(word,k)==formula(sum(word),k)
                checked+=1
    assert checked==24573
    rng=random.Random(28420261122)
    path=rng.choices((1,64,65),weights=(4,4,2),k=100000)
    m=sum(q!=65 for q in path)
    runs={}
    for k in (2,3,4):
        start=time.perf_counter(); cost=cache_oracle_count(path,k)
        ms=(time.perf_counter()-start)*1000
        assert cost==formula(m,k)
        runs[str(k)]={'oracle_reads':cost,'python_loop_ms':round(ms,4)}
    start=time.perf_counter();idx=inverse[B[0]];checksum=0
    for q in path:
        idx ^=q; checksum ^=f[idx]^f[idx^65]
    index_ms=(time.perf_counter()-start)*1000
    assert m==80025
    cert={'schema':'R284EF_DYNAMIC_PORT_CACHE_FRONTIER_V1',
          'frozen_source_commit':PIN,'frozen_source_blob_sha1':PIN_BLOB,
          'source_states':65536,'arcs':64,
          'max_port_value':max(f),'min_port_value':min(f),
          'port_value_bit_width':max(f).bit_length(),
          'cache_dp_words':8191,'cache_dp_cases':checked,
          'recovered_states':len(inverse),'verified_R_W_RW_successors':196608,
          'benchmark':{'python':sys.version.split()[0],
            'seed':28420261122,'steps':len(path),'symbol_counts':dict(Counter(path)),
            'diagonal_switches':m,'port_cache':runs,
            'index_route':{'initial_oracle_reads':2,'subsequent_oracle_reads':0,
                           'python_loop_ms':round(index_ms,4)},
            'f_table_build_ms':round(build_ms,4),
            'inverse_plus_full_successor_check_ms':round(inverse_ms,4)},
          'status':'AUTHOR_EXACT_CHECKED / NOT_REVIEWED',
          'scope':'Frozen auxiliary named Port readings; separate oracle/cache vs indexed-table models'}
    from pathlib import Path
    path=Path(__file__).with_name('R284EF_dynamic_port_tradeoff_certificate.json')
    path.write_text(json.dumps(cert,indent=2,ensure_ascii=False)+'\\n',encoding='utf-8')
    print(json.dumps(cert,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
