from plaw.lemmy import Lemmy 

my_lemmy = Lemmy("https://fanaticus.social", "fanny_b", "zby3vzb1HXQ.ftb0czp")

comm = my_lemmy.getCommunity('baseball')

posts = my_lemmy.getPost(494)

print(posts)
# print(my_lemmy.auth_token)
