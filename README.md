# StemsOrganizer Script

## Description
This script is designed to sort audio stems (such as vocal, guitar, synth, orchestral, bass, drums, and samples) into respective directories based on keywords in their filenames. It also generates an info.txt file containing project details like song name, tempo (BPM), scale, and any additional remarks.

## Installation

To get started, clone the repository to your local machine:
1. open terminal in prefered location
2. Clone the github repository to your machine
   ```sh
   git clone git@github.com:swarajvee/Stems-Organizer.git
   ```

4. Navigate to the script directory:

```sh
  cd Stems-Organizer
```


## Usage

3. Run the script by executing the following command in your terminal:
```sh
python StemsOrganizer.py
```

4. You will be prompted to enter the path to the 'Stems Directory'. This is the directory where your stem files are located.

5. The script will list all the files in the directory (excluding subdirectories and system files).

6. It will then attempt to categorize the files based on predefined keywords and move them into their respective folders. If a file matches multiple categories, you will be asked to choose the correct folder.

7. Once the files are sorted, you will be prompted to enter project details:
   - Project Name (Song name)
   - Project BPM (Tempo)
   - Project Scale
   - Any Remarks you may want to add

8. An `info.txt` file will be created with the provided project details, which will be saved in the same directory.

9. Once the process is complete, the script will confirm that all files have been successfully moved and that the `info.txt` file has been created.

## Notes
- The script assumes the presence of a 'Stems Directory' where all audio files are stored.
- If a folder for a stem type already exists, it will not be recreated.
- Ensure that your files contain relevant keywords in their filenames, such as 'vox' for vocals, 'guitar' for guitars, etc.

## Example Directory Structure
```sh
Stems Directory/
  |- Voxes/
  |- Guitars/
  |- Synths and Keys/
  |- Orchestral/
  |- Basses/
  |- Drums and Percs/
  |- Samples and Fx/
  |- info.txt
```

## License
This script is provided as-is, and you are free to modify and use it according to your needs.
