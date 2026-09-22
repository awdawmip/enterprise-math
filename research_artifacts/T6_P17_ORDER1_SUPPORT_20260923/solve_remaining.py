"""Reuse the proved two-branch tree for the remaining order1 inputs only."""
import hashlib
import json
import time
from pathlib import Path

import solve_r1 as support


def main():
    base=Path(__file__).resolve().parent
    common=json.loads(base.joinpath("portable_input.json").read_text())
    bundle=json.loads(base.joinpath("remaining_inputs.json").read_text())
    R, exact=support.R,support.exact
    basis=[[int(x) for x in row] for row in common["weighted_basis"]]
    weights=[int(x) for x in common["weights"]]
    norms=[R(int(n),int(d)) for n,d in common["gram_schmidt_squared"]]
    mu=[[R(int(n),int(d)) for n,d in row] for row in common["mu"]]
    reports=[]
    for case in bundle["cases"]:
        started=time.monotonic(); residue=int(case["residue"])
        x0=[int(x) for x in case["weighted_particular"]]
        centers=[R(int(n),int(d)) for n,d in case["centers"]]
        radius=R(int(case["radius_squared"]));positive=int(case["positive_q0_budget"])
        assert all(support.greater(d,radius) for d in norms)
        chosen=[0]*16;nodes=[];kernel=None
        def visit(i,partial):
            nonlocal kernel
            assert len(nodes)<131071
            center=centers[i]+sum(chosen[j]*mu[j][i] for j in range(i+1,16))
            quotient,remainder=exact.qr(center.n,center.d)
            index=len(nodes);node={"id":index,"level":i,"center":support.pack(center),"partial_before":support.pack(partial),"options":[]};nodes.append(node)
            for n in (-quotient-1,-quotient):
                chosen[i]=n;error=center+n;total=partial+error*error*norms[i]
                option={"coefficient":str(n),"partial_after":support.pack(total)};node["options"].append(option)
                if support.greater(total,radius):option["decision"]="PRUNE_EXACT_SQUARED_NORM"
                elif i:
                    option.update(decision="DESCEND",child=visit(i-1,total))
                    if kernel is not None:return index
                else:
                    weighted=[x0[t]+sum(chosen[j]*basis[j][t] for j in range(16)) for t in range(16)]
                    pos=sum(max(0,x) for x in weighted);neg=sum(max(0,-x) for x in weighted)
                    if pos<=positive and neg<=2331:
                        u=[exact.exact(x,w) for x,w in zip(weighted,weights)]
                        for k in range(1,7):
                            m=17**k;assert exact.rem(sum(a*exact.inv(j**k,m) for j,a in enumerate(u,1))+exact.inv((17+residue)**k,m),m)==0
                        kernel={"q0":[str(x) for x in u],"positive_total_mass":str(pos+int(case["vertical_mass"])),"negative_total_mass":str(neg)}
                        option["decision"]="MODULAR_KERNEL_FOUND"
                    else:option.update(decision="PRUNE_EXACT_SIDE_BUDGET",positive_q0_mass=str(pos),negative_q0_mass=str(neg))
            return index
        visit(15,R(0))
        report={"residue":residue,"maximal_prime17_admissible":case["maximal_prime17_admissible"],"status":"MODULAR_KERNEL_FOUND" if kernel else "AFFINE_CLASS_EMPTY","nodes":nodes,"node_count":len(nodes),"kernel":kernel,"input":case,"seconds":time.monotonic()-started}
        reports.append(report)
        print(json.dumps({k:v for k,v in report.items() if k not in {"nodes","input"}}),flush=True)
        if kernel is not None:break
    output={"schema":"T6_P17_ORDER1_ADDITIONAL_EXACT_CASES_V1","cases":reports,"all_15_completed":len(reports)==15,"common_input_sha256":hashlib.sha256(base.joinpath("portable_input.json").read_bytes()).hexdigest(),"remaining_input_sha256":hashlib.sha256(base.joinpath("remaining_inputs.json").read_bytes()).hexdigest(),"source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),"scope":"Each listed affine class only. Global T6 and higher vertical orders remain open."}
    base.joinpath("remaining_certificates.json").write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8',newline='\n')


if __name__=="__main__":main()
