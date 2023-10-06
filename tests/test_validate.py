from rdflib import Graph
from pathlib import Path

ONTOLOGY_FILE = Path(__file__).parent.parent / 'edpop-record-ontology.ttl'


def test_valid_turtle():
    g = Graph()
    g.parse(ONTOLOGY_FILE)
