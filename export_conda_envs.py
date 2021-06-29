'''
Author: Charlie-George

This script exports conda env yml files for all conda envs 
It does the following
 1) gets names of all conda envs
 2) for each conda env create a directory
 3) exports various ymls and files detailing revisions for
 full tracability/reinstatement of each conda env. The script currently runs the following export/list commands
     e.g. for base env all yml will be put in directory called `base`
     conda env export --name base > ./base/base.yml &&
     conda env export --name base --from-history > ./base/base_history.yml &&
     conda list --name base --revisions > ./base/base_revisions.txt &&
     conda list --name basee --explicit > ./base/base_list_explicit.txt &&
     conda env export --name base --no-builds > ./base/base_nobuild.yml
recommended workflow
---------------------
# set up a git repo to track your conda envs called something like conda_envs
# have folder for each cluster e.g.
    - conda_envs/ccb/
    - conda_envs/cgat/
    - conda_envs/rescomp/
    - conda_envs/laptop/
# make new branch with `clustername_date`
# go into the folder for the machine/cluster you are on
# run script
    # for each env create a directory if it doesn't exist and write yml files out - it will overwrite them if they already exist but as this is a branch so it should be fine
# after script has run add and commit files to git
# push to github branch, open pull request and merge in with master
 '''

import subprocess
import collections
import sys
import os
import re
import pysam
from pathlib import Path


# get list of conda envs
envs = subprocess.check_output('conda env list', shell=True)

# format envs output
# print(envs)
envs_list = str(envs).split('\\n')

# collect env names
env_names = []

# iterate over envs and output yml files
# There are some exceptions to remove envs not in current conda install
for line in envs_list:
    if '#' in line:
        pass
    else:
        line_list = line.rstrip(' ').split()
        # remove those old envs
        if line_list is None:
            pass
        elif len(line_list) > 1:
            # get conda env name
            conda_env = line_list[0]
            print(conda_env)

            # todo create folder if one does not already exist

            Path(f"./{conda_env}").mkdir(parents=True, exist_ok=True)
            # create command
            command = f'''conda env export --name {conda_env} > ./{conda_env}/{conda_env}.yml &&
                          conda env export --name {conda_env} --from-history > ./{conda_env}/{conda_env}_history.yml &&
                          conda list --name {conda_env} --revisions > ./{conda_env}/{conda_env}_revisions.txt &&
                          conda list --name {conda_env} --explicit > ./{conda_env}/{conda_env}_list_explicit.txt &&
                          conda env export --name {conda_env} --no-builds > ./{conda_env}/{conda_env}_nobuild.yml'''

            print(command)
            # run command
            # check = True raise exception if non-zero exit code
            subprocess.run(command, check=True,shell=True)
