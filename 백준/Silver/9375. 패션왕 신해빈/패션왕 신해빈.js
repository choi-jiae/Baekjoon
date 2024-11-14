const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const solution = (clothes_dic, result) => {
    let cnt = 1;
    for (type in clothes_dic){
        cnt *= clothes_dic[type] +1;
    }
    result.push(cnt-1);
};

let tc = null;
let clothes_num = null;
let clothes_dic = {};
const result = [];

rl.on('line', (line) => {
    if (!tc){
        tc = Number(line);
    } else{
        if (!clothes_num){
            clothes_num = Number(line);
            
            if (clothes_num == 0) {
                result.push(0);
                tc -= 1;
                clothes_num = null;
                clothes_dic = {};

                if (tc == 0){
                    rl.close();
                }

            }
        } else {
            const [name, type] = line.split(' ');

            if (type in clothes_dic){
                clothes_dic[type] += 1;
            } else {
                clothes_dic[type] = 1;
            }

            clothes_num -= 1;

            if (clothes_num == 0){
                solution(clothes_dic, result);
                tc -= 1;
                clothes_num = null;
                clothes_dic = {};
            }

            if (tc == 0){
                rl.close();
            }
        }
        
    }
}).on('close', () => {
    console.log(result.join('\n'));
    process.exit();
});