"""Heuristic integer-cover search on explicitly selected complete affine class orbits.
A timeout is recorded only as a timeout; any witness is checked by the native
finite observation implementation before it is accepted.
"""
from pathlib import Path
from collections import Counter
import argparse,json,sys,time
import numpy as np
from scipy.optimize import milp,LinearConstraint,Bounds
from scipy.sparse import coo_matrix

HERE=Path(__file__).resolve().parent
OLD=HERE.parent/'previous/previous/previous/previous/previous/previous'
sys.path.insert(0,str(OLD/'bounds'))
from cyclic11 import observations,class_cost
p=argparse.ArgumentParser()
p.add_argument('--sizes',default='9,10,11,12,13')
p.add_argument('--fix',type=int,default=13)
p.add_argument('--orbit',type=int,default=0)
p.add_argument('--fixed-classes',default='')
p.add_argument('--presolve',type=int,default=1)
p.add_argument('--budget',type=int,default=9995)
p.add_argument('--seconds',type=int,default=60)
p.add_argument('--output',default='milp_result.json')
a=p.parse_args()
sizes=set(map(int,a.sizes.split(',')))
rows=np.fromfile(HERE/'bank',dtype=[('lo','<u8'),('hi','<u8'),('cost','<u4'),('tag','<u4')])
rows=rows[np.isin(rows['tag']%256,list(sizes))]
# The row marker >=256 is one representative of each complete affine orbit.
reps=rows[(rows['tag']==a.fix+256)]
if a.fixed_classes:
    cl=json.loads((HERE.parent/'previous/previous/previous/c3/groups.json').read_text())
    bad,pair=observations()
    chosen=[sum(1<<x for x in cl[int(j)])for j in a.fixed_classes.split(',')]
    fixedcost=sum(class_cost(cl[int(j)],pair)for j in a.fixed_classes.split(','))
    used=sum(chosen)
    rows=rows[((rows['lo']&np.uint64(used%2**64))==0)&((rows['hi']&np.uint64(used>>64))==0)]
elif a.fix:
    fixed=reps[a.orbit]
    chosen=[int(fixed['lo'])+(int(fixed['hi'])<<64)]
    fixedcost=int(fixed['cost'])
    rows=rows[((rows['lo']&fixed['lo'])==0)&((rows['hi']&fixed['hi'])==0)]
else: chosen=[];fixedcost=0
masks=[int(r['lo'])+(int(r['hi'])<<64)for r in rows]
I=[];J=[];V=[]
for j,m in enumerate(masks):
    for i in range(125):
        if (m>>i)&1:I.append(i);J.append(j);V.append(1.)
    I.extend([125,126]);J.extend([j,j]);V.extend([1.,float(rows[j]['cost'])])
mat=coo_matrix((V,(I,J)),shape=(127,len(rows))).tocsc()
remain=((1<<125)-1)^sum(chosen)
lb=np.array([float((remain>>i)&1)for i in range(125)]+[12-len(chosen),-np.inf])
ub=np.array([float((remain>>i)&1)for i in range(125)]+[12-len(chosen),a.budget-fixedcost])
print('rows',len(rows),'fixed',a.fix,a.orbit,'budget',a.budget,flush=True)
start=time.time()
r=milp(rows['cost'].astype(float),integrality=np.ones(len(rows)),bounds=Bounds(0,1),constraints=LinearConstraint(mat,lb,ub),options={'disp':True,'time_limit':a.seconds,'mip_rel_gap':0,'presolve':bool(a.presolve)})
result={k:getattr(r,k,None)for k in ['status','message','fun','mip_node_count','mip_dual_bound','mip_gap']}
result.update(elapsed=time.time()-start,rows=len(rows),sizes=sorted(sizes),fixed_size=a.fix,fixed_classes=a.fixed_classes,fixed_orbit=a.orbit,budget=a.budget,scope='restricted candidate search; not a global exclusion')
if r.x is not None:
    chosen += [m for m,x in zip(masks,r.x)if x>.5]
    groups=[[i for i in range(125)if (m>>i)&1]for m in chosen]
    bad,pair=observations()
    assert len(groups)==12 and sorted(sum(groups,[]))==list(range(125))
    assert all(not(bad[i][j]&m)for m,cl in zip(chosen,groups)for i in cl for j in cl)
    cost=sum(class_cost(cl,pair)for cl in groups)
    assert cost<=a.budget
    result.update(groups=groups,verified_cost=cost)
(HERE/a.output).write_text(json.dumps(result,indent=2)+'\n')
print(result,flush=True)
