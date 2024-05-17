users = {
    "admin": "scrypt:32768:8:1$L79A2dzeYEs2oadu$4f365638b691bb0df592b9f0b5a04ebdeeba87247289cdb854f7ef26e4e3204d66f5d42b8834395ed6f0b1db648afb732ff1d338fce2067e19bc089413a7c89b",
    "user": "scrypt:32768:8:1$vfIa46715CnfB57i$7d2604a1fb0ef829fd62119096e62038acba12ecca56dc043a89c029d24204ab41e54ad91be63d6e9bdac92cd70a18a06a88befa9cb1064d68b85394b584883a"
}

print(users["admin"])


users = {
    "admin": {"id": 1, "name": "admin", "psw": "12345"},
    "user": {"id": 1, "name": "user", "psw": "12345"}
}

print(users["user"]['id'])