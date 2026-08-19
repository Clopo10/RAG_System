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
