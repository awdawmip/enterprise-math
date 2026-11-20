// All optimal refinements of one fixed incumbent class, using the original 250 observations.
#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
using W=uint64_t;
array<W,4> obs[125][125];
int main(int argc,char**argv){
    ifstream data(argv[1],ios::binary);
    if(!data.read(reinterpret_cast<char*>(obs),sizeof(obs)))return 2;
    int size;
    while(cin>>size){
        vector<int> row(size);
        for(int&x:row)cin>>x;
        int all=(1<<size)-1;
        vector<int> price(all+1);
        for(int mask=1;mask<=all;++mask){
            for(int p=mask;p;p&=p-1){
                int a=row[countr_zero(unsigned(p))];
                array<W,4> forced{};
                for(int q=mask;q;q&=q-1){
                    const auto &o=obs[a][row[countr_zero(unsigned(q))]];
                    for(int j=0;j<4;++j)forced[j]|=o[j];
                }
                for(W word:forced)price[mask]+=popcount(word);
            }
        }
        const int high=100000;
        vector<vector<int>> cost(all+1,vector<int>(size+1,high)),choice=cost;
        cost[0][0]=0;
        for(int m=1;m<=all;++m){
            cost[m][1]=price[m];choice[m][1]=m;
            int first=m&-m;
            for(int r=(m-1)&m;r;r=(r-1)&m){
                if(!(r&first))continue;
                int rest=m^r,cap=popcount(unsigned(rest));
                for(int j=1;j<=cap;++j){
                    int v=price[r]+cost[rest][j];
                    if(v<cost[m][j+1]){cost[m][j+1]=v;choice[m][j+1]=r;}
                }
            }
        }
        for(int j=1;j<=size;++j){
            cout<<j<<" "<<cost[all][j];
            int rest=all;
            for(int k=j;k;k--){int r=choice[rest][k];cout<<" "<<r;rest^=r;}cout<<"\n";
        }
    }
}
