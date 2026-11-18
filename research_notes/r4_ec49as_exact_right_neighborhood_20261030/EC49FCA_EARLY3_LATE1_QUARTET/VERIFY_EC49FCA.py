"""EC49FCA: exact signed-X6 3 early + 1 late four-exchange exhaustive test.
Frozen generator EC49FBY, immutable scientific input pin.
"""
from pathlib import Path
from itertools import combinations
import json,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'EC49FBY_COMPLETE_TRIPLE_RIGIDITY'))
from VERIFY_EC49FBY import build

BASE=158
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
def run():
    chosen,early,late,pools,single=build()
    assert len(early)==10 and len(late)==10 and len(single)==24
    data=[];raw_sum=mask_product=evals=pruned2=pruned3=0
    for E in combinations(early,3):
        for L in late:
            slots=E+(L,)
            remaining=0
            for key,value in single.items():
                if key not in slots:remaining|=value
            base=remaining.bit_count(); K=BASE-base
            filtered=[]
            for key in slots:
                filtered.append((key,list({v & ~remaining for v in pools[key] if (v & ~remaining).bit_count()<K})))
            filtered.sort(key=lambda q:len(q[1]))
            a,b,c,d=(q[1] for q in filtered)
            raw=1; product=1
            for key in slots:raw*=len(pools[key])
            for _,arr in filtered: product*=len(arr)
            raw_sum+=raw;mask_product+=product
            n=p=q=0;best=BASE
            for x in a:
                for y in b:
                    xy=x|y
                    if xy.bit_count()>=K:
                        p+=1;continue
                    for z in c:
                        xyz=xy|z
                        if xyz.bit_count()>=K:
                            q+=1;continue
                        for w in d:
                            n+=1
                            best=min(best,base+(xyz|w).bit_count())
            evals+=n;pruned2+=p;pruned3+=q
            data.append({'slots':slots,'rest_edges':base,'strict_threshold':K,
                         'filtered_unique_counts':[len(z) for _,z in filtered],
                         'sort_order':[key for key,_ in filtered],
                         'raw':raw,'eligible_product':product,'pair_pruned':p,
                         'triple_pruned':q,'fourth_evaluations':n,'minimum':best})
    assert len(data)==1200 and all(z['minimum']==158 for z in data)
    assert (raw_sum,mask_product,evals,pruned2,pruned3)==(12617337600,246160070,1306868,23658,200924)
    result={'schema':'EC49FCA_ALL_1200_EXACT_V1','pin':PIN,
            'source':'EC49FBY@5b10f1c296cb8826d4b69f6fd83dba89d765df1c',
            'groups':len(data),'minimum':158,'raw':raw_sum,
            'unique_residual_product':mask_product,'fourth_evaluations':evals,
            'pair_pruned':pruned2,'triple_pruned':pruned3,'per_group':data}
    Path(__file__).with_name('EXACT_REPORT_EC49FCA.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('PASS EC49FCA',len(data),'groups',evals,'fourth unions',result['minimum'],'edges')
    return result
if __name__=='__main__':run()
