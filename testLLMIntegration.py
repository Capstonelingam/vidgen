import script_preprocessor
import json

story = """In the enchanting city of New Orleans, the lively streets come alive with music and color. Emily, a passionate artist, wanders through the French Quarter, her sketchbook capturing the essence of the vibrant scenes around her. One day, her path crosses with Marcus, a reclusive writer, who plays his guitar on a corner. Intrigued by his melodies, Emily starts sketching him, and they strike up an unlikely friendship.

Meanwhile, across the country in the high-tech hub of Neonova, Alex, a skilled hacker, dives into the digital realm, seeking the thrill of challenges that push the boundaries. In this city of neon lights and innovation, Elena, a brilliant scientist, grapples with the moral implications of artificial intelligence. Through an online forum, Alex and Elena engage in intense debates, their virtual connection deepening.

As Emily and Marcus collaborate on an art exhibit inspired by the spirit of New Orleans, Alex and Elena's online exchanges evolve into a shared vision for a more responsible AI-driven future. Their paths unexpectedly cross when Elena is invited to speak at a conference in New Orleans, and Alex seizes the opportunity to meet in person. The chemistry between them is palpable, and their ideas flourish when brought together.

The art exhibit becomes a stunning reflection of Emily and Marcus' friendship and the soul of the city, while Alex and Elena's joint presentation at the conference sparks a fresh dialogue about ethics in technology. These four individuals, each driven by their unique passions, soon realize that their talents are complementary, sparking a collaborative project that marries art and technology to create social change.

Through twists and turns, challenges and triumphs, the four find themselves united by their shared purpose. The exhibit attracts attention not only for its beauty but also for the message it carries."""

# jsonDict = json.loads("""{

#     "Scene 1": {"Actions":["Aria discovers the ancient spellbook", "Kael joins Aria on her quest" ], "Env": "Forest" } ,

#     "Scene 2": {"Actions":["Aria and Kael encounter enchanted forest", "Kael reveals his past to Aria" ], "Env": "Enchanted Forest" } ,

#     "Scene 3": {"Actions":["Thalia creates an invention in Eldoria", "Elrik discovers Thalia's creation"  ], "Env": "City of Eldoria" } ,

#     "Scene 4": {"Actions":["Elrik and Thalia form a partnership", "Elrik's past is revealed"  ], "Env": "Underground of Eldoria" } ,

#     "Scene 5": {"Actions":["Aria, Kael, Thalia, and Elrik's paths converge", "The group faces a powerful foe"  ], "Env": "Mountain Pass" } ,

#     "Scene 6": {"Actions":["The group battles the powerful foe", "Aria unlocks the secrets of the spellbook"   ], "Env": "Battlefield" } ,

#     "Scene 7": {"Actions":["The group defeats the powerful foe", "Aria and Kael discover their shared past"   ], "Env": "Aftermath of Battle" } ,

#     "Scene 8": {"Actions":["The group faces an ancient darkness", "Their strengths are united against the darkness"    ], "Env": "Ancient Darkness" } ,

#     "Scene 9": {"Actions":["The group confronts their deepest fears", "Their strengths are put to the test"    ], "Env": "Final Battle" } ,

#     "Scene 10": {"Actions":["The group defeats the ancient darkness", "Their names are etched in history"    ], "Env": "Victory" } 
# }""")
#print(jsonDict)
charList = script_preprocessor.get_char_list(story)
jsonDict = script_preprocessor.createJSON(story)
print("### JSONDICT")
print(jsonDict)
print("### CHAR LIST")
print(charList)