def mask_sensitive_data(data):
    if isinstance(data, str) and len(data) > 4:
        return '*' * (len(data) - 4) + data[-4:]
    return data

sensitive_info = "1234567812345678"
masked_info = mask_sensitive_data(sensitive_info)
print(masked_info)  # Output: ************5678