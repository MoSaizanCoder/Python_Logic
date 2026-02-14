f = open("C:/Users/91626/Desktop/VS Code/Python/100_Questions_and_Solution/file.txt","a")
f.write("\nthis is my demo file")
t = "\nHope you like it"
for i in range (0,5):
    f.write(t)
f.close()