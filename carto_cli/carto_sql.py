import click
import os.path
import yaml

from .carto.carto_user import CARTOUser
from .carto.version import version

from .commands.sql import execute_sql
from .commands.sql.running_queries import queries


@click.group(help='Performs different actions against the SQL API')
@click.option('-u','--user-name', envvar='CARTO_USER',
              help='Your CARTO.com user. It can be omitted if $CARTO_USER '+
              'is available')
@click.option('-o','--org-name', envvar='CARTO_ORG',
              help='Your organization name. It can be ommitted if $CARTO_ORG '+
              'is available')
@click.option('-a','--api-url', envvar='CARTO_API_URL',
              help='If you are not using carto.com you need to specify your ' +
              'API endpoint. It can be omitted if $CARTO_API_URL is available')
@click.option('-k','--api-key', envvar='CARTO_API_KEY',
              help='It can be omitted if $CARTO_API_KEY ' +
              'is available')
@click.help_option('-h', '--help')
@click.pass_context
def cli(ctx, user_name, org_name, api_url, api_key):
    if not ctx.obj:
      ctx.obj = {}
    ctx.obj['carto'] = CARTOUser(user_name=user_name,org_name=org_name,api_url=api_url,api_key=api_key)

cli.add_command(version)
cli.add_command(queries)
cli.add_command(execute_sql.run)
cli.add_command(execute_sql.kill)
cli.add_command(execute_sql.functions)
cli.add_command(execute_sql.schemas)



if __name__ == '__main__':
    cli(obj={})
