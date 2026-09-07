from fractions import Fraction as Q
from itertools import combinations
import json
import random
import noisy_recovery as noisy
from exact_feasibility import verify_certificate

rng=random.Random(202609071909)
D=((0,)*6,(1,0,0,0,0,0))
checks=0
statuses={'FEASIBLE':0,'INFEASIBLE':0}

def observed_residual(tables, cells, masses):
    total=Q(0)
    for axes in noisy.AXES:
        predicted={}
        for point,mass in zip(cells,masses):
            addr=tuple(point[j] for j in axes)
            predicted[addr]=predicted.get(addr,Q(0))+mass
        for addr in predicted.keys()|tables[axes].keys():
            total+=abs(predicted.get(addr,Q(0))-tables[axes].get(addr,Q(0)))
    return total

for trial in range(16):
    cells=D[:1] if trial<8 else D
    tables={axes:{} for axes in noisy.AXES}
    for axis_index,axes in enumerate(noisy.AXES):
        for point in cells:
            addr=tuple(point[j] for j in axes)
            if rng.randrange(4):
                tables[axes][addr]=Q(rng.randrange(-4,9),rng.randrange(1,5))
        if axis_index%4==trial%4:
            tables[axes][(8,9,10)]=Q(rng.randrange(-3,4),3)
    if len(cells)==1:
        ys=sorted(tables[axes].get((0,0,0),Q(0)) for axes in noisy.AXES)
        median=max(Q(0),ys[9])
        optimum=observed_residual(tables,cells,(median,))
    else:
        # Piecewise-linear objective in the nonnegative quadrant. Its affine
        # cells are cut by v=a, w=b and v+w=c; a minimum occurs at a vertex.
        # Enumerate all line intersections exactly, independently of Phase I.
        lines={(Q(1),Q(0),Q(0)),(Q(0),Q(1),Q(0))}
        for axes in noisy.AXES:
            projected=[tuple(point[j] for j in axes) for point in cells]
            for addr in set(projected):
                lines.add((Q(projected[0]==addr),Q(projected[1]==addr),tables[axes].get(addr,Q(0))))
        vertices={(Q(0),Q(0))}
        for (a,b,c),(d,e,f) in combinations(lines,2):
            determinant=a*e-b*d
            if determinant:
                v=(c*e-b*f)/determinant
                w=(a*f-c*d)/determinant
                if v>=0 and w>=0: vertices.add((v,w))
        optimum=min(observed_residual(tables,cells,mass) for mass in vertices)
    for budget in (optimum,optimum+Q(1,13),max(Q(0),optimum-Q(1,7))):
        expected=budget>=optimum
        try:
            answer=noisy.fit_budgeted_noise(tables,cells,residual_budget=budget,truth_noise_budget=Q(2,7))
        except noisy.InfeasibleNoiseBudgetError as error:
            assert not expected,(trial,budget,optimum)
            assert verify_certificate(error.rows,error.rhs,error.certificate)
            assert error.scope=='DECLARED_FINITE_CARRIER_AND_RESIDUAL_BUDGET_ONLY'
            statuses['INFEASIBLE']+=1
        else:
            assert expected,(trial,budget,optimum)
            fit=dict(answer['distribution'])
            residual=observed_residual(tables,cells,tuple(fit.get(x,Q(0)) for x in cells))
            assert residual==answer['actual_stacked_l1_residual'] and residual<=budget
            assert answer['conditional_l1_bound']==Q(111,20)*(Q(2,7)+residual)
            statuses['FEASIBLE']+=1
        checks+=1
print(json.dumps({'status':'PASS','seed':202609071909,'independent_oracle_systems':16,'budget_boundary_checks':checks,'statuses':statuses,'oracles':['one-variable constrained median','two-variable rational kink-vertex enumeration']}))
