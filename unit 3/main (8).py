class student:

  def __init__(self,name, roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  #sort the list of student in descenaing order of CGPA
  sorted_student = sorted(student_list,
                         key=lambda student: student.cgpa,
                         reverse=True)
  return sorted_students


# Example usage:
student = [
  student("Hari", "A123", 7.8),
  student("Srikanth", "A124", 8.9),
  student("saunya", "A125", 9.9),
]

sorted_student = sort_students(sort_students)

# print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll number: {}, CGPA: {}".format(student.name,)
                                                            student.roll_number,
                                            student.cgpa))