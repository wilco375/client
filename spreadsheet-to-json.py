import json
import re
from pandas_ods_reader import read_ods

parties = {
    "cu": {
        "alias": "cu",
        "name": {
            "nl": "ChristenUnie",
            "en": "ChristenUnie (Christian Union)"
        },
        "short": {
            "nl": "CU",
            "en": "CU"
        },
        "description": {
            "nl": "",
            "en": ""
        },
        "logo": None
    },
    "dpe": {
        "alias": "dpe",
        "name": {
            "nl": "Democratisch Platform Enschede",
            "en": "Democratisch Platform Enschede (Democratic Platform Enschede)"
        },
        "short": {
            "nl": "DPE",
            "en": "DPE"
        },
        "description": {
            "nl": "",
            "en": ""
        },
        "logo": None
    },
    "pvv": {
        "alias": "pvv",
        "name": {
            "nl": "Partij voor Vrijheid",
            "en": "Partij voor Vrijheid (Party for Freedom)"
        },
        "short": {
            "nl": "PVV",
            "en": "PVV"
        },
        "description": {
            "nl": "",
            "en": ""
        },
        "logo": None
    },
    "volt": {
        "alias": "volt",
        "name": {
            "nl": "Volt",
            "en": "Volt"
        },
        "short": {
            "nl": "Volt",
            "en": "Volt"
        },
        "description": {
            "nl": "",
            "en": ""
        },
        "logo": None
    },
    "ve": {
        "alias": "ve",
        "name": {
            "nl": "Verbindend Enschede",
            "en": "Verbindend Enschede (Connecting Enschede)"
        },
        "short": {
            "nl": "VE",
            "en": "VE"
        },
        "description": {
            "nl": "",
            "en": ""
        },
        "logo": None
    },
    "bbe": {
        "alias": "bbe",
        "name": {
            "nl": "Burger Belangen Enschede",
            "en": "Burger Belangen Enschede (Citizen Interests Enschede)"
        },
        "short": {
            "nl": "BBE",
            "en": "BBE"
        },
        "description": {
            "nl": "",
            "en": ""
        },
        "logo": None
    },
    "pvda": {
        "alias": "pvda",
        "name": {
            "nl": "PvdA",
            "en": "PvdA"
        },
        "short": {
            "nl": "PvdA",
            "en": "PvdA"
        },
        "description": {
            "nl": "",
            "en": ""
        },
        "logo": None
    },
    "gl": {
        "alias": "gl",
        "name": {
            "nl": "GroenLinks",
            "en": "GroenLinks (Green Left)"
        },
        "short": {
            "nl": "GL",
            "en": "GL"
        },
        "description": {
            "nl": "",
            "en": ""
        },
        "logo": None
    },
    "d66": {
        "alias": "d66",
        "name": {
            "nl": "D66",
            "en": "D66"
        },
        "short": {
            "nl": "D66",
            "en": "D66"
        },
        "description": {
            "nl": "",
            "en": ""
        },
        "logo": None
    },
    "pvdd": {
        "alias": "pvdd",
        "name": {
            "nl": "Partij voor de Dieren",
            "en": "Partij voor de Dieren (Party for the Animals)"
        },
        "short": {
            "nl": "PvdD",
            "en": "PvdD"
        },
        "description": {
            "nl": "",
            "en": ""
        },
        "logo": None
    },
    "link": {
        "alias": "link",
        "name": {
            "nl": "LINK",
            "en": "LINK"
        },
        "short": {
            "nl": "LINK",
            "en": "LINK"
        },
        "description": {
            "nl": "",
            "en": ""
        },
        "logo": None
    },
    "sp": {
        "alias": "sp",
        "name": {
            "nl": "SP",
            "en": "SP"
        },
        "short": {
            "nl": "SP",
            "en": "SP"
        },
        "description": {
            "nl": "",
            "en": ""
        },
        "logo": None
    },
    "cda": {
        "alias": "cda",
        "name": {
            "nl": "CDA",
            "en": "CDA"
        },
        "short": {
            "nl": "CDA",
            "en": "CDA"
        },
        "description": {
            "nl": "",
            "en": ""
        },
        "logo": None
    },
    "vvd": {
        "alias": "vvd",
        "name": {
            "nl": "VVD",
            "en": "VVD"
        },
        "short": {
            "nl": "VVD",
            "en": "VVD"
        },
        "description": {
            "nl": "",
            "en": ""
        },
        "logo": None
    }
}

result = {
    "version": "1",
    "algorithm": "hybrid",
    "languages": [
        {
            "name": "Nederlands",
            "code": "nl"
        },
        {
            "name": "English",
            "code": "en"
        }
    ],
    "title": {
        "nl": "Studentenkieswijzer Gemeenteverkiezingen Enschede",
        "en": "Student Election Guide Municipal Elections Enschede"
    },
    "subtitle": {
        "nl": "Deze kieswijzer is samengesteld door P.K.v.V. Fact",
        "en": "This election guide has been compiled by P.K.v.V. Fact"
    },
    "introduction": {
        "heading": {
            "nl": "Welkom bij de studentenkieswijzer",
            "en": "Welcome to the student election guide"
        },
        "text": {
            "nl": "In deze kieswijzer kom je te weten welke gemeentepartij het beste jouw belangen vertegenwoordigt als student.",
            "en": "In this election guide you will find out which municipal party best represents your interests as a student."
        }
    },
    "parties": [],
    "theses": [
        {
            "title": {
                "nl": "Algemeen",
                "en": "General"
            },
            "statement": {
                "nl": "Studenten zouden meer inspraak moeten hebben in the politiek van Enschede",
                "en": "Students should be involved more in the politics of Enschede"
            },
            "positions": {}
        },
        {
            "title": {
                "nl": "Algemeen",
                "en": "General"
            },
            "statement": {
                "nl": "Studeren in Enschede moet binnen Nederland beter gepromoot worden",
                "en": "Studying in Enschede should be promoted more within the Netherlands"
            },
            "positions": {}
        },
        {
            "title": {
                "nl": "Algemeen",
                "en": "General"
            },
            "statement": {
                "nl": "De gemeente Enschede moet meer studenteninitiatieven ondersteunen",
                "en": "The municipality Enschede should support more student initiatives"
            },
            "positions": {}
        },
        {
            "title": {
                "nl": "Algemeen",
                "en": "General"
            },
            "statement": {
                "nl": "De gemeente Enschede moet meer samenwerken met de Universiteit Twente en het Saxion",
                "en": "The municipality Enschede should work together more with the University of Twente and the Saxion highschool"
            },
            "positions": {}
        },
        {
            "title": {
                "nl": "Carrière na studie",
                "en": "Career after study"
            },
            "statement": {
                "nl": "Enschede moet meer ruimte bieden voor carrière na het afronden van een studie",
                "en": "Enschede should offer more possibilities for a career after finishing a study"
            },
            "positions": {}
        },
        {
            "title": {
                "nl": "Internationalisatie",
                "en": "Internationalization"
            },
            "statement": {
                "nl": "Er moeten meer internationale studenten naar Enschede komen",
                "en": "More international students should come to Enschede"
            },
            "positions": {}
        },
        {
            "title": {
                "nl": "Internationalisatie",
                "en": "Internationalization"
            },
            "statement": {
                "nl": "Er moeten meer internationaal toegankelijke evenementen worden opgezet in Enschede",
                "en": "More international events should be set up in Enschede"
            },
            "positions": {}
        },
        {
            "title": {
                "nl": "Internationalisatie",
                "en": "Internationalization"
            },
            "statement": {
                "nl": "Er moet meer worden gedaan om te zorgen dat internationale studenten zich thuis voelen in Enschede",
                "en": "More should be done to make international students feel at home in Enschede"
            },
            "positions": {}
        },
        {
            "title": {
                "nl": "Internationalisatie",
                "en": "Internationalization"
            },
            "statement": {
                "nl": "De gemeente Enschede moet zorgen dat internationale studenten niet meer betalen voor een kamer dan Nederlandse studenten",
                "en": "The municipality Enschede should take care that international students do not pay more for a room than Dutch students"
            },
            "positions": {}
        },
        {
            "title": {
                "nl": "Huisvesting",
                "en": "Housing"
            },
            "statement": {
                "nl": "Er moet meer ruimte komen voor huisvesting van studenten in Enschede",
                "en": "More space must be created for student housing in Enschede"
            },
            "positions": {}
        },
        {
            "title": {
                "nl": "Huisvesting",
                "en": "Housing"
            },
            "statement": {
                "nl": "Het moet mogelijk worden om als grotere groep studenten samen een appartement of huis te huren in Enschede",
                "en": "It should be made possible to rent a house or an apartment a bigger group of students in Enschede"
            },
            "positions": {}
        },
        {
            "title": {
                "nl": "Huisvesting",
                "en": "Housing"
            },
            "statement": {
                "nl": "Het moet makkelijker worden voor particulieren om een appartement of huis te verhuren als kamers aan studenten",
                "en": "It should become easier for private individuals to rent out an apartment or house as rooms to students"
            },
            "positions": {}
        },
        {
            "title": {
                "nl": "Studentenwelzijn",
                "en": "Student wellbeing"
            },
            "statement": {
                "nl": "De gemeente Enschede moet meer aandacht besteden aan de mentale gesteldheid van studenten",
                "en": "The municipality Enschede should pay more attention to the mental wellbeing of students"
            },
            "positions": {}
        },
    ],
    "analysis": {
        "endpoint": None,
        "institution": {
            "nl": "P.K.v.V. Fact",
            "en": "P.K.v.V. Fact"
        },
        "survey": {}
    },
    "footer-links": [
        {
            "text": {
                "nl": "P.K.v.V. Fact",
                "en": "P.K.v.V. Fact"
            },
            "href": {
                "nl": "https://pkvvfact.nl",
                "en": "https://pkvvfact.nl"
            }
        }
    ]
}

df = read_ods("answers.ods", 1)
df.sort_values(by=["Partijnaam"], inplace=True)
for row_index in range(1, df.shape[0]):
    row = df.iloc[row_index]
    party_id = row[1].lower()
    parties[party_id]["description"]["nl"] = row[2]
    parties[party_id]["description"]["en"] = row[3]
    for i in range(0, len(result["theses"])):
        position = row[i * 3 + 4]
        if position is not None:
            position = {
                "Heel erg mee eens": "strongly-approve",
                "Mee eens": "approve",
                "Neutraal": "neutral",
                "Mee oneens": "reject",
                "Heel erg mee oneens": "strongly-reject"
            }[position]
        explanation_nl = row[i * 3 + 5]
        explanation_en = row[i * 3 + 6]
        if explanation_nl is None:
            explanation_nl = ""
        if explanation_en is None:
            explanation_en = ""
        result["theses"][i]["positions"][party_id] = {
            "position": position,
            "explanation": {
                "nl": explanation_nl,
                "en": explanation_en
            }
        }
    result["parties"].append(parties[party_id])

with open('public/index.html', 'r') as f:
    contents = f.read()

with open('public/index.html', 'w') as f:
    json_start = '<script type="application/json" id="oec-content">'
    json_end = '</script>'

    # Replace text between json_start and json_end with result
    contents = contents[:contents.find(json_start) + len(json_start)] + \
               json.dumps(result, indent=4) + \
               contents[contents.find(json_end):]
    f.write(contents)
