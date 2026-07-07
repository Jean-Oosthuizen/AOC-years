#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

void part1(){
    // init vars
    string line;
    int elf_total = 0, max_calories = 0;

    // open file
    ifstream file("input1.txt");
    if(!file){
        cout << "Input file missing for part 1\n";
        return;
    }

    while(getline(file, line)){
        // if this is the end of the elf's inventory
        if (line.empty()){
            // update max calorie value
            if(max_calories < elf_total){
                max_calories = elf_total;
            }
            elf_total = 0;
        } else{
            // continue tallying elf's inventory
            elf_total += stoi(line);
        }
    }
    cout << max_calories << "\n";
}

void part2(){
    // init variables
    string line;
    vector<int> top_three = {0, 0, 0};
    int lowest_max = 0;
    int answer = 0;
    int elf_total = 0;

    // open file
    ifstream file("input1.txt");
    if(!file){
        cout << "Input file missing for part 2\n";
        return;
    }

    while(getline(file, line)){
        // if this is the end of an elf's inventory
        if (line.empty()){
            // find the smallest calorie count in top 3
            lowest_max = top_three[0];
            for(int val : top_three){
                if (lowest_max >= val){
                    lowest_max = val;
                }
            }

            // replace the smallest calorie count
            // if new count is larger
            if(lowest_max < elf_total){
                for(int& val : top_three){
                    if(val == lowest_max){
                        val = elf_total;
                        break;
                    }
                }
            }
            elf_total = 0;
        } else{
            // continue tallying single elf's inventory
            elf_total += stoi(line);
        }
    }
    // calculate answer from top 3
    for(int val : top_three){
        answer += val;
    }
    cout << answer << "\n";
}

int main(){
    part1();
    part2();
}