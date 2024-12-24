studentgrads = {"Alice", 85 , "Bob", 92, "charile", 76}
print(f"Int Dic: {studentgrads}")

studentgrads("David") = 88
print(f"New dic {studentgrads}")

studentgrads("Alice") = 90
print(f"New dic {studentgrads}")

del studentgrads("David")
print("Final Dic", studentgrads)