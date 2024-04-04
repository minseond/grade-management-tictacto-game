# 입력 함수
def input_student_info():
    student_info = []
    for i in range(5):
        print(f"학생 {i+1} 정보 입력:")
        student_id = input("학번: ")
        name = input("이름: ")
        english_score = int(input("영어 점수: "))
        c_score = int(input("C-언어 점수: "))
        python_score = int(input("파이썬 점수: "))
        student_info.append((student_id, name, english_score, c_score, python_score))
    return student_info

# 총점/평균 계산 함수
def calculate_total_average(student_info):
    for i, student in enumerate(student_info):
        total_score = sum(student[2:5])
        average_score = total_score / 3
        student_info[i] += (total_score, average_score)
    return student_info

# 학점 계산 함수
def calculate_grade(score):
    if score >= 90:
        return "A+"
    elif 80 <= score < 90:
        return "A"
    elif 70 <= score < 80:
        return "B+"
    elif 60 <= score < 70:
        return "B"
    elif 50 <= score < 60:
        return "C+"
    elif 40 <= score < 50:
        return "C"
    else:
        return "F"

# 등수 계산 함수
def calculate_rank(student_info):
    sorted_student_info = sorted(student_info, key=lambda x: x[5], reverse=True)
    for i, student in enumerate(sorted_student_info):
        sorted_student_info[i] += (i+1,)
    return sorted_student_info

# 출력 함수
def print_student_info(student_info):
    print("\n\t\t\t\t\t성적관리 프로그램")
    print("=" * 150)
    print("학번\t\t\t이름\t\t\t영어\t\tC-언어\t\t파이썬\t\t총점\t\t평균\t\t학점\t\t등수")
    print("=" * 150)
    for student in student_info:
        print(f"{student[0]}\t\t{student[1]}\t\t\t{student[2]}\t\t{student[3]}\t\t{student[4]}\t\t{student[5]}\t\t{student[6]:.2f}\t\t{calculate_grade(student[6])}\t\t{student[7]}")

# 삽입 함수
def insert_student_info(student_info, student_data):
    student_info.append(student_data)
    return student_info

# 삭제 함수
def delete_student_info(student_info, student_id):
    for student in student_info:
        if student[0] == student_id:
            student_info.remove(student)
            break
    return student_info

# 탐색 함수(학번)
def search_by_student_id(student_info, student_id):
    for student in student_info:
        if student[0] == student_id:
            return student
    return None

# 탐색 함수(이름)
def search_by_name(student_info, name):
    for student in student_info:
        if student[1] == name:
            return student
    return None

# 정렬 함수(총점)
def sort_by_total_score(student_info):
    return sorted(student_info, key=lambda x: x[5], reverse=True)

# 80점 이상 학생 수 카운트 함수
def count_students_above_80(student_info):
    count = 0
    for student in student_info:
        if student[5] >= 80:
            count += 1
    return count

# 메인 함수
def main():
    student_info = input_student_info()
    student_info = calculate_total_average(student_info)
    student_info = calculate_rank(student_info)
    print_student_info(student_info)

if __name__ == "__main__":
    main()
