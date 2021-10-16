default_item = {
    "files": [
        (
            "thumbnail",
            (
                "laptopgrande.webp",
                open("tests/api/images/laptopgrande.webp", "rb"),
                "image/webp",
            ),
        ),
        (
            "pictures_file",
            (
                "laptopgrande.webp",
                open("tests/api/images/laptopgrande.webp", "rb"),
                "image/webp",
            ),
        ),
    ],
    "data": {
        "name": "Televisor",
        "description": "4k full hd lg",
        "brand": "LG",
        "price": 10000000,
        "rating": 4,
        "city_id": 1,
    },
}

default_item_without_name = {
    "files": [
        (
            "thumbnail",
            (
                "laptopgrande.webp",
                open("tests/api/images/laptopgrande.webp", "rb"),
                "image/webp",
            ),
        ),
        (
            "pictures_file",
            (
                "laptopgrande.webp",
                open("tests/api/images/laptopgrande.webp", "rb"),
                "image/webp",
            ),
        ),
    ],
    "data": {
        "description": "4k full hd lg",
        "brand": "LG",
        "price": 10000000,
        "rating": 4,
        "city_id": 1,
    },
}

default_item_bad_format = {
    "files": [
        (
            "thumbnail",
            (
                "laptopgrande.xlsx",
                open("tests/api/images/laptopgrande.webp", "rb"),
                "text/json",
            ),
        ),
        (
            "pictures_file",
            (
                "laptopgrande.pdf",
                open("tests/api/images/laptopgrande.webp", "rb"),
                "text/json",
            ),
        ),
    ],
    "data": {
        "name": "Televisor",
        "description": "4k full hd lg",
        "brand": "LG",
        "price": 10000000,
        "rating": 4,
        "city_id": 1,
    },
}
