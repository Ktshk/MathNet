import connect

ms = connect.MongoService()

# ms.add_problem('639a13be1d8c938b41ea7c76', '6 * 7 = ?', 'The answer about life, space and other', '42', True)
# ms.add_comment('639a149e0e684fc5d482d699', '639a13be1d8c938b41ea7c76', 'Good!', True, '40', False)
ms.add_like('639a149e0e684fc5d482d699', '639a13be1d8c938b41ea7c76', True)
