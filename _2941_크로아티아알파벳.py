# https: // www.acmicpc.net/problem/2941

s = input()
visited = [0]*len(s)

answer = 0

for i in range(len(s)):
    try:
        if visited[i]:
            continue

        # temp = s[i] + s[i+1]  # 2글자씩 확인
        temp = s[i:i+2]

        if temp == "dz" and s[i+2] == "=":  # dz=는 세글자 이므로 특수한 경우임
            answer += 1
            visited[i:i+3]
            i += 2

        if temp in ["c=", "c-", "d-", "lj", "nj", "s=", "z="]:
            answer += 1
            visited[i:i+2]
            i += 1
    except IndexError as identifier:
        pass

for i in range(len(s)):  # 목록에 없는 알파벳은 한 글자씩 센다
    if not visited[i]:
        answer += 1

print(answer)
