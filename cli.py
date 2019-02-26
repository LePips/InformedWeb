# cli.py
from __future__ import absolute_import

import logging
import os
import re
import subprocess
import sys

import click

logger = logging.getLogger(__name__)

DEFAULT_MACHINE_NAME = os.environ.get('DO_MACHINE_NAME')

# use to allow -h for for help
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

def get_container_id(name):
    name_id = _run_command('docker-compose ps -q {}'.format(name))

    name_id = name_id.strip()

    if '\n' in name_id:
        name_id = name_id.split('\n')[-1]

    return name_id.strip()

@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option('1.0.0')
@click.pass_context
def cli(ctx):
    pass

@cli.command(context_settings=dict(
    ignore_unknown_options=True,
))
@click.argument('ARGS', nargs=-1, type=click.UNPROCESSED)
def migrate(args):
    """Migrate the Django app"""
    web_id = get_container_id('web')

    _run_command(
        'docker exec -it {} python manage.py migrate --noinput {}'.format(
            web_id, ' '.join(args)),
        interactive=True,
        unbuffered_print=True)

@cli.command(context_settings=dict(
    ignore_unknown_options=True,
))
@click.argument('ARGS', nargs=-1, type=click.UNPROCESSED)
def makemigrations(args):
    """Make migrations"""
    web_id = get_container_id('web')

    _run_command(
        'docker exec -it {} python manage.py makemigrations --noinput {}'.format(
            web_id, ' '.join(args)),
        interactive=True,
        unbuffered_print=True)

@cli.command()
def attach():
    """Attach to the running web container for debugging"""
    web_id = get_container_id('web')

    _run_command(
        'docker attach {}'.format(web_id),
        interactive=True,
        unbuffered_print=True)

@cli.command()
@click.argument('CONTAINER', default='web', type=click.STRING, nargs=1)
def bash(container):
    """Start a bash shell on CONTAINER. Default: web"""
    container_id = get_container_id(container)

    _run_command(
        'docker exec -it {} /bin/bash --login'.format(container_id),
        interactive=True)

def _run_command(cmd, interactive=False, use_docker_env=False,
                 unbuffered_print=False):
    """
    Executes a given shell command

    Args:
        cmd (str): The command to execute
        interact (bool): If True hand the controlling terminal over to the
            subprocess. Useful when user input is needed for the command
        use_docker_env (bool): Prefix the commands with the output of
            ``docker-machine env <machine name>``.

    Returns:
        str: Output of the command
    """
    logger.debug(cmd)
    env = None
    if use_docker_env:
        env = docker_env_prefix()

    if interactive:
        try:
            import pexpect
        except ImportError:
            sys.stderr.write('Missing pexpect requirement. pip install '
                             'pexpect')
            sys.exit(1)
        sys.stdout.write('Running interactive command...\n')

        cmd = cmd.split(' ')
        pexpect.spawn(cmd[0], list(cmd[1:]), env=env).interact()
    else:
        import subprocess

        try:
            p = subprocess.Popen(
                cmd.strip(),
                shell=True,
                bufsize=0,
                stdout=subprocess.PIPE,
                stderr=sys.stderr,
                env=env)

            if unbuffered_print:
                while p.poll() is None:
                    for l in p.stdout.readline():
                        click.echo(l, nl=False)
            else:
                p.wait()
                return p.stdout.read().decode("utf8")

        except subprocess.CalledProcessError:
            sys.exit(1)


if __name__ == "__main__":
    cli()
