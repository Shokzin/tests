def get_user_data(user_id):
    # ❌ Vulnerável
    return database.get(user_id)