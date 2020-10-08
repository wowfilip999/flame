import os
os.system("java extesion1.java")
os.system("python3 clear.py")
while True:
  a = input(">>")
  if a == ("python3"):
    h = ("python3")
  if a == ("java"):
    f = open("extesion1.java", "w")
    f.close()
  if a == ("add java"):
    n = input("name:")
    f = open("run.py", "a")
    f.write("os.system(")
    f.write(" ' ")
    f.write("java")
    f.write(n)
    f.write(" ' ")
    f.write(")")
    f.close()
  if a == ("add python"):
    n = input("name:")
    f = open("run.py", "a")
    f.write("os.system(")
    f.write(" ' ")
    f.write("python3")
    f.write(n)
    f.write(" ' ")
    f.write(")")
    f.close()
  if a == ("exit"):
    break
