import nltk
import random
from nltk.corpus import wordnet as wn

# [[subject, number, [adjectives]], [verb, tense, adverb], [noun, tense, adjective, number, proper], [punctuation]]

# Parts of speech
nouns = [synset for synset in list(wn.all_synsets(wn.NOUN))]
numbers = ['singular', 'plural']
adjectives = []
persons = ['first', 'second', 'third']
tenses = []

# Sentence Structures
sentenceTypes = ['simple', 'compound', 'complex', 'compound/complex']
clauseTypes = ['independent', 'dependent']
purposes = ['Declarative', 'Interrogative', 'Imperative', 'Exclamatory']
sentenceParts = ['subject', 'predicate', 'direct object', 'indirect object', 'subject compliment']

example = []


# Generate a concept to turn into a sentence
def imagine():
    concept = []
    type = random.choice(sentenceTypes)
    if type == 'simple':
        subject = genSubject()
        predicate = genPredicate(subject)


# Generate a clause



# Generate a subject
def genSubject():
    subject = [random.choice(nouns), '', '']
    subject[1] = random.choice(persons)
    subject[2] = random.choice(numbers)
    subject[3] = random.choice(['', random.choice(adjectives)])

    return subject


# Generate a predicate
def genPredicate(subject):
    predicate = [subject, '', '', '']
    predicate[1] = subject[1]
    predicate[2] = subject[2]
    predicate[3] = random.choice(tenses)

    return predicate


# build a sentence from a collection of clauses
def generate(clauses):
    sentence = ''
