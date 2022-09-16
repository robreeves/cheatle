from curses.ascii import isalpha
from email.policy import default
import click

#function that takes in the known/green values
#would like to set a default value to "_____" but when I do that within the click option "Green Letters:  [_____]:" is displayed as the prompt
@click.command()
@click.option('--known', prompt = "Green Letters", help='Letters that are in the correct position. Use a "_" for letters that are not in the right position')
def known_word(known):
    #check to make sure user only used letters and "_" for known
    for i in known:
        if i != "_" and isalpha(i) != True:
            click.echo(click.ClickException('Please use letters and "_" for unknown letters'))
            break

    #check to make sure know is 5 chracters
    if len(known) != 5:
        click.echo(click.ClickException('Please provide atleast 5 characters'))

    else:
        click.echo(known)

if __name__ == '__main__':
    known_word()