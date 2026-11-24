#!/usr/bin/env python3
"""Recheck full R5 H12 f8 query-type/cardinality Pareto certificate."""
import hashlib, json, subprocess, sys
from pathlib import Path
L=25845652773852463277015040000
U=58182461585441404127941754880
SHA='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
H=(18,24,82,34,17,0,1,2,3,144,208,255)
WIT=((0,1,214,221),(18,82,223,290),(18,34,296,312))
THREE=(216,223,296)
def family(values,tau):
    by={}
    for i,v in enumerate(values):by[v]=by.get(v,0)|(1<<i)
    cans={sum(mask for val,mask in by.items() if lo<=val<=lo+tau) for lo in by}
    return tuple(sorted(s for s in cans if not any(s!=t and s&t==s for t in cans)))
def main():
    if len(sys.argv)!=5:
        raise SystemExit('usage: verifier.py FROZEN_TABLE.json PRIOR_RESULTS.json EXACT_SMALL_BINARY OUTPUT.json')
    infile,oldfile,solver,out=map(Path,sys.argv[1:])
    buf=infile.read_bytes()
    assert hashlib.sha256(buf).hexdigest()==SHA
    raw=json.loads(buf)['counts_and_cohorts']
    assert set(map(int,raw))==set(range(214,315))
    assert all(len(v['counts'])==256 for v in raw.values())
    old=json.loads(oldfile.read_text())
    assert old['f']==8 and tuple(old['H12'])==H and old['frozen_table_sha256']==SHA
    assert old.get('four_minimum_at_left',old.get('minimum_four_cost_on_left'))==8343
    assert old.get('four_subsets_total',old.get('four_family_subsets_total'))==126
    assert old['four_pairwise_impossible']==117
    assert len(old['four_finite_exact_results'])==9
    assert min(x['optimal_cost'] for x in old['four_finite_exact_results'])==8343
    assert old['right_five_action_result']['optimal_cost']==8335
    rows={k:tuple(map(int,raw[str(k)]['counts'])) for k in range(214,315)}
    witnesses={}
    for label,tau in [('L',L),('U_minus_1',U-1)]:
        arr=[]
        for p,q,lo,hi in WIT:
            ks=[k for k in rows if abs(rows[k][p]-rows[k][q])>tau]
            assert ks==list(range(lo,hi+1)),(p,q,ks)
            arr.append({'states':[p,q],'first':lo,'last':hi,'count':len(ks)})
        witnesses[label]=arr
    supp={k:family(tuple(rows[k][h] for h in H),U-1) for k in THREE}
    act='12 3\n'+''.join(f'{k} {len(supp[k])} '+' '.join(map(str,supp[k]))+'\n' for k in THREE)
    actfile=out.with_name('ACTIONS_H12_F8_THREE_RIGHT.txt')
    actfile.write_text(act)
    got=subprocess.run([str(solver),str(actfile),'8'],capture_output=True,text=True,check=True,timeout=120)
    assert got.stdout.strip()=='EXACT_RESTRICTED n=12 f=8 V=8343 states=576895 actions=3',got.stdout
    obj={'schema':'R5_H12_F8_QUERY_TYPE_PARETO_V1','frozen_source_commit':'435e77af0d180eac32bd1f9c4c464bc4010b7551','input_sha256':SHA,'H12':list(H),'f':8,'L':str(L),'U_exclusive':str(U),'witnesses':witnesses,'three_action_right':{'costs':list(THREE),'minimax':8343,'states':576895,'stdout':got.stdout.strip(),'support_text_sha256':hashlib.sha256(act.encode()).hexdigest()},'reused_four_budget_left_lower':8343,'reused_five_budget_right_upper':8335,'pareto':{'m_le_2':'infinite','m_3_or_4':8343,'m_ge_5':8335},'review':'NOT_REVIEWED'}
    out.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
    print('PASS_R5_H12_F8_QUERY_TYPE_PARETO no_2_types=YES C3=C4=8343 C5plus=8335 three_Bellman_states=576895')
if __name__=='__main__':main()
