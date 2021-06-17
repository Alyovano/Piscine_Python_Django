from path import Path

def func():
    try:
        # Path("Dossier_Uniquement_Util_Pour_Lexo").mkdir(1)
        Path.makedirs('Exercise_Directory')
    except Exception as error:
        print(error)
    Path.touch('Exercise_Directory/Exercise_File')
    pathOfFile = Path('Exercise_Directory/Exercise_File')
    pathOfFile.write_lines(['it', 'works'])
    print(pathOfFile.read_text())


if __name__ == '__main__':
    func()