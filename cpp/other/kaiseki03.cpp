#include<iostream>
#include<cmath>
#include<vector>
#include<numeric>
using namespace std;

const int datasize = 10;
const int qsize = 5;

int main(){
    vector<double> d1{31.15,31.10,31.10,31.20,31.25,31.15,31.20,31.15,31.10,31.15};
    vector<double> d2{25.75,25.70,25.75,25.80,25.85,25.80,25.75,25.70,25.75,25.75};
    vector<double> d3(datasize), d4(datasize), d5(datasize);
    vector<double> ave(qsize,0.0), s(qsize,0.0), e(qsize,0.0), ans(qsize,0.0);

    for(int i=0;i<datasize;i++){
        d3.at(i) = d1.at(i) - d2.at(i);
        d4.at(i) = d1.at(i) * 2 + d2.at(i) * 2;
        d5.at(i) = d1.at(i) * d2.at(i);
    }

    ave.at(0) = accumulate(d1.begin(),d1.end(),0.0) / datasize;
    ave.at(1) = accumulate(d2.begin(),d2.end(),0.0) / datasize;
    ave.at(2) = accumulate(d3.begin(),d3.end(),0.0) / datasize;
    ave.at(3) = accumulate(d4.begin(),d4.end(),0.0) / datasize;
    ave.at(4) = accumulate(d5.begin(),d5.end(),0.0) / datasize;

    for(int i=0;i<datasize;i++){
        s.at(0) += pow(d1.at(i) - ave.at(0), 2.0);
        s.at(1) += pow(d2.at(i) - ave.at(1), 2.0);
        s.at(2) += pow(d3.at(i) - ave.at(2), 2.0);
        s.at(3) += pow(d4.at(i) - ave.at(3), 2.0);
        s.at(4) += pow(d5.at(i) - ave.at(4), 2.0);
    }

    for(int i=0;i<qsize;i++){
        s.at(i) = sqrt(s.at(i) / ((double)datasize - 1.0));
        e.at(i) = s.at(i) / sqrt(datasize);
        ans.at(i) = ave.at(i) + e.at(i);
    }

    for(int i=0;i<qsize;i++){
        printf("(%d) heikin:%f\n",i+1,ave.at(i));
        printf("(%d) gosa:%f\n",i+1,e.at(i));
    }
    return 0;
}