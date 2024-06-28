def solution(priorities, location):
    process = [i for i in range(len(priorities))]
    answer = 0
    max_priority = max(priorities)
    
    while process:
        i = process.pop(0)
        
        if priorities[i] < max_priority:
            process.append(i)

        else:
            answer += 1
            if i == location:
                break
            else:
                priorities[i] = 0
                max_priority = max(priorities)

    return answer