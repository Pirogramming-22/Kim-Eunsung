#함수 이름은 변경 가능합니다.

## 학생 목록 담는 dictionary
# {
#     "name" : [mid_score, final_score, grade]
# }
students = {}

##############  학생 존재 여부 확인
def isExistStudent(studentName):
    return studentName in students

##############  menu 1
def Menu1(name, mid_score, final_score):
    #사전에 학생 정보 저장하는 코딩 
    students[name] = [mid_score, final_score, None]

##############  menu 2
def Menu2() :
    #학점 부여 하는 코딩
    for name, info in students.items():
        if info[2] == None:
            avg_score = (info[0] + info[1]) / 2
            if avg_score >= 90:
                info[2] = "A"
            elif avg_score >= 80:
                info[2] = "B"
            elif avg_score >= 70:
                info[2] = "C"
            else:
                info[2] = "D"

##############  menu 3
def Menu3() :
    #출력 코딩
    borderline = "-" * 31
    
    print()
    print(borderline)
    print("name", "mid", "final", "grade", sep="\t")
    print(borderline)
    for name, info in students.items():
        print(name, info[0], info[1], info[2], sep="\t")

##############  menu 4
def Menu4(studentName):
    #학생 정보 삭제하는 코딩
    del students[studentName]

    

#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        #학생 정보 입력받기
        inputs = input("Enter name mid-score final-score : ").split()
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        if len(inputs) != 3:
            print("Num of data is not 3!")
            continue
        name, mid_score, final_score = inputs
        if isExistStudent(name):
            print("Already exist name!")
            continue
        try:
            mid_score = int(mid_score)
            final_score = int(final_score)
            assert mid_score > 0
            assert final_score > 0
        except:
            print("Score is not positive integer!")
            continue
        #예외사항이 아닌 입력인 경우 1번 함수 호출 
        Menu1(name, mid_score, final_score)

    elif choice == "2" :
        #예외사항 처리(저장된 학생 정보의 유무)
        if not students:
            print("No student data!")
            continue
        #예외사항이 아닌 경우 2번 함수 호출
        Menu2()
        #"Grading to all students." 출력
        print("Grading to all students.")

    elif choice == "3" :
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        if not students:
            print("No student data!")
            continue
        try:
            for name, info in students.items():
                if info[2] == None:
                    raise Exception()
        except:
            print("There is a student who didn't get grade.")
            continue
        #예외사항이 아닌 경우 3번 함수 호출
        Menu3()

    elif choice == "4" :
        #예외사항 처리(저장된 학생 정보의 유무)
        if not students:
            print("No student data!")
            continue
        
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        name = input("Enter the name to delete : ")
        
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        if not isExistStudent(name):
            print("Not exist name!")
            continue
        
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
        Menu4(name)
        print(f"{name} student information is deleted.")

    elif choice == "5" :
        #프로그램 종료 메세지 출력
        print("Exit Program!")
        #반복문 종료
        break

    else :
        #"Wrong number. Choose again." 출력
        print("Wrong number. Choose again.")
        continue
        
