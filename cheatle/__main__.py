import click
import re

def validate_known_input(ctx, known, value):
    if re.search('^[a-zA-Z_]{5}$', value) == None:
        raise click.BadParameter("Please only use characters and '_' for known value and make sure it is 5 characters long")
    else:
        return value

def validate_yellow_input(ctx, yellow, value):
    if re.search('[A-Za-z1-5]$', value) == None:
        raise click.BadParameter("Please use characters and number value for the place it was tried(1-5) EX:b1")
    else:
        return value

def validate_not_in_word_input(ctx, not_in_word, value):
    if re.search('[a-zA-Z]$', value) == None:
        raise click.BadParameter("Please only use letters, spaces are not necessary")
    else:
        return value

#would like to set a default value of "_____"
@click.command()
@click.option('--known', prompt=True, type=click.UNPROCESSED, callback=validate_known_input,help='Letters that are in the correct position. Use a "_" for letters that are not in the right position')
@click.option('--yellow', prompt=True, type=click.UNPROCESSED, callback=validate_yellow_input,help='Letters that are in the word but not in the correct position. Use the character and a number to represent the places tried. EX: b13')
@click.option('--not_in_word', prompt='Not in the word', type=click.UNPROCESSED, callback=validate_not_in_word_input,help='Letters that have been tried but are not in the puzzle')
def cheatle(known,yellow,not_in_word):
    click.echo(known)
    click.echo(yellow)
    click.echo(not_in_word)

if __name__ == '__main__':
    cheatle()
