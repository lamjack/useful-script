#!/usr/bin/env python

import os
import time
import commands
import sys

MYSQL_DUMP_PATH = '/usr/local/bin/mysqldump'
MYSQL_HOST      = 'localhost'
MYSQL_ROOT_USER = 'dev'
MYSQL_ROOT_PASS = 'zx123456'
MYSQL_PORT      = 3306

GZIP_PATH       = '/usr/local/bin/gzip'

BACKUP_DBS      = ['dev_groupvbs', 'dev_isbn']
BACKUP_PATH     = '/Users/jack/Backup/mysql'
KEEP_DAY        = 7

if not os.path.exists(BACKUP_PATH):
    os.makedirs(BACKUP_PATH)
    
DATETIME = time.strftime('%Y%m%d-%H%M%S')
    
def main():
    run_command("find %s -name \"*.sql.gz\" -type f -mtime +%d -exec rm {} \;" % (BACKUP_PATH, KEEP_DAY))
    for DB in BACKUP_DBS:
        do_mysql_backup(DB)
    
def run_command(command):
    result = commands.getstatusoutput(command)
    if result[0] == 0:
        return result[1]
    else:
        raise Exception("Invalid command output", command)
    
def do_mysql_backup(db):
    filename = BACKUP_PATH + '/' + db + '-' + DATETIME + '.sql.gz'
    cmd = "%s -h %s -P %s -u %s -p%s %s | gzip > %s" % (MYSQL_DUMP_PATH, MYSQL_HOST,  MYSQL_PORT, MYSQL_ROOT_USER, MYSQL_ROOT_PASS, db, filename)
    run_command(cmd)
        
if __name__ == "__main__":
    main()