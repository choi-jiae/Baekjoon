const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const solution = (M, N, K, idxs, space) => {
    const y_move = [-1, 1, 0, 0];
    const x_move = [0, 0, -1, 1];
    let bug_cnt = 0;

    for (let idx of idxs){
        const [key_x, key_y] = idx;

        if (space[key_y][key_x] == 1){
            const stack = [[key_x, key_y]];
            bug_cnt += 1;

            while (stack.length > 0){
                const [now_x, now_y] = stack.pop();
                space[now_y][now_x] = 0;

                let new_x, new_y;

                for (let i = 0; i < 4; i++){
                    new_x = now_x + x_move[i];
                    new_y = now_y + y_move[i];

                    if (new_x >= 0 && new_x <= M-1 && new_y >=0 && new_y <= N-1 && space[new_y][new_x] == 1){
                        stack.push([new_x, new_y]);
                    }
                } 
            }
        }
    }
    
    result.push(bug_cnt);

};

let T = null;
let M, N, K = null;
let idxs = [];
let space = [];
const result = []

rl.on('line', (line) => {
    if (!T) {
        T = Number(line);
    } else {
        if (!M){
            const els = line.split(' ').map((e) => Number(e));
            M = els[0];
            N = els[1];
            K = els[2];
            space = Array.from(Array(N), () => Array(M).fill(0));
        } else {
            const [x, y] = line.split(' ').map((e) => Number(e))
            idxs.push([x, y]);
            space[y][x] = 1;
            
            if (idxs.length == K){
                solution(M, N, K, idxs, space);
                T -= 1;
                // 새로운 test case를 위한 초기화
                idxs = [];
                space = []
                M = null;
                N = null;
                K = null;

                if (T == 0){
                    rl.close();
                }
            }

        }

    }
}).on('close', () => {
    console.log(result.join('\n'));
    process.exit();
})
