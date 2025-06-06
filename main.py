from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import Response

app = FastAPI()


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class UserDataCreateBody(BaseModel):
    name: str
    job: str


class UserDataUpdateBody(BaseModel):
    name: str
    job: str


class UserDataCreateResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str


class UserDataUpdateResponse(BaseModel):
    name: str
    job: str
    updatedAt: str


class ResourceData(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str


class SupportData(BaseModel):
    url: str
    text: str


class ResponseModel(BaseModel):
    data: UserData
    support: SupportData


class ResponseModelList(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[UserData]
    support: SupportData


class ResponseModelListResource(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[ResourceData]
    support: SupportData


users = {
    2: {
        "page": 2,
        "per_page": 7,
        "total": 13,
        "total_pages": 2,
        "data": [
            {
                "id": 2,
                "email": "janet.weaver@reqres.in",
                "first_name": "Janet",
                "last_name": "Weaver",
                "avatar": "https://reqres.in/img/faces/2-image.jpg"
            },
            {
                "id": 7,
                "email": "michael.lawson@reqres.in",
                "first_name": "Michael",
                "last_name": "Lawson",
                "avatar": "https://reqres.in/img/faces/7-image.jpg"
            },
            {
                "id": 8,
                "email": "lindsay.ferguson@reqres.in",
                "first_name": "Lindsay",
                "last_name": "Ferguson",
                "avatar": "https://reqres.in/img/faces/8-image.jpg"
            },
            {
                "id": 9,
                "email": "tobias.funke@reqres.in",
                "first_name": "Tobias",
                "last_name": "Funke",
                "avatar": "https://reqres.in/img/faces/9-image.jpg"
            },
            {
                "id": 10,
                "email": "byron.fields@reqres.in",
                "first_name": "Byron",
                "last_name": "Fields",
                "avatar": "https://reqres.in/img/faces/10-image.jpg"
            },
            {
                "id": 11,
                "email": "george.edwards@reqres.in",
                "first_name": "George",
                "last_name": "Edwards",
                "avatar": "https://reqres.in/img/faces/11-image.jpg"
            },
            {
                "id": 12,
                "email": "rachel.howell@reqres.in",
                "first_name": "Rachel",
                "last_name": "Howell",
                "avatar": "https://reqres.in/img/faces/12-image.jpg"
            }
        ],
        "support": {
            "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
            "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
        }
    }
}


@app.get("/api/users", response_model=ResponseModelList)
def get_list_users(page: int = 2):
    user_data = users.get(page)
    if not user_data:
        raise HTTPException(status_code=404, detail="Page not found")

    return user_data


@app.get("/api/users/{user_id}", response_model=ResponseModel)
def get_single_user(user_id: int):
    for page_data in users.values():
        for user in page_data["data"]:
            if user["id"] == user_id:
                return {"data": user,
                        "support": page_data["support"]}

    raise HTTPException(status_code=404, detail="User not found")


@app.get("/api/unknown", response_model=ResponseModelListResource)
def get_list_resource():
    resources = {
        1: {
            "page": 1,
            "per_page": 6,
            "total": 12,
            "total_pages": 2,
            "data": [
                {
                    "id": 1,
                    "name": "cerulean",
                    "year": 2000,
                    "color": "#98B2D1",
                    "pantone_value": "15-4020"
                },
                {
                    "id": 2,
                    "name": "fuchsia rose",
                    "year": 2001,
                    "color": "#C74375",
                    "pantone_value": "17-2031"
                },
                {
                    "id": 3,
                    "name": "true red",
                    "year": 2002,
                    "color": "#BF1932",
                    "pantone_value": "19-1664"
                },
                {
                    "id": 4,
                    "name": "aqua sky",
                    "year": 2003,
                    "color": "#7BC4C4",
                    "pantone_value": "14-4811"
                },
                {
                    "id": 5,
                    "name": "tigerlily",
                    "year": 2004,
                    "color": "#E2583E",
                    "pantone_value": "17-1456"
                },
                {
                    "id": 6,
                    "name": "blue turquoise",
                    "year": 2005,
                    "color": "#53B0AE",
                    "pantone_value": "15-5217"
                }
            ],
            "support": {
                "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
                "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
            }
        }
    }

    resource_data = resources.get(1)
    if not resource_data:
        raise HTTPException(status_code=404, detail="Resource not found")

    return {
        "page": resource_data["page"],
        "per_page": resource_data["per_page"],
        "total": resource_data["total"],
        "total_pages": resource_data["total_pages"],
        "data": resource_data["data"],
        "support": resource_data["support"],
    }


@app.post("/api/users", response_model=UserDataCreateResponse, status_code=201)
def create_user(user: UserDataCreateBody):
    if not user.name or not user.job:
        raise HTTPException(status_code=400, detail="Name and job are required")

    return {
        "name": user.name,
        "job": user.job,
        "id": "409",
        "createdAt": "2025-05-30T08:46:33.132Z"
    }


@app.put("/api/users/{user_id}", response_model=UserDataUpdateResponse)
def update_user_put(user: UserDataUpdateBody):
    return {
        "name": user.name,
        "job": user.job,
        "updatedAt": "2025-05-30T09:58:46.242Z"
    }


@app.patch("/api/users/{user_id}", response_model=UserDataUpdateResponse)
def update_user_patch(user: UserDataUpdateBody):
    return {
        "name": user.name,
        "job": user.job,
        "updatedAt": "2025-05-30T10:29:24.851Z"
    }


@app.delete("/api/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    return Response(status_code=204)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
