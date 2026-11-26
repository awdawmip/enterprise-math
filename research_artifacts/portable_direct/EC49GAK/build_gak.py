from pathlib import Path
s=Path("gaj_solver.cpp").read_text()
s=s.replace("satPrunes=0;int bin", "satPrunes=0,wordPrunes=0,wordChecks=0;int bin")
mark=" if(ids.size()==1)return mem.emplace(key,-3).first->second;"
assert s.count(mark)==1
s=s.replace(mark,'\n // Exact necessary interval Hall bound on padded binary answer words.\n if(getenv("EM_WORD") && ids.size()>1){\n   ++wordChecks;\n   long long d[16][16]={};\n   for(int i=0;i<(int)ids.size();i++){\n     int p=free[i],b=H-pc(B[i]);\n     for(int z=0;z<=min(p,b);z++){\n       int hi=(z==b?k:k-p+z);\n       d[z][hi]+=bin[p][z];\n     }\n   }\n   long long pref[17]={};\n   for(int j=0;j<=k;j++)pref[j+1]=pref[j]+bin[k][j];\n   for(int a=k;a>=0;a--)for(int b=0;b<=k;b++){\n     if(a<k)d[a][b]+=d[a+1][b];\n     if(b)d[a][b]+=d[a][b-1];\n     if(a<k&&b)d[a][b]-=d[a+1][b-1];\n     if(b>=a&&d[a][b]>pref[b+1]-pref[a]){\n       ++wordPrunes;return mem.emplace(key,-1).first->second;\n     }\n   }\n }\n'+mark)
s=s.replace('<<dense.products<<endl','<<dense.products<<","<<v.wordChecks<<","<<v.wordPrunes<<endl')
Path("gak_solver.cpp").write_text(s)
