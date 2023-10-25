def parse(query: str) -> dict:
    query_dict = {}
    if '?' in query:
        query_params = query.split('?')[1].split('&')
        for param in query_params:
            if '=' in param:
                key, value = param.split('=')
                query_dict[key] = value
    return query_dict


if __name__ == '__main__':
    result = parse('https://example.com/path/to/page?name=ferret&color=purple&')
    print(result)

    result = parse('http://example.com/')
    print(result)

    result = parse('http://example.com/?')
    print(result)

    result = parse('http://example.com/?name=Dima')
    print(result)
