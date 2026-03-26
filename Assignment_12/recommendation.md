# Assignment (07/03/2026)

# Assignment Name : KNN in Real Life
# Description : Explain Netflix-like recommendations using KNN and create a  small similarity example.

## Netflix-like Recommendation 

# When we use apps like Netflix:
- It checks what movies/shows I watched
- It finds users similar to me
- Then it recommends what those similar users liked

👉 Example:
# If I watched:
- Action movies
- Thriller shows

👍Then Netflix will suggest:

👌More action + thriller content

# Small Similarity Example

| User | Action | Comedy | Romance |
| ---- | ------ | ------ | ------- |
| A    | 5      | 1      | 0       |
| B    | 4      | 1      | 1       |
| C    | 1      | 5      | 4       |
| D    | 5      | 0      | 0       |

👉 Ratings are from 0–5

# Step 1: Find Similar Users
    Let’s say we want recommendations for User A
- Compare A with B → Similar (both like Action)
- Compare A with D → Very similar
- Compare A with C → Not similar
👉 So nearest neighbors of A = B and D

# Step 2: Recommend Based on Neighbors
- User B likes a bit of Romance
- User D mostly likes Action
👉 So we can recommend:
- More Action movies
- Maybe some Romance (from B)


