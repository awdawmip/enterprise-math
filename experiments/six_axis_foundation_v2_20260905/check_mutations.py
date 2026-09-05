"""Focused mutation controls: ensure wrong mathematical shortcuts are caught."""
from unittest.mock import patch
from pathlib import Path
import json
from fractions import Fraction as F
import sympy as s
import six_axis as a
import ports
from vendor import atlas_brc as old


def require(c):
    if not c:raise AssertionError('mutant violated the invariant')

def must_reject(fn):
    try:fn()
    except (ValueError,TypeError):return
    raise AssertionError('unsafe input was accepted')


def main():
    z,t=s.symbols('z t')
    sig=ports.schur_ports(s.Matrix([[0,z/t],[t*z,0]]),(0,1),(1,),z)
    plain=ports.FormalPortSignature(('a',),s.ImmutableMatrix([[z]]),s.Integer(1),z)
    renamed=ports.FormalPortSignature(('b',),plain.effective,plain.hidden_determinant,z)
    h=(0,2,3,1)
    k=old.BranchKey(F(1),(1,0,0,0,0,0),h,1)
    q=old.BranchKey(F(1),(1,0,0,0,0,0),old.IDENTITY,1)
    original_then=old.BranchKey.then
    def drop_frame(self,other):
        r=original_then(self,other)
        return old.BranchKey(r.weight,r.axes,old.IDENTITY,r.length)
    original_rotation=a.rotation_matrix
    def invert_rotation(g):return tuple(tuple(-x for x in row) for row in original_rotation(g))
    bad={0:(0,0,0),1:(0,0,0),2:(0,1,0),3:(0,0,0)}
    r=(1,1,0,0,0,0);u=(0,0,1,0,0,0)
    def wrong_carry(r,u,g=old.IDENTITY):
        return old.compression_carry(old.BranchKey(1,r,g),old.BranchKey(1,u))
    mutants=[
      ('improper_instead_of_proper_rotation',a,'rotation_matrix',invert_rotation,
       lambda:require(s.Matrix(a.rotation_matrix(old.IDENTITY)).det()==1)),
      ('skip_chart_cycle_consistency',a,'reconstruct',lambda charts:(0,)*6,
       lambda:must_reject(lambda:a.reconstruct(bad))),
      ('erase_common_depth',a.CountAtlas,'decode',lambda self:a.reconstruct(dict(enumerate(self.charts))),
       lambda:require(a.CountAtlas.encode((7,)*6).decode()==(7,)*6)),
      ('replace_depth_carry_by_extraction_carry',a,'depth_carry',wrong_carry,
       lambda:require(a.depth_carry(r,u)==0)),
      ('erase_resulting_rotation_frame',old.BranchKey,'then',drop_frame,
       lambda:require(k.then(q).frame==h)),
      ('ignore_port_labels',ports,'same_labeled_ports',lambda *args,**kw:True,
       lambda:require(not ports.same_labeled_ports(plain,renamed))),
      ('specialize_through_original_pole',ports,'specialize_ports',lambda *args,**kw:sig,
       lambda:must_reject(lambda:ports.specialize_ports(sig,{t:0}))),
    ]
    caught=[]
    for name,obj,attr,replacement,oracle in mutants:
        oracle()  # Original implementation must pass the SAME oracle.
        with patch.object(obj,attr,replacement):
            try:oracle()
            except AssertionError:caught.append(name)
            else:raise AssertionError('mutant escaped: '+name)
    result={'status':'PASS_ALL_TARGETED_MUTANTS_KILLED','mutant_count':len(caught),'mutants':caught,
            'scope':'Focused negative controls, not exhaustive mutation coverage.'}
    Path(__file__).with_name('verification_mutations.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
