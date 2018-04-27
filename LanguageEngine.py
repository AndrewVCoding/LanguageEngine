import sys
import configparser
import sentence
import MySQLdb
from dictionary import dictionary


# Write the configuration file
def write_config(f='config.ini'):
    config = configparser.ConfigParser()
    config['DICTIONARY'] = {'host': '',
                            'user': '',
                            'passwd': '',
                            'dbname': ''}
    with open(f, 'w') as configfile:
        config.write(configfile)


# Load Configuration file
def load_config(f=None):
    if f is None:
        f = 'config.ini'
    config = configparser.ConfigParser()
    config.read(f)
    return config


# Generate a list of sentences with the option of including parameters
def gen_sentence(dictionary=None, num_sentences=1, num_clauses=1):
    sentences = list()
    for x in range(1, num_sentences):
        sentences.append(sentence.gen_sentence(dictionary=dictionary, purpose='declarative', sentence_type='simple',
                                               num_clauses=num_clauses))

    return sentences


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print('Loading configuration file:', sys.argv[1])
        config = load_config(sys.argv[1])

        dict = dictionary()

        print('Initializing Dictionary Connection')
        try:
            dict.init(host=config['DICTIONARY']['host'], user=config['DICTIONARY']['user'],
                      passwd=config['DICTIONARY']['passwd'], dbname=config['DICTIONARY']['dbname'])

            sentences = gen_sentence(dictionary=dict, num_sentences=int(sys.argv[2]))
            for concept in sentences:
                print(concept)

            dict.close()

        except KeyError:
            print(
                'Configuration file is not set up properly. Please check that [DICTIONARY] contains values for host,',
                'user, passwd, and dbname')
        except MySQLdb.connections.OperationalError:
            print('Could not connect to database')
        except all:
            try:
                dict.close()
            except all:
                exit(0)

    else:
        print('Incorrect number of parameters given. Need 2, received ', (len(sys.argv) - 1))
