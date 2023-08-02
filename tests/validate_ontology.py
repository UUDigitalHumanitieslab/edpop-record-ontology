#!/usr/bin/env python3
from rdflib import Graph
from pathlib import Path
import sys

ONTOLOGY_FILE = Path(__file__).parent.parent / 'edpop-record-ontology.ttl'

g = Graph()
try:
    g.parse(ONTOLOGY_FILE)
except Exception as err:
    sys.exit('Parsing failed:\n{}'.format(err))
else:
    print('Ontology is a valid Turtle file')
