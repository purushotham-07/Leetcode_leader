import requests

def fetch_leetcode_data(username):
    query = '''
    query getUserProfile($username: String!) {
      allQuestionsCount { difficulty count }
      matchedUser(username: $username) {
        submitStatsGlobal {
          acSubmissionNum { difficulty count }
        }
        profile {
          realName
          userAvatar
        }
      }
    }
    '''
    variables = {"username": username}
    response = requests.post(
        "https://leetcode.com/graphql/",
        json={"query": query, "variables": variables}
    )

    if response.status_code == 200:
        data = response.json()['data']
        stats = data['matchedUser']['submitStatsGlobal']['acSubmissionNum']
        profile = data['matchedUser']['profile']
        return {
            'easy': stats[1]['count'],
            'medium': stats[2]['count'],
            'hard': stats[3]['count'],
            'total': sum(i['count'] for i in stats[1:]),
            'avatar': profile['userAvatar'],
            'realName': profile['realName']
        }
    return None
