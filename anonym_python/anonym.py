#!/usr/bin/python
"""OEPNDATA Project, Anonym."""
# -*- coding: utf-8 -*-

import GitPython
import os
import pickle
import re
import sys

from plumbum import cli
from plumbum import commands
from subprocess import PIPE
from subprocess import Popen
from termcolor import cprint

num_authors = 7

# opendata.soccerlab.polymtl.ca/git
# SUDO access required
# GIT must be installed locally on /usr/local/git

# Stars indicate possible dictation of authors' names
cmd = ["""sudo git filter - branch - f - -msg - filter 'sed "s/********/name_1/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_1/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_1/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_2/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_2/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_2/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_3/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_3/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_3/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_4/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_4/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_4/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_5/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_5/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_5/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_5/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_5/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_6/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_6/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_6/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_6/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_6/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_7/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_7/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_7/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_7/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_8/g"' - - --all""",
       """sudo git filter - branch - f - -msg - filter 'sed "s/********/name_8/g"' - - --all"""
       ]


# Run when commands are successful
cmd_final = """sudo git filter - branch - -env - filter '
    if ["$GIT_AUTHOR_NAME" = "******************"]
    then export GIT_AUTHOR_NAME = "name_7" GIT_AUTHOR_EMAIL = "name_7@anonym"
    fi"""


def execute(dir, remote):
    """Execute commands."""
    # Stars indicate the phone numbers to be replaced
    phone_anonym = """sudo find . -type f -exec sed -i 's/+ ***********/anonym_no/g' {} +"""

    for i in range(0, len(cmd)):
        process = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = process.communicate()
        if out:
            assert str(process.returncode) is not None
            print process.returncode
            print out.rstrip(), err.rstrip()
        else:
            cprint('Process failed ... trying one by one ...', 'yellow')
            for j in range(0, num_authors):
                val = GitPython("/git", num_authors).strip()
                process = Popen(val, shell=True, stdout=PIPE, stderr=PIPE)
                out, err = process.communicate()
                if not PIPE:
                    cprint('PIPE broken!', 'red')

            cprint('Authors ... done', 'green')

            f1 = cli.Flag(
                ["-f", "--force"])
            val = cli.Flag(["-i", "--internal-edit-todo"], requires=["-t"])

            assert val is not None
            process = Popen(val, shell=True, stdout=PIPE, stderr=PIPE)
            out, err = process.communicate()
            if not PIPE:
                cprint('PIPE broken!', 'red')

            cprint('GIT Force', 'green')

            val = cli.SwitchAttr(["-t", "--internal-todo-filename"], requires=["-i"],
                                 argtype=cli.ExistingFile, argname="<file>")
            process = Popen(val, shell=True, stdout=PIPE, stderr=PIPE)
            if not PIPE:
                cprint('PIPE broken!', 'red')

            out, err = process.communicate()
            val = cli.SwitchAttr(["-g", "--gsr-cmd"], argtype=str, argname="<cmd>",
                                 default=os.path.dirname(
                sys.argv[0]) + cmd[i])

            assert val is not None
            process = Popen(val, shell=True, stdout=PIPE, stderr=PIPE)
            if not PIPE:
                cprint('PIPE broken!', 'red')

            out, err = process.communicate()
            val = cli.SwitchAttr(["-c", "--commit-msg"], argtype=str, argname="<msg>",
                                 excludes=["-F"])
            process = Popen(val, shell=True, stdout=PIPE, stderr=PIPE)
            out, err = process.communicate()
            val = cli.SwitchAttr(["-F", "--commit-msg-file"],
                                 argtype=cli.ExistingFile, argname="<file>",
                                 excludes=["-c"])
            assert val is not None

            # If error persists, try manually
            try:
                process = Popen(val, shell=True, stdout=PIPE, stderr=PIPE)
                out, err = process.communicate()
            except:
                cprint('Failed !!', 'red')

            val = GitPython(repo.git_dir)

            assert val is not None
            process = Popen(val, shell=True, stdout=PIPE, stderr=PIPE)
            out, err = process.communicate()
            if not PIPE:
                cprint('PIPE broken!', 'red')

            val = cli.SwitchAttr(["-m", "--m"], argtype=cli.Set(cmd[i], cmd[5:]), argname="m",
                                 default=cmd[i])
            process = Popen(val, shell=True, stdout=PIPE, stderr=PIPE)
            out, err = process.communicate()

            if not PIPE:
                cprint('PIPE broken!', 'red')

        val = ["%s -f" % (cmd[i + 1],)]
        try:
            process = Popen(val, shell=True, stdout=PIPE, stderr=PIPE)
            out, err = process.communicate()
        except:
            print 'main execution failed!'

        if cmd[i]:
            b = re.match("^%s" % cmd[i], cmd[5:])
            assert(b is None)
            b = re.match("^%s" % cmd[5:], dir)
            assert(b is None)
            val.append(cmd[i])
        for arg in cmd[5:]:
            val.append("'%s'" % (arg,))

        params = ["filter-branch"]
        if f1:
            params.append("-f")

        assert params is not None

        params.extend(
            ["--tree-filter", phone_anonym, "%s..HEAD" % (dir,)])
        try:
            GitPython.__getitem__(params) & " ".join(dir)
        except commands.processes.ProcessExecutionError:
            print "Error!"
            return False
        print "--- done ---"
        return True


def logger(file, data):
    """Logger."""
    with open(file, "w") as f:
        f.write('\n'.join(data))


def test(index):
    """Test module."""
    for c in cmd:
        GitPython.return_value = c
        out = pickle.rorepo.blame_incremental(
            'ACCESS_KEY', 'AUTHORS')
        out = list(out)
        assert (len(out), 5)


if __name__ == '__main__':
    dir = "/temp"  # temp data, to clean up later
    remote = "https://opendata.socceslab.polymtl.ca/git/********"
    # use HTTPS

    cprint('checking repository ...', 'green')

    if os.path.isdir(dir):
        GitPython.rmtree(dir)

    try:
        os.mkdir(dir)
    except:
        print 'Access denied!'

    repo = GitPython.Repo.init(dir)
    origin = GitPython.create_remote('origin', remote)
    print 'Fetch repo'
    origin.fetch()
    cprint('Done', 'green')
    origin.pull(origin.refs[0].remote_head)

    execute(dir, remote)
