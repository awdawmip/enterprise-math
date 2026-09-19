from __future__ import annotations
import copy
import hashlib
import json
import math
import tempfile
import unittest
from pathlib import Path
from nollm_visual_toolkit import core as c

class CoreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full = c.demo_hex()
        cls.small = c.demo_hex(256)
        cls.x6 = c.demo_x6()

    def test_population_unique_coordinates(self):
        self.assertEqual(len(self.full['records']), 65536)
        self.assertEqual(len({tuple(r['coord']) for r in self.full['records']}), 65536)

    def test_65536_identity_inverse(self):
        inv = {tuple(r['coord']):r['n'] for r in self.full['records']}
        for r in self.full['records']:
            self.assertEqual(inv[tuple(r['coord'])],r['n'])

    def test_periodic_complete(self):
        self.assertEqual(len({tuple(x%256 for x in r['coord']) for r in self.full['records']}),65536)

    def test_base4_rotation_all(self):
        rows=self.full['records']
        for n in range(16384):
            self.assertEqual(rows[4*n]['coord'],list(2*x for x in c.rotate_hex(rows[n]['coord'])))

    def test_complement_all(self):
        rows=self.full['records']
        for n in range(32768):
            self.assertEqual([a+b for a,b in zip(rows[n]['coord'],rows[65535-n]['coord'])],[-1,257])

    def test_mod3_all(self):
        for row in self.full['records']:
            q,r=row['coord'];self.assertEqual((q-r)%3,row['n']%3)

    def test_prime_zero_and_one(self):
        rows=self.full['records'];self.assertFalse(rows[0]['fields']['prime']);self.assertFalse(rows[1]['fields']['prime'])
        self.assertEqual(sum(r['fields']['prime'] for r in rows),6542)
        self.assertIsNone(rows[0]['fields']['v2'])

    def test_rotations_and_metric(self):
        for q in range(-5,6):
            for r in range(-5,6):
                self.assertEqual(c.rotate_hex((q,r),6),(q,r))
                a,b=c.rotate_hex((q,r));self.assertEqual(c.hex_norm_sq(q,r),c.hex_norm_sq(a,b))
                cube=c.cube_coordinate((q,r));self.assertEqual(sum(cube),0)
                self.assertEqual(sum(x*x for x in cube),2*c.hex_norm_sq(q,r))

    def test_six_directions(self):
        self.assertEqual(len(set(c.HEX_DIRECTIONS)),6)
        for d in c.HEX_DIRECTIONS:
            self.assertEqual(c.hex_distance(d,(0,0)),1)
            self.assertEqual(sum(c.cube_coordinate(d)),0)

    def test_twelve_x6_signed_axes(self):
        for i in range(6):
            for sign in (1,-1):
                a=[0]*6;a[i]=sign
                self.assertEqual(c.project_x6(a),tuple(sign*x for x in c.FCC_AXES[i]))

    def test_projection_loss_retains_ids(self):
        data={'schema':c.SCHEMA,'kind':'x6','records':[{'id':'a','coord':[0]*6},{'id':'b','coord':[1,0,-1,0,0,-1]}]}
        self.assertEqual(c.collision_groups(data),[{'position':[0,0,0],'ids':['a','b']}])
        self.assertNotEqual(data['records'][0]['coord'],data['records'][1]['coord'])

    def test_selected_axes_not_padding(self):
        self.assertEqual(c.project_x6([1,2,3,4,5,6],[5,0,3]),(6,1,4))
        for a in ([0,0,1],[1,2],[0,2,6]):
            with self.assertRaises(ValueError):c.project_x6([1]*6,a)
        with self.assertRaises(ValueError):c.project_x6([1,2,3])

    def test_x6_demo(self):
        self.assertEqual(len(self.x6['records']),729)
        self.assertEqual(len(c.collision_groups(self.x6)),135)
        self.assertEqual(len(c.neighborhood(self.x6,'x364',1)),13)

    def test_trajectory_sparse_labels(self):
        data={'schema':c.SCHEMA,'kind':'hex','records':[{'id':'twelve','n':12,'coord':[0,0]},{'id':'three','n':3,'coord':[1,0]},{'id':'fortyeight','n':48,'coord':[2,0]}]}
        self.assertEqual(c.trajectory(data,3,4),['three','twelve','fortyeight'])

    def test_trajectory_cycles(self):
        self.assertEqual(c.trajectory(self.small,0,4),['0'])
        self.assertEqual(c.trajectory(self.small,3,1),['3'])
        self.assertEqual(c.trajectory(self.small,10000,4),[])

    def test_trajectory_ambiguity(self):
        d=copy.deepcopy(self.small);d['records'][0]['n']=1
        with self.assertRaises(ValueError):c.trajectory(d,1,4)

    def test_neighborhood(self):
        ids=c.neighborhood(self.full,'12345',2)
        self.assertIn('12345',ids);self.assertLessEqual(len(ids),19)
        with self.assertRaises(ValueError):c.neighborhood(self.small,'0',-1)
        with self.assertRaises(KeyError):c.neighborhood(self.small,'missing')

    def test_profile_counts(self):
        for axis in [0,1,'s']:
            self.assertEqual(sum(x['count'] for x in c.profile(self.full,axis)),65536)
        for axis in range(6):
            self.assertEqual([x['count'] for x in c.profile(self.x6,axis)],[243]*3)
        with self.assertRaises(ValueError):c.profile(self.x6,'s')

    def test_q16_exhaustive(self):
        for w in (0,2730,2731,49152,65536):
            for n in range(65536):
                q,r=c.q16(n,w);self.assertEqual(q*65536+r,n*w);self.assertTrue(0<=r<65536)
        self.assertEqual(len({c.q16(n,2731)[1] for n in range(65536)}),65536)

    def test_q16_invalid(self):
        for n,w in [(-1,3),(65536,3),(1,-1),(1,65537),(True,3)]:
            with self.assertRaises(ValueError):c.q16(n,w)

    def test_json_csv_preserve_extras(self):
        data=copy.deepcopy(self.small);data['records'][0]['note']='逗号,引号"\n换行';data['records'][0]['fields']['none']=None
        data['relations']=[{'source':'0','target':'1','kind':'test','multiplicity':2}]
        with tempfile.TemporaryDirectory() as d:
            for ext in ['json','csv']:
                p=Path(d)/('data.'+ext);c.write_data(data,p);got=c.read_data(p);self.assertEqual(got,data);self.assertEqual(c.fingerprint(got),c.fingerprint(data))

    def test_reject_invalid_data(self):
        mutations=[lambda d:d.update(kind='3d'),lambda d:d.update(records=[]),lambda d:d['records'][0].update(coord=[0,1,2]),lambda d:d['records'][0].update(coord=[0.5,1]),lambda d:d['records'][0].update(coord=[True,1]),lambda d:d['records'][0].update(coord=[1000001,1]),lambda d:d['records'][0].update(n=2**53),lambda d:d['records'][0].update(id='1'),lambda d:d.update(relations=[{'source':'0','target':'no'}]),lambda d:d['records'][0].update(fields={'bad':float('nan')})]
        for mutation in mutations:
            data=copy.deepcopy(self.small);mutation(data)
            with self.assertRaises(ValueError):c.validate(data)

    def test_no_implicit_x6_upgrade(self):
        d=copy.deepcopy(self.small);d['kind']='x6'
        with self.assertRaises(ValueError):c.validate(d)

    def test_untrusted_html_strings_not_executable(self):
        d=copy.deepcopy(self.small);d['title']='</script><script>window.pwned=true</script>'
        with tempfile.TemporaryDirectory() as x:
            p=c.html(d,Path(x)/'a.html');s=p.read_text();self.assertNotIn(d['title'],s);self.assertIn('\\u003c/script>',s)
            self.assertNotIn('__PAYLOAD__',s);self.assertNotIn('__FINGERPRINT__',s)

    def test_legacy_json_table_parser(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'a.html';p.write_text('const P= [ [0,0,0,16], [1,0,0,0] ]; not JSON later')
            data=c.legacy_html(p);self.assertIsNone(data['records'][0]['fields']['v2']);self.assertEqual(data['records'][1]['coord'],[1,0])

    def test_static_zoom_extent(self):
        try:
            import matplotlib
            matplotlib.use('Agg')
            from nollm_visual_toolkit.static import plot_hex
        except ImportError:self.skipTest('optional Matplotlib not installed')
        import matplotlib.pyplot as plt
        fig,ax=plot_hex(self.full,center_id='12345',radius=2)
        self.assertLess(ax.get_xlim()[1]-ax.get_xlim()[0],10)
        self.assertLess(ax.get_ylim()[1]-ax.get_ylim()[0],10)
        plt.close(fig)

if __name__=='__main__':unittest.main(verbosity=2)
