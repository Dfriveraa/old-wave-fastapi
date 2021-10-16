create_item_mock = {
    "name": "Televisor",
    "description": "4k full hd lg",
    "brand": "LG",
    "price": 10000000,
    "rating": 4,
    "city": {"name": "Medellin", "id": 1},
    "id": 1,
    "seller": {
        "id": 7,
        "name": "FastAPI",
        "logo": "https://worldvectorlogo.com/es/download/fastapi-1.svg",
    },
    "pictures": ["https://dev-empresariales.s3.amazonaws.com/grande.webp"],
}

get_all_item_mock = {
    "query": "",
    "total": 2,
    "items": [
        {
            "name": "Televisor",
            "description": "4k full hd lg",
            "brand": "LG",
            "price": 10000000,
            "rating": 4,
            "city": {"name": "Medellin", "id": 1},
            "id": 1,
            "thumbnail": "https://dev-empresariales.s3.amazonaws.com/pequena.webp",
        },
        {
            "name": "Laptop ultima en guaracha",
            "description": "300 gb de ram",
            "brand": "Mac",
            "price": 9999999,
            "rating": 5,
            "city": {"name": "Medellin", "id": 1},
            "id": 2,
            "thumbnail": "https://dev-empresariales.s3.amazonaws.com/laptop_p.webp",
        },
    ],
    "seller": {
        "id": 7,
        "name": "FastAPI",
        "logo": "https://worldvectorlogo.com/es/download/fastapi-1.svg",
    },
}
