#!/usr/bin/env python3
"""Independent lexicographic (key count, sum canonical native-word lengths) exact DP.
Weight is the sum of one fixed-key native-word length per selected key;
NOT distinct signed-prefix-union cost. Uses only integer arithmetic.
"""
from collections import Counter
from json import dumps,loads
from pathlib import Path
from VERIFY_EC49FFG import N, greedy, key_for_horizon, keymask


def oracle(positive=False):
    keys=([(2,1,1)] if positive else [(3,0,1),(2,1,1)])+[key_for_horizon(H) for H in range(3,18)]
    covers=[keymask(k) for k in keys]
    lens=[2*(x+y+z-1) for x,y,z in keys]
    masks=[0]*(1<<len(keys))
    counts=[0]*(1<<len(keys))
    lengths=[0]*(1<<len(keys))
    INF=1_000_000
    best=[INF]*N
    witness=[0]*N
    best[0]=0
    for s in range(1,1<<len(keys)):
        bit=s&-s;j=bit.bit_length()-1;prev=s^bit
        m=masks[prev]|covers[j]
        masks[s]=m
        counts[s]=counts[prev]+1
        lengths[s]=lengths[prev]+lens[j]
        sc=counts[s]*1000+lengths[s]
        if sc<best[m]:best[m]=sc;witness[m]=s
    for j in range(17):
        bit=1<<j
        for m in range(N):
            if not m&bit and best[m|bit]<best[m]:
                best[m]=best[m|bit];witness[m]=witness[m|bit]
    return keys,best,witness

def main():
    reportfile=Path(__file__).parent/'EXACT_REPORT_EC49FFG.json'
    report=loads(reportfile.read_text())
    length_improved={}
    samples={}
    for name,positive in [('count_admissible',False),('strict_positive',True)]:
        keys, scores,wit=oracle(positive)
        diff=0;max_saving=0
        for m in range(N):
            if positive and m&(1<<15):
                assert scores[m]==1_000_000
                continue
            chosen=greedy(m,positive)
            assert len(chosen)==scores[m]//1000
            greedy_length=sum(2*(x+y+z-1) for x,y,z in chosen)
            saving=greedy_length-scores[m]%1000
            assert saving>=0
            if saving:
                diff+=1
                max_saving=max(max_saving,saving)
        length_improved[name]={'masks_where_length_surrogate_improves_vs_right_endpoint_greedy':diff,'max_total_length_saving':max_saving}
        low=(1<<8)-1
        orig=greedy(low,positive)
        selected=wit[low]
        opt=[keys[j] for j in range(len(keys)) if selected&(1<<j)]
        samples[name]={'all_low_requirement':low,'right_end_greedy_keys':orig,'right_end_greedy_total_path_length':sum(2*(x+y+z-1) for x,y,z in orig),'lexicographic_opt_keys':opt,'lexicographic_opt_total_path_length':scores[low]%1000,'minimum_keys':scores[low]//1000}
        assert scores[low]//1000==4
        assert scores[low]%1000==54, opt
    report['secondary_surrogate_lexicographic']={'scope':'canonical representatives, first minimize number of keys, then minimize sum of one native word length per key; not ordered prefix union', 'verification':'EXACT_ALL_SUBSET_AND_SUPERMASK_PASS', 'improvements':length_improved,'examples':samples}
    reportfile.write_text(dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print('EXACT_SECONDARY_PASS',length_improved)
    print('all 8 lows:',samples['count_admissible'])

if __name__=='__main__':main()
