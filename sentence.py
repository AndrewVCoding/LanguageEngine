import dictionary
import nltk
import random
from nltk.corpus import wordnet as wn

# [[subject, number, [adjectives]], [verb, tense, adverb], [noun, tense, adjective, number, proper], [punctuation]]

# Parts of speech
nouns = [synset for synset in list(wn.all_synsets(wn.NOUN))]
numbers = ['SG', 'PL']
genders = ['neuter', 'male', 'female']
adjectives = []
persons = ['first', 'second', 'third']
tenses = ['past', 'present', 'future']

# Sentence Structures
sentenceTypes = ['simple', 'compound', 'complex', 'compound/complex']
clauseTypes = ['independent', 'dependent']
purposes = ['declarative', 'interrogative', 'imperative', 'ixclamatory']
sentenceParts = ['subject', 'predicate', 'direct object', 'indirect object', 'subject compliment']

# Modifiers
adverbModifiers = ['adverb', 'superlative', 'comparative', 'basic']
subjectModifiers = ['adjective', 'verb', 'directed verb']

# Random choices
r_num_objects = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4]


# Get an appropriate adjective
def getAdjective(dictionary=None, subject=None, degree=None):
    if subject is None and degree is None:
        return dictionary.random('a')


# Get an appropriate verb
def getVerb(dictionary=None, subject=None, degree=None):
    if subject is None and degree is None:
        return dictionary.randomverb()


# Generate a modifier for a subject
def genModifier(dictionary=None, subject=None, modifier=None):
    mod = None

    if modifier is None:
        modifier = random.choice(subjectModifiers)

    # If the modifier is an adjective, pick an adjective to modify the subject with
    if modifier is 'adjective':
        mod = getAdjective()


# Generate a purpose
def genPurpose(dictionary=None, purpose=None, subject=None, tense=None, number=None, modifier=None):
    if purpose is None:
        purpose = random.choice(purposes)

    if purpose == 'declarative':
        if subject is None:
            subject = gen_object()
        if tense is None:
            tense = random.choice(tenses)
        if number is None:
            number = random.choice(numbers)
        if modifier is None:
            modifier = genModifier()

    return [purpose, subject, tense, number, modifier]


# Generate a concept to turn into a sentence
# The concept consists of up to 5 clauses
def imagine(dictionary=None):
    clauses = []
    senType = random.choice(sentenceTypes)
    purpose = genPurpose()

    # If the purpose is declarative, then pick a subject and something to say about the subject
    if purpose == 'declarative':
        subject = gen_object()

        # Pick if describing subject itself or describing an action the subject is taking


# Generate a clause
def genClause(dictionary=None, type=None, subject=None, tense=None, person=None, number=None):
    label = 'CLAUSE'
    clause = [label, None, None]
    if type == 'independent':
        label = 'IC'
        subject = gen_object()
        clause = [label, subject, gen_predicate(subject)]

    if type == 'dependent':
        label = 'DC'

    return [label, clause]


# Generate an object
def gen_object(dictionary=None, label='OBJECT GROUP', object_group=None, num_objects=None, number=None, person=None,
               gender=None, modifier=None):
    # Define a group of objects
    if object_group is None:
        object_group = [None, None, None, None, None]
        if num_objects is 0:
            return [None, None, None, None, None]
        elif num_objects is None:
            num_objects = random.choice(r_num_objects)

        # If person is first or second, then an appropriate pronoun needs to be chosen
        for x in range(0, num_objects):
            object_group[x] = dictionary.get_object(number=number, person=person, gender=gender)

    return [label, num_objects, object_group]


# Generate a predicate
def gen_predicate(dictionary=None, tense=None, verb=None, adverb=None):
    label = 'PREDICATE'
    # Pick a tense for the verb
    if tense is None:
        tense = random.choice(tenses)

    # pick a verb for the predicate
    if verb is None:
        verb = dictionary.random(pos="""'v'""")

    # Pick a modifier for the verb
    if adverb is None:
        adverb = [random.choice([None, dictionary.random(pos="""'r'""")]), None]
        if adverb[0] is not None:
            adverb[1] = random.choice(adverbModifiers)

    return [label, verb, tense, adverb]


def gen_subject_predicate_clause(dictionary=None, subject=None, predicate=None, indirect_object=None,
                                 direct_object=None):
    # Ensure there is a subject for the clause
    if subject is None:
        subject = gen_object(dictionary=dictionary, label='SUBJECT')

    # Decide whether or not there will be a direct object
    if direct_object is None:
        if random.choice([True, False]):
            direct_object = gen_object(dictionary=dictionary, label='DIRECT OBJECT')

    # Decide whether or not to have an indirect object
    if direct_object is not None:
        if indirect_object is None:
            if random.choice([True, False]):
                indirect_object = gen_object(dictionary=dictionary, label='INDIRECT OBJECT')

    # Generate the predicate
    if predicate is None:
        predicate = gen_predicate(dictionary=dictionary)

    return ['SUBJECT-PREDICATE CLAUSE', subject, predicate, indirect_object, direct_object]


# Generate a declarative sentence concept
def gen_declarative_sentence(dictionary=None, sentence_type=None, num_clauses=0):
    if dictionary is None:
        print('Can not generate a sentence concept. No dictionary provided')
        return None
    elif not dictionary.connected:
        print('Can not generate a sentence concept. Provided dictionary is not connected to a db')
        return None

    subject_predicate_clause = None

    if sentence_type is None:
        sentence_type = random.choice(sentenceTypes)
        if num_clauses is 0:
            num_clauses = random.choice([0, 1, 2, 3, 4, 5])

    if sentence_type is 'simple':
        subject_predicate_clause = gen_subject_predicate_clause(dictionary=dictionary)

    return [subject_predicate_clause]


# generate a sentence
def gen_sentence(dictionary=None, purpose=None, sentence_type=None, num_clauses=None):
    if dictionary is None:
        print('Can not generate a sentence. No dictionary provided')
        return None
    elif not dictionary.connected():
        print('Can not generate a sentence. Dictionary Connection: ', dictionary.connected())
        return None

    sentence = None
    if purpose is None:
        purpose = random.choice(purposes)
    if sentence_type is None:
        sentence_type = random.choice(sentenceTypes)
    if num_clauses is None:
        num_clauses = random.choice([1, 2, 3, 4, 5])

    if purpose is 'declarative':
        sentence = gen_declarative_sentence(dictionary=dictionary, sentence_type=sentence_type, num_clauses=num_clauses)

    return [purpose, sentence_type, num_clauses, sentence]
