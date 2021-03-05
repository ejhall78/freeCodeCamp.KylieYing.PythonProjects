"""
Empty Compose Template to implement :D

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import os
import re
import string
import random

from graph import Graph, Vertex

def get_words_from_text(text_path):
    with open(text_path, 'r') as f: # here r stands for read
        text = f.read()

        # remove [text in brackets] using a regular expression
        text = re.sub(r'\[(.+)\]', ' ', text)

        text = ' '.join(text.split()) # this is saying take all the whitespace
        text = text.lower() # easier to compare when everything lowercase

        # we also don't want any punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split() # automatically splits where spaces occur
    return words 

def make_graph(words):
    g = Graph()

    # for each word, check if in the graph, then if not, add it
    # if there was a previous word, add an edge if it doesn't exist in the graph
    # otherwise increment weight by 1
    # set our word to previous word and iterate

    # now remember that we want to generate the probability mappings before composing
    # this is a great place to do it before we return the graph object
    previous_word = None

    for word in words:
        word_vertex = g.get_vertex(word)
        if previous_word:
            previous_word.increment_edge(word_vertex)

        previous_word = word_vertex

    g.generate_probability_mappings()

    return g


def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words)) # pick a random word to start from
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition

def main():
    words = get_words_from_text('MarkovChainTextComposer/texts/hp_sorcerer_stone.txt')

    g = make_graph(words)

    composition = compose(g, words, 100)
    return ' '.join(composition)
if __name__ == '__main__':
    print(main())