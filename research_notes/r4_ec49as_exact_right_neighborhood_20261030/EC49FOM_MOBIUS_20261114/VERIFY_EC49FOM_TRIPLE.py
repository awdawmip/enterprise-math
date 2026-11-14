#!/usr/bin/env python3
"""Independent original-native triple identity check for EC49FOM.

Usage:
  python VERIFY_EC49FOM_TRIPLE.py master_and_radius3_cases.txt \
      /path/to/VERIFY_EC49FOK_INDEPENDENT.py
The second file is the independently authored exact signed-prefix trie DP from
EC49FOK / PR #2393, also bundled with EC49FOL evidence. This script consumes
no C++ profile CSV, C++ cost table, or EC49FOM polynomial certificate.
"""
import importlib.util,itertools,sys,collections
from pathlib import Path
def main(source,previous):
    spec=importlib.util.spec_from_file_location("original_native",Path(previous))
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    mod.IDS=(32315,32303)
    words,cases=mod.parse(source)
    roots=(3,5,6,7)
    profiles={k:{r:mod.table(words,cases[k],r) for r in roots} for k in mod.IDS}
    dom={k:mod.domain(profiles[k]) for k in mod.IDS}
    assert dom[32315]==dom[32303]
    d=dom[32315]
    assert {i:d[i] for i in range(24) if len(d[i])>1} == {
      5:(5,7),7:(6,7),13:(6,7),15:(3,5,7),
      17:(3,6,7),19:(3,5,7),21:(3,6,7)}
    baseline={i:min(d[i]) for i in range(24)}
    counts=collections.Counter()
    witness=None
    for tup in itertools.product(*(d[i] for i in range(24))):
        choice=dict(enumerate(tup));actual={}
        for k in mod.IDS:
            actual[k]=sum(
              profiles[k][r][2][sum(
                1<<profiles[k][r][1][i]
                for i in range(24) if choice[i]==r)]
              for r in roots)
        change=actual[32303]-actual[32315]
        pred=-int(all(choice[i]==7 for i in (13,17,21)))
        assert change==pred,(tup,change,pred)
        counts[change]+=1
        if change==-1 and all(choice[i]==baseline[i] for i in range(24) if i not in (13,17,21)):
            witness=actual
    assert counts=={0:612,-1:36} and witness=={32315:180,32303:179}
    print("EC49FOM_INDEPENDENT_EXACT_PASS",dict(counts),"shortest_witness",witness)
if __name__=="__main__":main(*sys.argv[1:])
