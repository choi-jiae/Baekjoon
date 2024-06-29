function solution(n, control) {
    var answer = n;
    for (i=0; i < control.length; i++){
        const word = control[i];
        
        if (word == 'w') {
            answer += 1
        } else if (word == 's'){
            answer -= 1
        } else if (word == 'd'){
            answer += 10
        } else {
            answer -= 10
        }
    }
    return answer;
}