li = [4,6,1,7,2,8,3,5,9,10,12,11]

length = len(li) - 1

for i in range(length):
    min_idx = i
    for j in range(i + 1, length+1):
        if li[min_idx] > li[j]:
            min_idx = j
    li[i], li[min_idx] = li[min_idx], li[i]
# print(li)

scores = []

for i in range(10):
    score = int(input(f"{i + 1}번 학생의 점수를 입력해주세요 : "))
    scores.append(score)

for i in range(length):
    min_idx = i
    for j in range(i + 1, length+1):
        if scores[min_idx] > scores[j]:
            min_idx = j
    scores[i], scores[min_idx] = scores[min_idx], scores[i]

print(f"내림차순 정렬 결과 : {scores}")