import random, unittest
import r024_collapse_atlas as r

class R024Tests(unittest.TestCase):
    def test_exact_root_64bit(self):
        rng=random.Random(24001)
        for p in range(2,17):
            for _ in range(300):
                n=rng.randrange(0,1<<64); k,L,U=r.locate_basin(p,n)
                self.assertEqual(L,k**p); self.assertEqual(U,(k+1)**p); self.assertLessEqual(L,n); self.assertLess(n,U)
    def test_every_higher_anchor_1e18(self):
        for p in range(3,17):
            a=r.BoundaryAtlas.build(p,10**18)
            for k,L0 in enumerate(a.anchors):
                L=int(L0); self.assertEqual(a.locate(L)[:2],(k,L))
                if L: self.assertEqual(a.locate(L-1)[0],max(0,k-1))
    def test_fd(self):
        for p,kmax in [(2,10000),(3,5000),(4,1000),(5,200)]:
            self.assertEqual(list(r.boundaries_fd(p,kmax**p)),[k**p for k in range(kmax+1)])
    def test_cursor_and_large_jump(self):
        c=r.BasinCursor.from_n(3,100**3+1); n=c.n
        for d in [10,1000,50000,10**13,7,9]:
            n+=d; c.advance(d); self.assertEqual((c.k,c.L,c.U),r.locate_basin(3,n))
    def test_symbolic_support(self):
        for p,k,c in [(2,20,7),(3,15,19),(4,7,33)]:
            iv=r.power_basin_interval(p,k); iv=r.IntInterval(max(iv.lo,iv.hi-2000),iv.hi).translate(c)
            roots={r.locate_basin(p,n)[0] for n in range(iv.lo,iv.hi)}; s=r.collapsed_support(p,iv)
            self.assertEqual(roots,set(range(s.k_lo,s.k_hi+1)))
    def test_hazard_version_and_horizon(self):
        reg=r.FutureRegistry(); f1=reg.compile(r.FutureDescriptor((1,),((1,1,1),))); f2=reg.compile(r.FutureDescriptor((2,),((1,1,1),)))
        sig=r.hazard_signature(2,r.IntInterval(1020,1022),f1)
        self.assertTrue(r.hazard_query(sig,f1,'one_step',0)); self.assertFalse(r.hazard_query(sig,f1,'suffix',0))
        with self.assertRaises(ValueError): r.hazard_query(sig,f2,'one_step',0)
    def test_cache_corruption(self):
        c=r.BucketHotCache(10**12,[3],16); n=123456789; good=c.locate(3,n); key=(3,n//c.bucket_sizes[3]); c.entries[key]=(4,*good)
        self.assertEqual(c.locate(3,n),good); self.assertEqual(c.entries[key][0],3)
    def test_dense(self):
        for v in ['collapse_u64','root_u32','root_u32_next_u64']:
            d=r.DenseTable.build(3,5000,v)
            for n in [0,1,2,7,8,9,4999,5000]: self.assertEqual(d.locate(n),r.locate_basin(3,n))
    def test_selfcheck(self): self.assertEqual(r.self_check()['status'],'OK')

if __name__=='__main__': unittest.main(verbosity=2)
