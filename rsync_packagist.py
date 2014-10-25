#!/usr/bin/env python
# -*- coding: utf-8 -*-

import commands, os, sys, json, subprocess

# 当前路径
GIT = "/usr/local/bin/git"

work_path = os.path.abspath(os.getcwd())


def run_file(file_path):
    configs = json.load(open(file_path))
    for proj, config in configs.items():
        if not os.path.exists(proj):
            os.mkdir(proj)
        git_handle(proj, config)
    print "同步Packagist完成"


def git_handle(proj, config):
    os.chdir(work_path + "/" + proj)
    source = config['source']
    target = config['target']
    cp = subprocess.Popen(GIT + " log", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, error) = cp.communicate()
    if len(error) > 0:
        if error.find("Not a git repository"):
            clone_cmd = GIT + " clone --mirror " + source + " ."
            push_cmd = GIT + " remote add wilead " + target + " && " + GIT + " push wilead --mirror"
            print commands.getoutput(clone_cmd)
            print commands.getoutput(push_cmd)
        else:
            sys.stderr.write("项目" + proj + "操作失败!\n");
    else:
        pull_cmd = GIT + " remote update"
        push_cmd = GIT + " push wilead --mirror"
        print commands.getoutput(pull_cmd)
        print commands.getoutput(push_cmd)
    os.chdir(work_path)


def main():
    config_file_name = "packagist.json"
    if os.path.exists(config_file_name):
        run_file(config_file_name)
    else:
        sys.stderr.write("无配置文件!\n");
        sys.exit()


main();