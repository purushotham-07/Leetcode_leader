import requests

def fetch_leetcode_stats(username):
    url = f"https://leetcode-stats-api.herokuapp.com/{username}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                'easy': data.get('easySolved', 0),
                'medium': data.get('mediumSolved', 0),
                'hard': data.get('hardSolved', 0),
                'total': data.get('totalSolved', 0)
            }
    except Exception as e:
        print("Error fetching LeetCode stats:", e)
    return {'easy': 0, 'medium': 0, 'hard': 0, 'total': 0}
