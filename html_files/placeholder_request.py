import requests 

BASE_URL = 'https://jsonplaceholder.typicode.com'


def getAllPost():
    try:
        response = requests.get(f'{BASE_URL}/posts') 
        # response.raise_for_status() 
        return response.json()
    except Exception as e:
        print(f'Error occurred while fetching posts: {e}')
        return None 


def presentPostData(postsData: list):
    print('\n' + '=' * 15 + ' POSTS ' + '=' * 15)
    for post in postsData:
        print(f'Title      :  {post.get("title")}')
        print(f'Content    :  {post.get("body")}')
        print(f'Posted by user with id {post.get("userId")}')
        print("+" * 20)
    print('=' * 37)


def getAllComment():
    try:
        response = requests.get(f'{BASE_URL}/comments') 
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f'Error occurred while fetching comments: {e}')
        return None 


def presentCommentsData(commentsData: list):
    print('\n' + '=' * 14 + ' COMMENTS ' + '=' * 13)
    for comment in commentsData:
        print(f'Name       :  {comment.get("name")}')
        print(f'PostID     :  {comment.get("postId")}')
        print(f'Comment ID :  {comment.get("id")}')
        print("+" * 20)
    print('=' * 37)



def postArticle(title,body,userId):
    try :
        response = requests.post(f'{BASE_URL}/posts', json={
            'title': title,
            'body': body,
            'userId': userId,
        })
        if response.ok :
            data = response.json()
            print('Article posted successfull')
            return data 
    except Exception as e :
        print(f'An error occurred : {e}')
        return None

if __name__ == "__main__":
    # posts = getAllPost()
    # if posts: 
    #     presentPostData(posts)
        
    # comments = getAllComment()
    # if comments: 
    #     presentCommentsData(comments)
    data = postArticle("EPL WINNERS",'The gunners finally lifted the long awaited 22 years trophyless trophy',5)
    print(data)