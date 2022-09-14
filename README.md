# cheatle
A CLI to generate wordle guesses

## CLI
```bash
# maybe and not are mutually exclusive
# maybe is characters that could be in word
# not is characters that have been guessed and aren't in the word
# yellow is in format <character>=<position1><position2><...>
cheatle --known gu*s* --yellow a=12 --yellow b=23 --maybe ts
cheatle --known gu*s* --yellow a=12 --yellow b=23 --not xyz
```

Behavior:

1. Find all words that match existing pattern (greens, yellows, available letters)
2. Maximize information gain
2a. In valid words from step 1, find most common letters and most common position of letters.
2b. Using info from 2a pick a word that uses the most common letters, prefer ones where they are in most common position. May need to support multiple strategies.
3. If more than one option pick a random one or print them to the output.
