#!/usr/bin/env python3
import script_preprocessor

text = """In a small, remote village surrounded by dense forests, lived a young girl named Elara. Elara was unlike any other child in the village, for she possessed an insatiable curiosity and a deep love for exploration. Her favorite place in the world was her grandfather's study, a room filled with dusty books, old maps, and an antique globe.

Elara's grandfather, affectionately known as Old Geppetto, was a retired cartographer who had spent his youth traveling the world and mapping the most remote and enigmatic places. He was renowned for his expertise and the intricate, hand-drawn maps he created.

Elara spent countless hours in her grandfather's study, listening to his stories and studying the mesmerizing maps that adorned the walls. One day, she noticed an old, tattered atlas on a dusty shelf. It was unlike any other book in the room, its pages made of delicate parchment and covered in peculiar symbols and illustrations.

Old Geppetto noticed her fascination with the atlas and decided it was time to reveal its secret. He explained that it was called "The Enchanted Atlas" and had been passed down through their family for generations. This atlas, he said, held the power to reveal hidden places and forgotten treasures to those who could decipher its mysteries.

Elara was entranced. She begged her grandfather to teach her the secrets of the atlas, and Old Geppetto agreed to be her guide on this extraordinary journey. He explained that each symbol in the atlas corresponded to a real-world location or a unique place, but only the most determined and imaginative explorers could unlock its full potential.

Over the years, Elara and her grandfather embarked on countless adventures inspired by the Enchanted Atlas. They ventured into dark forests, climbed treacherous mountains, and crossed vast deserts. They sought the lost city of Atlantis, the Fountain of Eternal Youth, and the legendary library of Alexandria.

Their journeys were not without challenges. They faced perilous encounters with wild creatures, navigated treacherous terrain, and solved intricate puzzles to decipher the symbols within the atlas. Along the way, Elara's grandfather passed down his knowledge of cartography and the art of navigation.

As the years went by, Elara and her grandfather's bond grew stronger, as did their determination to unlock the secrets of the Enchanted Atlas. The atlas revealed to them hidden waterfalls, ancient ruins, and breathtaking landscapes that few had ever seen. Each discovery deepened their appreciation for the wonders of the world and the power of imagination.

One particularly cold winter, Elara and her grandfather stumbled upon an entry in the atlas that read, "The Starlit Caverns of Eternal Dreams." It was said to be a place where dreams turned into reality, a realm where the boundaries of the possible and impossible blurred. They knew they had to find it.

Their journey took them to the far reaches of a frozen tundra, where the land was blanketed in a sea of white and the northern lights painted the sky with ethereal colors. They followed the cryptic clues in the atlas, overcoming freezing temperatures and fierce blizzards.

Finally, after weeks of searching, they stood before a massive ice wall adorned with strange symbols. Old Geppetto deciphered the riddles, and they discovered that by playing a hauntingly beautiful tune on a flute given to them by a kindly traveler they had met on their journey, the ice would part, revealing the entrance to the Starlit Caverns of Eternal Dreams.

Inside, they found a world beyond their wildest imagination. Crystals of every hue lined the walls, casting mesmerizing reflections across the cavern. A shimmering pool at the center of the cave held the power to make dreams come true.

Elara and her grandfather realized that they had discovered the most extraordinary place of all. Here, they played the melody of their hearts on the flute, and before their eyes, their dreams materialized. They saw themselves traveling to distant planets, unlocking the secrets of the universe, and exploring the very boundaries of reality.

Elara's grandfather's dream was to map the entire cosmos, and in the Starlit Caverns, he saw his maps expand to include far-off galaxies and unknown worlds. Elara's dream was to become an explorer like her grandfather, and in the caverns, she witnessed herself as a fearless adventurer, unveiling the world's hidden wonders.

With hearts filled with wonder, they left the caverns, their spirits uplifted, knowing that the Enchanted Atlas had led them to the most extraordinary treasure of all—the realization of their dreams.

Years passed, and Elara and her grandfather continued their journeys, forever guided by the Enchanted Atlas. They grew to appreciate the world's beauty and its endless secrets. The atlas had taught them that the most remarkable adventures were not found in far-off lands but in the boundless imagination of those who dared to dream.

As they ventured into their golden years, they remained the heart and soul of their village, inspiring the next generation with their tales of wonder and their belief that every dream, no matter how fantastical, could become a reality. Elara had learned that the greatest treasure in life was the wisdom passed down through generations and the endless magic found within the pages of the Enchanted Atlas."
"""
print(script_preprocessor.get_char_list(text))
print(script_preprocessor.createJSON(text))
while True:
    print("Hello")
