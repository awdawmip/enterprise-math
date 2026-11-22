"""Check the two new larger inventories against the original positive paths."""
from argparse import ArgumentParser
from pathlib import Path
import hashlib
import json

from all_origins_compare import load_kernel


def main():
    parser=ArgumentParser()
    parser.add_argument("--kernel",type=Path,required=True)
    args=parser.parse_args()
    kernel=load_kernel(args.kernel)
    cases=0
    for n in (23,24):
        for v in range(2,9):
            for w in range(2,v+1):
                assert kernel.kernel_tail_ratios(n,v,w)==kernel.positive_path_tail_ratios(n,v,w)
                cases+=1
    result={"base_inventory":8,"stocks":[23,24],"templates":28,
            "inventory_template_cases":cases,"individual_tail_equalities":3*cases,
            "arithmetic":"fractions.Fraction","all_equalities_passed":True,
            "scope":"New larger inventories used by this round; old checks are not counted again.",
            "kernel_sha256":hashlib.sha256(args.kernel.read_bytes()).hexdigest()}
    Path(__file__).with_name("native_new_stock_path_checks.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))


if __name__=="__main__":
    main()
