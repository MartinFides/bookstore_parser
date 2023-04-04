import pydantic


class Model(pydantic.BaseModel):
    class Config:
        validate_all = True
        extra = pydantic.Extra.forbid
        allow_population_by_field_name = True
        use_enum_values = True
        validate_assignment = True
