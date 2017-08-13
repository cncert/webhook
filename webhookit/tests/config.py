# -*- coding: utf-8 -*-



# This means:
# When get a webhook request from `repo_name` on branch `branch_name`,
# will exec SCRIPT on servers config in the array.
WEBHOOKIT_CONFIGURE = {
    # a web hook request can trigger multiple servers.
    'repo_name/branch_name': [{
        # The webhook shell script path.
        'SCRIPT': '/home/hustcc/exec_hook_shell.sh'
    }, {
        # if exec shell on local server, keep empty.
        'HOST': '192.168.1.103',  # will exec shell on which server.
        'PORT': '22',  # ssh port, default is 22.
        'USER': 'wt',  # linux user name
        'PWD': '111111',  # user password or private key.

        # The webhook shell script path.
        'SCRIPT': '/webhookit/tests/t.py'
    }]
}
