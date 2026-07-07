#include <iostream>
#include <fstream>
#include <string>
using namespace std;


void part1(){
    ifstream file("input2.txt");
    string line;
    char o, m;
    int answer = 0;
    while(getline(file, line)){
        o = line[0];
        m = line[2];
        if(m == 'X'){
            // I'm rock
            answer += 1;
            if(o == 'A'){
                answer += 3;
            } else if(o == 'B'){
                answer += 0;
            } else{
                answer += 6;
            }
        } else if (m == 'Y'){
            // I'm paper
            answer += 2;
            if(o == 'A'){
                answer += 6;
            } else if(o == 'B'){
                answer += 3;
            } else{
                answer += 0;
            }
        } else if (m == 'Z'){
            // I'm scissors
            answer += 3;
            if(o == 'A'){
                answer += 0;
            } else if(o == 'B'){
                answer += 6;
            } else{
                answer += 3;
            }
        }
    }
    cout << answer << "\n";
}

void part2(){
    ifstream file("input2.txt");
    string line;
    char o, m;
    int answer = 0;
    while(getline(file, line)){
        o = line[0];
        m = line[2];
        if(m == 'X'){
            // I lose
            if(o == 'A'){
                answer += 3;
            } else if(o == 'B'){
                answer += 1;
            } else{
                answer += 2;
            }
        } else if (m == 'Y'){
            // I draw
            answer += 3;
            if(o == 'A'){
                answer += 1;
            } else if(o == 'B'){
                answer += 2;
            } else{
                answer += 3;
            }
        } else if (m == 'Z'){
            // I win
            answer += 6;
            if(o == 'A'){
                answer += 2;
            } else if(o == 'B'){
                answer += 3;
            } else{
                answer += 1;
            }
        }
    }
    cout << answer << "\n";
}


int main(){
    part1();
    part2();
}