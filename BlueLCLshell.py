import BlueLCL



print("BlueLCL version 0.0.1dp. Licensed under GNU General Public License v3.0.")
while True:
    start = 1
    text = input("BlueLCL >>> ")
    if not "LOADFILE" in text:
        pass
    else:
        try:
            pathtofile = text.replace("LOADFILE ", "")
            if ".BlueLCL" in text:
                file = open(pathtofile, "r")
                text = file.read()
            else:
                print(f"ShellCodeFileOpeningError: Unable to load file '{pathtofile}'. Check if the file exists or has '.BlueLCL' extension.")
                start = 0
        except:
            print(f"ShellCodeFileOpeningError: Unable to load file '{pathtofile}'. Check if the file exists or has '.BlueLCL' extension.")
            start = 0
    if text.strip() == "" or start == 0: continue
    result, error = BlueLCL.run('<stdin>', text)
    if error:
        print(error.as_string())
    else:
        print(result)

def runonce(text):
    if text.strip() == "": pass
    result, error = BlueLCL.run('<stdin>', text)
    if error:
        print(error.as_string())
    else:
        print(result)
