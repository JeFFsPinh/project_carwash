class ValidationError(Exception):
    pass

def validate(data: dict) -> dict:
    try:
        assert data.get('plate') is not None, "Plate wasn't defined."
        assert data.get('description') is not None, "Description wasn't defined."
        assert data.get('color') is not None, "Color wasn't defined." 
    except AssertionError as ae:
        raise ValidationError(ae)

    try:
        assert len(data['plate']) == 7
    except AssertionError:
        raise ValidationError("Plate needs 7 characters exactly.")

    return data