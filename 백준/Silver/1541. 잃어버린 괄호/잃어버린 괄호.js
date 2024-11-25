const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});


const solution = (s) => {
    
    const plus_elements = s.split('-');
    const plus_results = [];

    for (let el of plus_elements){
        const el_nums = el.split('+').map((e) => Number(e));
        plus_results.push(el_nums.reduce((a, b) => a + b, 0)); 
        
    }

    const result = plus_results.reduce((a, b) => a - b, plus_results[0]*2);
    console.log(result);

};

let s;

rl.on('line', (line) => {
    s = line;
    rl.close();
}).on('close', () => {
    solution(s);
    process.exit();
})