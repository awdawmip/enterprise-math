#include<bits/stdc++.h>
using namespace std;
int h(int q){int a=2%q;for(int d=1;d<=(q*2);d++){if(a==1||a==q-1)return d;a=(a*2)%q;}return -1;}
int main(){const int p=17,N=1<<p,M=(1<<11)-1,T=N*(p+1);vector<int> good;for(int q=3;q<=M;q+=2)if(h(q)>=p)good.push_back(q);
  vector<int> marks(M+1);int epoch=0;vector<int> seen(N);int total=0, tested=0; long long eligible_pairs=0;auto t0=chrono::steady_clock::now();
  for(int q1:good){if(1LL*q1*M<T)continue;
    int cnt=(N+q1-1)/q1; if(cnt*(p+1)>M)continue;
    vector<int> cand;for(int q2:good){if(1LL*q1*q2<T)continue;int g=gcd(q1,q2);if(1LL*q1*q2/g<N)continue; if(q2<cnt*(p+1))continue;cand.push_back(q2);}
    if(cand.empty())continue; tested++; eligible_pairs += cand.size();
    for(int r=0;r<q1 && !cand.empty();++r){vector<int> next;for(int u=r;u<N;u+=q1){next.push_back(u);for(int i=0;i<p;++i)next.push_back(u^(1<<i));}
      epoch++; bool dup=false;for(int v:next){if(seen[v]==epoch){dup=true;break;}seen[v]=epoch;}if(dup){cand.clear();break;}
      vector<int> filtered;for(int q2:cand){epoch++;bool collision=false;for(int v:next){int rr=v%q2;if(marks[rr]==epoch){collision=true;break;}marks[rr]=epoch;}if(!collision)filtered.push_back(q2);}
      cand.swap(filtered);
    }
    for(int q2:cand){cout<<"SOLUTION "<<q1<<" "<<q2<<"\n";total++;}
    if(tested%20==0)cerr<<"q1 checked="<<tested<<" q1="<<q1<<" elapsed="<<chrono::duration<double>(chrono::steady_clock::now()-t0).count()<<"\n";
  }
  if(good.size()!=958 || tested!=441 || eligible_pairs!=113884 || total!=0){cerr<<"BAD CERTIFICATE\n";return 1;}
  cerr<<"DONE good="<<good.size()<<" q1-tested="<<tested<<" eligible_pairs="<<eligible_pairs<<" solutions="<<total<<" time="<<chrono::duration<double>(chrono::steady_clock::now()-t0).count()<<"\n";
}
