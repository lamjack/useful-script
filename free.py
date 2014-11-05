#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import re
import sys

if "darwin" != sys.platform:
    sys.stderr.write("本工具只能用於Mac OS!\n")
    sys.exit(1)

# Get process info
ps = subprocess.Popen(['ps', '-caxm', '-orss,comm'], stdout=subprocess.PIPE).communicate()[0]
vm = subprocess.Popen(['vm_stat'], stdout=subprocess.PIPE).communicate()[0]

# Iterate processes
processLines = ps.split('\n')
sep = re.compile('[\s]+')
rssTotal = 0 # kB
for row in range(1,len(processLines)):
    rowText = processLines[row].strip()
    rowElements = sep.split(rowText)
    try:
        rss = float(rowElements[0]) * 1024
    except:
        rss = 0
    rssTotal += rss

# Process vm_stat
vmLines = vm.split('\n')
sep = re.compile(':[\s]+')
vmStats = {}
for row in range(1,len(vmLines)-2):
    rowText = vmLines[row].strip()
    rowElements = sep.split(rowText)
    vmStats[(rowElements[0])] = int(rowElements[1].strip('\.')) * 4096

print 'Wired(系統核心佔用記憶體):\n%d MB' % ( vmStats["Pages wired down"]/1024/1024 )
print 'Active Memory(使用中或剛被使用過記憶體):\n%d MB' % ( vmStats["Pages active"]/1024/1024 )
print 'Inactive Memory(有效但未被使用記憶體):\n%d MB' % ( vmStats["Pages inactive"]/1024/1024 )
print 'Free Memory(可被程序分配記憶體):\n%d MB' % ( vmStats["Pages free"]/1024/1024 )
print 'Real Mem Total(實際記憶體總量):\n%.3f MB' % ( rssTotal/1024/1024 )