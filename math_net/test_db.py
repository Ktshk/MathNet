import connect

ms = connect.MongoService()

# ms.add_problem('639a13be1d8c938b41ea7c76', '6 * 7 = ?', 'The answer about life, space and other', '42', True)
# ms.add_comment('639a149e0e684fc5d482d699', '639a13be1d8c938b41ea7c76', 'Good!', True, '40', False)
# ms.add_like('639a149e0e684fc5d482d699', '639a13be1d8c938b41ea7c76', True)
# ms.create_user('clever_man',  "you_don't_understand_he_is_very_clever", 'password', "morcik155@gmail.com")
it = ms.client.math_net.users.find()
for user in it:
    print(user)
print()
print()
it2 = ms.client.math_net.problems.find()
for problem in it2:
    print(problem)
