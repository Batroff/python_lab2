# БСБО-05-19 Савранский Сергей

n = int(input('N >> '))
post = input('Post >> ').split(' опубликовал пост, количество просмотров: ')
popularity = {post[0]: [int(post[-1]), 'origin']}
for _ in range(n - 1):
    post = input()
    repost_user, post = post.split(' отрепостил пост у ')
    author, views = post.split(', количество просмотров: ')
    popularity[repost_user] = [int(views), author]
    while author != 'origin':
        popularity[author][0] += int(views)
        author = popularity[author][1]

print(*(v[0] for v in popularity.values()), sep='\n')
