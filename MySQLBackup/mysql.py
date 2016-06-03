#!/usr/bin/env python

import os
import time
import commands
import sys
import yaml

CONF_PATH = os.path.dirname(os.path.abspath(__file__)) + '/mysql.conf.yaml'
with open(CONF_PATH, 'r') as stream:
    try:
        configs = yaml.load(stream)
    except yaml.YAMLError as exc:
        sys.exit()

MYSQL_HOST      = configs['MYSQL_HOST']
MYSQL_PORT      = configs['MYSQL_PORT']
MYSQL_USER      = configs['MYSQL_USER']
MYSQL_PASSWORD  = configs['MYSQL_PASSWORD']

MYSQLDUMP_PATH  = configs['MYSQLDUMP_PATH']
GZIP_PATH       = configs['GZIP_PATH']

BACKUP_DBS      = configs['BACKUP_DBS']
BACKUP_PATH     = configs['BACKUP_PATH']
KEEP_DAY        = configs['KEEP_DAY']

DATETIME = time.strftime('%Y%m%d-%H%M%S')

if not os.path.exists(BACKUP_PATH):
    os.makedirs(BACKUP_PATH)
    
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
    cmd = "%s -h %s -P %s -u %s -p%s %s | gzip > %s" % (MYSQLDUMP_PATH, MYSQL_HOST,  MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, db, filename)
    run_command(cmd)
        
if __name__ == "__main__":
    main()