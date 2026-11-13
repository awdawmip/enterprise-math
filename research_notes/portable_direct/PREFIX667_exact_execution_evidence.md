# PREFIX-667 — Complete 16-sector certificate evidence

The rows below are **decimal diagnostic renderings** of Fraction-exact computed bounds and should not be reinterpreted as exact rational certificates. Exact rational assertions are recomputed on all sectors by `PREFIX667_native_variance_subdivision_certificate.py` (on this research branch); the corresponding local executed script `PREFIX667_interval_certificate.py` and raw JSON are in the attached conversation tarball. Each of the 16 tests checks `L_mu>88`, `L_mupp>200`, `U_Hpp<24000`, and `U_Wpp<-8000` in Fraction arithmetic.

Verified summary: `ALL_INTERVALS_CERTIFIED 16`.

```csv
p_lo,p_hi,L_mu,L_mupp,U_Hpp,U_Wpp
0,1/1024,88.48390215690075,205.02960469768013,12115.340671569178,-12052.957619536784
1/1024,1/512,88.48638316519148,211.84849025873456,12730.391771279945,-12030.629821443557
1/512,3/1024,88.4890924944506,218.77432067193317,13366.293564199346,-11985.695066299892
3/1024,1/256,88.49203811314537,225.8014879836581,14023.413680168851,-11916.440400971916
1/256,5/1024,88.4952281417655,232.92703699358373,14702.324251797112,-11821.214054671063
5/1024,3/512,88.49867085195737,240.15039408162792,15403.783791630854,-11698.413778333977
3/512,7/1024,88.50237466820592,247.47308721490015,16128.718517271507,-11546.474735438367
7/1024,1/128,88.50634817178067,254.89846570718836,16878.20375056248,-11363.857207541256
1/128,9/1024,88.51060010666293,262.4314264623285,17653.445876137554,-11149.03433378145
9/1024,5/512,88.5151393871765,270.0781518332136,18455.765221895388,-10900.480066105067
5/512,11/1024,88.519975107057,277.8458628472279,19286.580117882913,-10616.657489904954
11/1024,3/256,88.52511654970995,285.74259036670037,20147.392299345276,-10296.007632165803
3/256,13/1024,88.53057319942647,293.7769657519149,21039.773743154154,-9936.938855302296
13/1024,7/512,88.53635475334534,301.9580317581479,21965.354963341422,-9537.816914039751
7/512,15/1024,88.54247113397061,310.29507371202527,22925.81473995512,-9096.95573441032
15/1024,1/64,88.54893250207544,318.79747046184025,23922.87121484723,-8612.608957821305
```

Independent BRC native Fraction evaluations at the same frozen pin, p endpoints/midpoint and central z:

```csv
p,z,mu,mu_pp,H_pp,W_pp,exact_assertions_pass
0,19/128,89.45535046017046,231.5048167050821,10472.97350345458,-20518.59216045346,true
1/128,19/128,89.50050879332443,301.6657226045709,15136.86705862091,-23818.961953347636,true
1/64,19/128,89.56414168310465,384.3484516086845,21140.979448836322,-26747.501861216933,true
```

Verifier: `PREFIX667_sample_crosscheck.py`; output `ALL_SAMPLES_PASS 3`. The three exact samples corroborate the code, while the finite rational Bernstein coverings and inherited edge lemmas establish the continuum rectangle.

Local material SHA-256, to resolve the uncompressed complete package: 
- Executed interval certificate: `fed169f8b2034399ed383c18dbd2146435881a757f00b88f2597926db87d121a`
- Raw 16-sector JSON: `a0290c8a2c5189d038ed80b0ad4759b40da912cb873c7f8a8e7d7d16a9be0cc6`
- Exact certificate log: `ffd865708619a907b6bb1bd6e2635cfbc63cc251fb0b24c1574038cf66f63093`
- Independent sample code: `971e6bbc2d4fa9a608dd9c9a0f9fec6e7aa5e9de5f3022226b593fe4508d50d6`
- Independent sample JSON: `a9541e1469740022327162d42d4f9d8aac47da274d0f1cb43b28f84d2a697ade`
- Full local paper: `1b1d7f23e5aceb14ebe7ddae109ab6e55303d5e24afb165330a7cc8f3b3b524b`

Frozen science: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Authorship-only evidence, not an independently reviewed formal Task Result.

## Byte-identical published-source re-execution

After initial publication, the full source retrieved from the immutable Git commit was reconstructed locally and checked to have **Git blob SHA-1 `1d74ba0df2827e27d369893ee76a585ae00751f5`**, equal to the actual GitHub `fetch_file` remote blob. This byte-identical program was then run under Python with the frozen PREFIX-666 native inputs. It produced `ALL_INTERVALS_CERTIFIED 16`; the complete output log had SHA-256 `ffd865708619a907b6bb1bd6e2635cfbc63cc251fb0b24c1574038cf66f63093`, identical to the separately executed certificate log. This closes the published-source execution correspondence without altering the scientific pin.
