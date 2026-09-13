"""Runtime and schema integration checks; not a substitute for Lean proofs."""
from __future__ import annotations
import itertools, json, math, random, subprocess, sys, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from enterprise_math.cell_address import (FinalCellAddress, encode_raw_slice,
    decode_raw_slice, step_cell, cell_step_distance, cell_squared_distance)

DIRS={'E1_FORWARD':(1,0),'E1_REVERSE':(-1,0),'E2_FORWARD':(0,1),'E2_REVERSE':(0,-1)}
INV={'E1_FORWARD':'E1_REVERSE','E1_REVERSE':'E1_FORWARD','E2_FORWARD':'E2_REVERSE','E2_REVERSE':'E2_FORWARD'}

class CellAddressContractTests(unittest.TestCase):
    def test_roundtrip_unique_grid(self):
        seen=set()
        for p in itertools.product(range(-12,13),repeat=2):
            a=encode_raw_slice(p)
            self.assertEqual(decode_raw_slice(a),p)
            self.assertNotIn(a,seen);seen.add(a)
            self.assertEqual(FinalCellAddress.from_json(a.to_json()),a)
        self.assertEqual(len(seen),625)

    def test_all_four_transitions_and_inverse(self):
        for p in itertools.product(range(-12,13),repeat=2):
            a=encode_raw_slice(p)
            for d,v in DIRS.items():
                b=step_cell(a,d)
                self.assertEqual(decode_raw_slice(b),(p[0]+v[0],p[1]+v[1]))
                self.assertEqual(step_cell(b,INV[d]),a)
                self.assertEqual(cell_step_distance(a,b),1)

    def test_equal_boundary_family(self):
        for k in range(1,129):
            a=FinalCellAddress((0,1,k,0,0,0))
            self.assertEqual(step_cell(a,'E1_FORWARD').coordinates,(1,0,k,0,0,0))
            a=FinalCellAddress((k,0,1,0,0,0))
            self.assertEqual(step_cell(a,'E2_FORWARD').coordinates,(k,1,0,0,0,0))

    def test_adjusted_boundary_family(self):
        for k in range(128):
            a=FinalCellAddress((0,k+2,1,0,0,0))
            self.assertEqual(step_cell(a,'E1_FORWARD').coordinates,(1,k+1,0,0,0,0))

    def test_original_zero_cell_not_deleted(self):
        a=encode_raw_slice((0,0))
        self.assertEqual(a.coordinates,(0,1,1,0,0,0))
        self.assertEqual(cell_step_distance(a,a),0)
        self.assertNotEqual(a.coordinates,(0,)*6)

    def test_distance_uses_decoded_cells(self):
        a=FinalCellAddress((0,1,4,0,0,0));b=FinalCellAddress((1,0,4,0,0,0))
        self.assertEqual(cell_step_distance(a,b),1)
        self.assertEqual(cell_squared_distance(a,b),1)
        self.assertEqual(sum(abs(x-y) for x,y in zip(a.coordinates,b.coordinates)),2)
        from enterprise_math.geometry import l1_distance
        with self.assertRaises(TypeError): l1_distance(a,b)
        self.assertEqual(l1_distance((-3,-3),(-2,-3)),1)

    def test_illegal_coordinates_rejected(self):
        for c in [(0,)*6,(-1,2,0,0,0,0),(1,2,3,0,0,0),(0,1,2,1,0,0),
                  (0,1,True,0,0,0),(0,1,2.0,0,0,0),(0,1,'2',0,0,0),
                  (0,1,None,0,0,0),(0,1,2),[0,1,2,0,0,0]]:
            with self.subTest(c=c),self.assertRaises(ValueError): FinalCellAddress(c)

    def test_invalid_envelopes_and_versions(self):
        base=encode_raw_slice((0,0)).to_wire()
        for k,v in [('codec','full_x6'),('version',True),('version',2),('frame','changed')]:
            bad=dict(base);bad[k]=v
            with self.assertRaises(ValueError): FinalCellAddress.from_wire(bad)
        for bad in [base['coordinates'],{},dict(base,origin=[0,0]),dict(base,negative_axes=True)]:
            with self.assertRaises(ValueError):FinalCellAddress.from_wire(bad)
        with self.assertRaises(ValueError):encode_raw_slice((0,0,1,0,0,0))

    def test_display_is_not_operand(self):
        for x in [None,0,{'type':'DISPLAY_REFERENCE'},(0,)*6]:
            with self.assertRaises(TypeError):step_cell(x,'E1_FORWARD')
        a=encode_raw_slice((0,0))
        for d in ['CROSS_AND_INCREMENT','E3_FORWARD',0,None]:
            with self.assertRaises(ValueError):step_cell(a,d)

    def test_strict_json(self):
        a=encode_raw_slice((0,0));text=a.to_json()
        for bad in [text.replace('"version":1','"version":1.0'),
                    text.replace('"version":1','"version":true'),
                    text.replace('"version":1','"version":1,"version":1'),
                    text.replace('[0,1,1,0,0,0]','[0,1,NaN,0,0,0]')]:
            with self.assertRaises(ValueError):FinalCellAddress.from_json(bad)

    def test_large_exact_integers(self):
        for p in [(2**256,2**512),(-2**256,2**512),(-2**512,-2**256)]:
            a=encode_raw_slice(p)
            self.assertEqual(decode_raw_slice(FinalCellAddress.from_json(a.to_json())),p)

    def test_random_paths(self):
        rng=random.Random(20260913)
        for _ in range(100):
            p=(rng.randint(-30,30),rng.randint(-30,30));a=encode_raw_slice(p)
            for _ in range(100):
                d=rng.choice(tuple(DIRS));v=DIRS[d]
                p=(p[0]+v[0],p[1]+v[1]);a=step_cell(a,d)
                self.assertEqual(decode_raw_slice(a),p)

    def test_brc_words_not_erased(self):
        start=encode_raw_slice((-2,1));target=encode_raw_slice((2,-1))
        words=set(itertools.permutations(['E1_FORWARD']*4+['E2_REVERSE']*2))
        self.assertEqual(len(words),math.comb(6,2))
        for w in words:
            a=start
            for d in w:a=step_cell(a,d)
            self.assertEqual(a,target)
        self.assertEqual(step_cell(step_cell(start,'E1_FORWARD'),'E1_REVERSE'),start)
        self.assertEqual(cell_step_distance(start,target),6)

    def test_json_schema(self):
        from jsonschema import Draft202012Validator
        schema=json.loads((ROOT/'schemas/cell_address.schema.json').read_text())
        Draft202012Validator.check_schema(schema)
        validator=Draft202012Validator(schema)
        for p in [(0,0),(-5,2),(3,-1),(2,4)]:validator.validate(encode_raw_slice(p).to_wire())
        base=encode_raw_slice((0,0)).to_wire()
        for c in [[-1,1,0,0,0,0],[0]*6,[1,2,3,0,0,0],[0,1,True,0,0,0],[0,1,2,0,0,1]]:
            bad=dict(base);bad['coordinates']=c
            self.assertFalse(validator.is_valid(bad))

    def test_cli(self):
        a=encode_raw_slice((0,0))
        good=subprocess.run([sys.executable,str(ROOT/'tools/validate_cell_address.py')],input=a.to_json(),text=True,capture_output=True)
        self.assertEqual(good.returncode,0,good.stderr)
        self.assertTrue(json.loads(good.stdout)['valid'])
        bad=subprocess.run([sys.executable,str(ROOT/'tools/validate_cell_address.py')],input='{"type":"DISPLAY_REFERENCE"}',text=True,capture_output=True)
        self.assertEqual(bad.returncode,2,bad.stderr)

    def test_contract_does_not_promote_full_x6(self):
        c=json.loads((ROOT/'coordinate_address_contract.json').read_text())
        self.assertEqual(c['types']['FINAL_CELL_ADDRESS']['field_count'],6)
        self.assertFalse(c['crossing']['forced_increment'])
        self.assertFalse(c['full_x6_codec']['fallback_to_slice'])
        self.assertEqual(list(c['registered_codecs']),['three_region_slice_v1'])

if __name__=='__main__':unittest.main()
