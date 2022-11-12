from flask_app.models import user, item, category

category1 = {
    "name": "clothing"
}

category2 = {
    "name": "electronics"
}

category3 = {
    "name": "outdoors"
}

# category.Category.createCategory(category1)
# category.Category.createCategory(category2)
# category.Category.createCategory(category3)


item1 = {
    "item_name" : "shoes",
    "cost" : "10",
    "location" : "Seattle",
    "image" : "image.png",
    "brief_desc" : "used Nike size 9",
    "details" : "Nikes red and black, size 9, bought in 2019, only worn twice",
    "user_id" : "1",
    "category_id" : "1",
}

item2 = {
    "item_name" : "headphones",
    "cost" : "30",
    "location" : "Bellevue",
    "image" : "image.png",
    "brief_desc" : "new Bose headphones",
    "details" : "black 2020 Bose headphones, brand new in box",
    "user_id" : "2",
    "category_id" : "2",
}

item3 = {
    "item_name" : "kayak",
    "cost" : "250",
    "location" : "issaquah",
    "image" : "image.png",
    "brief_desc" : "inflatable kayak",
    "details" : "2003 NRS inflatable kayak, 2 patched holes, a few scuff marks",
    "user_id" : "2",
    "category_id" : "3",
}

item3a = {
    'id': 3,
    "item_name" : "NRS kayak",
    "cost" : "250",
    "location" : "Issaquah",
    "image" : "image.png",
    "brief_desc" : "inflatable kayak",
    "details" : "2003 NRS inflatable kayak, 2 patched holes, a few scuff marks",
    "user_id" : "2",
    "category_id" : "3",
}

# item.Item.save(item1)
# item.Item.save(item2)
# item.Item.save(item3)

# print(item.Item.get_all())

# print(item.Item.get_one(1))

# item.Item.update(item3a)

# item.Item.delete(2)