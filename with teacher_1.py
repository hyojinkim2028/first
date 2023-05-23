import time


starting_count = 0

with open("test.txt","r") as f:

# while문 버전 (용량이 클때 좋음)

    while True:

        line = f.readline()
        if line == "":
            break

        line = line.strip()

        if line != "":  # line에 문자열이 있는 경우

            starting_count += len(line)

            while True: # "참"일동안 진행

                print("\n",line)
                start_time = time.time()
                user = input("타자입력:")
                end_time = time.time()

                if line == user: # line == user 면 멈추고 다음으로 이어 진행
                    break
                else: # 거짓일 경우 똑같은거 계속 반복함. 맞을때까지.
                    print("잘못입력했습니다.\n")


t_time = end_time-start_time
print(f"총 {t_time}초 걸렸습니다.")
taza = starting_count/t_time*60
print(f"타자는 분당{int(taza)} 입니다.")

# print(f"걸린시간:{t_time}초, 타자속도는 분당{taza} 입니다.")

# for문 버전(구현하기 좋음)

    # for line in f.readlines():
    #     line = line.strip()
    #     if line == "":
    #         continue  # if line != "": -> 이렇게 표현하면 더 간결하게 작성 가능
    #     print(line)

    #     user = input("user:")
    #     print(line == user)
                            # if line == user:
                            #     print("성공")
                            # else:
                            #     print("다시 도전!")


    # line = f.readlines()
    # print(line)

    # 사용자 = input("입력:")
    # if line == 사용자:
    #     print("True")
    # else:
    #     print("False")

