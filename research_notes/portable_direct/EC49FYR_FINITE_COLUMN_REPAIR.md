# EC49FYR — finite-column guided repair: preservation of previous local result

2026-11-24. Frozen BRC16943 auxiliary Boolean observer, continuation of FYQ (ce7abff378aa77006334656fd9396bf9f8666bdf). Original local C++ source now preserved byte-for-byte at 46fce67764a5b12324d116162c3331fb1e2623f1:research_notes/portable_direct/EC49FYR_GUIDED.cpp, Git blob 8899178876a3a265319a420217f696c0f1c0c0bb, checked by actual remote readback against original mounted file. For 3 holes and 10 columns, compile g++ -O3 -std=c++17 EC49FYR_GUIDED.cpp -o guided; run ./guided 3 5 10. The guided finite search and raw labeled replay completed in the preceding round: all 50*(1+10+45+120)=8800 states, maximum 15 queries. Parent FYO lower m+5 and column extension yield Q_3(m)=m+5 for all m>=10. Finite m=7,8,9 remain open; the 9-column attempts and 4-hole log are incomplete, not negative proofs. The current FYS theorem is independent of this result. Historical researcher provenance EM-DIRECT-23537B; no new CLAIM or independent review. Source and output logs preserved after previous round's incomplete publication. The following transcript text is copied from the original files, with the original blob IDs for individual logs. The 9-column rerun completed its abstract phase, not its finite phase.

### guided.out
Original Git blob: 64932a7fa3da6877f7572700286243c82b5dc465
```text
abstract 1 4744482 886971
3,5,1,75570,18946
replay 10 pass 8800 failfresh 0 failsat 0 failbudget 0 max 15 total 129703 reused 0
```

### guided9.err
Original Git blob: 4db9232031be591288abf4a4336bdcbb5fe442c8
```text
1000000 memo 216520 seconds 3.75822
3000000 memo 577663 seconds 12.0837
4000000 memo 759687 seconds 16.3924
```

### search.err
Original Git blob: 5237fccd15cc75281e8086c937a71a844b1acbce
```text
1000000 memo 206539 seconds 4.05143
5000000 memo 971254 seconds 24.5629
```

### guided9_new.out
Original Git blob: 0e18b771b6d49239e87177720a7470d490aa0a5b
```text
abstract 1 4744482 886971
```

### guided9_new.err
Original Git blob: da30e294cdd8f070304d84dbbc6bad1232ca268e
```text
1000000 memo 216520 seconds 5.04096
3000000 memo 577663 seconds 16.1063
4000000 memo 759687 seconds 21.9523
```
