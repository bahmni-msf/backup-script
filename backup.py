import os
import sys

release_version = 'rel_1.2'
pgsql_version = '9.6'


def backup(version, pgsql_ver):
    # Update the release version to current one.
    with open("backup_cmd", 'r') as o:
        with open('temp_backup_file', 'w') as p:
            content = o.read()
            p.write(content.replace("release_version", str(version)))

    # Not using with as there is some compatibility issue with 2.6 to replace the pgsql version
    read_file = open("temp_backup_file", "r")
    new_file_content = ""
    for line in read_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace("pgsql_version", pgsql_ver)
        new_file_content += new_line + "\n"
    read_file.close()

    writing_file = open("temp_backup_file", "w")
    writing_file.seek(0)
    writing_file.write(new_file_content)
    writing_file.close()

    # Execute unix commands for backup for the current release
    with open("temp_backup_file", 'r') as p:
        for line in p:
            if line:
                if line.startswith("#"):
                    print("'\033[1;33m {0}\033[0m'".format(line))
                else:
                    # subprocess.check_output(line, shell=False)
                    os.system('{0}'.format(line))

    os.remove('temp_backup_file')
    exit('Backup phase Completed')


backup(release_version, pgsql_version)
