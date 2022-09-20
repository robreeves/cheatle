import click
import re

#validate user input for known
def validate_input(ctx, known, value):
    if re.search('^[a-zA-Z_]{5}$', value) == None:
        raise click.BadParameter("Please only use characters and '_' for known value and make sure it is 5 characters long")

    else:
        return value

#would like to set a default value of "_____"
@click.command()
@click.option('--known', prompt=True, type=click.UNPROCESSED, callback=validate_input,)
def cheatle(known):
    click.echo(known)

if __name__ == '__main__':
    cheatle()
