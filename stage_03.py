with open("artifact.txt","r") as f:
    text = f.read()

with open("artifact.txt", "w") as f:
    f.write( text+ "\n I have added new line ")
print(text)
print("end of stage 3!")