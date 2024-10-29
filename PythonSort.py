li = [8,7,3,4,9,10,5,6,1,2]
li = sorted(li)
print(li)

scores = []

for i in range(10):
    score = int(input(f"{i + 1}번 학생의 점수를 입력해주세요 : "))
    scores.append(score)

scores = sorted(scores)

print(f"내림차순 정렬 결과 : {scores}")