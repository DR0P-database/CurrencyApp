def format_port_type(port):
    try:
        return int(port)
    except ValueError:
        return 8000
