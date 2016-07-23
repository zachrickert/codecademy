"""Grade book for students in a class."""


def main():
    """Grade book for students in a class."""
    lloyd = {"name": "Lloyd",
             "homework": [90.0, 97.0, 75.0, 92.0],
             "quizzes": [88.0, 40.0, 94.0],
             "tests": [75.0, 90.0]}

    alice = {"name": "Alice",
             "homework": [100.0, 92.0, 98.0, 100.0],
             "quizzes": [82.0, 83.0, 91.0],
             "tests": [89.0, 97.0]}

    tyler = {"name": "Tyler",
             "homework": [0.0, 87.0, 75.0, 22.0],
             "quizzes": [0.0, 75.0, 78.0],
             "tests": [100.0, 100.0]}

    students = [lloyd, alice, tyler]

    for student in students:
        print(student["name"])
        print("  homework: {}".format(student["homework"]))
        print("  quizzes: {}".format(student["quizzes"]))
        print("  tests: {}".format(student["tests"]))


def average(numbers):
    """Find the mean of a list of numbers."""
    total = float(sum(numbers))
    return total / float(len(numbers))


def get_average(student):
    """Find the weighted average of hw(10%), quizzes(30%) and tests(60%)."""
    hw = average(student["homework"])
    qz = average(student["quizzes"])
    ts = average(student["tests"])

    return 0.1 * hw + 0.3 * qz + 0.6 * ts


main()
