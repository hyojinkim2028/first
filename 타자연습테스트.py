import game 
import os


file_list= os.listdir()
print(file_list)

txt_list = []

for path in file_list:
    #if path[-3:] == "txt":
    # 또는 if path.split(".")[-1] == "txt":
    if path.endswith("txt"):
        txt_list.append(path)

while True:
    for i in range(len(txt_list)):
        file_name = txt_list[i].split(".")[0]
        print(f"{i+1}) {file_name}")
    print("4) 종료")

    sel = input("> ")
    if sel == "4":
        break

    idx = int(sel) - 1

    game.play_type_game(txt_list[idx])
    #print(txt_list[idx]) #계산된 idx 값으로 슬라이싱이 되어 그에 맞는 txt_list가 프린트됨.
    print("press enter key to continue")
    input()
    os.system("cls")



