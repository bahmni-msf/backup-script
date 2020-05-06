# backup-script
This scipt will execute all the commands necessaary for taking backup during release activity.

`backup_cmd` : This file contails all the Unix commands, which will be performed during release activity

`backup.py` : This script will execute the commands present in backup_cmd file


### What is `backup.py`
- This is a script written in python where latest release version can be provided(ex release_1.0) during the release activity before triggering the script.
- This code will update the release version in a new file by considering data from `backup_cmd`(with the version given).
 
 
### What is `backup_cmd`
 - This is a normal text file, which contains the unix back up commands(used during any new release).
 - Any update to the commands like adding new one or update/delete existing one, should be mentioned in this file.
 
### Dependencies
- Program works with inbuilt python libraries.
- No external library required.
- works with python version 2.x / 3.x

### How to run
- git clone https://github.com/bahmni-msf/backup-script.git ( from any path)
- set the release_version variable to current release value in backup.py (line #4)
```
Ex. 
release_version = "release_1.0"
```
- to execute the backup commands trigger the backup.py(from the same path where it resides)
by running below commands
```python backup.py```
- Output will be displayed in console.
