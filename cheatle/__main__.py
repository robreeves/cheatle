import click

#validate uuser input
def validate_input(ctx, known, value):
    #check to make sure input is 5 chracters
    click.echo(type(known))

#would like to set a default value
@click.command()
@click.option('--known', prompt=True, type=click.UNPROCESSED, callback=validate_input,)
def cheatle(known):
    click.echo(known)

if __name__ == '__main__':
    cheatle()
