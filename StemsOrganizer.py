import os

LOGO = r"""
   _____ _                               _ 
  / ____| |                             (_)
 | (___ | |__   __ _ _ __ ___  _ __ ___  _ 
  \___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \| |
  ____) | | | | (_| | | | | | | | | | | | |
 |_____/|_| |_|\__,_|_| |_| |_|_| |_| |_|_|
                                           
-----------THE STEMS ORGANIZER------------                                           

"""

print(LOGO)

dir = input("Enter the path to 'Stems Directory':")
os.chdir(dir)

print("Here are the Stems")
files = [f for f in os.listdir() if not os.path.isdir(f) and f != '.DS_Store']
for file in files:
    print(file)

stemDirs = ['Voxes', 'Guitars', 'Synths and Keys', 'Orchestral', 'Basses', 'Drums and Percs', 'Samples and Fx']
for folder in stemDirs:
    try:
        os.mkdir(folder)
    except FileExistsError:
        print(f'Folder "{folder}" already exists')
        
Voxes_keywords =           ['vox', 'vocal', 'main vocal', 'dub', 'addlip', 'doubble', 'backing vocal', 'chorus', 'acapella']
Guitars_keywords =         ['gtr','guitar']
Synths_and_Keys_keywords = ['massive', 'synth', 'key', 'piano', 'pad', 'organ', 'lead', 'kontakt', 'mallets', 'snth']
Orchestral_keywords =      ['violin', 'viola', 'cello', 'double bass', 'harp', 'flute', 'piccolo', 'oboe', 
                            'english horn', 'clarinet', 'bass clarinet', 'bassoon', 'contrabassoon', 'saxophone', 
                            'trumpet', 'horn', 'trombone', 'bass trombone', 'tuba', 'flute', 'piccolo', 'clarinet',
                            'oboe', 'bassoon', 'saxophone', 'french horn', 'trumpet', 'tuba']
Bass_keywords =            ['sub', 'bass', '808']
Drums_and_Percs_keywords = ['kick', 'snare', 'drum', 'hat', 'cymbal', 'clap', 'crash',
                                'tambourine', 'shaker', 'tom-tom', 'drum machine', 'congas',
                                'tabla', 'cajon', 'bongo', 'mridangam', 'mandoolin', 
                                'timbales', 'dholak', 'percs']
Samples_and_Fx_keywords =  ['riser', 'sample', 'fx', 'noise', 'scratch', 'ambience']

for file in files:
    matched_folders = []
    if any(keyword in file.lower() for keyword in Voxes_keywords):
        #os.replace(os.path.join(dir,file), os.path.join(dir, 'Voxes', file))
        matched_folders.append('Voxes')
    if any(keyword in file.lower() for keyword in Guitars_keywords):
        #os.replace(os.path.join(dir,file), os.path.join(dir, 'Guitars', file))
        matched_folders.append('Guitars')
    if any(keyword in file.lower() for keyword in Synths_and_Keys_keywords):
        #os.replace(os.path.join(dir,file), os.path.join(dir, 'Synths and Keys', file))
        matched_folders.append('Synths and Keys')
    if any(keyword in file.lower() for keyword in Orchestral_keywords):
        #os.replace(os.path.join(dir,file), os.path.join(dir, 'Orchestral', file))
        matched_folders.append('Orchestral')
    if any(keyword in file.lower() for keyword in Bass_keywords):
        #os.replace(os.path.join(dir,file), os.path.join(dir, 'Basses', file))
        matched_folders.append('Basses')
    if any(keyword in file.lower() for keyword in Drums_and_Percs_keywords):
        #os.replace(os.path.join(dir,file), os.path.join(dir, 'Drums and Percs', file))
        matched_folders.append('Drums and Percs')
    if any(keyword in file.lower() for keyword in Samples_and_Fx_keywords):
        #os.replace(os.path.join(dir,file), os.path.join(dir, 'Samples and Fx', file))
        matched_folders.append('Samples and Fx')
    
    if len(matched_folders)>1:
        print(f"file {file} matches in the following Folders {matched_folders}")
        try:
            user_choice = int(input(f"Where should the '{file}' go? choose the respective numbers (eg: for first folder press 1 and enter):"))

            if 1 <= user_choice <= len(matched_folders):
                choosen_folder = matched_folders[user_choice - 1]
                os.replace(os.path.join(dir, file), os.path.join(dir, choosen_folder, file))
                print(f"Moved '{file}' to {matched_folders[user_choice - 1]}")
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    if len(matched_folders)==1:
        os.replace(os.path.join(dir,file), os.path.join(dir, matched_folders[0], file))
        print(f"Moved '{file}' to {matched_folders[0]}")

print("All files moved successfully")
print("Creating info.txt file")

intoFile = os.path.join(dir, 'info.txt')
songName = input("Enter the Project Name here: ")
bpm      = input("Enter the Prjoect Tempo here: ")
scale    = input("Enter the Project Scale here: ")
notes    = "The Project stems are in respective folders"
remarks  = input("Enter if you want to mention any remarks (press enter if you dont have any remarks): ")
with open('info.txt', "w") as txtFile:
    txtFile.write(f"Project Name: {songName}\n")
    txtFile.write(f"Project BPM: {bpm}\n")
    txtFile.write(f"Project Scale: {scale}\n")
    txtFile.write(f"Notes and Remarks: {notes}. {remarks}\n")

print("info.txt file is created")
print("All set...All the best")
