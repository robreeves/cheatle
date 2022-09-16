from email.policy import default
import click

#function that takes in the known/green values
#would like to set a default value to "_____" but when I do that within the click option "Green Letters:  [_____]:" is displayed as the prompt
@click.command()
@click.option('--known', prompt = "Green Letters: ", help='Letters that are in the correct position. Use a "_" for letters that are not in the right position')
def known_word(known):
    click.echo(known)

if __name__ == '__main__':
    known_word()