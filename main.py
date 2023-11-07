def parse_cookie(query: str) -> dict:
    cookie_dict = {}
    if query:
        cookie_params = query.split(';')
        for param in cookie_params:
            param_parts = param.strip().split('=', 1)
            if len(param_parts) == 2:
                key, value = param_parts
                cookie_dict[key] = value
    return cookie_dict


if __name__ == '__main__':
    result = parse_cookie('name=Dima;')
    print(result)

    result = parse_cookie('')
    print(result)

    result = parse_cookie('name=Dima;age=28;')
    print(result)

    result = parse_cookie('name=Dima=User;age=28;')
    print(result)