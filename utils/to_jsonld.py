from rdflib import Graph
from pathlib import Path

ONTOLOGY_FILE = Path(__file__).parent.parent / 'edpop-record-ontology.ttl'
JSONLD_FILE = ONTOLOGY_FILE.parent / (ONTOLOGY_FILE.name.removesuffix(".ttl") + ".json")


context = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "dc": "http://purl.org/dc/elements/1.1/",
    "dcterms": "http://purl.org/dc/terms/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "edpoprec": "https://dhstatic.hum.uu.nl/edpop-records/0.1.0-SNAPSHOT/",
}


g = Graph()
g.parse(ONTOLOGY_FILE)
g.serialize(format="json-ld", destination=JSONLD_FILE, context=context)
