import click

#validate user input for known
def validate_input(ctx, known, value):
    #check to make sure input is 5 chracters
    if len(value) != 5:
        click.echo(value)
        raise click.BadParameter("Must be atleast 5 characters")

    return value

#would like to set a default value
@click.command()
@click.option('--known', prompt=True, type=click.UNPROCESSED, callback=validate_input,)
def cheatle(known):
    click.echo(known)

if __name__ == '__main__':
    cheatle()
