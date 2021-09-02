def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result


print(
    full_emails(
        [("jon@example.com", "Jon Mockbee"), ("shay@example.com", "shay Brandt")]
    )
)
