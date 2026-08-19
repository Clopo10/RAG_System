--> FAILURE CASE ANALYSIS <--
Question: What is the maximum depth the Seamoth can reach with upgrades?
AI response: The maximum depth the Seamoth can reach with upgrades is 200m below sea level, which is its crush depth.
Correct answer: 900m

Chunk settings: max size 500 & overlap 50

Analysis: The model failed because the maximum chunk size of 500 was too small to include the 900m statistic into the chunk. The chunk only contained the 200m statistic and that was what the AI used for the response.

Solution: Increase maximum chunk size

========================================================================================================================================

--> SIMILARITY SCORE EXPLANATION <--
I used a sentence transformer model (all-MiniLM-L6-v2) to convert both wiki text chunks and the user's question into mathematical vectors. These vectors exist in a multi-dimensional space, where text with similar meaning is grouped closer together.

ChromaDB measures Vector similarity by calculating the mathematical distance between the question's vector and the text chunk's vector.
That is the Distance metric. The lower the metric, the better correlated the question and the text are.

========================================================================================================================================

--> CHUNK SIZE EXPERIMENTATION <--
I increased the maximum chunk size from 500 characters to 1200 characters and the overlap from 50 to 120.
After this change the model successfully responded to the question from the FAILURE CASE EXAMPLE.

AI response:
The maximum depth the Seamoth can reach with upgrades is 900m, achieved with the MK3 Depth Module.

========================================================================================================================================

--> Hallucination example <--
I have a safeguard in the prompt:
Answer the user's question using ONLY the provided context below.
If the answer is not in the context, say "I cannot answer this based on the provided information."

Normal response:
I cannot answer this based on the provided information.

Hallucination: (no safeguard)
The Seamoth Laser Cannon is not capable of killing the Reaper Leviathan. While it can inflict significant damage, it is not enough to kill the creature. The Reaper Leviathan's massive size and durability make it resistant to most attacks, including the Seamoth Laser Cannon.

Hallucination: (temperature 1, no safeguard)
Unfortunately, the Seamoth Laser Cannon is not capable of killing a Reaper Leviathan. Despite its powerful beam, the Reaper Leviathan has a surprisingly high amount of health and can withstand significant damage from the laser cannon. In fact, even a fully-powered laser blast may not be enough to kill a Reaper Leviathan, and repeated shots are often needed to cause significant damage.

Hallucination: (temperature 1.5, no safeguard)
The Seamoth Laser Cannon can kill a Reaper Leviathan.

Hallucination: (temperature 2, no safeguard prompt)
The Seamoth Laser Cannon is a formidable attack option against Reaper Leviathans, but its effectiveness in killing them depends on various factors, including the vehicle's power levels and the leviathan's hull integrity.

According to the Subnautica Wiki, a fully charged Laser Cannon blast will deal significant damage to a Reaper Leviathan, but it may not be enough to instantly kill it.
A well-powered Seamoth, equipped with a sufficient amount of Oxygen and Energy Cells, can deliver a devastating blast that will inflict substantial damage on the Reaper Leviathan, potentially even killing it.

However, if the Reaper Leviathan is close to its maximum health or has already suffered significant damage from other attacks, the Laser Cannon blast might not be enough to finish it off. In such cases, multiple shots from the Laser Cannon may be necessary to finally defeat the creature.

Keep in mind that Reaper Leviathans can recover from some damage, and a well-placed Laser Cannon blast might only knock them off their fins or temporarily stun them.

Overall, while the Seamoth Laser Cannon is a strong tool against Reaper Leviathans, it may not always be enough to guarantee a quick kill, especially against a more aggressive or well-fed leviathan.
