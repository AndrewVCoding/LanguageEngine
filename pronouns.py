# Pronoun types
personal = {'i', 'we', 'you', 'he', 'she', 'it', 'they', 'me', 'us', 'him', 'her', 'them'}
indefinite = {'anyone', 'anybody', 'anything', 'either', 'each', 'no one', 'nobody', 'nothing', 'another', 'one',
              'someone', 'somebody', 'something', 'any', 'everyone', 'everybody', 'everything', 'both', 'few', 'many',
              'several', 'most', 'all', 'none', 'some', 'neither'}
possessive = {'my', 'our', 'your', 'his', 'her', 'its', 'their', 'whose', 'mine', 'ours', 'yours', 'hers', 'others'}
reflexive = {'myself', 'ourselves', 'yourself', 'yourselves', 'himself', 'herself', 'itself', 'themselves'}
relative = {'that', 'who', 'whoever', 'whose', 'which', 'whom', 'whomever', 'what'}
demonstrative = {'this', 'these', 'that', 'those'}
# Pronoun person
first = {'i', 'we', 'me', 'us', 'my', 'our', 'mine', 'ours', 'myself', 'ourselves'}
second = {'you', 'your', 'yours', 'yourself', 'yourselves'}
third = {'he', 'she', 'it', 'they', 'him', 'her', 'them', 'his', 'her', 'its', 'their', 'whose', 'hers', 'others',
         'himself', 'herself', 'itself', 'themselves'}
# Pronoun number
singular = {'i', 'you', 'he', 'she', 'it', 'they', 'me', 'him', 'her', 'anyone', 'anybody', 'anything', 'either',
            'each', 'no one', 'nobody', 'nothing', 'another', 'one', 'someone', 'somebody', 'something', 'everyone',
            'everybody', 'everything', 'most', 'any', 'all', 'none', 'some', 'neither', 'my', 'your', 'his', 'her',
            'its', 'their', 'whose', 'mine', 'yours', 'his', 'hers'}
plural = {'we', 'y\'all', 'you', 'us', 'them', 'both', 'few', 'many', 'several', 'our', 'their', 'ours', 'ourselves',
          'yourselves', 'themselves', 'these', 'those'}
# Pronoun Objectivity
subjective = {'i', 'we', 'you', 'y\'all', 'he', 'she', 'it', 'they', 'my', 'our', 'your', 'his', 'her', 'its', 'their',
              'whose', 'that', 'who', 'whoever', 'whose', 'this', 'that', 'these', 'those'}
objective = {'me', 'us', 'you', 'y\'all', 'him', 'her', 'it', 'them', 'mine', 'ours', 'yours', 'his', 'hers', 'others',
             'myself', 'ourselves', 'yourself', 'yourselves', 'himself', 'herself', 'itself', 'themselves', 'which',
             'whom', 'whomever', 'what', 'this', 'these', 'that', 'those'}
# Pronoun gender
male = {'he', 'him', 'his', 'himself'}
female = {'she', 'her', 'hers', 'herself'}
neuter = {'it', 'they', 'them', 'us', 'i', 'we', 'me', 'anyone', 'anybody', 'anything', 'either', 'each', 'no one',
          'nobody', 'nothing', 'another', 'one', 'someone', 'somebody', 'something', 'any', 'everyone', 'everybody',
          'everything', 'both', 'few', 'many', 'several', 'most', 'all', 'none', 'some', 'neither', 'my', 'our', 'your',
          'its', 'their', 'whose', 'mine', 'ours', 'yours', 'others', 'myself', 'ourselves', 'yourself', 'yourselves',
          'itself', 'themselves', 'that', 'who', 'whoever', 'whose', 'which', 'whom', 'whomever', 'what', 'this',
          'these', 'that', 'those', 'y\'all'}
# Pronoun proximity
close = {'this', 'these'}
far = {'that', 'those'}

# Pronoun specificity
general = {'anyone', 'anybody', 'anything', 'either', 'another', 'any', 'either'}
specific = {'one', 'someone', 'somebody', 'something'}
total = {'each', 'everyone', 'everybody', 'everything'}
exclusive = {'no one', 'nobody', 'nothing'}


def pronoun(type='', person='', objectivity='', gender='', number='', proximity='', quantity=0, specificity=''):
    categories = list()
    if type == 'personal':
        categories.append(personal)
    if type == 'indefinite':
        categories.append(indefinite)
    if type == 'possessive':
        categories.append(possessive)
    if type == 'reflexive':
        categories.append(reflexive)
    if type == 'relative':
        categories.append(relative)
    if type == 'demonstrative':
        categories.append(demonstrative)

    if person == 'first':
        categories.append(first)
    if person == 'second':
        categories.append(second)
    if person == 'third':
        categories.append(third)

    if objectivity == 'subjective':
        categories.append(subjective)
    if objectivity == 'objective':
        categories.append(objective)

    if gender == 'male':
        categories.append(male)
    if gender == 'female':
        categories.append(female)
    # And everything else is neuter
    if gender == 'neuter':
        categories.append(neuter)

    if number == 'plural':
        categories.append(plural)
    if number == 'singular':
        categories.append(singular)

    if proximity == 'close':
        categories.append(close)
    if proximity == 'far':
        categories.append(far)

    if quantity == 2:
        categories.append({'both'})
    if quantity in range(3, 4):
        categories.append({'few'})
    if quantity in range(5, 10):
        categories.append({'several'})
    if quantity > 10:
        categories.append({'many'})

    if specificity == 'general':
        categories.append(general)
    if specificity == 'specific':
        categories.append(specific)
    if specificity == 'total':
        categories.append(total)
    if specificity == 'exclusive':
        categories.append(exclusive)

    pronoun = set.intersection(*categories)
    return pronoun


print(pronoun(type='personal', gender='female', person='third'))
