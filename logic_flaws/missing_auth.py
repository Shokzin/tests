def delete_user(user_id):
    # ❌ Vulnerável
    database.delete(user_id)