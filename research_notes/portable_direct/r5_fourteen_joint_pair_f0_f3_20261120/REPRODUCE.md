# Exact reconstruction

Frozen science: EXACT_R5_ALL_101_BUDGETS.json and stages_18.json at enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551, SHA256 of former 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b.

Use the prior frozen source make_adj.py to write window_adj.bin: for each k=214..314, h,j=0..255, byte 1 precisely when 0<=N_j(k)-N_h(k)<=tau, in that k,h,j order. Expected length 6,619,136 bytes.

Compile the two C++ sources in this directory using g++ -O3 -std=c++17. First run F0 source on window_adj.bin to output 29,646 pair rows with their signature IDs. Then run GENERAL source for each f=1,2,3 on that pair CSV; it solves one representative per price-aware signature class, emitting 1,906 rows for each f. Join class_id to pair rows. All outputs match RESULT.json and the full local delivered reproduction ZIP. For additional cross-check, reconstruct masks from doubled-left endpoints rather than the right-window adjacency; the delivered ZIP includes the independent Python verifier, 44 successful comparisons, frozen input bytes, complete logs, raw outputs and SHA-256 manifest.
