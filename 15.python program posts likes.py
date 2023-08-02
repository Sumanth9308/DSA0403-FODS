from collections import defaultdict

def calculate_likes_distribution(posts_data):
    likes_distribution = defaultdict(int)

    for post in posts_data:
        likes = post.get("likes")
        if likes is not None:
            likes_distribution[likes] += 1

    return likes_distribution

posts_data = []
num_posts = int(input("Enter the number of posts: "))

for i in range(num_posts):
    title = input(f"Enter the title of post {i+1}: ")
    likes = int(input(f"Enter the number of likes for post {i+1}: "))
    posts_data.append({"title": title, "likes": likes})

likes_distribution = calculate_likes_distribution(posts_data)

print("\nLikes Distribution of Posts:")
for likes, count in likes_distribution.items():
    print(f"{likes} likes: {count} posts")
