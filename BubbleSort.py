li = [10,2,3,4,1,7,0]
for i in range(len(li) - 1):
    for j in range(len(li) - 1 - i):
        if li[j] > li[j+1]:
            li[j],li[j+1] = li[j+1], li[j]
# print(li)

scores = []
for i in range(10):
    score = int(input(f"{i + 1}번 학생의 점수를 입력해주세요 : "))
    scores.append(score)

for i in range(len(scores) - 1):
    for j in range(len(scores) - 1 - i):
        if scores[j] > scores[j+1]:
            scores[j],scores[j+1] = scores[j+1], scores[j]
print(f"내림차순 정렬 결과 : {scores}")
