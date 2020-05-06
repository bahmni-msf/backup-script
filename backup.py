import sys
import os

release_version = "1.0"

# Update the release version to current one.
with open("backup_cmd", 'r') as o, open('temp_backup_file', 'w') as p:
    content = o.read()
    o.seek(0)
    p.write(content.replace("release_version", release_version))

# Execute unix commands for backup for the current release
with open("temp_backup_file", 'r') as p:
    for line in p:
        if line:
            if line.startswith("#"):
                print("'\033[1;33m {}\033[0m'".format(line))
            else:
                os.system('{}'.format(line))

os.remove('temp_backup_file')
