const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});


const upHeap = (arr) => {
    let now = arr.length -1;
    let parent = Math.floor((now-1)/2);

    while ( now != 0) {
        if (arr[now] < arr[parent]){
            const [a, b] = [arr[now], arr[parent]];
            arr[now] = b;
            arr[parent] = a;
        } else {
            return arr;
        }
        
        now = parent;
        parent = Math.floor((now-1)/2);
    }
    return arr;
};

const downHeap = (arr) => {
    let now = 0;
    let child = 1;


    while (child <= arr.length) {
        if (arr[child] > arr[child+1]){
            child += 1;
        }

        if (arr[now] > arr[child]){
            const [a, b] = [arr[now], arr[child]];
            arr[now] = b;
            arr[child] = a;

            now = child;
            child = now*2+1;
        } else {
            return arr;
        }
    }
    return arr;
};

let N;
let heap = [];
const result = [];
let cnt = 0;

rl.on('line', (line) => {
    if (!N){
        N = Number(line);
    } else {
        const num = Number(line);

        if (num == 0){
            if (heap.length == 0){
                result.push(0);
            } else {
                min_num = heap.shift();
                result.push(min_num);
                if (heap.length > 0){
                    let last = heap.pop();
                    heap.unshift(last);
                    heap = downHeap(heap);
                }
                
            }
        } else {
            heap.push(Number(line));
            heap = upHeap(heap);
        }

        cnt++;
        if (cnt == N){
            rl.close();
        };

    }
}).on('close', () => {
    console.log(result.join('\n'));
    process.exit();
});