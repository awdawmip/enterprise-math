import json
from pathlib import Path
from itertools import combinations
import sympy as s
root=Path(__file__).parent
obj=json.loads((root/'derived.json').read_text())
l=s.Symbol('lambda');x,y=s.symbols('x y')
shapes=[[s.sympify(t.replace('lambda','lam'),locals={'lam':l}) for t in row['centered']] for row in obj['phase_coefficients']]
full=[[s.sympify(t.replace('lambda','lam'),locals={'lam':l}) for t in row['r_inverse']] for row in obj['phase_coefficients']]
for name, data in [('shape',shapes),('full',full)]:
    same=[];free=[]
    for a,b in combinations(range(6),2):
        sol=s.solve([p-q for p,q in zip(data[a],data[b])],[l],dict=True)
        if sol:same.append((a,b,sol))
        sol=s.solve([p.subs(l,x)-q.subs(l,y) for p,q in zip(data[a],data[b])],[x,y],dict=True)
        for v in sol:
            radius=max([abs(t) for t in v.values()]+[s.Integer(0)])
            free.append((a,b,{str(k):str(t) for k,t in v.items()},str(radius)))
    print(name, 'known shared lambda',same)
    print(name, 'independent lambda collisions',free)
    obj[name+'_known_lambda_collisions']=[{'phases':[a,b],'lambda':str(sol[0][l])} for a,b,sol in same]
    obj[name+'_unknown_lambda_collisions']=free
(root/'classified.json').write_text(json.dumps(obj,indent=2)+'\n')
