from faker import Faker


def get_fake_user():
    fake = Faker()
    user = {
        "name": fake.name(),
        "address": fake.address(),
        "email": fake.email(),
    }
    return user


async def delete_user(database, user_id: str):
    print("[delete_user][START] user_id:", user_id)
    await database.delete(user_id)
    print("[delete_user][END] user_id:", user_id)


async def create_user(database, user):
    print("[create_user][START] user:", user)
    response = await database.create("users", user)
    print("[create_user][RESPONSE] response:", response)
    response = response[0]
    user = await database.select(response["id"])
    print("[create_user][END] user:", user)
    return user


async def update_user(database, user_id, updated_user):
    print("[update_user][START] updated_user:", updated_user)
    await database.query(f"update {user_id} merge {updated_user}")
    updated_user = await database.select(user_id)
    print("[update_user][END] updated_user:", updated_user)
    return updated_user
