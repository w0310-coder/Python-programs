# 以此代码演示了面向对象编程、字典列表操作、异常处理和交互式菜单系统的综合应用
class Student:
    """学生类，封装学生信息和成绩"""
    def __init__(self, student_id: int, name: str):
        self.student_id = student_id
        self.name = name
        self.scores = {}
    def add_score(self, subject: str, score: int) -> bool:
        """添加成绩"""
        if 0 <= score <= 100:
            self.scores[subject] = score
            return True
        return False
    def get_average_score(self) -> float:
        """计算平均分"""
        if not self.scores:
            return 0.0
        return sum(self.scores.values()) / len(self.scores)
    def __str__(self) -> str:
        """学生信息字符串表示"""
        avg = self.get_average_score()
        return f"学号: {self.student_id}, 姓名: {self.name}, 平均分: {avg:.2f}, 各科成绩: {self.scores}"
class ScoreManager:
    """成绩管理系统类"""
    def __init__(self):
        self.students = {}
    def add_student(self) -> None:
        """添加学生"""
        try:
            student_id = int(input("请输入学生学号: "))
            if student_id in self.students:
                print("该学号已存在！")
                return
            name = input("请输入学生姓名: ")
            self.students[student_id] = Student(student_id, name)
            print(f"学生 {name} 添加成功！")
        except ValueError:
            print("学号必须是数字！")
    def add_score_to_student(self) -> None:
        """给学生添加成绩"""
        try:
            student_id = int(input("请输入学生学号: "))
            if student_id not in self.students:
                print("该学生不存在！")
                return
            subject = input("请输入科目名称: ")
            score = int(input("请输入成绩: "))
            if self.students[student_id].add_score(subject, score):
                print("成绩添加成功！")
            else:
                print("成绩必须在0-100之间！")
        except ValueError:
            print("输入格式错误！")
    def show_all_students(self) -> None:
        """显示所有学生信息"""
        if not self.students:
            print("暂无学生信息！")
            return
        print("\n" + "="*50)
        print("所有学生信息:")
        for student in self.students.values():
            print(student)
        print("="*50)
    def search_student(self) -> None:
        """查询学生信息"""
        keyword = input("请输入学生学号或姓名: ")
        found = False
        print("\n查询结果:")
        for student in self.students.values():
            if keyword in str(student.student_id) or keyword in student.name:
                print(student)
                found = True
        if not found:
            print("未找到匹配的学生！")
    def run(self) -> None:
        """运行成绩管理系统"""
        while True:
            print("\n===== 学生成绩管理系统 =====")
            print("1. 添加学生")
            print("2. 添加成绩")
            print("3. 显示所有学生")
            print("4. 查询学生")
            print("0. 退出系统")
            try:
                choice = int(input("请输入您的选择: "))
                if choice == 0:
                    print("感谢使用，再见！")
                    break
                elif choice == 1:
                    self.add_student()
                elif choice == 2:
                    self.add_score_to_student()
                elif choice == 3:
                    self.show_all_students()
                elif choice == 4:
                    self.search_student()
                else:
                    print("无效的选择，请重新输入！")
            except ValueError:
                print("请输入数字！")
if __name__ == "__main__":
    manager = ScoreManager()
    manager.run()