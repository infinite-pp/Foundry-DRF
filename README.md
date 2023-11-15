# Test 1:

 - Create element with non alphabetic name and symbol

**Api url:** 

 - http://127.0.0.1:8000/api/elements/

**Method:**

 - POST

**Payload:**

```
{
    "name":"Carbon1",
    "symbol":"c"
}
```

**Response:** 

```
{
    "non_field_errors": [
        {
            "name": "Name Carbon1 can be alphabetic only"
        },
        {
            "symbol": "Symbol ca1 can be alphabetic only"
        }
    ]
}
```

**Status Code:**

 - 400

-------------------------------------------------------------------

# Test 2:

 - Create element with non alphabetic name and symbol

**Api url:** 

 - http://127.0.0.1:8000/api/elements/

**Method:**

 - POST

**Payload:**

```
{
    "name":"Carbon",
    "symbol":"c"
}
```

**Response:**

```
{
    "non_field_errors": [
        {
            "symbol": "Symbol c should start with uppercase"
        }
    ]
}
```

**Status Code:**

 - 400

---------------------------------------------------------------------------

# Test 3:

 - Create element with duplicate symbol

**Api url:** 

 - http://127.0.0.1:8000/api/elements/

**Method:**

 - POST

**Payload:**

```
{
    "name":"Sulphur",
    "symbol":"S"
}
```

**Response:** 

```
{
    "non_field_errors": [
        {
            "symbol": "Symbol S already exists"
        }
    ]
}
```

**Status Code:**

 - 400

------------------------------------------------------------------------------

# Test 4:

 - Create grade with proper data

**Api url:** 

 - http://127.0.0.1:8000/api/grades/

**Method:**

 - POST

**Payload:**

```
{
    "name": "Grade 6",
    "code": "G6",
    "grade_tc": [
        {
            "element": 2,
            "min_rate": 4,
            "max_rate": 5
        }
    ]
}
```

**Response:** 

```
{
    "id": 5,
    "name": "Grade 6",
    "code": "G6",
    "grade_tc": [
        {
            "element": 2,
            "min_rate": "4.000",
            "max_rate": "5.000",
            "relaxed_min_rate": "3.960",
            "relaxed_max_rate": "5.050"
        }
    ]
}
```

**Status Code:**

 - 201

-----------------------------------------------------------------------------

# Test 5:

 - Create grade with missing data

**Api url:** 

 - http://127.0.0.1:8000/api/grades/

**Method:**

 - POST

**Payload:**

```
{
    "name": "",
    "code": "G2",
    "grade_tc": [
        {
            "element": 2,
            "min_rate": 4,
            "max_rate": 5
        }
    ]
}
```

**Response:** 

```
{
    "name": [
        "This field may not be blank."
    ]
}
```

**Status Code:**

 - 400

-----------------------------------------------------------------------

# Test 6:

 - Create grade with non alphanum code

**Api url:** 

 - http://127.0.0.1:8000/api/grades/

**Method:**

 - POST

**Payload:**

```
{
    "name": "Grade 2",
    "code": "G2@#",
    "grade_tc": [
        {
            "element": 2,
            "min_rate": 4,
            "max_rate": 5
        }
    ]
}
```

**Response:** 

```
{
    "non_field_errors": [
        {
            "Grade code": "G2@# can be alphanumeric only"
        }
    ]
}
```

**Status Code:**

 - 400

-----------------------------------------------------------------------

# Test 7:

 - Create grade with missing grade TC

**Api url:** 

 - http://127.0.0.1:8000/api/grades/

**Method:**

 - POST

**Payload:**

```
{
    "name": "Grade 3",
    "code": "G3",
    "grade_tc": []
}
```

**Response:** 

```
{
    "id": 3,
    "name": "Grade 3",
    "code": "G3",
    "grade_tc": []
}
```

**Status Code:**

 - 201

-----------------------------------------------------------------------

# Test 8:

 - Create grade with duplicate code

**Api url:** 

 - http://127.0.0.1:8000/api/grades/

**Method:**

 - POST

**Payload:**

```
{
    "name": "Grade 2",
    "code": "G2",
    "grade_tc": [
        {
            "element": 2,
            "min_rate": 4,
            "max_rate": 5
        }
    ]
}
```

**Response:** 

```
{
    "non_field_errors": [
        {
            "Grade code": "Grade code G2 already exists"
        }
    ]
}
```

**Status Code:**

 - 400

-----------------------------------------------------------------------

# Test 9:

 - Create grade with duplicate TC elements

**Api url:** 

 - http://127.0.0.1:8000/api/grades/

**Method:**

 - POST

**Payload:**

```
{
    "name": "Grade 2",
    "code": "G4",
    "grade_tc": [
        {
            "element": 2,
            "min_rate": 4,
            "max_rate": 5
        }
    ]
}
```

**Response:** 

```
{
    "id": 4,
    "name": "Grade 2",
    "code": "G4",
    "grade_tc": [
        {
            "element": 2,
            "min_rate": "4.000",
            "max_rate": "5.000",
            "relaxed_min_rate": "3.960",
            "relaxed_max_rate": "5.050"
        }
    ]
}
```

**Status Code:**

 - 201

-----------------------------------------------------------------------

# Test 10:

 - Create grade with min_rate >= max_rate

**Api url:** 

 - http://127.0.0.1:8000/api/grades/

**Method:**

 - POST

**Payload:**

```
{
    "name": "Grade 2",
    "code": "G5",
    "grade_tc": [
        {
            "element": 2,
            "min_rate": 4,
            "max_rate": 3
        }
    ]
}
```

**Response:** 

```
{
    "non_field_errors": [
        {
            "grade_tc": "Min > Max for element Silicon - Si"
        }
    ]
}
```

**Status Code:**

 - 400

-----------------------------------------------------------------------

# Test 11:

 - Create grade with min_rate = alphabet

**Api url:** 

 - http://127.0.0.1:8000/api/grades/

**Method:**

 - POST

**Payload:**

```
{
    "name": "Grade 2",
    "code": "G5",
    "grade_tc": [
        {
            "element": 2,
            "min_rate": "alphabet",
            "max_rate": 5
        }
    ]
}
```

**Response:** 

```
{
    "grade_tc": [
        {
            "min_rate": [
                "A valid number is required."
            ]
        }
    ]
}
```

**Status Code:**

 - 400

-----------------------------------------------------------------------

# Test 12:

 - Create grade with min_rate = alphabet

**Api url:** 

 - http://127.0.0.1:8000/api/grades/

**Method:**

 - POST

**Payload:**

```
{
    "name": "Grade 2",
    "code": "G5",
    "grade_tc": [
        {
            "element": 2,
            "min_rate": "alphabet",
            "max_rate": 5
        }
    ]
}
```

**Response:** 

```
{
    "grade_tc": [
        {
            "min_rate": [
                "A valid number is required."
            ]
        }
    ]
}
```

**Status Code:**

 - 400

-----------------------------------------------------------------------

# Test 13:

 - Update grade without sending TC

**Api url:** 

 - http://127.0.0.1:8000/api/grades/1/

**Method:**

 - PATCH

**Payload:**

```
{
    "name": "Grade 1",
    "code": "G1",
    "grade_tc": []
}
```

**Response:** 

```
{
    "id": 1,
    "name": "Grade 1",
    "code": "G1",
    "grade_tc": []
}
```

**Status Code:**

 - 200

-----------------------------------------------------------------------

# Test 14:

 - Update grade with changed TC

**Api url:** 

 - http://127.0.0.1:8000/api/grades/2/

**Method:**

 - PATCH

**Payload:**

```
{
    "name": "Grade 2",
    "code": "G5",
    "grade_tc": [
        {
            "element": 2,
            "min_rate": 2,
            "max_rate": 5
        }
    ]
}
```

**Response:** 

```
{
    "id": 2,
    "name": "Grade 2",
    "code": "G5",
    "grade_tc": [
        {
            "element": 2,
            "min_rate": "2.000",
            "max_rate": "5.000",
            "relaxed_min_rate": "1.980",
            "relaxed_max_rate": "5.050"
        }
    ]
}
```

**Status Code:**

 - 200

-----------------------------------------------------------------------

# Test 15:

 - Upgrade grade with duplicate code

**Api url:** 

 - http://127.0.0.1:8000/api/grades/2/

**Method:**

 - PATCH

**Payload:**

```
{
    "name": "Grade 3",
    "code": "G3",
    "grade_tc": [
        {
            "element": 2,
            "min_rate": 7,
            "max_rate": 10
        }
    ]
}
```

**Response:** 

```
{
    "non_field_errors": [
        {
            "Grade code": "Grade code G3 already exists"
        }
    ]
}
```

**Status Code:**

 - 400
