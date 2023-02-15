import rdflib

# Load the RDF/XML data
g = rdflib.Graph()
g.parse("data.rdf", format="xml")

# Find all individuals of type Inhabitant
inhabitants = g.query('''
    PREFIX eco: <http://example.com/ontology/ecolopes#>
    SELECT ?inhabitant
    WHERE {
        ?inhabitant rdf:type eco:Inhabitant .
    }
''')

print("Inhabitants:")
for row in inhabitants:
    print(row.inhabitant)

# Find all object properties with domain of type Envelope and range of type Building
object_properties = g.query('''
    PREFIX eco: <http://example.com/ontology/ecolopes#>
    SELECT ?property
    WHERE {
        ?property rdf:type owl:ObjectProperty .
        ?property rdfs:domain eco:Envelope .
        ?property rdfs:range eco:Building .
    }
''')

print("Object properties:")
for row in object_properties:
    print(row.property)

# Find all named individuals that are of type Human
humans = g.query('''
    PREFIX eco: <http://example.com/ontology/ecolopes#>
    SELECT ?human
    WHERE {
        ?human rdf:type eco:Human .
    }
''')

print("Humans:")
for row in humans:
    print(row.human)
