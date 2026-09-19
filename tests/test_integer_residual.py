"""Independent exact-oracle regression tests; Fraction is TEST ONLY."""
import ast
from dataclasses import replace
from fractions import Fraction
import json
from pathlib import Path
from random import Random
import unittest

import importlib
from enterprise_math.exact_arithmetic import (
    DivisionExpr, RootExpr, brc_scaled_evaluate, brc_scaled_evaluate_root,
)
from enterprise_math.integer_residual import (
    SignedDivisionExpr as R, IntegerResidual, RationalEnclosure, CertifiedOrder,
    brc_rational_root_scaled_evaluate as root_cell,
)

COUNTS = {}


class IntegerResidualTests(unittest.TestCase):
    def test_signed_division_exhaustive(self):
        count = 0
        for n in range(-60, 61):
            for d in range(1, 31):
                for s in (1, 2, 7, 10, 1000):
                    result = R(n, d).at_scale(s)
                    self.assertEqual((result.index, result.remainder), divmod(n*s, d))
                    self.assertEqual(Fraction(result.index, s) + Fraction(result.remainder, d*s), Fraction(n, d))
                    self.assertTrue(result.enclosure().contains(R(n,d)))
                    count += 1
        COUNTS['signed_division_cases'] = count

    def test_negative_floor_and_grid(self):
        a = R(-1,7).at_scale(1000)
        self.assertEqual((a.index,a.remainder,a.denominator),(-143,1,7))
        self.assertEqual((R(-14,7).at_scale(1).index,R(-14,7).at_scale(1).remainder),(-2,0))
        self.assertEqual(R(0,19).at_scale(7).source, R(0,19))

    def test_source_identity_is_not_value_identity(self):
        a,b = R(2,4),R(1,2)
        self.assertNotEqual(a,b)
        self.assertEqual(a.compare_value(b),0)
        self.assertEqual(len({a,b}),2)
        self.assertNotEqual(a.at_scale(1).remainder,b.at_scale(1).remainder)

    def test_random_signed_arithmetic(self):
        random = Random(20260919)
        for _ in range(2500):
            a,c = (random.getrandbits(180)*random.choice((-1,1)) for _ in range(2))
            b,d = (random.getrandbits(100)+1 for _ in range(2))
            x,y = R(a,b),R(c,d)
            ox,oy = Fraction(a,b),Fraction(c,d)
            added, multiplied = x.plus(y),x.times(y)
            self.assertEqual(Fraction(added.numerator,added.denominator),ox+oy)
            self.assertEqual(Fraction(multiplied.numerator,multiplied.denominator),ox*oy)
            self.assertEqual(x.compare_value(y),(ox>oy)-(ox<oy))
            if a:
                inverse = x.reciprocal()
                self.assertEqual(Fraction(inverse.numerator,inverse.denominator),1/ox)
        COUNTS['random_arithmetic_cases'] = 2500

    def test_refinement_carry_and_nesting(self):
        count = 0
        for n in range(-40,41):
            for d in range(1,20):
                coarse = R(n,d).at_scale(7)
                for factor in (1,2,3,11):
                    fine = coarse.refine(factor)
                    carry,rem = divmod(factor*coarse.remainder,d)
                    self.assertEqual((fine.index,fine.remainder),(factor*coarse.index+carry,rem))
                    self.assertTrue(coarse.enclosure().contains_enclosure(fine.enclosure()))
                    self.assertIs(fine.source,coarse.source)
                    count += 1
        COUNTS['refinement_cases'] = count

    def test_unmodified_positive_facade_reused(self):
        count=0
        for n in range(50):
            for d in range(1,11):
                for scale in (1,3,100):
                    old=brc_scaled_evaluate(DivisionExpr(n,d),scale)
                    new=R(n,d).at_scale(scale)
                    self.assertEqual(old.trace,new.magnitude_trace)
                    count+=1
        COUNTS['positive_facade_comparisons']=count

    def test_rational_roots_exhaustive(self):
        count=0
        for n in range(61):
            for d in range(1,11):
                for degree in range(1,6):
                    for scale in (1,2,7):
                        cell=root_cell(R(n,d),degree,scale)
                        q=cell.index
                        self.assertLessEqual(d*q**degree,n*scale**degree)
                        self.assertLess(n*scale**degree,d*(q+1)**degree)
                        self.assertEqual(cell.residual,n*scale**degree-d*q**degree)
                        self.assertEqual(cell.on_grid,cell.residual==0)
                        count+=1
        COUNTS['rational_root_cases']=count

    def test_unmodified_root_facade_reused(self):
        count=0
        for n in range(61):
            for degree in range(1,6):
                for scale in (1,3,10):
                    old=brc_scaled_evaluate_root(RootExpr(n,degree),scale)
                    new=root_cell(R(n),degree,scale)
                    self.assertEqual(old.trace,new.root_trace)
                    count+=1
        COUNTS['root_facade_comparisons']=count

    def test_root_exact_boundary_and_units(self):
        a=root_cell(R(2),2,1000)
        self.assertEqual((a.index,a.residual),(1414,604))
        fake=Fraction(a.index,a.scale)+Fraction(a.residual,a.source.denominator*a.scale)
        self.assertNotEqual(fake*fake,Fraction(2))
        exact=root_cell(R(9,4),2,2)
        self.assertEqual((exact.index,exact.residual),(3,0))
        self.assertTrue(exact.enclosure().is_point)
        self.assertTrue(a.enclosure().contains_enclosure(a.refine(10).enclosure()))

    def test_interval_tristate_and_truth_coercion(self):
        a=RationalEnclosure(R(0),R(2))
        b=RationalEnclosure(R(1),R(3))
        self.assertIs(a.compare(b),CertifiedOrder.UNRESOLVED)
        self.assertIs(a.compare(RationalEnclosure(R(3),R(4))),CertifiedOrder.LESS)
        self.assertIs(b.compare(RationalEnclosure(R(-2),R(-1))),CertifiedOrder.GREATER)
        self.assertIs(RationalEnclosure(R(2,4),R(2,4)).compare(RationalEnclosure(R(1,2),R(1,2))),CertifiedOrder.EQUAL)
        self.assertIs(RationalEnclosure(R(0),R(1)).compare(RationalEnclosure(R(1),R(2))),CertifiedOrder.UNRESOLVED)
        for item in CertifiedOrder:
            with self.assertRaises(TypeError):
                bool(item)

    def test_large_bits_and_near_boundary(self):
        n=2**1024
        a,b=R(n-1,n),R(1)
        self.assertEqual(a.compare_value(b),-1)
        self.assertEqual(a.at_scale(1).index,0)
        negative=R(-1,n).at_scale(1)
        self.assertEqual((negative.index,negative.remainder),(-1,n-1))
        a=R(2**4096+1,2**2048+3).at_scale(2**128)
        self.assertEqual(IntegerResidual.from_wire(a.to_wire()),a)

    def test_native_reciprocal_depth_witness(self):
        u=[R(3,8)]+[R(-1,8)]*5
        v=[R(7,12)]+[R(1,12)]*5
        du,dv=u[1],v[1]
        self.assertNotEqual(du.compare_value(dv),0)
        for x,y in zip(u,v):
            self.assertEqual(x.plus(du.negative()).compare_value(y.plus(dv.negative())),0)
        self.assertEqual([x.at_scale(24).index for x in u],[9,-3,-3,-3,-3,-3])
        self.assertEqual([x.at_scale(24).index for x in v],[14,2,2,2,2,2])

    def test_strict_inputs_and_zero(self):
        for bad in (True,False,0.5,float('nan'),float('inf'),'1',Fraction(1,2)):
            with self.assertRaises((TypeError,ValueError)):
                R(bad)
            with self.assertRaises((TypeError,ValueError)):
                R(1,bad)
            with self.assertRaises((TypeError,ValueError)):
                R(1).at_scale(bad)
            for operation in (R(1).plus,R(1).times,R(1).compare_value):
                with self.assertRaises(TypeError):
                    operation(bad)
        with self.assertRaises(ZeroDivisionError):
            R(0).reciprocal()
        for d in (0,-1):
            with self.assertRaises(ValueError):
                R(1,d)
        with self.assertRaises(ValueError):
            root_cell(R(-1),3,100)
        with self.assertRaises(ValueError):
            R(1).at_scale(1).refine(0)
        with self.assertRaises(ValueError):
            RationalEnclosure(R(2),R(1))

    def test_wire_and_forgery_rejection(self):
        original=R(-1,7).at_scale(1000)
        wire=json.loads(json.dumps(original.to_wire()))
        self.assertEqual(IntegerResidual.from_wire(wire),original)
        for bad in ('1.0','1e5','+1','-0','01','\u0661',1,True):
            invalid=wire|{'numerator':bad}
            with self.assertRaises(ValueError):
                IntegerResidual.from_wire(invalid)
        with self.assertRaises(ValueError):
            IntegerResidual.from_wire(wire|{'remainder':'2'})
        with self.assertRaises(ValueError):
            replace(original,index=original.index+1)
        with self.assertRaises(ValueError):
            replace(original,magnitude_trace=replace(original.magnitude_trace,quotient=0))
        root=root_cell(R(2),2,1000)
        with self.assertRaises(ValueError):
            replace(root,residual=root.residual+1)

    def test_core_static_inventory(self):
        # Exactly this tested dependency slice, not all repository Python modules.
        paths=[Path(importlib.import_module("enterprise_math."+name).__file__)
               for name in ("core", "division", "exact_arithmetic", "integer_residual")]
        for path in paths:
            for node in ast.walk(ast.parse(path.read_text())):
                self.assertFalse(isinstance(node,ast.Constant) and isinstance(node.value,(float,complex)),(path,node))
                self.assertFalse(isinstance(node,ast.BinOp) and isinstance(node.op,ast.Div),(path,node))
                if isinstance(node,ast.Call) and isinstance(node.func,ast.Name):
                    self.assertNotIn(node.func.id,('float','complex','round'),(path,node))
        COUNTS['strict_core_files']=len(paths)
