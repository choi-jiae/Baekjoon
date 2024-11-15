const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const solution = (N, M, N_nums, range_nums) => {
    const sum_result = [0];
    const answer = [];

    for (let i =0; i < N; i++){
        sum_result.push(sum_result[i]+N_nums[i]);
    }


    for (let i = 0; i < M; i++){
        answer.push(sum_result[range_nums[i][1]]-sum_result[range_nums[i][0]-1]);
    }

    console.log(answer.join('\n'));

}

let N, M = null;
let N_nums = [];
const range_nums = [];

rl.on('line', (line) => {
    if (!N && !M) {
        [N, M] = line.split(' ').map((e)=>Number(e));
    } else {
        if (N_nums.length == 0){
            N_nums = line.split(' ').map((e)=>Number(e));
        } else {
            range_nums.push(line.split(' ').map((e)=>Number(e)));

            if (range_nums.length == M){
                rl.close();
            }
        }
    }

}).on('close', () => {
    solution(N, M, N_nums, range_nums);
    process.exit();
});