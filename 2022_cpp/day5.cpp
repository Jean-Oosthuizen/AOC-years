#include <iostream>
#include <fstream>
#include <array>
#include <string>
#include <sstream>
#include <stack>
using namespace std;

void part1(){
    // set up variables
    ifstream file("input5.txt");
    array<stack<char>, 9> stacks;
    array<string, 8> stack_start;
    
    // grab initial state
    for(int i = 0; i < 8; ++i){
        getline(file, stack_start[i]);
    }
    // convert initial state into stack data struct
    string line;
    for(int i = 7; i >= 0; --i){
        line = stack_start[i];
        for(int j = 1; j < line.size(); j += 4){
            if(line[j] != ' '){
                stacks[(j - 1 ) / 4].push(line[j]);
            }
        }
    }

    // move down to the list of instructions
    getline(file, line);
    getline(file, line);

    // extract instructions and execute them
    int amount, from, to;
    string word;
    
    while(getline(file, line)){
        // extract values from instruction
        stringstream ss(line);
        ss >> word >> amount >> word >> from >> word >> to;

        // execute instruction
        for(int i = 0; i < amount; ++i){
            stacks[to - 1].push(stacks[from - 1].top());
            stacks[from - 1].pop();
        }
    }
    // extract solution
    for(int i = 0; i < 9; i++){
        cout << stacks[i].top();
    }
    cout << "\n";
}

void part2(){
    // set up variables
    ifstream file("input5.txt");
    array<stack<char>, 9> stacks;
    array<string, 8> stack_start;
    
    // grab initial state
    for(int i = 0; i < 8; ++i){
        getline(file, stack_start[i]);
    }
    // convert initial state into stack data struct
    string line;
    for(int i = 7; i >= 0; --i){
        line = stack_start[i];
        for(int j = 1; j < line.size(); j += 4){
            if(line[j] != ' '){
                stacks[(j - 1 ) / 4].push(line[j]);
            }
        }
    }

    // move down to the list of instructions
    getline(file, line);
    getline(file, line);

    // extract instructions and execute them
    int amount, from, to;
    string word;
    stack<char> temp_stack;
    while(getline(file, line)){
        // extract values from instruction
        stringstream ss(line);
        ss >> word >> amount >> word >> from >> word >> to;

        // move batch onto crane
        for(int i = 0; i < amount; ++i){
            temp_stack.push(stacks[from - 1].top());
            stacks[from - 1].pop();
        }
        // move batch off of crane
        for(int i = 0; i < amount; ++i){
            stacks[to - 1].push(temp_stack.top());
            temp_stack.pop();
        }
    }
    // extract solution
    for(int i = 0; i < 9; i++){
        cout << stacks[i].top();
    }
    cout << "\n";
}

int main(){
    part1();
    part2();
    return 0;
}