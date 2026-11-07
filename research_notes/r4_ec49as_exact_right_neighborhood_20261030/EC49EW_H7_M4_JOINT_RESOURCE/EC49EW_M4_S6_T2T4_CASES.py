#!/usr/bin/env python3
"""Complete exact exhaustive certificate for 7-window 4-key schedules of type 22242.
T2 for h3,h4,h5,h7 and T4 for h6. No filter on candidate native words.
"""
import json,subprocess,re,time
from pathlib import Path
import EC49EW_S6_SEARCH as m
root=Path(__file__).parent
K=(2,2,2,4,2)
f={h:[p for p,t in m.FIBERS[h].items() if t==str(K[h-3])] for h in range(3,8)}
ss=[]
for p3 in f[3]:
 for p4 in f[4]:
  for p5 in f[5]:
   for p6 in f[6]:
    for p7 in f[7]:
     ps=(m.P0,p3,p4,p5,p6,p7)
     if len(set(ps))==4:ss.append(ps)
assert ss
exe=root/'ec49ew_dp'
subprocess.run(['g++','-O3','-std=c++17',str(root/'VERIFY_EC49EU_EXACT_DP.cpp'),'-o',str(exe)],check=True)
out=[];t=time.monotonic()
for index,ps in enumerate(ss):
 data,N,ncolors=m.trie(ps)
 proc=subprocess.run([str(exe)],input=data,capture_output=True,text=True,check=True)
 match=re.fullmatch(r'PASS min_extra=(\d+) total=(\d+) nodes=(\d+) colors=(\d+) largest_states=(\d+) convolutions=(\d+)',proc.stdout.strip())
 assert match
 extra,total,nodes,colors,states,convolutions=map(int,match.groups())
 assert total==28+extra and nodes==N and colors==ncolors
 out.append({'index':index,'p_h2_to_h7':list(ps),'exact_E':total,'tree_nodes':N,'color_count':colors,'max_live_states':states,'convolutions':convolutions})
 print('DONE',index,'E',total,flush=True) if index%20==0 else None
best=min(row['exact_E'] for row in out)
report={'status':'PASS','scope':'H=2..7, M=4,S<=6, observer schedule T2,T2,T2,T4,T2 for h3..h7, all frozen native 7-operation words','all_candidate_key_schedules':len(ss),'complete_exact_DP_case_count':len(out),'minimum_E_in_subfamily':best,'minimizers':[x for x in out if x['exact_E']==best],'exact_case_distribution':{str(e):sum(x['exact_E']==e for x in out) for e in sorted(set(x['exact_E'] for x in out))},'all_cases':out,'seconds':round(time.monotonic()-t,3),'proof':'Each schedule is enumerated by all positive-key fibers with the declared required full-rank T2/T4 signatures. All eligible returning signed-six-axis paths enter a native-step trie; the exact group-Steiner OR-mask integer DP minimizes union native prefix edges. Finite exhaustive schedules and exact DP certify subfamily minimum; independent witness checker certifies upper bound for unrestricted M4,S<=6.'}
(root/'EC49EW_T2T4_EXACT_EXECUTED.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('SUMMARY',json.dumps({k:v for k,v in report.items() if k not in ['all_cases','minimizers']},ensure_ascii=False,indent=2))
print('WINNERS',json.dumps(report['minimizers'][:3],ensure_ascii=False))
