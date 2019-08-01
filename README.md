# Genius Plaza test project for recipes

Sample JSON request response

URL: POST:recipes/

Request:
{
    "name": "Pasta",
    "user": 1,
    "ingredient_recipe": [
        {
            "text": "sphagetti, pesto, cream"
        }
    ],
    "step_recipe": [
        {
            "step_text": "update all of the above"
        }
    ]
}

Response:
{
    "id": 4,
    "name": "Pasta",
    "user": 1,
    "ingredient_recipe": [
        {
            "id": 3,
            "text": "sphagetti, pesto, cream"
        }
    ],
    "step_recipe": [
        {
            "id": 3,
            "step_text": "update all of the above"
        }
    ]
}

URL: GET:recipes/

Request: None

Response:
[
    {
        "id": 4,
        "name": "Pasta",
        "user": 1,
        "ingredient_recipe": [
            {
                "id": 3,
                "text": "sphagetti, pesto, cream"
            }
        ],
        "step_recipe": [
            {
                "id": 3,
                "step_text": "update all of the above"
            }
        ]
    }
]

URL : PUT:recipe/4/

Request:
{
    "name": "Pasta",
    "user": 1,
    "ingredient_recipe": [
        {
            "text": "sphagetti, pesto, cream"
        }
    ],
    "step_recipe": [
        {
            "step_text": "Remove all of the above"
        }
    ]
}

Response:
{
    "id": 4,
    "name": "Pasta",
    "user": 1,
    "ingredient_recipe": [
        {
            "id": 3,
            "text": "sphagetti, pesto, cream"
        }
    ],
    "step_recipe": [
        {
            "id": 3,
            "step_text": "Remove all of the above"
        }
    ]
}

URL: GET:/user/1/

Request: None

Response:
{
    "id": 4,
    "name": "Pasta",
    "user": 1,
    "ingredient_recipe": [
        {
            "id": 3,
            "text": "sphagetti, pesto, cream"
        }
    ],
    "step_recipe": [
        {
            "id": 3,
            "step_text": "Remove all of the above"
        }
    ]
}

URL: DELETE:recipe/4/

Request: None
Response: None