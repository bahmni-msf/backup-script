import os

release_version = 'rel_1.2'
pgsql_version = '9.6'


def backup(version, pgsql_ver):
    # Update the release version to current one.
    with open("backup_cmd", 'r') as o:
        with open('temp_backup_file', 'w') as p:
            content = o.read()
            p.write(content.replace("release_version", str(version)))

    with open('temp_backup_file', 'r+') as p:
        content = p.read()
        p.seek(0)
        p.write(content.replace("pgsql_version", str(pgsql_ver)))


    #Execute unix commands for backup for the current release
    with open("temp_backup_file", 'r') as p:
        for line in p:
            if line:
                if line.startswith("#"):
                    print("'\033[1;33m {0}\033[0m'".format(line))
                else:
                    # subprocess.check_output(line, shell=False)
                    os.system('{0}'.format(line))

    os.remove('temp_backup_file')


backup(release_version, pgsql_version)