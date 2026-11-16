# R437 full fourth-order execution, actual stdout

~~~text
R437_PF4_R23_CERTIFIED u1=1..5 pos=186745397 zero=0 neg=0 total=186745397 exact_fallback=0 cutoff=1e-15 mant=64
elapsed_seconds=14.53
R437_PF4_R23_CERTIFIED u1=6..10 pos=252167517 zero=0 neg=0 total=252167517 exact_fallback=0 cutoff=1e-15 mant=64
elapsed_seconds=19.92
R437_PF4_R23_CERTIFIED u1=11..15 pos=301527687 zero=0 neg=0 total=301527687 exact_fallback=0 cutoff=1e-15 mant=64
elapsed_seconds=23.29
R437_PF4_R23_CERTIFIED u1=16..21 pos=399634500 zero=0 neg=0 total=399634500 exact_fallback=0 cutoff=1e-15 mant=64
elapsed_seconds=31.10
R437_EXACT_PASS lower {1: {'positive': 22, 'zero': 0, 'negative': 0}, 2: {'positive': 8393, 'zero': 0, 'negative': 0}, 3: {'positive': 3101868, 'zero': 0, 'negative': 0}} spot4 30880 negative_E23 -114029467521030273094612955135626559374030500000000
~~~

Note: the initial unsharded command was terminated by execution timeout without output. It was not counted as verified. These four subsequent disjoint runs successfully produced all requested records. The last line is from the separately executed local full Python verifier. The code and exact-source evidence package is also retained as a local ZIP in the conversation.